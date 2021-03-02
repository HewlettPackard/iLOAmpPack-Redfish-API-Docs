# Use Cases

This section covers the basic use cases of RESTful APIs provided by iLO Amplifier Pack.

## Discovering Servers

The discovery APIs allow users to add assets to manage with iLO Amplifier Pack. These APIs allow users to discover individual servers, servers in iLO Federation groups, servers within an IPv4 range, and servers listed in a CSV file.

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
sys.stdout.write("Adding server %s\n" % body["ManagerAddress"])
response = REDFISH_OBJ.post("/redfish/v1/AggregatorService/ManagedSystems/", body=body)

location = None
slash = 0

if response.status == 201:
    location = response.getheader("Location")

if location is None:
    sys.stdout.write("Unable to add server\n")
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
        sys.stdout.write("Unable to get status of discovery\n")
        sys.stdout.write("%s\n" % managed_system)
        break
    dstate = managed_system.dict["SystemSummary"]["Discovery"]["State"]
    sys.stdout.write("Discovery %s\n" % dstate)
    time.sleep(1)
 
# Logout of the current session
REDFISH_OBJ.logout()
```

The `/redfish/v1/AggregatorService/ManagedSystems` collection lists all the servers managed by iLO Amplifier Pack. Performing a `POST` on this collection adds a server in iLO Amplifier Pack. When `POST` is performed on this URI, the response header contains the `Location` and `Link` of the newly added server. A `GET` on the link will retrieve the discovery state of the server. The discovery state of the server can be one of the following:

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

When a server is added, iLO Amplifier Pack performs a detailed inventory of the server which takes a few seconds. Once the inventory is complete, different server information can be obtained. Performing a GET on the below Redfish APIs obtains the corresponding server information.

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

## Adding a range of Servers

```shell
curl https://{iLOAmpServer}/redfish/v1/AggregatorService/Actions/HpeWfmAggregatorService.DiscoverServersInRange/ 
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
sys.stdout.write("Adding servers in range %s to %s\n" % (body["StartAddress"], body["EndAddress"]))
response = REDFISH_OBJ.post("/redfish/v1/AggregatorService/Actions/HpeWfmAggregatorService.DiscoverServersInRange/", body=body)

location = None
slash = 0

if response.status != 202:
    sys.stdout.write("Unable to initiate discovering servers in range\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

dstate = "InProgress"

while dstate != "Complete" and dstate != "Successful":
    managed_system = REDFISH_OBJ.get("/redfish/v1/AggregatorService/")
    if managed_system.status != 200:
        sys.stdout.write("Unable to get status of IP range discovery\n")
        sys.stdout.write("%s\n" % managed_system)
        break
    dstate = managed_system.dict["ActionStatus"]["DiscoverServersInRange"]["DiscoveryStatus"]
    sys.stdout.write("Discovery %s\n" % dstate)
    time.sleep(1)
 
# Logout of the current session
REDFISH_OBJ.logout()
```

iLO Amplifier Pack allows users to discover more than one server at a time. Using IP range discovery, iLO Amplifier Pack can discover multiple servers simultaneously. The IP range discovery is advertised as an action on `/redfish/v1/AggregatorService` URI. 

Once the action is triggered, the IP range discovery is performed as a task by iLO Amplifier Pack. The discovery process can take a while to complete. To know the progress of the discovery status, perform a GET on `/redfish/v1/AggregatorService` URI and look at the `ActionStatus.DiscoverServersInRange` object. The `DiscoveryStatus` field will be set to `Complete` once the discovery process is complete.

## Performing Jobs

```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.RefreshJob/ 
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
      "SelectedSystemsManagerAddress": [</br>
	    "{Manager1_IP_Address}",</br>
	    "{Manager2_IP_Address}"</br>
	  ]</br>
    }</br>
    </code></p>
</blockquote>
```python

# Perform refresh of servers job
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
sel_sys = body["SelectedSystemsManagerAddress"] = list()
sel_sys.append("{Manager1_IP_Address}")
sel_sys.append("{Manager2_IP_Address}")

# Perform a POST to trigger the action
sys.stdout.write("Refreshing %d servers\n" % (len(body["SelectedSystemsManagerAddress"])))
response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.RefreshJob/", body=body)

location = None
slash = 0

if response.status != 202:
    sys.stdout.write("Unable to initiate refresh of servers\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

# Extract the newly created job
refresh_job_uri = response.dict["error"]["@Message.ExtendedInfo"][0]["MessageArgs"][0]

# Check for the job status
dstate = "InProgress"

while dstate != "Completed" and dstate != "Successful":
    refresh_job = REDFISH_OBJ.get(refresh_job_uri)
    if refresh_job.status != 200:
        sys.stdout.write("Unable to get status of refresh job\n")
        sys.stdout.write("%s\n" % refresh_job)
        break
    dstate = refresh_job.dict["JobState"]
    sys.stdout.write("Refreshing servers %s\n" % dstate)
    time.sleep(1)
 
# Logout of the current session
REDFISH_OBJ.logout()
```

iLO Amplifier Pack v1.50 introduces the JobService and Jobs API. Users can create a job by performing a `POST` action on the URIs listed in JobService. A Job can be initiated on multiple servers at a time by specifiying the manager address of the systems or by specifying the group name in which case the job will run on the servers in the group. Below are the list of jobs that can be performed.

| Jobs | Description |
|------|-------------|
|AhsDownloadJobs|Download AHS files from the specified systems|
|ApplyConfigurationBaselineJobs|Apply a configuration baseline on specified systems|
|AssignRecoveryPolicyJob|Assign a recovery policy for specified systems|
|ConfigureRemoteSyslogJobs|Configure remote syslog of the iLO for specified systems|
|CreateGroupJobs|Create a federation group on iLO for specified systems|
|DeleteCompletedJobs|Delete completed jobs from the appliance|
|DeleteJobs|Remove managed systems from the appliance|
|DownloadAuditLogsJobs|Download audit logs from the appliance|
|DownloadReportJobs|Download report for specified systems|
|ExcludeServersFromInfoSight|Exclude systems from sending data to HPE InfoSight|
|ImportBaselineJobs|Import a firmware basline into the appliance|
|ImportConfigurationBaselineJobs|Import a configuration baseline from a system|
|ImportOSBaselineJobs|Import an OS baseline into the appliance|
|ManualRecoveryJobs|Initiate a recovery job on selected systems|
|OnDemandAhsJobs|Send AHS logs to HPE InfoSight for selected systems|
|RefreshJob|Refresh the inventory for selected systems|
|ResetSystemJobs|Perform power actions on selected systems|
|ServerGroupActionJobs|Perform actions on server groups|
|ServerUpdateJobs|Perform fimrware/software update on selected systems|
|SetIndicatorLedJobs|Change indicator LED status on selected systems|
|SppComplianceJobs|Peform SPP compliance for selected systems|
|UnAssignRecoveryPolicyJob|Unassign recovery policy for specified systems|
|UpdateFirmwareJobs|Update core platform firmware on selected systems|
|VirtualMediaJobs|Mount or unmount virtual media on selected systems|

