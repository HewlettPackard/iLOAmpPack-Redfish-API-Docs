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

# Perform action on server group

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
operationType = ["RefreshGroup","DeleteGroup", "UID", "Power"]
indicatorType = ["Lit", "Off"]
resetType = ["On", "ForceOff", "ForceRestart", "PushPowerButton"]
my_parser.add_argument('--iLOAmpAddress', action=Once, required=True, type=str)
my_parser.add_argument('--Username', action=Once, required=True, type=str)
my_parser.add_argument('--Password', action=Once, required=True, type=str)
my_parser.add_argument('--OutputFileName', action=Once, type=str)
my_parser.add_argument('--GroupName', action=Once, required=True, type=str)
my_parser.add_argument('--OperationType', action=Once, choices=operationType, required=True, type=str)
my_parser.add_argument('--IndicatorLED', action=Once, choices=indicatorType, type=str)
my_parser.add_argument('--ResetType', action=Once, choices=resetType, type=str)
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
    print("Wrong iLO Amplifier Pack address/credential or iLO Amplifier Pack is not reachable\n")
    exit()

# Login into iLO Amplifier Pack and create a session
try:
    REDFISH_OBJ.login(auth="session")
except:
    print("Invalid iLO Amplifier Pack credential\n")
    exit()

body = dict()
if args.OperationType.lower() != "uid" and args.OperationType.lower() != "power":
    body["Name"] = args.GroupName
else:
    body["GroupName"] = args.GroupName
body["AllSystemsInGroup"] = True
if args.OperationType.lower() == "refreshgroup":
    body["OperationType"] = "RefreshGroup"
elif args.OperationType.lower() == "deletegroup":
    body["OperationType"] = "DeleteGroup"
elif args.OperationType.lower() == "uid":
    body["IndicatorLED"] = args.IndicatorLED
    body["OperationType"] = "UID"
elif args.OperationType.lower() == "power":
    body["OperationType"] = "Power"
    body["ResetType"] = args.ResetType

if args.OperationType.lower() != "uid" and args.OperationType.lower() != "power":
    uri = "/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs"
else:
    uri = "/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupActionJobs"

# Do a POST on a given path
try:
    response = REDFISH_OBJ.post(uri, body=body)
except:
    sys.stdout.write("POST request to %s failed\n", uri)
    REDFISH_OBJ.logout()
    exit()

errMessage = ""
if response.status != 202:
    sys.stdout.write("Unable to perform server group action\n")
    sys.stdout.write("status code %s\n" % response.status)
    try:
        sys.stdout.write("ErrorType: %s\n" % response.dict["error"]["@Message.ExtendedInfo"][0]["MessageId"].split(".")[-1])
        for errStr in response.dict["error"]["@Message.ExtendedInfo"][0]["MessageArgs"]:
            errMessage += errStr + ", "
        sys.stdout.write("errMessage: %s\n" % errMessage)
    except:
        pass
    REDFISH_OBJ.logout()
    exit()

jobCreatedLink = response.getheader("Location")
if jobCreatedLink == None:
    jobCreatedLink = response.getheader("Link")
    if jobCreatedLink == None:
        jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]

jobId = jobCreatedLink.split("/")[-1]
sys.stdout.write("Group action job has been created successfully\n")
sys.stdout.write("check job status using jobId %s\n" % jobId)

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
