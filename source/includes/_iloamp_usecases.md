# Use Cases

This section covers the basic use cases of RESTful APIs provided by iLO Amplifier Pack

## Discovering Servers

The discovery APIs allow users to add assets to manage with iLO Amplifier Pack. These APIs allow users to discover individual servers, servers in iLO Federation groups, servers within an IPv4 range, and servers listed in CSV file.

## Adding a single server

```shell
curl https://{iLOAmpServer}//redfish/v1/AggregatorService/ManagedSystems/ 
  -H "Content-Type: application/json" 
  -X POST 
  --data "@data.json"  
  -u username:password 
  --insecure
```
<blockquote class="lang-specific shell">
	<p>Contents of data.json file </p>
    <p><code>
    {<br>
    "ManagerAddress":"{iLOAddress}",</br>
    "UserName":"{iLOUsername}",</br>
    "Password":"{iLOPassword}"</br>
    }</br>
    </code></p>
</blockquote>
```python
# Discovering a server
import sys
import redfish
import time

# When running remotely connect using the address, account name, 
# and password to send https requests
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

## Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

body = dict()
body["ManagerAddress"] = "{iLOAddress}"
body["UserName"] = "{iLOUsername}"
body["Password"] = "{iLOPassword}"

# Do a GET on a given path
sys.stdout.write("Adding server %s.\n" % body["ManagerAddress"])
response = REDFISH_OBJ.post("/redfish/v1/AggregatorService/ManagedSystems/", body=body)

location = None
slash = 0

if response.status == 201:
    location = response.getheader("Location")

if location is None:
    sys.stdout.write("Unable to add server.\n")
    sys.stdout.write("%s\n" % response)

# find the 3rd slash in location
slash = location.find("/", slash)
slash = location.find("/", slash+2)
location = location[slash:]
sys.stdout.write("location: %s\n" % location)

dstate = "InProgress"

while dstate != "Complete":
    managed_system = REDFISH_OBJ.get(location)
    if managed_system.status != 200:
        sys.stdout.write("Unable to get status of discovery.\n")
        sys.stdout.write("%s\n" % managed_system)
        break
    dstate = managed_system.dict["SystemSummary"]["Discovery"]["State"]
    sys.stdout.write("Discovery %s.\n" % dstate)
    time.sleep(1)
 
# Logout of the current session
REDFISH_OBJ.logout()
```

The `/redfish/v1/AggregatorService/ManagedSystems` collection lists all the servers managed by iLO Amplifier Pack. Performing a `POST` on this collection adds a server in iLO Amplifier Pack. When `POST` is performed on this URI, the response header contains the `Location` and `Link` of the newly added server. A `GET` on the link will retrive the discovery state of the server. The discovery state of the server can be one of the following:

* NotInitiated
* Processing
* InProgress
* Complete
* NotResponding
* NotReachable
* FirmwareUpdateInProgress
* Discovered
* Refreshing

## Viewing the information of a managed server

When a server is added, iLO Amplifier Pack performs a detailed inventory of the server. The process takes few seconds for a server. Once the inventory is complete, the various information of the server can be obtained. Performing a GET on the below Redfish APIs obtains the server information.

Inventory | URI
----------|-----
System Overview | /redfish/v1/Systems/{item}
CPU Details  | /redfish/v1/Systems/{item}/Processor/{item}
Memory Detials | /redfish/v1/Systems/{item}/Memory/{item}
PCIe Devices | /redfish/Systems/{item}/PCIeDevices
Chassis | /redfish/v1/Chassis/{item}
Fan Details | /redfish/v1/Chassis/{item}/Thermal
Power Details | /redfish/v1/Chassis/{item}/Power
Storage | /redfish/v1/Systems/{item}/Storage
iLO Details | /redfish/v1/Managers/{item}
Firmware Inventory | /redfish/v1/UpdateService/FirmwareInventory
Software Inventory | /redfish/v1/UpdateService/SoftwareInventory

## Adding range of Servers

```shell
curl https://{iLOAmpServer}//redfish/v1/AggregatorService/Actions/HpeWfmAggregatorService.DiscoverServersInRange/ 
  -H "Content-Type: application/json" 
  -X POST 
  --data "@data.json"  
  -u username:password 
  --insecure
```
<blockquote class="lang-specific shell">
	<p>Contents of data.json file </p>
    <p><code>
    {</br>
    "StartAddress":"{IP_Address_Range_Start}", </br>
    "EndAddress":"{IP_Address_Range_End}", </br>
    "UserName":"username", </br>
    "Password":"password", </br>
    "PortNumber":443 </br>
    }</br>
    </code></p>
</blockquote>
```python

# Discovering a server
import sys
import redfish
import time

# When running remotely connect using the address, account name, 
# and password to send https requests
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

## Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

body = dict()
body["StartAddress"] = "{IP_Address_Range_Start}"
body["EndAddress"] = "{IP_Address_Range_End}"
body["PortNumber"] = 443
body["UserName"] = "username"
body["Password"] = "password"

# Do a GET on a given path
sys.stdout.write("Adding servers in range %s to %s.\n" % (body["StartAddress"], body["EndAddress"]))
response = REDFISH_OBJ.post("/redfish/v1/AggregatorService/Actions/HpeWfmAggregatorService.DiscoverServersInRange/", body=body)

location = None
slash = 0

if response.status != 202:
    sys.stdout.write("Unable to initiate discovering servers in range.")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

dstate = "InProgress"

while dstate != "Complete" and dstate != "Successful":
    managed_system = REDFISH_OBJ.get("/redfish/v1/AggregatorService/")
    if managed_system.status != 200:
        sys.stdout.write("Unable to get status of IP range discovery.\n")
        sys.stdout.write("%s\n" % managed_system)
        break
    dstate = managed_system.dict["ActionStatus"]["DiscoverServersInRange"]["DiscoveryStatus"]
    sys.stdout.write("Discovery %s.\n" % dstate)
    time.sleep(1)
 
# Logout of the current session
REDFISH_OBJ.logout()
```

iLO Amplifier Pack allows users to discover more than one server at a time. Using IP range discovery, iLO Amplifier Pack can discover multiple servers simultaneously. The IP range discovery is advertised as an aciton on `/redfish/v1/AggregatorService` URI. 

Once the action is triggered, the IP range discovery is performed as a task by iLO Amplifier. The discovery process can take a while to complete. In order to know the progress of the discovery status, perform a GET on `/redfish/v1/AggregatorService` URI and look at the `ActionStatus.DiscoverServersInRange` object. The `DiscoveryStatus` field will be set to `Complete` once the discovery process is complete.