When any of the above actions are performed, iLO Amplifier Pack creates a Job and the response body of the action specifies the URI for the job. A job may take a while to complete. In order to know the status of the job, perform a `GET` on the job URI. The `JobState` property in the job resource specifies if the job is completed or not.

## Creating a Server Group
```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs 
-H "Content-Type: application/json" 
-X POST 
--data "@data.json" 
-u admin:admin 
--insecure
```
<blockquote class="lang-specific shell">
	<p>Contents of data.json file </p>
    <p><code>
    {<br>
    "Name":"{groupName}",</br>
    "ServerList":"{serversList}",</br>
    "OperationType":"{operationType}",</br>
    "GroupDescription":"{groupDescription}"</br>
    }</br>
    </code></p>
</blockquote>
```python
import sys
import redfish

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

body = dict()
body["Name"] = "{GroupName}"
body["ServerList"] = "{ServerList}"
body["OperationType"] = "{CreateGroup}"
body["GroupDescription"] = "{description}"

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs", body=body)

if response.status != 202:
    sys.stdout.write("Unable to create server group\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

# Logout of the current session
REDFISH_OBJ.logout()
```
Performing a `GET` operation on the  `/redfish/v1/AggregatorService/ManagedServerGroups` collection, will list all the Server Groups created in iLO Amplifier Pack. 

**Prerequisites**  
Users with the following privileges can create a Server Group:

* Configure Manager with Security
* Configure Manager
* Configure User
* Configure Devices

**Performing the Job**  
To create a new Server Group, perform a `POST` operation on the `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs` action, with the folowing properties:

| Property | Type | Description |
| --- | --- | --- |
| **GroupDescription** | string | The description of the group that is to be created |
| **Name** | string | The name of the group that is to be created |
| **OperationType** | string | The type of operation to be performed on the group. Value for this action will be "CreateGroup" |
| **ServerList** | array | The list of servers to add to the group |

Sample payload is as shown below:

{
&nbsp;&nbsp;`"GroupDescription`": "Group1",  
&nbsp;&nbsp;&nbsp;&nbsp;`"Name"`: "Group1",  
&nbsp;&nbsp;&nbsp;&nbsp;`"OperationType"`: "CreateGroup",  
&nbsp;&nbsp;&nbsp;&nbsp;`"ServerList"`: ["123.123.12.12", "123.123.12.15"]  
}

 When `POST` operation is performed on this URI, a job will be created. A `GET` operation on the URI `/redfish/v1/JobService/Jobs/{jobID}` will retrieve the state of the job created. 

When the job has successfully completed, all the groups added can be viewed by performing a `GET` operation on the URI `/redfish/v1/AggregatorService/ManagedServerGroups`.

## Group Actions
```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupActionJobs 
-H "Content-Type: application/json" 
-X POST 
--data "@data.json" 
-u admin:admin 
--insecure
```
```python
import sys
import redfish

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

OperationType = "{OperationType}"
body = dict()
body["GroupName"] = "{GroupName}"
body["AllSystemsInGroup"] = "{boolValue}"
body["OperationType"] = OperationType
if OperationType.lower() == "refreshgroup":
    body["OperationType"] = "RefreshGroup"
elif OperationType.lower() == "deletegroup":
    body["OperationType"] = "DeleteGroup"
elif OperationType.lower() == "uid":
    body["IndicatorLED"] = "{IndicatorLED}"
    body["OperationType"] = "UID"
elif OperationType.lower() == "power":
    body["OperationType"] = "Power"
    body["ResetType"] = "{ResetType}"

# Do a POST on a given path

response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupActionJobs", body=body)

if response.status != 202:
    sys.stdout.write("Unable to perform server group action\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

sys.stdout.write("Group action job has been created successfully\n")

# Logout of the current session
REDFISH_OBJ.logout()
```
**Prerequisites**  
Users with the following privileges can perform actions on the Server Group:

* Configure Manager with Security
* Configure Manager
* Configure User
* Configure Devices

**Performing the Job**  
The following actions can be performed on all the servers in a Server Group:

**1.  Managing UID status**  
The UID status for all the servers in a Server Group can be changed by performing a `POST` operation on the URI `redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupActionJob` with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **GroupDescription** | string | The name of the group on which action is to be performed |
| **OperationType** | string | The action to be performed on the group. Value for this action will be "UID" |
| **AllSystemsInGroup** | boolean | This flag suggests whether all the servers in the group are selected |
| **IndicatorLED** | string | The Indicator State of the UID to which it needs to be changed |

Sample payload is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"GroupName"`: "Group1",   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"OperationType"`: "UID",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"AllSystemsInGroup"`: true,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"IndicatorLED"`: "UID"  
}

**2. Managing Power Status**  
The Power status for all the servers in a Server Group can be changed by performing a `POST` operation on the URI `redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupActionJob` with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **GroupName** | string | The name of the group on which action is to be performed |
| **OperationType** | string | The action to be performed on the group. Value for this action will be "Power" |
| **AllSystemsInGroup** | boolean | This flag suggests whether all the servers in the group are selected |
| **ResetType** | string | The reset type to be performed for the system |

Sample payload is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"GroupName"`: "Group1",,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"OperationType"`: "Power",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"AllSystemsInGroup"`: true,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"ResetType"`: "On"  
}

**3.  Refresh**  
Refresh of all the servers in a Server Group can be performed by a `POST` operation on the URI `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupActionJob/` with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **Name** | string | The name of the group that is to be created or joined to |
| **OperationType** | string | The action to be performed on the group. Value for this action will be "RefreshGroup" |
| **AllSystemsInGroup** | boolean | This flag suggests whether all the servers in the group are selected |

Sample payload is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Name"`: "Group1",   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"OperationType"`:"RefreshGroup",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"AllSystemsInGroup"`:true    
}

**4.  Deletion**  
Deletion of all the servers of a Server Group can be performed by a `POST` operation on the URI `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupActionJob/` with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **Name** | string | The name of the group that is to be deleted |
| **OperationType** | string | The action to be performed on the group. Value for this action will be "DeleteGroup" |
| **DeleteServers** | boolean | This flag specifies if Servers in the group should be deleted |

Sample payload is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Name"`: "Group1",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"OperationType"`:"DeleteGroup",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"DeleteServers"`:true     
}

**Post Condition:**  

When `POST` operation is performed on the above URIs for different actions, jobs are created. A `GET` operation on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created.

The results of these jobs can be checked by performing a `GET` operation on `/redfish/v1/JobService/Results/ServerGroupActionJobs/{jobID}/1/`

## Join Server Group
```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs 
-H "Content-Type: application/json" 
-X POST 
--data "@data.json"  
-u admin:admin 
--insecure
```
<blockquote class="lang-specific shell">
	<p>Contents of data.json file </p>
    <p><code>
    {<br>
    "Name":"{groupName}",</br>
    "ServerList":"{serversList}",</br>
    "OperationType":"{operationType}"</br>
    }</br>
    </code></p>
