# Navigating the Data Model

Unlike some simple REST service, this API is designed to be implemented on many different management appliances, different models of servers, and other IT infrastructure devices for years to come.  These devices may be quite different from one another.  For this reason, the API does not specify the URIs to various resources. Do not assume the BIOS version information is always at a particular URI.

This is more complex for the client, but is necessary to make sure the data model can change to accommodate various future server architectures without requiring specification changes. As an example, if the BIOS version is at `/redfish/v1/systems/1/`, and a client assumed it is always there, the client would then break when the interface is implemented on a different type of architecture with many compute nodes, each with its own BIOS version. 

<aside class="warning">
A select few URIs are documented to be stable starting points. Your client code should not assume anything about the URIs that you find in the data model. You must treat them as opaque strings or your client will not interoperate with other implementations of the RESTful API.  
</aside>

The supported stable URIs are those referenced directly in this API reference and include:

* /redfish/v1/
* /redfish/v1/systems/
* /redfish/v1/chassis/
* /redfish/v1/managers/
* /redfish/v1/sessions/


## Iterating Collections

```shell
curl https://{iLOAmpServer}/redfish/v1/systems/ --insecure -u username:password -L
```

```python
# Perform GET operation against a resource at /redfish/v1/systems/
import sys
import redfish

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

# Do a GET on a given path
response = REDFISH_OBJ.get("/redfish/v1/systems/")

# Print out the response
sys.stdout.write("%s\n" % response.text)

# Logout of the current session
REDFISH_OBJ.logout()
```

> The above command (or program) returns the JSON response body as below:

```json
{
	"@odata.context" : "/redfish/v1/$metadata#ComputerSystemCollection.ComputerSystemCollection",
	"@odata.etag" : "W/\"09FA012B\"",
	"@odata.id" : "/redfish/v1/Systems",
	"@odata.type" : "#ComputerSystemCollection.ComputerSystemCollection",
	"Description" : "System Collection View",
	"Id" : "Systems",
	"Members" : [{
			"@odata.id" : "/redfish/v1/Systems/E1D8B426"
		}, {
			"@odata.id" : "/redfish/v1/Systems/E905C3FF"
		}, {
			"@odata.id" : "/redfish/v1/Systems/EF2BF486"
		}
	],
	"Members@odata.count" : 3,
	"Name" : "ComputerSystemCollection"
}
```

Many operations will require you to locate the resource you wish to use.  Most of these resources are members of "collections" (arrays of similar items).  The method to find collections members is consistent for compute nodes, chassis, management processors, and many other resources in the data model.

## Find a Compute Node

```shell
curl https://{iLOAmpServer}/redfish/v1/systems/{item}/ --insecure -u username:password -L
```

```python
# Perform GET operation against a resource at /redfish/v1/systems/{item}
import sys
import redfish

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

# Do a GET on a given path
response = REDFISH_OBJ.get("/redfish/v1/systems/{item}/")

# Print out the response
sys.stdout.write("%s\n" % response.text)

# Logout of the current session
REDFISH_OBJ.logout()
```

> JSON response body example:

```json
{
	"@odata.context" : "/redfish/v1/$metadata#ComputerSystem.ComputerSystem",
	"@odata.etag" : "W/\"404C537A\"",
	"@odata.id" : "/redfish/v1/Systems/E1E4C0C1",
	"@odata.type" : "#ComputerSystem.v1_3_0.ComputerSystem",
	"Description" : "Computer System View",
	"EthernetInterfaces" : {
		"@odata.id" : "/redfish/v1/Systems/E1E4C0C1/EthernetInterfaces"
	},
	"HostName" : "ESX-e1e4c0c1e82fbfa4",
	"Id" : "E1E4C0C1",
	"IndicatorLED" : "Lit",
	"Manufacturer" : "HPE",
	"Memory" : {
		"@odata.id" : "/redfish/v1/Systems/E1E4C0C1/Memory"
	},
	"MemorySummary" : {
		"Status" : {
			"Health" : "OK"
		},
		"TotalSystemMemoryGiB" : 8
	},
	"Model" : "ProLiant DL160 Gen9",
	"Name" : "Computer System",
	"PCIeDevices" : {
		"@odata.id" : "/redfish/v1/Systems/E1E4C0C1/PCIeDevices"
	},
	"PowerState" : "Off",
	"ProcessorSummary" : {
		"Count" : 1,
		"Model" : "Intel(R) Xeon(R) CPU E5-2603 v4 @ 1.70GHz",
		"Status" : {
			"Health" : "OK"
		}
	},
	"Processors" : {
		"@odata.id" : "/redfish/v1/Systems/E1E4C0C1/Processors"
	},
	"SKU" : "830570-B21",
	"SerialNumber" : "JBX4TXEARD",
	"Status" : {
		"Health" : "OK",
		"State" : "Enabled"
	},
	"Storage" : {
		"@odata.id" : "/redfish/v1/Systems/E1E4C0C1/Storage"
	},
	"SystemType" : "Physical",
	"UUID" : "00000000-0000-4286-9d93-000000000000"
}
```

