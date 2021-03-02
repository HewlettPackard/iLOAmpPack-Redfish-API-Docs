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

# Create and download compliance report

import sys
import redfish
import json
import argparse
import requests
import csv
import time
from datetime import datetime

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--iLOAmpAddress', action='store', required=True, type=str)
my_parser.add_argument('--Username', action='store', required=True, type=str)
my_parser.add_argument('--Password', action='store', required=True, type=str)
my_parser.add_argument('--ServerAddress', action='store', required=True, type=str, nargs='*')
my_parser.add_argument('--BaselineId', action='store', required=True, type=int)
args = my_parser.parse_args()

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

serverVsJobId = dict()
jobList = []
body = dict()
body["BaselineId"] = args.BaselineId

# Do a POST on a given path
for iLOAddress in args.ServerAddress:
    body["SelectedSystemsManagerAddress"] = [iLOAddress]
    try:
        response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.SppComplianceJobs",
                                    body=body)
    except:
        sys.stdout.write("POST request to /redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.SppComplianceJobs failed for server %s\n" % iLOAddress)
        continue

    errMessage = ""
    if response.status != 202:
        sys.stdout.write("Unable to create compliance report for server %s\n" % iLOAddress)
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

    jobCreatedLink = response.getheader("Location")
    if jobCreatedLink == None:
        jobCreatedLink = response.getheader("Link")
        if jobCreatedLink == None:
            jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]

    jobId = jobCreatedLink.split("/")[-1]
    sys.stdout.write("Compliance report job for server %s has been created successfully\n" % iLOAddress)
    serverVsJobId[iLOAddress] = jobId
    jobList.append(jobId)
    
#Checking the status of compliance report
while len(jobList) > 0:
    for jobId in jobList:
        jobCreatedLink = "/redfish/v1/JobService/Jobs/" + jobId
        sys.stdout.write("Job %s is in progress\n" % jobId)
        dstate = "InProgress"
        try:
            managed_system = REDFISH_OBJ.get(jobCreatedLink)
        except:
            sys.stdout.write("GET request to %s failed\n" % jobCreatedLink)
            sys.stdout.write("%s\n" % managed_system)
            continue
        errMessage = ""
        if managed_system.status != 200:
            jobList.remove(jobId)
            continue
        print("managed=", managed_system)
        dstate = managed_system.dict["JobState"]
        if dstate == "Exception":
            jobList.remove(jobId)
        else:
            PercentComplete = managed_system.dict["PercentComplete"]
            if PercentComplete == 100:
                sys.stdout.write("Job %s is in completed\n" % jobId)
                jobList.remove(jobId)
        time.sleep(5)


for serverInfo in serverVsJobId:
    downloadReportUri = "http://" + serverInfo + "/report/ComplianceReport_" + serverVsJobId[serverInfo] + ".csv"
    downloadReportUri = "/report/ComplianceReport_" + serverVsJobId[serverInfo] + ".csv"
    response = REDFISH_OBJ.get(downloadReportUri)
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    fd = open('ComplianceReport_' + current_time + '.csv','w')
    fd.write(response.text)
    fd.close()

# Logout of the current session
REDFISH_OBJ.logout()