</blockquote>
```python
import sys
import redfish
import time
import json

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

body = dict()
body["Name"] = "{GroupName}"
body["ServerList"] = "{ServerAddress}"
body["OperationType"] = "{JoinGroup}"

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs", body=body)

errMessage = ""
if response.status != 202:
    sys.stdout.write("Unable to join the server into the group\n")
    sys.stdout.write("Response %s\n" % response)
    REDFISH_OBJ.logout()
    exit()

jobCreatedLink = response.getheader("Location")
if jobCreatedLink == None:
    jobCreatedLink = response.getheader("Link")
    if jobCreatedLink == None:
        jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]

jobID = jobCreatedLink.split("/")[-1]
sys.stdout.write("Join Server group job has been created successfully\n")
sys.stdout.write("check job status using jobID %s\n" % jobID)

# Logout of the current session
REDFISH_OBJ.logout()
```
**Prerequisites**  

Users with the following privileges can Join Servers to a Group:
* Configure Manager with Security
* Configure Manager
* Configure User
* Configure Devices

**Performing the Job:**  
To add servers to an existing Server Group, perform a `POST` operation on the URI `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs/` with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **Name** | string | The name of the group that is to be joined to |
| **OperationType** | string | The action to be performed on the group. Value for this action will be "JoinGroup" |
| **ServerList** | array | All the selected servers to join to the group |

Sample payload is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Name"`: "Group1",   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"OperationType"`:"JoinGroup",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"ServerList"`:["123.123.12.12", "123.123.12.15"]   
}

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created.

When the Job has successfully completed, the servers that belong to a Server Group can be obtained by doing a `GET` operation  on the URI `/redfish/v1/AggregatorService/ManagedServerGroups/{groupName}/ManagedSystems/Summary/` to check if the servers have been added to the group.

##Unjoin Server Group
```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs 
-H "Content-Type: application/json" 
-X POST 
--data "@data.json"  
-u admin:admin 
--insecure
```
<blockquote class="lang-specific shell">
	<p>Contents of data.json file </p>
    <p><code>
    {<br>
    "Name":"{groupName}",</br>
    "ServerList":"{serversList}",</br>
    "OperationType":"{operationType}"</br>
    }</br>
    </code></p>
</blockquote>

```python
import sys
import redfish
import time
import json

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

body = dict()
body["Name"] = "{GroupName}"
body["ServerList"] = "{ServerAddress}"
body["OperationType"] = "{UnjoinGroup}"

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs", body=body)

errMessage = ""
if response.status != 202:
    sys.stdout.write("Unable to unjoin server from group\n")
    sys.stdout.write("Response %s\n" % response)
    REDFISH_OBJ.logout()
    exit()

jobCreatedLink = response.getheader("Location")
if jobCreatedLink == None:
    jobCreatedLink = response.getheader("Link")
    if jobCreatedLink == None:
        jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]

jobID = jobCreatedLink.split("/")[-1]
sys.stdout.write("Unjoin Server from group job has been created successfully\n")
sys.stdout.write("check job status using jobID %s\n" % jobID)

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
```
**Prerequisites**  
Users with the following privileges can Unjoin Servers from a Server Group:
* Configure Manager with Security
* Configure Manager
* Configure User
* Configure Devices

**Performing the Job:**  
To unjoin servers from an existing Server Group, perform a `POST` operation on the URI `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerGroupJobs` with the following properties:

| Property | Type | Description |
| --- | --- | --- |
| **Name** | string | The name of the group from which servers are to be unjoined|
| **OperationType** | string | The action to be performed on the group. Value for this action will be "UnjoinGroup" |
| **ServerList** | array | All the selected servers to unjoin from a group |

Sample payload is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;`"Name"`: "Group1",   
&nbsp;&nbsp;&nbsp;&nbsp;`"OperationType"`:"UnjoinGroup",  
&nbsp;&nbsp;&nbsp;&nbsp;`"ServerList"`:["123.123.12.12", "123.123.12.15"]    
}

When `POST` operation is performed on this URI, a job will be created. A `GET` operation on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created. 


When the Job has successfully completed, the servers that belong to a Server Group be obtained by performing a `GET` operation on the URI `/redfish/v1/AggregatorService/ManagedServerGroups/{groupName}/ManagedSystems/Summary/` to check if the servers have been removed from the group.

## Importing a firmware baseline 

```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ImportBaselineJobs/    
    -H "Content-Type: application/json" 
    -X POST 
    --data "@data.json" 
    -u admin:admin 
    --insecure
```

```python
import sys
import redfish
import time
import json

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

body = dict()
body["SourcePath"] = args.SourcePath
body["StorageType"] = args.StorageType

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ImportBaselineJobs", body=body)

errMessage = ""
if response.status != 202:
    sys.stdout.write("Unable to import baseline\n")
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
sys.stdout.write("Import baseline job has been created successfully\n")
sys.stdout.write("check job status using jobId %s\n" % jobId)

if args.OutputFileName != None:
    sys.stdout.close()

# Logout of the current session
REDFISH_OBJ.logout()
```
The `/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/` collection lists all the Firmware Baselines imported to iLO Amplifier Pack.  

**Prerequisite**  

- iLO Amplifier Pack supports up to 80 GB of baseline storage (which includes both firmware, OS baseline files and components downloaded from InfoSight). Please ensure that required space is available before importing any SPP.
- Users with the following privileges can import a firmware baseline:
    - Configure Manager with Security
    - Configure Manager
    - Configure User
    - Configure Devices

**Performing Job**

Firmware baseline can be imported with the following methods:

**1)Network Share (NFS)**

Perform a `POST` operation on the `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ImportBaselineJobs/` action. 

|Property|Type|Description|
|--------|----|-----------|
|**StorageType**| string| Type of storage on which the SPP Image is available. Value should be "NetworkShare".|
|**SourcePath** |string | Path to the SPP ISO file. This could be an http/https path or a normal file path.|
|**NetworkShareAddress** |string | Network share IP address or DNS name where the SPP ISO Image is hosted.|
|**MountPath** |string | Mount path of the network share server where the SPP ISO Image is hosted.|

Sample payload is as shown below:  
{  
&nbsp;&nbsp;&nbsp;&nbsp;"StorageType": "NetworkShare",  
&nbsp;&nbsp;&nbsp;&nbsp;"SourcePath": "",  
&nbsp;&nbsp;&nbsp;&nbsp;"NetworkShareAddress": "",  
&nbsp;&nbsp;&nbsp;&nbsp;"MountPath": ""  
}  

**2)HTTP/HTTPS Share**

Perform a `POST` operation on the `redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ImportBaselineJobs/` action. 

|Property|Type|Description|
|--------|----|-----------|
|**StorageType**| string| Type of storage on which the SPP Image is available. Value should be "HttpPath".|
|**SourcePath** |string | Path to the SPP ISO file. This could be an http/https path or a normal file path.|
|**NetworkShareAddress** |string | Network share IP address or DNS name where the SPP ISO Image is hosted.|
|**MountPath** |string | Mount path of the network share server where the SPP ISO Image is hosted.|

Sample payload is as shown below:  
{  
&nbsp;&nbsp;&nbsp;&nbsp;"StorageType": ""HttpPath"",  
&nbsp;&nbsp;&nbsp;&nbsp;"SourcePath": "",  
}  

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created.

## Firmware and driver updates for Gen9 servers

