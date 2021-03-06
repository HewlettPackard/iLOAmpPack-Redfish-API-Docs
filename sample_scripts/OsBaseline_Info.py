# (C) Copyright [2021] Hewlett Packard Enterprise Development LP
 
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
 
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Get imported Os baseline information

import sys
import redfish
import time
import argparse

# Check for the multiple occurance of same argument, if so raise exception
class Once(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    if hasattr(self, 'seen'):
      raise argparse.ArgumentError(self, 'Only once please')
    setattr(self, 'seen', True)
    setattr(namespace, self.dest, values)

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--iLOAmpAddress', action=Once, required=True, type=str)
my_parser.add_argument('--Username', action=Once, required=True, type=str)
my_parser.add_argument('--Password', action=Once, required=True, type=str)
my_parser.add_argument('--OutputFileName', action=Once, type=str)
args = my_parser.parse_args()

# Redirect standard output into a file(optional)
if args.OutputFileName != None:
    if (args.OutputFileName.find('.txt') == -1):
        args.OutputFileName += ".txt"
    sys.stdout = open(args.OutputFileName, "w")

# Connect using iLO Amplifier Pack address, username and password
login_host = "https://" + args.iLOAmpAddress
login_account = args.Username
login_password = args.Password

## Create a REDFISH object
try:
    REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password, timeout=10, max_retry=3)
except:
    print("Wrong iLO Amplifier Pack address/credential or iLO Amplifier Pack not reachable\n")
    exit()

# Login into iLO Amplifier Pack and create a session
try:
    REDFISH_OBJ.login(auth="session")
except:
    print("Invalid iLO Amplifier Pack credential\n")
    exit()

# Do a GET on a given path
uri = "/redfish/v1/Managers/iLOAmplifier/OSBaselineService/OSBaselines"
try:
    response = REDFISH_OBJ.get(uri)
except:
    print("exception for get request %s" %uri)
    REDFISH_OBJ.logout()
    exit()

if response.status != 200:
    sys.stdout.write("Failed to get os baseline information\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

Baseline_Count = response.dict["Members@odata.count"]
if Baseline_Count > 0:
  Baseline_Info = response.dict["Members"]
  for Baseline in Baseline_Info:
      sys.stdout.write("OsBaselineId=%s, OsImage=%s\n" % (Baseline["Id"], Baseline["Name"]))
else:
    sys.stdout.write("No Baseline found\n")

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
