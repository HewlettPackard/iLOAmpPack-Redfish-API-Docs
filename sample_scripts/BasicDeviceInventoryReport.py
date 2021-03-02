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

# Download basic device inventory report

import sys
import redfish
import time
import argparse
from datetime import datetime

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
    print("Wrong iLO Amp address/credential or iLO Amp not reachable")
    exit()

# Login into iLO Amplifier Pack and create a session
try:
    REDFISH_OBJ.login(auth="session")
except:
    print("Invalid iLO Amp credential")
    exit()

body = dict()
body["SelectedFields"] = ["ILOIPv4Address", "ILOIPv6Address", "iLOHostName", "ProductName", "ServerHostName", "SerialNumber",\
                          "iLOFirmware", "SystemRom", "SystemRomBackup", "IntelligentProvisioning", "IntelligentPlatformAbstractionData",\
                          "PowerManagementControllerFirmware", "PowerManagementControllerBootloader", "SystemProgrammableLogicDevice", \
                          "ServerPlatformServicesFirmware", "PCIDevices-Name", "PCIDevices-Version", "PCIDevices-Location", "NetworkDevices-Name", \
                          "NetworkDevices-Version", "ArrayControllers-Name", "ArrayControllers-Version", "StorageDevicesName", "StorageDevicesVersion", \
                          "PhysicalDrivesName", "PhysicalDrivesVersion"]
body["ServerCategory"] = "StandAlone"
body["ReportType"] = "BasicDevice"

# Do a POST on a given path
uri = "/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.DownloadReportJobs"
try:
    response = REDFISH_OBJ.post(uri, body=body)
except:
    print("exception for POST request %s" %uri)
    exit()

if response.status != 202:
    sys.stdout.write("Unable to create report.")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    time.sleep(300)
    exit()

jobCreatedLink = response.getheader("Location")
if jobCreatedLink == None:
    jobCreatedLink = response.getheader("Link")
    if jobCreatedLink == None:
        jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]
jobID = jobCreatedLink.split("/")[-1]
time.sleep(5)
# Do a GET on a given path
uri =  "/report/Report_" + jobID + ".csv"
try:
    response1 = REDFISH_OBJ.get(uri,None)
except:
    REDFISH_OBJ.logout()
    time.sleep(300)
    exit()
  
if response1.status != 200:
    sys.stdout.write("Unable to download report %s." %uri)
    sys.stdout.write("%s" % response1)
else:
    now = datetime.now()
    # yy_mm_dd_H_M_S
    dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    f = open('BasicDeviceInvenotry_' + dt_string + '.csv', "w")
    f.write(response1.text)
    f.close()
    sys.stdout.write("Successfully downloaded report.")


if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