```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs
-H "Content-Type: application/json"
-X POST
--data "@data.json"
-u admin:admin
--insecure
```
```python
# Gen9_Server_Update
import sys
import redfish

 

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

 

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

 

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

 

body = dict()
body["OperationStrategy"] = "{OperationStrategy}"
if body["OperationStrategy"] != "DeployOnly":
  body["BaselineID"] = "{BaselineID}"
body["BatchSize"] = "{BatchSize}"
body["CleanUpRepository"] = "{boolValue}"
body["OperationType"] = "{OperationType}"

 

if body["OperationStrategy"] == "StageAndDeploy":
    if body["OperationType"] == "LegacyOffline":
        body["DowngradeFlag"] = False
        body["ResetFlag"] = False
    else:
        body["ResetFlag"] = False
        body["DowngradeFlag"] = False
elif body["OperationStrategy"] == "StageOnly":
    body["DowngradeFlag"] = False
    body["ResetFlag"] = False
else:
  body["ResetFlag"] = False
  body["CleanUpRepository"] = False

 

body["SelectedSystemsManagerAddress"] = "{updateServerList}"
ManagerCredentials = dict()
ManagerCredentials["UserName"] = ""
ManagerCredentials["Password"]: ""
body["ManagerCredentials"] = ManagerCredentials
body["UseExternalWebServer"] = False

 

response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs", body=body)

 

if response.status != 202:
    sys.stdout.write("Unable to update gen 9 server\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

 

sys.stdout.write("Gen9 server update job has been created successfully\n")

 

# Logout of the current session
REDFISH_OBJ.logout()
```
Firmware and driver updates for Gen9 servers can be performed on selected servers of type iLO4 using below methods:
- Online Method
- Offline Method


**Offline Method**


**Prerequisite**

- Bootable baseline ISO image of the firmware update imported into iLO Amplifier Pack. (Please refer to Importing a Firmware Baseline use case) / Bootable baseline ISO image of the firmware update extracted to a shared HTTP/HTTPS location on the network and a dedicated web server for hosting SPP (HPE Support Pack for ProLiant) ISO images and files.  
- Firmware and driver updates can be triggered only on supported server models. Please refer to user guide (Server firmware and driver updates chapter) for more details.  
- Servers managed by HPE OneView or vCenter Lifecycle Manager (vLCM) cannot be updated by iLO Amplifier.  
- iLO Advanced License is required to perform an update.  
- Users with the following privileges can import a firmware baseline.   
    - Configure Manager with Security
    - Configure Manager
    - Configure User
    - Configure Devices


**Payload Properties for an Update**

|Property|Type|Description|  
|--------|----|-----------|  
|**SelectedSystemsManagerAddress**| array| An array of servers selected to perform server updates.| 
|**UseExternalWebServer** |boolean | Specifies whether to use external webserver or to use the internal webserver to host baselines. True if you want to use external web server else false.| 
|**BaselineID** | number | Specifies the ID of the imported Baseline.| 
|**BaselineUri** |string | The URL of the SPP baseline extracted ISO image.| 
|**BaselineUriISO**| string| The URL of the SPP baseline ISO image.| 
|**OperationType** |string | Specifies the type of operation to be performed for an update. Values for this property field can be "iLORepositoryOnline", "LegacyOnlineBaselineAutomatic", "iLORepositoryOffline", "iLORepositoryOffline". | 
|**OperationStrategy** |string | Specifies the kind of operation to be performed during an online update. Values for this property field can be "StageAndDeploy", "StageOnly" and "DeployOnly".| 
|**ResetFlag** |boolean | Specified whether to reboot the server during an update if required.| 
|**DowngradeFlag**| boolean | Support downgrade.True-support,false-not support.| 
|**CleanUpRepository** |boolean | Specifies whether to delete the uploaded components from repository after the update.| 
|**ForceInstall** |boolean | HPSUM performs a forcible upgrade or downgrade of the firmware and drivers in the baseline when set to true.| 
|**MediaPath** |string | The URL of the baseline ISO image.| 
|**BatchSize** |number | The batch size of the update which is, number of parallel updates supported.| 
|**ManagerCredentials** |string | Username and Password to be provided only in case of federated nodes.|


**Performing Job**: 

Offline Updates of iLO4 supports only "Stage and Deploy" strategy. To update a server of type iLO4, perform a `POST` operation on `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/` action. 

  
Sample payload for imported baseline is as shown below: 

{  
&nbsp;&nbsp;&nbsp;&nbsp;"SelectedSystemsManagerAddress": [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress1, 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress2, .  
&nbsp;&nbsp;&nbsp;&nbsp;],  
&nbsp;&nbsp;&nbsp;&nbsp;"ManagerCredentials": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"UserName": "",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Password": ""  
&nbsp;&nbsp;&nbsp;&nbsp;},  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationStrategy": "StageAndDeploy",  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationType": "LegacyOffline",  
&nbsp;&nbsp;&nbsp;&nbsp;"ResetFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"DowngradeFlag": true/false,  
&nbsp;&nbsp;&nbsp;&nbsp;"CleanUpRepository": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"BaselineID": ,  
&nbsp;&nbsp;&nbsp;&nbsp;"BatchSize": (Any value between 10-30),  
&nbsp;&nbsp;&nbsp;&nbsp;"UseExternalWebServer": false  
}  

Sample payload for using external web server is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;"SelectedSystemsManagerAddress": [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress1,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress2, .  
&nbsp;&nbsp;&nbsp;&nbsp;],  
&nbsp;&nbsp;&nbsp;&nbsp;"ManagerCredentials": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"UserName": "",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Password": ""  
&nbsp;&nbsp;&nbsp;&nbsp;},  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationStrategy": "StageAndDeploy",  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationType": "LegacyOffline",  
&nbsp;&nbsp;&nbsp;&nbsp;"ResetFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"DowngradeFlag": true/false,  
&nbsp;&nbsp;&nbsp;&nbsp;"CleanUpRepository": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"BatchSize": (Any value between 10-50),  
&nbsp;&nbsp;&nbsp;&nbsp;"UseExternalWebServer": true  
&nbsp;&nbsp;&nbsp;&nbsp;"MediaPath": ""  
}

**NOTE**

1) `"BaselineID"` to be used for server update can be retrieved by performing a `GET` on `/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/`.  
2) Up to 30 parallel updates are supported if an imported baseline is used. Up to 50 parallel updates are supported if external webserver is selected.  
3) Other actions like Power toggling, Virtual Media Mounting etc. Cannot be performed on the selected servers being used for updates.  

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created and the following states will appear in progression:

- Pending
- Staging
- Staged
- Installing
- Installed
- Installed Pending Reboot
- Activated

Please refer to iLO Amplifier Pack user Guide for more information.

**Online Method (Baseline Automatic)**

**Prerequisite**

Refer to the prerequisites of offline method. Additional requirements for an online update are:

- Please refer iLO Amplifier User Guide (servers ad firmware updates chapter) for supported OSes, and iLO f/w version and SUT version details.  
- SUT Mode should be in either "AutoDeploy" or "AutoDeployReboot" or "AutoStage" mode.  
- SUT Service should always be running.  
- AMS Status should be "Complete". 
- AMS Version should be greater than 10.7 for Windows and 2.6.1 for Linux.

