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

# Get running job status

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
my_parser.add_argument('--iLOAmpAddress', action=Once, required=True, type=str)
my_parser.add_argument('--Username', action=Once, required=True, type=str)
my_parser.add_argument('--Password', action=Once, required=True, type=str)
my_parser.add_argument('--OutputFileName', action=Once, type=str)
my_parser.add_argument('--JobId', action=Once, required=True, type=str, nargs='*')
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

# Login into iLO Amplifier Pack and create a session
try:
    REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password, timeout=10, max_retry=3)
except:
    print("Wrong iLO Amplifier Pack address/credential or iLO Amplifier Pack is not reachable\n")
    exit()

# Login into the server and create a session
try:
    REDFISH_OBJ.login(auth="session")
except:
    print("Invalid iLO Amplifier Pack credential\n")
    exit()

jobList = []
if len(args.JobId) == 1 and args.JobId[0].lower() == "all":
    totalJobsListed = 0
    skip = 0
    while True:
        queryString = "/?$skip=%s" % skip
        getRunningJob = "/redfish/v1/JobService/Jobs" + queryString

        try:
            managed_system = REDFISH_OBJ.get(getRunningJob)
        except:
            sys.stdout.write("GET request to %s failed\n" % getRunningJob)
            REDFISH_OBJ.logout()
            exit()
        if managed_system.dict["Members@odata.count"] == 0:
            sys.stdout.write("iLO Amplifier Pack doesn't have any jobs to show\n")
            REDFISH_OBJ.logout()
            exit()

        for jobInfo in managed_system.dict["Members"]:
            jobList.append(jobInfo["Id"])
            totalJobsListed += 1
            skip += 1
        if managed_system.dict["Members@odata.count"] <= totalJobsListed:
            break
else:
    jobList = args.JobId

if jobList == []:
    sys.stdout.write("JobId's are needed in script and not provided by user\n")
    REDFISH_OBJ.logout()
    exit()
for jobId in jobList:
    jobCreatedLink = "/redfish/v1/JobService/Jobs/" + jobId
    sys.stdout.write("******** jobId %s ********\n" % jobId)
    dstate = "InProgress"
    try:
        managed_system = REDFISH_OBJ.get(jobCreatedLink)
    except:
        sys.stdout.write("GET request to %s failed\n" % jobCreatedLink)
        sys.stdout.write("%s\n" % managed_system)
        continue
    if managed_system.status != 200:
        sys.stdout.write("Unable to get status of running job with jobId %s\n" % jobId)
        sys.stdout.write("status code %s\n" % managed_system.status)
        sys.stdout.write("Please re-check jobId\n")
        continue

    outputMessage = ""
    dstate = managed_system.dict["JobState"]
    try:
        for outputStr in managed_system.dict["Messages"][0]["MessageArgs"]:
            outputMessage += outputStr + ", "
    except:
        pass
    if dstate == "Exception":
        sys.stdout.write("JobId = %s, JobState = Exception\n" % jobId)
    else:
        PercentComplete = managed_system.dict["PercentComplete"]
        sys.stdout.write("JobId = %s, JobState = %s, PercentComplete %s\n" % (jobId, dstate, PercentComplete))
    sys.stdout.write("Name: %s, Message: %s\n" % (managed_system.dict["Name"], outputMessage))
    time.sleep(1)

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
