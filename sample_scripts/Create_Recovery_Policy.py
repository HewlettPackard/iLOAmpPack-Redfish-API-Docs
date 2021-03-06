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

# Create recovery policy

import sys
import redfish
import time
import json
import argparse

# Check for the multiple occurance of same argument, if so raise exception
class Once(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    if hasattr(self, 'seen'):
      raise argparse.ArgumentError(self, 'Only once please')
    setattr(self, 'seen', True)
    setattr(namespace, self.dest, values)

my_parser = argparse.ArgumentParser()
Enabled = ["True", "False"]
my_parser.add_argument('--iLOAmpAddress', action=Once, required=True, type=str)
my_parser.add_argument('--Username', action=Once, required=True, type=str)
my_parser.add_argument('--Password', action=Once, required=True, type=str)
my_parser.add_argument('--OutputFileName', action=Once, type=str)
my_parser.add_argument('--PolicyName', action=Once, required=True, type=str)
my_parser.add_argument('--FirmwareBaselineId', action=Once, required=True, type=int)
my_parser.add_argument('--ConfigurationBaselineId', action=Once, type=int)
my_parser.add_argument('--iLOConfigurationBackupEnable', action=Once, choices=Enabled, required=True, type=str)
my_parser.add_argument('--OsBaseline', action=Once,  type=int)
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

# Create a REDFISH object
try:
    REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password, timeout=10, max_retry=3)
except:
    print("Wrong iLO Amplifier Pack address/credential or iLO Amplifier Pack is not reachable\n")
    exit()

# Login into iLO Amplifier Pack and create a session
try:
    REDFISH_OBJ.login(auth="session")
except:
    print("Invalid iLO Amplifier Pack credential\n")
    exit()

body = dict()
body["Name"] = args.PolicyName
body["BaselineID"] = args.FirmwareBaselineId
if args.ConfigurationBaselineId != None:
    body["PersonaID"] = args.ConfigurationBaselineId
else:
    body["PersonaID"] = 0
if args.OsBaseline != None:
    body["OperatingSystemID"] = args.OsBaseline
else:
    body["OperatingSystemID"] = 0
body["UseNANDBackupRestoreIfAvailable"] = True if args.iLOConfigurationBackupEnable == "True" else False

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/ManagedNodes/RecoveryPolicy", body=body)

errMessage = ""
if response.status != 201:
    sys.stdout.write("Failed to create recovery policy\n")
    sys.stdout.write("status code %s\n" % response.status)
    try:
        sys.stdout.write(
            "ErrorType: %s\n" % response.dict["error"]["@Message.ExtendedInfo"][0]["MessageId"].split(".")[-1])
        for errStr in response.dict["error"]["@Message.ExtendedInfo"][0]["MessageArgs"]:
            errMessage += errStr + ", "
        sys.stdout.write("errMessage: %s\n" % errMessage)
    except:
        pass
    REDFISH_OBJ.logout()
    exit()

sys.stdout.write("Recovery policy has been created successfully\n")

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