**Performing Job**

Baseline Automatic Online Updates of iLO4 supports three different strategies, namely:

- **Stage Only**

To stage firmware and driver components on selected servers, perform a `POST` operation on `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/` action.

Sample payload for imported baseline is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;"SelectedSystemsManagerAddress": [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress1,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress2,  
&nbsp;&nbsp;&nbsp;&nbsp;],  
&nbsp;&nbsp;&nbsp;&nbsp;"ManagerCredentials": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"UserName": "",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Password": ""  
&nbsp;&nbsp;&nbsp;&nbsp;},  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationStrategy": "StageOnly",  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationType": "LegacyOnlineBaselineAutomatic",  
&nbsp;&nbsp;&nbsp;&nbsp;"ResetFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"DowngradeFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"CleanUpRepository": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"BaselineID": ,  
&nbsp;&nbsp;&nbsp;&nbsp;"BatchSize": Any value ranging between 10-30,  
&nbsp;&nbsp;&nbsp;&nbsp;"UseExternalWebServer": false  
}


Sample payload for using external web server is as shown below: 

{  
&nbsp;&nbsp;&nbsp;&nbsp;"SelectedSystemsManagerAddress": [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress1,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress2,  
&nbsp;&nbsp;&nbsp;&nbsp;],  
&nbsp;&nbsp;&nbsp;&nbsp;"ManagerCredentials": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"UserName": "",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Password": ""},  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationStrategy": "StageOnly",  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationType": "LegacyOnlineBaselineAutomatic",  
&nbsp;&nbsp;&nbsp;&nbsp;"ResetFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"DowngradeFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"CleanUpRepository": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"BatchSize": Any value ranging between 10-50,  
&nbsp;&nbsp;&nbsp;&nbsp;"UseExternalWebServer": true  
&nbsp;&nbsp;&nbsp;&nbsp;"BaselineUri": "",  
&nbsp;&nbsp;&nbsp;&nbsp;"BaselineUriISO": ""
}

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created and the following states will appear in progression:

- Pending
- Staging
- Staged

- **Deploy Only**

To deploy staged firmware and driver components on selected servers, perform a `POST` operation on `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/` action.

Sample payload is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;"SelectedSystemsManagerAddress": [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress1,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress2, ...],  
&nbsp;&nbsp;&nbsp;&nbsp;"ManagerCredentials": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"UserName": ",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Password": ""},  
&nbsp;&nbsp;&nbsp;&nbsp;"BatchSize": Any value between 10 and 200,  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationStrategy": "DeployOnly",  
&nbsp;&nbsp;&nbsp;&nbsp;"ResetFlag": true,  
&nbsp;&nbsp;&nbsp;&nbsp;"DowngradeFlag": false,  
&nbsp;&nbsp;&nbsp;&nbsp;"CleanUpRepository": true,  
}

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created and the following states will appear in progression:

- Installing
- Installed
- Installed Pending Reboot
- Activated

- **Stage and Deploy**

To update a server of type iLO4, perform a `POST` operation on `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs` action.

Sample payload for imported baseline is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;"SelectedSystemsManagerAddress": [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress1,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress2, ...
&nbsp;&nbsp;&nbsp;&nbsp;],  
&nbsp;&nbsp;&nbsp;&nbsp;"ManagerCredentials": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"UserName": "",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Password": ""  
&nbsp;&nbsp;&nbsp;&nbsp;},  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationStrategy": "StageAndDeploy",  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationType": "LegacyOnlineBaselineAutomatic",  
&nbsp;&nbsp;&nbsp;&nbsp;"ResetFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"DowngradeFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"CleanUpRepository": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"BaselineID": ,  
&nbsp;&nbsp;&nbsp;&nbsp;"BatchSize": Any value ranging between 10-30,  
&nbsp;&nbsp;&nbsp;&nbsp;"UseExternalWebServer": false  
}

Sample payload for using external web server is as shown below:

{  
&nbsp;&nbsp;&nbsp;&nbsp;"SelectedSystemsManagerAddress": [  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress1,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IPAddress2, ...
&nbsp;&nbsp;&nbsp;&nbsp;],  
&nbsp;&nbsp;&nbsp;&nbsp;"ManagerCredentials": {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"UserName": "",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Password": ""},  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationStrategy": "StageAndDeploy",  
&nbsp;&nbsp;&nbsp;&nbsp;"OperationType": "LegacyOnlineBaselineAutomatic",  
&nbsp;&nbsp;&nbsp;&nbsp;"ResetFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"DowngradeFlag": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"CleanUpRepository": false/true,  
&nbsp;&nbsp;&nbsp;&nbsp;"BatchSize": Any value ranging between 10-50,  
&nbsp;&nbsp;&nbsp;&nbsp;"UseExternalWebServer": true  
&nbsp;&nbsp;&nbsp;&nbsp;"BaselineUriISO": ""  
}


When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created and the following states will appear in progression:

- Pending
- Staging
- Staged
- Installing
- Installed
- Installed Pending Reboot
- Activated

**NOTE:**

1) `"BaselineID"` to be used for server update can be retrieved by performing a `GET` on `/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/`.  
2) Up to 30 parallel updates are supported if an imported baseline is used. Up to 50 parallel updates are supported if external webserver is selected.  
3) Other actions like Power toggling, Virtual Media Mounting etc. Cannot be performed on the selected servers being used for updates.  

Please refer to iLO Amplifier Pack user Guide for more information.

## Firmware and driver updates for Gen10 servers:
```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/
	-H "Content-Type: application/json" 
	-X POST 
	--data "@data.json"  
	-u admin:admin 
	--insecure
```
```python
# Gen10_Server_Update
import sys
import redfish

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

body = dict()
body["BaselineID"] = "{BaselineID}"
body["BatchSize"] = "{BatchSize}"
body["OperationStrategy"] = "{OperationStrategy}"
body["OperationType"] = "{OperationType}"
body["DowngradeFlag"] = "{boolValue}"
if body["OperationType"] == "iLORepositoryOffline":
  body["ResetFlag"] = False
else:
  body["ResetFlag"] = "{boolValue}"
body["CleanUpRepository"] = "{boolValue}"
body["SelectedSystemsManagerAddress"] = "{updateServerList}"
ManagerCredentials = dict()
ManagerCredentials["UserName"] = ""
ManagerCredentials["Password"]: ""
body["ManagerCredentials"] = ManagerCredentials

response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs", body=body)

if response.status != 202:
    sys.stdout.write("Unable to update gen 10 server\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

sys.stdout.write("Gen10 server update job has been created successfully\n")

# Logout of the current session
REDFISH_OBJ.logout()
```
Gen10 server updates can be performed on selected servers using below two methods:

- Online Method
- Offline Method

**Offline Method**

**Prerequisite** 

