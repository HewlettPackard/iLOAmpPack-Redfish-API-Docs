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

# Adding a list of servers

import sys
import redfish
import time
import json
import argparse

# Check for the multiple occurance of same argument, if so raise exception 
class Once(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    if hasattr(self, 'seen'):
      raise argparse.ArgumentError(self, 'only one please')
    setattr(self, 'seen', True)
    setattr(namespace, self.dest, values)

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--iLOAmpAddress', action=Once, required=True, type=str)
my_parser.add_argument('--Username', action=Once, required=True, type=str)
my_parser.add_argument('--Password', action=Once, required=True, type=str)
my_parser.add_argument('--OutputFileName', action=Once, type=str)
my_parser.add_argument('--ServerUserName', action=Once, required=True, type=str)
my_parser.add_argument('--ServerPassword', action=Once, required=True, type=str)
my_parser.add_argument('--ServerGroupName', action=Once, type=str)
my_parser.add_argument('--ServerAddress', action=Once, required=True, type=str, nargs='*') # nargs='*' represents array of respective type
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
                                     password=login_password)
except:
    print("Wrong iLO Amplifier Pack address/credential or iLO Amplifier Pack is not reachable")
    exit()

# Login into iLO Amplifier Pack and create a session
try:
    REDFISH_OBJ.login(auth="session")
except:
    print("Invalid iLO Amplifier Pack credential")
    exit()

body = dict()
body["UserName"] = args.ServerUserName
body["Password"] = args.ServerPassword

#Create group before using here
if args.ServerGroupName != None:
  body["ServerGroupName"] = args.ServerGroupName

serverLocation = dict()

for iLOAddress in args.ServerAddress:
    location = None
    slash = 0
    body["ManagerAddress"] = iLOAddress
    # Do a POST on a given path
    try:
        response = REDFISH_OBJ.post("/redfish/v1/AggregatorService/ManagedSystems/",
                                    body=body)
    except:
        print("POST request to /redfish/v1/AggregatorService/ManagedSystems failed for server %s\n" %iLOAddress)
        continue

    errMessage = ""
    if response.status != 201:
        sys.stdout.write("Unable to Add server %s\n" %iLOAddress)
        sys.stdout.write("status code %s\n" % response.status)
        try:
            sys.stdout.write(
                "ErrorType: %s\n" % response.dict["error"]["@Message.ExtendedInfo"][0]["MessageId"].split(".")[-1])
            for errStr in response.dict["error"]["@Message.ExtendedInfo"][0]["MessageArgs"]:
                errMessage += errStr + ", "
            sys.stdout.write("errMessage: %s\n" % errMessage)
        except:
            pass
        continue
    else:
        location = response.getheader("Location")

    location = response.getheader("Location")
    if location is None:
        sys.stdout.write("Unable to add server %s.\n" %iLOAddress)

    #Location header prototype having sessionID is shown below
    #Location = https://iLOAmplifierPackaddress/redfish/v1/SessionService/Sessions/{SessionID}
    #Here part of Location header conatining sessionId is extarcted (/redfish/v1/SessionService/Sessions/{SessionID})
    # find the 3rd slash in location
    slash = location.find("/", slash)
    slash = location.find("/", slash + 2)
    location = location[slash:]
    serverLocation[iLOAddress] = location

#Checking status of discovery
while len(serverLocation) > 0:
    keys_to_be_removed = []
    for iLOAddress, location in serverLocation.items():
      dstate = "InProgress"

      managed_system = REDFISH_OBJ.get(location)
      if managed_system.status != 200:
        sys.stdout.write("Unable to get status of discovery of server %s.\n" % iLOAddress)
        sys.stdout.write("%s\n" % managed_system)
        keys_to_be_removed.append(iLOAddress)
        continue
      dstate = managed_system.dict["SystemSummary"]["Discovery"]["State"]
      sys.stdout.write("Discovery of server %s is %s.\n" % (iLOAddress, dstate))
      if dstate == "Complete":
        keys_to_be_removed.append(iLOAddress)
    for key in keys_to_be_removed:
      del serverLocation[key]
    time.sleep(5)

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
