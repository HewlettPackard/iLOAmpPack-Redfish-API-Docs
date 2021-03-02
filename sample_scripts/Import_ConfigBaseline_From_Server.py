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

# Import configuration baseline from server

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
my_parser.add_argument('--Name', action=Once, required=True, type=str)
my_parser.add_argument('--ServerAddress', action=Once, required=True, type=str)
args = my_parser.parse_args()

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

body = dict()
body["Name"] = args.Name
body["ServerConfigurationType"] = "SnapshotServerConfiguration"


# Do a POST on a given path
try:
    response = REDFISH_OBJ.post("/redfish/v1/ManagedNodes/ConfigurationBaselines", body=body)
except:
    print("Failed POST request to /redfish/v1/ManagedNodes/ConfigurationBaselines\n")
    REDFISH_OBJ.logout()
    exit()

errMessage = ""
if response.status != 201:
    sys.stdout.write("Unable to import configuration baseline from server\n")
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

time.sleep(5)
# Do a GET on a given path
try:
    response = REDFISH_OBJ.get("/redfish/v1/ManagedNodes/ConfigurationBaselines")
except:
    print("Failed GET request to /redfish/v1/ManagedNodes/ConfigurationBaselines\n")
    REDFISH_OBJ.logout()
    exit()

Configure_Baseline_Count = response.dict["Members@odata.count"]
if Configure_Baseline_Count > 0:
  Baseline_Info = response.dict["Members"]
  for Baseline in Baseline_Info:
      if Baseline["Name"] == args.Name:
          Id = Baseline["Id"]
else:
    sys.stdout.write("No Configuration Baseline created\n")
    REDFISH_OBJ.logout()
    exit()

body.clear()
body["ConfigurationBaselineId"] = int(Id)
body["SelectedSystemsManagerAddress"] = [args.ServerAddress]
# Do a POST on a given path
uri = "/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ImportConfigurationBaselineJobs"
try:
    response = REDFISH_OBJ.post(uri, body=body)
except:
    sys.stdout.write("Failed POST request to %s\n" % uri)
    REDFISH_OBJ.logout()
    exit()

errMessage = ""
if response.status != 202:
    sys.stdout.write("Unable to import configuration baseline from server\n")
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
sys.stdout.write("Import configuration baseline job has been created successfully\n")
sys.stdout.write("check job status using jobId %s\n" % jobId)

# Logout of the current session
REDFISH_OBJ.logout()

