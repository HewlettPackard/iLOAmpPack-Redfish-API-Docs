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

# Get redfish subscribers information

import sys
import redfish
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
my_parser.add_argument('--iLOAmpAddress', action='store', required=True, type=str)
my_parser.add_argument('--Username', action='store', required=True, type=str)
my_parser.add_argument('--Password', action='store', required=True, type=str)
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

# Do a GET on a given path
uri = "/redfish/v1/EventService/Subscriptions/"
try:
    response = REDFISH_OBJ.get(uri)
except:
    print("exception for get request %s\n" %uri)
    REDFISH_OBJ.logout()
    exit()

if response.status != 200:
    sys.stdout.write("Failed to get subscriber information\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

subscriber_Count = response.dict["Members@odata.count"]
if subscriber_Count > 0:
  subscriber_Info = response.dict["Members"]
  for subscriber in subscriber_Info:
      uri = subscriber["@odata.id"]
      try:
          response = REDFISH_OBJ.get(uri)
      except:
          print("exception for get request %s\n" % uri)
      events = ""
      eventTypes = response.dict["EventTypes"]
      for eventName in eventTypes:
        events += eventName + " "
      sys.stdout.write("SubscriberInfo destination=%s AlertType=%s Protocol=%s SubscriberId=%s\n" % (response.dict["Destination"], events, response.dict["Protocol"], response.dict["Id"]))
else:
    sys.stdout.write("No Subscribers found\n")


# Logout of the current session
REDFISH_OBJ.logout()
