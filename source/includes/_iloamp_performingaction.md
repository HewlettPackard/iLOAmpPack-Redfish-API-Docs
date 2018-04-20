# Performing Actions

> Example of a system resource advertising an available action:

```json
{
    "Actions": {
        "#ComputerSystem.Reset": {
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "ForceRestart",
                "Nmi",
                "PushPowerButton"
            ],
            "target": "/redfish/v1/Systems/{item}/Actions/ComputerSystem.Reset/"
        }
    }
}
```

> This action may be invoked by performing:

```shell
curl https://{iLOAmpServer}/redfish/v1/Systems/{item}/Actions/ComputerSystem.Reset/ 
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
      "ResetType": "ForceRestart"</br>
    }</br>
    </code></p>
</blockquote>

```python
# Performing an action
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

body = dict()
body["ResetType"] = "ForceRestart"

# Do a GET on a given path
response = REDFISH_OBJ.post("/redfish/v1/systems/{item}/Actions/ComputerSystem.Reset/", body=body)

# Print out the response
sys.stdout.write("%s\n" % response.text)

# Logout of the current session
REDFISH_OBJ.logout()
```

REST resources usually support HTTP GET to read the current state, and some support modification and removal with HTTP POST, PUT, PATCH, or DELETE.

There are some resources that support other types of operations not easily mapped to HTTP operations.  For this reason the Redfish specification defines "Actions".  Actions are HTTP POST operations with a specifically formatted JSON request including the operation to perform and any parameters.  For instance, it is not enough to simply tell a server to reset, but it is also necessary to specify the type of reset:  cold boot, warm boot, PCI reset, etc.  Actions are often used when the operation causes iLO Amplifier Pack not just to update a value, but to change system state.

In Redfish, the available actions that can be invoked are identified by a "target" property in the resource's "Actions" object definitions.  The parameters identify the supported values with the annotation `@Redfish.AllowableValues.`

## Actions on HPE-specific Extensions

> Example of a extended manager resource advertising an available action:

```json
{
	"Oem" : {
		"Hpe" : {
			"Actions" : {
				"#HpeWfmManagerExt.Backup" : {
					"target" : "/redfish/v1/Managers/iLOAmplifier/Actions/Oem/Hpe/HpeWfmManagerExt.Backup"
				},
				"#HpeWfmManagerExt.Restore" : {
					"target" : "/redfish/v1/Managers/iLOAmplifier/Actions/Oem/Hpe/HpeWfmManagerExt.Restore"
				}
			}
		}
	}
}
```
> This action may be invoked by performing:

```shell
curl https://{iLOAmpServer}/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/
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
    "StorageType" : "USB",<br>
	"Password" : "password",<br>
	"DestinationPath" : "folder/filename",<br>
	"RemovableStorageDeviceName" : "sd1_vol1"<br>
    }</br>
    </code></p>
</blockquote>
```python
# Performing an OEM extended action
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

body = dict()
body["ResetType"] = "ForceRestart"
body["StorageType"] = "USB"
body["Password"] = "password"
body["DestinationPath"] = "folder/filename"
body["RemovableStorageDeviceName"] = "sd1_vol1"

# Do a GET on a given path
response = REDFISH_OBJ.post("/redfish/v1/Managers/iLOAmplifier/Actions/Oem/Hpe/HpeWfmManagerExt.Backup/", body=body)

# Print out the response
sys.stdout.write("%s\n" % response.text)

# Logout of the current session
REDFISH_OBJ.logout()
```

The embedded OEM extensions may also have Actions not specified by the Redfish standard.  They are invoked in a similar way.  The POST URI indicate's the HPE specific nature of the action.