- Bootable baseline ISO image of the firmware update imported into iLO Amplifier Pack. (Please refer to Importing a Firmware Baseline use case) / Bootable baseline ISO image of the firmware update extracted to a shared HTTP/HTTPS location on the network and a dedicated web server for hosting SPP (HPE Support Pack for ProLiant) ISO images and files.
- Firmware and driver updates can be triggered only on supported server models. Please refer to user guide (Server firmware and driver updates chapter) for more details.
- Servers managed by HPE OneView or vCenter Lifecycle Manager (vLCM) cannot be updated by iLO Amplifier.
- iLO Advanced License is required to perform an update.
- For servers set to the HighSecurity/FIPS/CNSA state, please refer to user guide (Server firmware and driver updates chapter) for supported iLO and SPP versions.
- Users with the following privileges can import a firmware baseline:
  - Configure Manager with Security
  - Configure Manager
  - Configure User
  - Configure Devices

**Possible Payload Properties for an Update** 

|Property|Type|Description|  
|--------|----|-----------|  
|**SelectedSystemsManagerAddress**| array| An array of servers selected to perform server updates.|  
|**UseExternalWebServer** |boolean | Specifies whether to use external webserver or to use the internal webserver to host baselines. True if you want to use external web server else false.|  
|**BaselineID** | number | Specifies the ID of the imported Baseline.|  
|**BaselineUri** |string | The URL of the SPP baseline extracted ISO image.|  
|**BaselineUriISO**| string| The URL of the SPP baseline ISO image.|  
|**OperationType** |string | Specifies the type of operation to be performed for an update. Values for this property field can be "iLORepositoryOnline", "LegacyOnlineBaselineAutomatic", "iLORepositoryOffline", "iLORepositoryOffline". |  
|**OperationStrategy** |string | Specifies the kind of operation to be performed during an online update. Values for this property field can be "StageAndDeploy", "StageOnly" and "DeployOnly".|  
|**ResetFlag** |boolean | Specified whether to reboot the server during an update if required.|  
|**DowngradeFlag**| boolean | Support downgrade.True-support,false-not support.|  
|**CleanUpRepository** |boolean | Specifies whether to delete the uploaded components from repository after the update.|  
|**ForceInstall** |boolean | HPSUM performs a forcible upgrade or downgrade of the firmware and drivers in the baseline when set to true.|  
|**MediaPath** |string | The URL of the baseline ISO image.|  
|**BatchSize** |number | The batch size of the update which is, number of parallel updates supported.|  
|**ManagerCredentials** |string | Username and Password to be provided only in case of federated nodes.|

**Performing Job**  

Offline Updates of iLO5 supports only "Stage and Deploy" strategy. To update a server of type iLO5, perform a `POST` operation on `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/` action.

Sample Payload for Offline Update  is shown as below:  
{  
&nbsp; &nbsp; &nbsp; &nbsp;"SelectedSystemsManagerAddress": [  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;IPAddress1, ... 
&nbsp; &nbsp; &nbsp; &nbsp;],  
&nbsp; &nbsp; &nbsp; &nbsp;"ManagerCredentials": {  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"UserName": "",  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Password": ""  
&nbsp; &nbsp; &nbsp; &nbsp;},  
&nbsp; &nbsp; &nbsp; &nbsp;"OperationStrategy": "StageAndDeploy",  
&nbsp; &nbsp; &nbsp; &nbsp;"OperationType": "iLORepositoryOffline",  
&nbsp; &nbsp; &nbsp; &nbsp;"ResetFlag": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"DowngradeFlag": true/false,  
&nbsp; &nbsp; &nbsp; &nbsp;"CleanUpRepository": true/false,  
&nbsp; &nbsp; &nbsp; &nbsp;"BaselineID": 15,  
&nbsp; &nbsp; &nbsp; &nbsp;"BatchSize": 10-30  
}

**NOTE:** 

1) `"BaselineID"` to be used for server update can be retrieved by performing a `GET` on `/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/`.  
2) Up to 30 parallel updates are supported if an imported baseline is used.  
3) Other actions like Power toggling, Virtual Media Mounting etc. Cannot be performed on the selected servers being used for updates.  

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created.

Please refer to iLO Amplifier Pack user Guide for more information.

**Online Method**

**Prerequisite**

Refer to the prerequisites of offline method. Additional requirements for an online update are:

- iSUT (Integrated Smart Update Tools) should be greater than v2.3.0 and above for Gen10 servers. 
- iSUT should be greater than v2.5.0 and above for Gen10 Plus servers. 
- iSUT should be greater than 2.3.6 and above for Gen10 servers running VMware ESXi OS. 

**Performing Job**

iLO Repository Online Updates of supports three different strategies:

- **Stage Only**

To stage firmware and driver components on selected servers, perform a `POST` operation on   `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/` action. 

Sample Payload for Stage Only operation is shown as below::

{  
&nbsp; &nbsp; &nbsp; &nbsp;"SelectedSystemsManagerAddress": [  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;IPAddress1, ...  
&nbsp; &nbsp; &nbsp; &nbsp;],  
&nbsp; &nbsp; &nbsp; &nbsp;"ManagerCredentials": {  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"UserName": "",  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Password": ""  
&nbsp; &nbsp; &nbsp; &nbsp;},  
&nbsp; &nbsp; &nbsp; &nbsp;"OperationStrategy": "StageOnly",  
&nbsp; &nbsp; &nbsp; &nbsp;"OperationType": "iLORepositoryOnline",  
&nbsp; &nbsp; &nbsp; &nbsp;"ResetFlag": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"DowngradeFlag": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"CleanUpRepository": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"BaselineID": 16,  
&nbsp; &nbsp; &nbsp; &nbsp;"BatchSize": 10-30  
} ?????

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created.

- **Deploy Only**

To deploy staged firmware and driver components on selected servers, perform a `POST` operation on   `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/`** action. 

Sample Payload for Deploy Only operation  is shown as below::

{  
&nbsp; &nbsp; &nbsp; &nbsp;"ManagerCredentials": {  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"UserName": "",  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Password": ""  
&nbsp; &nbsp; &nbsp; &nbsp;},  
&nbsp; &nbsp; &nbsp; &nbsp;"BatchSize": 10-200,  
&nbsp; &nbsp; &nbsp; &nbsp;"OperationStrategy": "DeployOnly",  
&nbsp; &nbsp; &nbsp; &nbsp;"ResetFlag": true/false,  
&nbsp; &nbsp; &nbsp; &nbsp;"DowngradeFlag": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"CleanUpRepository": true/false,  
&nbsp; &nbsp; &nbsp; &nbsp;"SelectedSystemsManagerAddress":  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [IPAddress1, ...]  
}


When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created.

- **Stage and Deploy**

To update a server of type iLO5, perform a `POST` operation on   `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.ServerUpdateJobs/`** action. 

Sample Payload for StageAndDeploy operation strategy is shown as below:

{  
&nbsp; &nbsp; &nbsp; &nbsp;"SelectedSystemsManagerAddress": [  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;IPAddress1, ...
&nbsp; &nbsp; &nbsp; &nbsp;],  
&nbsp; &nbsp; &nbsp; &nbsp;"ManagerCredentials": {  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"UserName": "",  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"Password": ""  
&nbsp; &nbsp; &nbsp; &nbsp;},  
&nbsp; &nbsp; &nbsp; &nbsp;"OperationStrategy": "StageAndDeploy",  
&nbsp; &nbsp; &nbsp; &nbsp;"OperationType": "iLORepositoryOffline",  
&nbsp; &nbsp; &nbsp; &nbsp;"ResetFlag": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"DowngradeFlag": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"CleanUpRepository": false/true,  
&nbsp; &nbsp; &nbsp; &nbsp;"BaselineID": 16,  
&nbsp; &nbsp; &nbsp; &nbsp;"BatchSize": 10-30  
}

When `POST` is performed on this URI, a job will be created. A `GET` on the URI `/redfish/v1/JobService/Jobs/{jobID}/` will retrieve the state of the job created.

**NOTE:** 

1) `"BaselineID"` to be used for server update can be retrieved by performing a `GET` on `/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/`.  
2) Other actions like Power toggling, Virtual Media Mounting etc. Cannot be performed on the selected servers being used for updates.  

Please refer to iLO Amplifier Pack user Guide for more information.

## Delete baseline

```shell
curl https://{iLOAmpServer}/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/{BaselineID}
  -X DELETE 
  -u username:password 
  --insecure
```
```python
import sys
import redfish

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

uri = "/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/" + "{BaselineID}"
response = REDFISH_OBJ.delete(uri)
print("exception for DELETE request %s" %uri)

if response.status != 200:
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()
sys.stdout.write("Baseline has been deleted successfully\n")
# Logout of the current session
REDFISH_OBJ.logout()
```

To delete baseline, perform DELETE on the uri /redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/{BaselineID} with the baseline ID corrosponding to ISOImage needed to be deleted. on successful POST baseline will be deleted from iLO Amplifier Pack

##Create user

```shell
curl https://{iLOAmpServer}/redfish/v1/AccountService/Accounts 
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
	"UserName": "{userName}",<br>
	"Password": "{Password}",<br>
	"Oem": {<br>
		"Hpe": {<br>
			"Enabled": true,<br>
			"DisplayName": "{displayName}",<br>
			"Privilege": "{privilege}"<br>
			}<br>
		}<br>
	
	}<br>
    </code></p>
</blockquote>
```python
import sys
import redfish

# When running remotely connect using the address, account name,
# and password to send https requests
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

Hpe = dict()
Hpe["DisplayName"] = "{DisplayName}"
Hpe["Enabled"] = True
# Set the required privilege for the user, here "login" privilege is assigned
Hpe["Privilege"] = "Login"   
Oem = dict()
Oem["Hpe"] = Hpe
body = dict()
body["UserName"] = "{createUserName}"
body["Password"] = "{createPassword}"
body["Oem"] = Oem

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/AccountService/Accounts", body=body)

if response.status != 201:
  sys.stdout.write("Unable to to create user\n")
  sys.stdout.write("%s" % response)
  REDFISH_OBJ.logout()
  exit()
```

The `/redfish/v1/AccountService/Accounts` collection list all the users created in iLO Amplifier Pack. Perform POST operation on this collection to add user in iLO Amplifier Pack. The payload for POST must contains user name, display name, password and user privilege need to add user. User name - must use printable characters, privilege - can be one of the following

* `Configure Manager with Security` - Allows all operations including recovery management.
* `Configure Manager` - Allows all operations except recovery management.
* `Configure User` - Allows configuring users with device privileges
* `Configure Devices` - Allows configuring and performing actions on devices and login privileges.
* `Login` - Allows report generating and read operations, such as viewing discovered servers and groups.

All the users and their ID's can be obtained by peroforming GET on the uri `/redfish/v1/AccountService/Accounts`

##Delete user

```shell
curl https://{iLOAmpServer}/redfish/v1/AccountService/Accounts/{ID} 
  -X DELETE 
  -u username:password 
  --insecure
```
```python
import sys
import redfish

# When running remotely connect using the address, account name,
# and password to send https requests
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

uri = "/redfish/v1/AccountService/Accounts/{UserID}"
# Do a POST on a given path
response = REDFISH_OBJ.delete(uri)

if response.status != 200:
    sys.stdout.write("Failed to delete user\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

sys.stdout.write("User has been deleted successfully\n")

# Logout of the current session
REDFISH_OBJ.logout()
```

To delete user, first get the user ID's by perform GET on the uri `/redfish/v1/AccountService/Accounts`, which lists all the users and their respective user ID's.
Performing DELETE operation on the uri `/redfish/v1/AccountService/Accounts/{ID}` with the user ID corrosponding to user needed to be deleted will delete user

##Get job status

```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Jobs/{JobID}
  -X GET 
  -u username:password 
  --insecure
```
```python
import sys
import redfish

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

jobList = "{[JobID]}"

if len(jobList) == 1 and jobList[0].lower() == "all":
    totalJobsListed = 0
    skip = 0
    while True:
        queryString = "/?$skip=%s" % skip
        getRunningJob = "/redfish/v1/JobService/Jobs" + queryString

        try:
            managed_system = REDFISH_OBJ.get(getRunningJob)
        except:
            sys.stdout.write("GET request to %s failed\n" % getRunningJob)
            sys.stdout.write("%s\n" % getRunningJob)
            exit()
        if managed_system.dict["Members@odata.count"] == 0:
            sys.stdout.write("iLO Amp doesn't have any jobs to show\n")
            exit()

        for jobInfo in managed_system.dict["Members"]:
            jobList.append(jobInfo["ID"])
            totalJobsListed += 1
            skip += 1
        if managed_system.dict["Members@odata.count"] <= totalJobsListed:
            break

if jobList == []:
    sys.stdout.write("Please provide jobID\n")
for jobID in jobList:
    jobCreatedLink = "/redfish/v1/JobService/Jobs/" + jobID
    sys.stdout.write("******** jobID %s ********\n" % jobID)
    dstate = "InProgress"
    managed_system = REDFISH_OBJ.get(jobCreatedLink)
    dstate = managed_system.dict["JobState"]
    PercentComplete = managed_system.dict["PercentComplete"]
    sys.stdout.write("JobID = %s, JobState = %s, PercentComplete %s\n" % (jobID, dstate, PercentComplete))

# Logout of the current session
REDFISH_OBJ.logout()
```

To know the status and completion percentage of job created in iLO Amplifier pack, perform GET operation on the uri `/redfish/v1/JobService/Jobs/{jobID}` using respective job ID generated during job creation. Job state can be any of the following

* Starting
* Running
* Pending
* Completed
* Cancelled
* Exception
* Failed

## Compliance report

```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.SppComplianceJobs
  -H "Content-Type: application/json" 
  -X POST 
  --data "@data.json"  
  -u username:password 
  --insecure
curl https://{iLOAmpServer}/report/ComplianceReport_{jobID}.csv 
  -X GET  
  -u admin:admin 
  --insecure
```
<blockquote class="lang-specific shell">
	<p>Contents of data.json file </p>
    <p><code>
	{<br>
	"BaselineID" : "{BaselineID}",<br>
	"SelectedSystemsManagerAddress" :"[{iLOAddress}]",<br>
	}<br>
    </code></p>
</blockquote>
```python
import sys
import redfish
import json
import csv
import time
from datetime import datetime

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

serverVsJobID = dict()
jobList = []
body = dict()
body["BaselineID"] = "{BaselineID}"
body["SelectedSystemsManagerAddress"] = "[{iLOAddress}]"

response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.SppComplianceJobs",
                                    body=body)