A Compute node represents a logical computer system with attributes such as processors, memory, BIOS, power state, firmware version, etc.  To find a compute node `GET /redfish/v1/systems/` and iterate the "Members" array in the returned JSON.  Each member has a link to a compute node.

Find a compute node by iterating the systems collection at `/redfish/v1/systems/`.

## Find a Chassis

```shell
curl https://{iLOAmpServer}/redfish/v1/chassis/{item}/ --insecure -u username:password -L
```

```python
# Perform GET operation against a resource at /redfish/v1/chassis/{item}
import sys
import redfish

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

# Do a GET on a given path
response = REDFISH_OBJ.get("/redfish/v1/chassis/{item}/")

# Print out the response
sys.stdout.write("%s\n" % response.text)

# Logout of the current session
REDFISH_OBJ.logout()
```

> JSON response example:

```json
{
	"@odata.context" : "/redfish/v1/$metadata#Chassis.Chassis",
	"@odata.etag" : "W/\"A23FA931\"",
	"@odata.id" : "/redfish/v1/Chassis/E1E4C0C1",
	"@odata.type" : "#Chassis.v1_4_0.Chassis",
	"Description" : "Computer System Chassis",
	"Id" : "E1E4C0C1",
	"IndicatorLED" : "Lit",
	"Manufacturer" : "HPE",
	"Model" : "ProLiant DL160 Gen9",
	"Name" : "Computer System Chassis",
	"Power" : {
		"@odata.id" : "/redfish/v1/Chassis/E1E4C0C1/Power"
	},
	"PowerState" : "Off",
	"SKU" : "830570-B21",
	"SerialNumber" : "JBX4TXEARD",
	"Status" : {
		"Health" : "OK",
		"State" : "Enabled"
	},
	"Thermal" : {
		"@odata.id" : "/redfish/v1/Chassis/E1E4C0C1/Thermal"
	}
}
```

A Chassis represents a physical or virtual container of compute resources with attributes such as FRU information, power supplies, temperature, etc.  To find a chassis `GET /redfish/v1/chassis` and iterate the "Members" array in the returned JSON.  Each member has a link to a chassis.

Find a chassis by iterating the chassis collection at `/redfish/v1/chassis/`.

## Find the iLO Management Processor

```shell
curl https://{iLOAmpPack}/redfish/v1/managers/{item}/ --insecure -u username:password -L
```

```python
# Perform GET operation against a resource at /redfish/v1/managers/{item}
import sys
import redfish

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

# Do a GET on a given path
response = REDFISH_OBJ.get("/redfish/v1/managers/{item}/")

# Print out the response
sys.stdout.write("%s\n" % response.text)

# Logout of the current session
REDFISH_OBJ.logout()
```

> JSON response example:

```json
{
	"@odata.context" : "/redfish/v1/$metadata#Manager.Manager",
	"@odata.etag" : "W/\"BEB98442\"",
	"@odata.id" : "/redfish/v1/Managers/E1E4C0C1",
	"@odata.type" : "#Manager.v1_3_0.Manager",
	"Description" : "Manager View",
	"EthernetInterfaces" : {
		"@odata.id" : "/redfish/v1/Managers/E1E4C0C1/EthernetInterfaces"
	},
	"FirmwareVersion" : "iLO 4 v2.53",
	"Id" : "E1E4C0C1",
	"ManagerType" : "BMC",
	"Name" : "Manager",
	"UUID" : "00000000-0000-4c8a-a283-000000000000"
}
```

A Manager represents a management processor (or "BMC") that manages chassis and compute resources.  For HPE Gen10 Servers, the manager is iLO 5.  Managers contain attributes such as networking state and configuration, management services, security configuration, etc.  To find a manager `GET /redfish/v1/managers` and iterate the "Members" array in the returned JSON.  Each member has a link to a manager.

Find a manager by iterating the manager collection at `/redfish/v1/managers/`.


