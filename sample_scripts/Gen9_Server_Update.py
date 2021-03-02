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

# Gen9 server update

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
operationType = ["LegacyOnlineBaselineAutomatic", "LegacyOffline"]
operationStrategy = ["StageAndDeploy", "DeployOnly", "StageOnly"]
boolValue = ["True", "False"]
my_parser.add_argument('--iLOAmpAddress', action=Once, required=True, type=str)
my_parser.add_argument('--Username', action=Once, required=True, type=str)
my_parser.add_argument('--Password', action=Once, required=True, type=str)
my_parser.add_argument('--BaselineId', action=Once, required=True, type=int)
my_parser.add_argument('--OperationStrategy', action=Once, choices=operationStrategy, required=True, type=str)
my_parser.add_argument('--OperationType', action=Once, choices=operationType, required=True, type=str)
my_parser.add_argument('--ResetFlag', action=Once, choices=boolValue, type=str, default="False")
my_parser.add_argument('--DowngradeFlag', action=Once, choices=boolValue, type=str, default="False")
my_parser.add_argument('--CleanUpRepository', action=Once, choices=boolValue, type=str, default="False")
my_parser.add_argument('--BatchSize', action=Once, type=int, default=20)
my_parser.add_argument('--OutputFileName', action=Once, type=str)
my_parser.add_argument('--ServerAddress', action=Once, required=True, type=str, nargs='*')
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
    print("Wrong iLO Amplifier Pack address/credential or iLO Amplifier Pack is not reachable\n")
    exit()

# Login into iLO Amplifier Pack and create a session
try:
    REDFISH_OBJ.login(auth="session")
except:
    print("Invalid iLO Amplifier Pack credential\n")
    exit()


updateServerList = list( dict.fromkeys(args.ServerAddress))


body = dict()
if args.OperationStrategy != "DeployOnly":
  body["BaselineId"] = args.BaselineId
body["BatchSize"] = args.BatchSize
body["CleanUpRepository"] = False
body["OperationStrategy"] = args.OperationStrategy
body["OperationType"] = args.OperationType

if args.OperationStrategy == "StageAndDeploy":
    if args.OperationType == "LegacyOffline":
        body["DowngradeFlag"] = True if args.DowngradeFlag == "True" else False
        body["ResetFlag"] = False
    else:
        body["ResetFlag"] = True if args.ResetFlag == "True" else False
        body["DowngradeFlag"] = False
elif args.OperationStrategy == "StageOnly":
    body["DowngradeFlag"] = False
    body["ResetFlag"] = False
else:
  body["ResetFlag"] = True if args.ResetFlag == "True" else False
  body["CleanUpRepository"] = True if args.CleanUpRepository == "True" else False

body["SelectedSystemsManagerAddress"] = updateServerList
ManagerCredentials = dict()
ManagerCredentials["UserName"] = ""
ManagerCredentials["Password"]: ""
body["ManagerCredentials"] = ManagerCredentials
body["UseExternalWebServer"] = False
try:
    response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs", body=body)
except:
    print("POST request to /redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs\n")
    REDFISH_OBJ.logout()
    exit()
errMessage = ""
if response.status != 202:
    sys.stdout.write("Unable to update gen 9 server\n")
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

jobCreatedLink = response.getheader("Location")
if jobCreatedLink == None:
    jobCreatedLink = response.getheader("Link")
    if jobCreatedLink == None:
        jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]

jobId = jobCreatedLink.split("/")[-1]
sys.stdout.write("Gen9 server update job has been created successfully\n")
sys.stdout.write("check job status using jobId %s\n" % jobId)

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