if response.status != 202:
    sys.stdout.write("Unable to create compliance report for server %s\n" % "{iLOAddress}")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

jobCreatedLink = response.getheader("Location")
if jobCreatedLink == None:
    jobCreatedLink = response.getheader("Link")
    if jobCreatedLink == None:
        jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]

jobID = jobCreatedLink.split("/")[-1]
sys.stdout.write("Compliance report job for server %s has been created successfully\n" % "{iLOAddress}")
jobCreatedLink = "/redfish/v1/JobService/Jobs/" + jobID
dstate = "InProgress"
while dstate != "Complete" and dstate != "Successful":
    managed_system = REDFISH_OBJ.get(jobCreatedLink)
    if managed_system.status != 200:
        jobList.remove(jobID)
        continue
    PercentComplete = managed_system.dict["PercentComplete"]
    if PercentComplete == 100:
        sys.stdout.write("job %s is completed\n" % jobID)
    else:
        sys.stdout.write("job %s is inprogress\n" % jobID)

downloadReportUri = "/report/ComplianceReport_" + jobID + ".csv"
response = REDFISH_OBJ.get(downloadReportUri)
now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
fd = open('ComplianceReport_' + current_time + '.csv','w')
fd.write(response.text)
fd.close()

# Logout of the current session
REDFISH_OBJ.logout()
```

**Prerequisites**

* Firmware baseline ISO image has to be imported into iLO Amplifier Pack (Please refer import firmware baseline use case)

**Create baseline compliance report**

Perform POST operation on the redfish action uri `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.SppComplianceJobs` with the baseline ID corresponding to the respective baseline(Please refer Get baseline info use case) and server for which compliance report has  to be created. on successful POST a job will be created, a GET on uri `/redfish/v1/JobService/Jobs/{jobID}` or get job status use case to check the status of job.

**Download compliance report**

Perform GET operation on the uri `/report/ComplianceReport_{jobID}.csv` will download the compliance report in csv format. Corresponding
create baseline compliance report jobID has to be provided in uri during GET operation.
On successful download csv file conatining compliance information will be saved in local folder.

## Create recovery policy

```shell
curl https://{iLOAmpServer}/redfish/v1/ManagedNodes/RecoveryPolicy
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
	"Name": "{PolicyName}",<br>
	"BaselineID": "{FirmwareBaselineID}",<br>
	"PersonaID": "{ConfigurationBaselineID}",<br>
	"OperatingSystemID": "{OsBaseline}",<br>
	"UseNANDBackupRestoreIfAvailable": "{bool}"<br>
	}<br>
    </code></p>
</blockquote>
```python

# Create recovery policy
import sys
import redfish
import time
import json

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")


body = dict()
body["Name"] = "{PolicyName}"
body["BaselineID"] = "{FirmwareBaselineID}"
body["PersonaID"] = "{ConfigurationBaselineID}"
body["OperatingSystemID"] = "{OsBaseline}"
body["UseNANDBackupRestoreIfAvailable"] = "{bool}"

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/ManagedNodes/RecoveryPolicy", body=body)

if response.status != 201:
    sys.stdout.write("Failed to create recovery policy\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

sys.stdout.write("Recovery policy has been created successfully\n")

# Logout of the current session
REDFISH_OBJ.logout()
```

**Prerequisites**

* Users with the following privileges can create recovery policy
	- Configure Manager with Security
* Firmware baseline ISO image has to be imported into iLO Amplifier Pack(Please refer import firmware baseline use case)
* Create or import a configuration baseline from a server(optional)
* OS baseline ISO image has to be imported into iLO Amplifier Pack(optional)

**Creating a recovery policy**

Perform POST operation on the redfish uri `/redfish/v1/ManagedNodes/RecoveryPolicy` with the payload containing policy name, firmware baseline ID, OS baseline ID and configuration baseline ID. All baselines are not mandatory, supported combinations are as following

* Firmware only
* Firmware + Configuration
* Operating System only
* Firmware + Configuration + Operating System
Policy will be created in iLO Amplifier Pack on successful POST operation

## Assign recovery policy

```shell
curl https://{iLOAmpServer}/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.AssignRecoveryPolicyJob
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
	"ActionType" : "{ActionType}",<br>
    "SelectedSystemsManagerAddress" : "{ServerAddress}",<br>
    "RecoveryPolicyID" : "{RecoveryPolicyID}",<br>
	}<br>
    </code></p>
</blockquote>
```python
#Assign recovery policy
import sys
import redfish
import time
import json

# Connect using iLO Amplifier address, username and password
login_host = "https://{iLOAmpServer}"
login_account = "username"
login_password = "password"

# Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, \
                                     username=login_account, \
                                     password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

ServerAddress = "{[serverlist]}"

body = dict()
body["ActionType"] = "{ActionType}"
body["SelectedSystemsManagerAddress"] = ServerAddress
if body["ActionType"] != "Quarantine":
    body["RecoveryPolicyID"] = "{RecoveryPolicyID}"

# Do a POST on a given path
response = REDFISH_OBJ.post("/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.AssignRecoveryPolicyJob", body=body)

if response.status != 202:
    sys.stdout.write("Unable to assign recovery policy\n")
    sys.stdout.write("%s" % response)
    REDFISH_OBJ.logout()
    exit()

jobCreatedLink = response.getheader("Location")
if jobCreatedLink == None:
    jobCreatedLink = response.getheader("Link")
    if jobCreatedLink == None:
        jobCreatedLink = response.dict['error']['@Message.ExtendedInfo'][0]['MessageArgs'][0]

jobID = jobCreatedLink.split("/")[-1]
sys.stdout.write("Assign recovery policy job has been created successfully\n")
sys.stdout.write("check job status using jobID %s\n" % jobID)

# Logout of the current session
REDFISH_OBJ.logout()
```

**Prerequisites**

* Users with the following privileges can create recovery policy
	- Configure Manager with Security
* Servers must be gen10 or gen10+(for more information on iLO versions refer user guide)
* Server must be in monitored state
* Recovery policy containing necessary baselines needed to perform action 

**Assign recovery policy**

There are three different types of recovery action iLO Amplifier Pack can assign it to servers and are mentioned below

* Auto Recovery Policy
* Quarantine
* Device Initiated Full Auto Recovery

Perform POST operation on the redfish action uri `/redfish/v1/JobService/Actions/Oem/Hpe/HpeWfmJobServiceExt.AssignRecoveryPolicyJob` with the payload containing recovery action type, recovery policy ID corresponding to the respective recovery policy and server list for while policy has to be assigned. For device initiated action, recovery policy must contain all three baselines. Provide one of the action types mentioned below

*Quarantine 
*Auto
*DeviceInitiated
on successful POST a job will be created, a GET on uri `/redfish/v1/JobService/Jobs/{jobID}` or get job status use case to check the status of job.





