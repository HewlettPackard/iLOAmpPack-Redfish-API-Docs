## AccountService 1.3.0

The AccountService schema contains properties for managing user accounts. The properties are common to all user accounts, such as password requirements, and control features such as account lockout. The schema also contains links to the collections of Manager Accounts and Roles.

|     |     |     |
| --- | --- | --- |
| **AccountLockoutCounterResetAfter** | number<br>(seconds)<br><br>*read-write* | The interval of time in seconds between the last failed login attempt and reset of the lockout threshold counter. This value must be less than or equal to AccountLockoutDuration. Reset sets the counter to zero. |
| **AccountLockoutDuration** | number<br>(seconds)<br><br>*read-write<br>(null)* | The time in seconds an account is locked out. The value must be greater than or equal to the value of the AccountLockoutCounterResetAfter property. If set to 0, no lockout occurs. |
| **AccountLockoutThreshold** | number<br><br>*read-write<br>(null)* | The number of failed login attempts allowed before a user account is locked for a specified duration. A value of 0 means it is never locked. |
| **Accounts** { | object | A link to a collection of Manager Accounts. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *ManagerAccount*. See the ManagerAccount schema for details. |
| } |   |   |
| **ActiveDirectory** { | object | The first ActiveDirectory external account provider this AccountService supports. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AccountProviderType** | string<br>(enum)<br><br>*read-only<br>(null)* | This property contains the type of external account provider this resource references. *For the possible property values, see AccountProviderType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Authentication** { | object<br><br>*<br>(null)* | This property contains the authentication information for the external account provider. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AuthenticationType** | string<br>(enum)<br><br>*read-write<br>(null)* | This property contains the type of authentication used to connect to the external account provider. *For the possible property values, see AuthenticationType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**KerberosKeytab** | string<br><br>*read-write<br>(null)* | This property is used with a PATCH or PUT to write a base64 encoded version of the kerberos keytab for the account.  This property is null on a GET. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Password** | string<br><br>*read-write<br>(null)* | This property is used with a PATCH or PUT to write the password for the account service.  This property is null on a GET. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Token** | string<br><br>*read-write<br>(null)* | This property is used with a PATCH or PUT to write the token for the account.  This property is null on a GET. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Username** | string<br><br>*read-write* | This property contains the user name for the account service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LDAPService** { | object<br><br>*<br>(null)* | This property contains additional mapping information needed to parse a generic LDAP service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SearchSettings** { | object<br><br>*<br>(null)* | This property contains the settings needed to search an external LDAP service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaseDistinguishedNames** [ ] | array (string, null)<br><br>*read-write* | The base distinguished names to use when searching the LDAP service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GroupNameAttribute** | string<br><br>*read-write<br>(null)* | The attribute name that contains the name of the Group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GroupsAttribute** | string<br><br>*read-write<br>(null)* | The attribute name that contains the Groups for a user. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UsernameAttribute** | string<br><br>*read-write<br>(null)* | The attribute name that contains the Username. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteRoleMapping** [ { | array | This property contains a collection of the mapping rules to convert the external account providers account information to the local Redfish Role. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LocalRole** | string<br><br>*read-write<br>(null)* | The name of the local role in which to map the remote user or group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteGroup** | string<br><br>*read-write<br>(null)* | This property is the name of the remote group (or in the case of a Redfish Service, remote role) that will be mapped to the local role referenced by this entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteUser** | string<br><br>*read-write<br>(null)* | This property is the name of the remote user that will be mapped to the local role referenced by this entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServiceAddresses** [ ] | array (string, null)<br><br>*read-write* | This property contains the addresses of the user account providers this resource references. The format of this field depends on the Type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled. |
| } |   |   |
| **AdditionalExternalAccountProviders** { | object | The additional external account providers this AccountService is using. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *ExternalAccountProvider*. See the ExternalAccountProvider schema for details. |
| } |   |   |
| **AuthFailureLoggingThreshold** | number<br><br>*read-write* | The number of authorization failures allowed before the failure attempt is logged to the manager log. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **LDAP** { | object | The first LDAP external account provider this AccountService supports. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AccountProviderType** | string<br>(enum)<br><br>*read-only<br>(null)* | This property contains the type of external account provider this resource references. *For the possible property values, see AccountProviderType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Authentication** { | object<br><br>*<br>(null)* | This property contains the authentication information for the external account provider. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AuthenticationType** | string<br>(enum)<br><br>*read-write<br>(null)* | This property contains the type of authentication used to connect to the external account provider. *For the possible property values, see AuthenticationType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**KerberosKeytab** | string<br><br>*read-write<br>(null)* | This property is used with a PATCH or PUT to write a base64 encoded version of the kerberos keytab for the account.  This property is null on a GET. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Password** | string<br><br>*read-write<br>(null)* | This property is used with a PATCH or PUT to write the password for the account service.  This property is null on a GET. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Token** | string<br><br>*read-write<br>(null)* | This property is used with a PATCH or PUT to write the token for the account.  This property is null on a GET. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Username** | string<br><br>*read-write* | This property contains the user name for the account service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LDAPService** { | object<br><br>*<br>(null)* | This property contains additional mapping information needed to parse a generic LDAP service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SearchSettings** { | object<br><br>*<br>(null)* | This property contains the settings needed to search an external LDAP service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaseDistinguishedNames** [ ] | array (string, null)<br><br>*read-write* | The base distinguished names to use when searching the LDAP service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GroupNameAttribute** | string<br><br>*read-write<br>(null)* | The attribute name that contains the name of the Group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GroupsAttribute** | string<br><br>*read-write<br>(null)* | The attribute name that contains the Groups for a user. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UsernameAttribute** | string<br><br>*read-write<br>(null)* | The attribute name that contains the Username. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteRoleMapping** [ { | array | This property contains a collection of the mapping rules to convert the external account providers account information to the local Redfish Role. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LocalRole** | string<br><br>*read-write<br>(null)* | The name of the local role in which to map the remote user or group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteGroup** | string<br><br>*read-write<br>(null)* | This property is the name of the remote group (or in the case of a Redfish Service, remote role) that will be mapped to the local role referenced by this entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteUser** | string<br><br>*read-write<br>(null)* | This property is the name of the remote user that will be mapped to the local role referenced by this entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServiceAddresses** [ ] | array (string, null)<br><br>*read-write* | This property contains the addresses of the user account providers this resource references. The format of this field depends on the Type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled. |
| } |   |   |
| **LocalAccountAuth** | string<br>(enum)<br><br>*read-write* | Controls when this service will use the accounts defined withing this AccountService as part of authentication. *For the possible property values, see LocalAccountAuth in Property Details.* |
| **MaxPasswordLength** | number<br><br>*read-only* | The maximum password length for this service. |
| **MinPasswordLength** | number<br><br>*read-only* | The minimum password length for this service. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PrivilegeMap** { | object | A reference to the Privilege mapping that defines the privileges needed to perform a requested operation on a URI associated with this service. See the *PrivilegeRegistry* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PrivilegeRegistry resource. See the Links section and the *PrivilegeRegistry* schema for details. |
| } |   |   |
| **Roles** { | object | A link to a collection of Roles. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Role*. See the Role schema for details. |
| } |   |   |
| **ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates whether this service is enabled.  If set to false, the AccountService is disabled.  This means no users can be created, deleted or modified.  Any service attempting to access the AccountService resource (for example, the Session Service) will fail.  New sessions cannot be started when the service is disabled. However, established sessions may still continue operating. This does not affect Basic AUTH connections. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

### Property Details

### AccountProviderType:


This property contains the type of external account provider this resource references.

| string | Description |
| --- | --- |
| ActiveDirectoryService | An external Active Directory Service. |
| LDAPService | A generic external LDAP Service. |
| OEM | An OEM specific external authentication or directory service. |
| RedfishService | An external Redfish Service. |

### AuthenticationType:


This property contains the type of authentication used to connect to the external account provider.

| string | Description |
| --- | --- |
| KerberosKeytab | A kerberos keytab. |
| OEM | An OEM specific authentication mechanism. |
| Token | An opaque authentication token. |
| UsernameAndPassword | Username and password combination. |

### LocalAccountAuth:


Controls when this service will use the accounts defined withing this AccountService as part of authentication.

| string | Description |
| --- | --- |
| Disabled | Authentication via accounts defined in this AccountService is disabled. |
| Enabled | Authentication via accounts defined in this AccountService is enabled. |
| Fallback | Authentication via accounts defined in this AccountService is only used if there are external account providers that are currently unreachable. |


## ActionInfo 1.0.3

The ActionInfo schema describes the parameters and other information necessary to perform a Redfish Action on a particular Action target. Parameter support can differ between vendors and even between instances of a resource. This data can be used to ensure Action requests from applications contain supported parameters.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Parameters** [ { | array | The parameters associated with the specified Redfish Action. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AllowableValues** [ ] | array (string, null)<br><br>*read-only* | A list of values for this parameter supported by this Action target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DataType** | string<br>(enum)<br><br>*read-only<br>(null)* | The JSON property type used for this parameter. *For the possible property values, see DataType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only required* | The name of the parameter for this Action. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ObjectDataType** | string<br><br>*read-only<br>(null)* | The OData Type of an object-based parameter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required** | boolean<br><br>*read-only* | Indicates whether the parameter is required to perform this Action. |
| } ] |   |   |

### Property Details

### DataType:

The JSON property type used for this parameter.

| string | Description |
| --- | --- |
| Boolean | A boolean (true or false). |
| Number | A number. |
| NumberArray | An array of numbers. |
| Object | An embedded JSON object. |
| ObjectArray | An array of JSON objects. |
| String | A string. |
| StringArray | An array of strings. |

## Chassis 1.7.0

The Chassis schema represents the physical components of a system.  This resource represents the sheet-metal confined spaces and logical zones such as racks, enclosures, chassis and all other containers. Subsystems (like sensors) that operate outside of a system's data plane (meaning the resources are not accessible to software running on the system) are linked either directly or indirectly through this resource.

|     |     |     |
| --- | --- | --- |
| **Assembly** {} | object | A reference to the Assembly resource associated with this chassis. See the *Assembly* schema for details on this property. |
| **AssetTag** | string<br><br>*read-write<br>(null)* | The user assigned asset tag of this chassis. |
| **ChassisType** | string<br>(enum)<br><br>*read-only required* | The type of physical form factor of the chassis. *For the possible property values, see ChassisType in Property Details.* |
| **DepthMm** | number<br>(mm)<br><br>*read-only<br>(null)* | The depth of the chassis. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **HeightMm** | number<br>(mm)<br><br>*read-only<br>(null)* | The height of the chassis. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **IndicatorLED** | string<br>(enum)<br><br>*read-write<br>(null)* | The state of the indicator LED, used to identify the chassis. *For the possible property values, see IndicatorLED in Property Details.* |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComputerSystems** [ { | array | An array of references to the computer systems contained in this chassis.  This will only reference ComputerSystems that are directly and wholly contained in this chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a ComputerSystem resource. See the Links section and the *ComputerSystem* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ContainedBy** { | object | A reference to the chassis that this chassis is contained by. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another Chassis resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Contains** [ { | array | An array of references to any other chassis that this chassis has in it. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another Chassis resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CooledBy** [ { | array | An array of ID[s] of resources that cool this chassis. Normally the ID will be a chassis or a specific set of fans. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Drives** [ { | array | An array of references to the disk drives located in this Chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Drive resource. See the Links section and the *Drive* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedBy** [ { | array | An array of references to the Managers responsible for managing this chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Manager resource. See the Links section and the *Manager* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagersInChassis** [ { | array | An array of references to the managers located in this Chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Manager resource. See the Links section and the *Manager* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PCIeDevices** [ { | array | An array of references to the PCIe Devices located in this Chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeDevice resource. See the Links section and the *PCIeDevice* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PoweredBy** [ { | array | An array of ID[s] of resources that power this chassis. Normally the ID will be a chassis or a specific set of Power Supplies. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResourceBlocks** [ { } ] | array (object) | An array of references to the Resource Blocks located in this Chassis. This schema defines a Resource Block resource. See the *ResourceBlock* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Storage** [ { | array | An array of references to the storage subsystems connected to or inside this Chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Storage resource. See the Links section and the *Storage* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Switches** [ { } ] | array (object) | An array of references to the Switches located in this Chassis. Switch contains properties describing a simple fabric switch. See the *Switch* schema for details on this property. |
| } |   |   |
| **Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| **LogServices** { | object | A reference to the logs for this chassis. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *LogService*. See the LogService schema for details. |
| } |   |   |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | The manufacturer of this chassis. |
| **Model** | string<br><br>*read-only<br>(null)* | The model number of the chassis. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NetworkAdapters** { | object | A reference to the collection of Network Adapters associated with this chassis. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *NetworkAdapter*. See the NetworkAdapter schema for details. |
| } |   |   |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PartNumber** | string<br><br>*read-only<br>(null)* | The part number of the chassis. |
| **PhysicalSecurity** { | object | The state of the physical security sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IntrusionSensor** | string<br>(enum)<br><br>*read-write<br>(null)* | This indicates the known state of the physical security sensor, such as if it is hardware intrusion detected. *For the possible property values, see IntrusionSensor in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IntrusionSensorNumber** | number<br><br>*read-only<br>(null)* | A numerical identifier to represent the physical security sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IntrusionSensorReArm** | string<br>(enum)<br><br>*read-only<br>(null)* | This indicates how the Normal state to be restored. *For the possible property values, see IntrusionSensorReArm in Property Details.* |
| } |   |   |
| **Power** { | object | A reference to the power properties (power supplies, power policies, sensors) of this chassis. See the *Power* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Power resource. See the Links section and the *Power* schema for details. |
| } |   |   |
| **PowerState** | string<br>(enum)<br><br>*read-only<br>(null)* | The current power state of the chassis. *For the possible property values, see PowerState in Property Details.* |
| **SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number of the chassis. |
| **SKU** | string<br><br>*read-only<br>(null)* | The SKU of the chassis. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **Thermal** { | object | A reference to the thermal properties (fans, cooling, sensors) of this chassis. See the *Thermal* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Thermal resource. See the Links section and the *Thermal* schema for details. |
| } |   |   |
| **UUID** | string<br><br>*read-only<br>(null)* | The Universal Unique Identifier (UUID) for this Chassis. |
| **WeightKg** | number<br>(kg)<br><br>*read-only<br>(null)* | The weight of the chassis. |
| **WidthMm** | number<br>(mm)<br><br>*read-only<br>(null)* | The width of the chassis. |

### Actions

### Reset


This action is used to reset the chassis. This action resets the chassis, not Systems or other contained resources, although side effects may occur which affect those resources.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResetType** | string<br>(enum)<br><br>*read-write* | The type of reset to be performed. *For the possible property values, see ResetType in Property Details.* |
| } |   |   |   |

### Property Details

### ChassisType:


The type of physical form factor of the chassis.

| string | Description |
| --- | --- |
| Blade | An enclosed or semi-enclosed, typically vertically-oriented, system chassis which must be plugged into a multi-system chassis to function normally. |
| Card | A loose device or circuit board intended to be installed in a system or other enclosure. |
| Cartridge | A small self-contained system intended to be plugged into a multi-system chassis. |
| Component | A small chassis, card, or device which contains devices for a particular subsystem or function. |
| Drawer | An enclosed or semi-enclosed, typically horizontally-oriented, system chassis which may be slid into a multi-system chassis. |
| Enclosure | A generic term for a chassis that does not fit any other description. |
| Expansion | A chassis which expands the capabilities or capacity of another chassis. |
| IPBasedDrive | A chassis in a drive form factor with IP-based network connections. |
| Module | A small, typically removable, chassis or card which contains devices for a particular subsystem or function. |
| Other | A chassis that does not fit any of these definitions. |
| Pod | A collection of equipment racks in a large, likely transportable, container. |
| Rack | An equipment rack, typically a 19-inch wide freestanding unit. |
| RackGroup | A group of racks which form a single entity or share infrastructure. |
| RackMount | A single system chassis designed specifically for mounting in an equipment rack. |
| Row | A collection of equipment racks. |
| Shelf | An enclosed or semi-enclosed, typically horizontally-oriented, system chassis which must be plugged into a multi-system chassis to function normally. |
| Sidecar | A chassis that mates mechanically with another chassis to expand its capabilities or capacity. |
| Sled | An enclosed or semi-enclosed, system chassis which must be plugged into a multi-system chassis to function normally similar to a blade type chassis. |
| StandAlone | A single, free-standing system, commonly called a tower or desktop chassis. |
| StorageEnclosure | A chassis which encloses storage. |
| Zone | A logical division or portion of a physical chassis that contains multiple devices or systems that cannot be physically separated. |

### IndicatorLED:


The state of the indicator LED, used to identify the chassis.

| string | Description |
| --- | --- |
| Blinking | The Indicator LED is blinking. |
| Lit | The Indicator LED is lit. |
| Off | The Indicator LED is off. |
| Unknown | The state of the Indicator LED cannot be determined. *This value has been Deprecated in favor of returning null if the state is unknown.* |

### IntrusionSensor:


This indicates the known state of the physical security sensor, such as if it is hardware intrusion detected.

| string | Description |
| --- | --- |
| HardwareIntrusion | A door, lock, or other mechanism protecting the internal system hardware from being accessed is detected as being in an insecure state. |
| Normal | No abnormal physical security conditions are detected at this time. |
| TamperingDetected | Physical tampering of the monitored entity is detected. |

### IntrusionSensorReArm:


This indicates how the Normal state to be restored.

| string | Description |
| --- | --- |
| Automatic | This sensor would be restored to the Normal state automatically as no abnormal physical security conditions are detected. |
| Manual | This sensor would be restored to the Normal state by a manual re-arm. |

### PowerState:


The current power state of the chassis.

| string | Description |
| --- | --- |
| Off | The components within the chassis has no power, except some components may continue to have AUX power such as management controller. |
| On | The components within the chassis has power on. |
| PoweringOff | A temporary state between On and Off. The components within the chassis can take time to process the power off action. |
| PoweringOn | A temporary state between Off and On. The components within the chassis can take time to process the power on action. |

### ResetType:


The type of reset to be performed.

| string | Description |
| --- | --- |
| ForceOff | Turn the unit off immediately (non-graceful shutdown). |
| ForceOn | Turn the unit on immediately. |
| ForceRestart | Perform an immediate (non-graceful) shutdown, followed by a restart. |
| GracefulRestart | Perform a graceful shutdown followed by a restart of the system. |
| GracefulShutdown | Perform a graceful shutdown and power off. |
| Nmi | Generate a Diagnostic Interrupt (usually an NMI on x86 systems) to cease normal operations, perform diagnostic actions and typically halt the system. |
| On | Turn the unit on. |
| PowerCycle | Perform a power cycle of the unit. |
| PushPowerButton | Simulate the pressing of the physical power button on this unit. |


## ComputerSystem 1.5.0

This schema defines a computer system and its respective properties.  A computer system represents a machine (physical or virtual) and the local resources such as memory, cpu and other devices that can be accessed from that machine.

|     |     |     |
| --- | --- | --- |
| **AssetTag** | string<br><br>*read-write<br>(null)* | The user definable tag that can be used to track this computer system for inventory or other client purposes. |
| **Bios** {} | object | A reference to the BIOS settings associated with this system. See the *Bios* schema for details on this property. |
| **BiosVersion** | string<br><br>*read-only<br>(null)* | The version of the system BIOS or primary system firmware. |
| **Boot** { | object | Information about the boot settings for this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootNext** | string<br><br>*read-write<br>(null)* | This property is the BootOptionReference of the Boot Option to perform a one time boot from when BootSourceOverrideTarget is UefiBootNext. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootOptions** { | object | A reference to the collection of the UEFI Boot Options associated with this Computer System. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *BootOption*. See the BootOption schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootOrder** [ ] | array (string, null)<br><br>*read-write* | Ordered array of BootOptionReference strings representing the persistent Boot Order associated with this computer system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootSourceOverrideEnabled** | string<br>(enum)<br><br>*read-write<br>(null)* | Describes the state of the Boot Source Override feature. *For the possible property values, see BootSourceOverrideEnabled in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootSourceOverrideMode** | string<br>(enum)<br><br>*read-write<br>(null)* | The BIOS Boot Mode (either Legacy or UEFI) to be used when BootSourceOverrideTarget boot source is booted from. *For the possible property values, see BootSourceOverrideMode in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootSourceOverrideTarget** | string<br>(enum)<br><br>*read-write<br>(null)* | The current boot source to be used at next boot instead of the normal boot device, if BootSourceOverrideEnabled is true. *For the possible property values, see BootSourceOverrideTarget in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UefiTargetBootSourceOverride** | string<br><br>*read-write<br>(null)* | This property is the UEFI Device Path of the device to boot from when BootSourceOverrideTarget is UefiTarget. |
| } |   |   |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EthernetInterfaces** { | object | A reference to the collection of Ethernet interfaces associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *EthernetInterface*. See the EthernetInterface schema for details. |
| } |   |   |
| **HostedServices** { | object | The services that this computer system supports. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StorageServices** { | object | A reference to a collection of storage services supported by this computer system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **HostingRoles** [ ] | array (string<br>(enum))<br><br>*read-only* | The hosing roles that this computer system supports. The enumerations of HostingRoles specify different features that the hosting ComputerSystem supports. *For the possible property values, see HostingRoles in Property Details.* |
| **HostName** | string<br><br>*read-write<br>(null)* | The DNS Host Name, without any domain information. |
| **HostWatchdogTimer** { | object | This object describes the Host Watchdog Timer functionality for this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FunctionEnabled** | boolean<br><br>*read-write required<br>(null)* | This indicates if the Host Watchdog Timer functionality has been enabled. Additional host-based software is necessary to activate the timer function. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TimeoutAction** | string<br>(enum)<br><br>*read-write required<br>(null)* | This property indicates the action to perform when the Watchdog Timer reaches its timeout value. *For the possible property values, see TimeoutAction in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WarningAction** | string<br>(enum)<br><br>*read-write<br>(null)* | This property indicates the action to perform when the Watchdog Timer is close (typically 3-10 seconds) to reaching its timeout value. *For the possible property values, see WarningAction in Property Details.* |
| } |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **IndicatorLED** | string<br>(enum)<br><br>*read-write<br>(null)* | The state of the indicator LED, used to identify the system. *For the possible property values, see IndicatorLED in Property Details.* |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Chassis** [ { | array | An array of references to the chassis in which this system is contained. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ConsumingComputerSystems** [ { | array | An array of references to ComputerSystems that are realized, in whole or in part, from this ComputerSystem. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another ComputerSystem resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CooledBy** [ { | array | An array of ID[s] of resources that cool this computer system. Normally the ID will be a chassis or a specific set of fans. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Endpoints** [ { } ] | array (object) | An array of references to the endpoints that connect to this system. This is the schema definition for the Endpoint resource. It represents the properties of an entity that sends or receives protocol defined messages over a transport. See the *Endpoint* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedBy** [ { | array | An array of references to the Managers responsible for this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Manager resource. See the Links section and the *Manager* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PoweredBy** [ { | array | An array of ID[s] of resources that power this computer system. Normally the ID will be a chassis or a specific set of Power Supplies. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResourceBlocks** [ { } ] | array (object) | An array of references to the Resource Blocks that are used in this Computer System. This schema defines a Resource Block resource. See the *ResourceBlock* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SupplyingComputerSystems** [ { | array | An array of references to ComputerSystems that contribute, in whole or in part, to the implementation of this ComputerSystem. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another ComputerSystem resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **LogServices** { | object | A reference to the collection of Log Services associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *LogService*. See the LogService schema for details. |
| } |   |   |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | The manufacturer or OEM of this system. |
| **Memory** { | object | A reference to the collection of Memory associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Memory*. See the Memory schema for details. |
| } |   |   |
| **MemoryDomains** { | object<br><br>*<br>(null)* | A reference to the collection of Memory Domains associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *MemoryDomain*. See the MemoryDomain schema for details. |
| } |   |   |
| **MemorySummary** { | object | This object describes the central memory of the system in general detail. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemoryMirroring** | string<br>(enum)<br><br>*read-only<br>(null)* | The ability and type of memory mirroring supported by this system. *For the possible property values, see MemoryMirroring in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalSystemMemoryGiB** | number<br><br>*read-only<br>(null)* | The total configured operating system-accessible memory (RAM), measured in GiB. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalSystemPersistentMemoryGiB** | number<br><br>*read-only<br>(null)* | The total configured, system-accessible persistent memory, measured in GiB. |
| } |   |   |
| **Model** | string<br><br>*read-only<br>(null)* | The product name for this system, without the manufacturer name. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NetworkInterfaces** { | object | A reference to the collection of Network Interfaces associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *NetworkInterface*. See the NetworkInterface schema for details. |
| } |   |   |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PartNumber** | string<br><br>*read-only<br>(null)* | The part number for this system. |
| **PCIeDevices** [ { | array | A reference to a collection of PCIe Devices used by this computer system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeDevice resource. See the Links section and the *PCIeDevice* schema for details. |
| } ] |   |   |
| **PCIeFunctions** [ { | array | A reference to a collection of PCIe Functions used by this computer system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeFunction resource. See the Links section and the *PCIeFunction* schema for details. |
| } ] |   |   |
| **PowerState** | string<br>(enum)<br><br>*read-only<br>(null)* | This is the current power state of the system. *For the possible property values, see PowerState in Property Details.* |
| **Processors** { | object | A reference to the collection of Processors associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Processor*. See the Processor schema for details. |
| } |   |   |
| **ProcessorSummary** { | object | This object describes the central processors of the system in general detail. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | number<br><br>*read-only<br>(null)* | The number of physical processors in the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LogicalProcessorCount** | number<br><br>*read-only<br>(null)* | The number of logical processors in the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | The processor model for the primary or majority of processors in this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| } |   |   |
| **Redundancy** [ { | array | A reference to a collection of Redundancy entities that each name a set of computer systems that provide redundancy for this ComputerSystem. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } ] |   |   |
| **SecureBoot** { | object | A reference to the UEFI SecureBoot resource associated with this system. See the *SecureBoot* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a SecureBoot resource. See the Links section and the *SecureBoot* schema for details. |
| } |   |   |
| **SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number for this system. |
| **SimpleStorage** { | object | A reference to the collection of storage devices associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *SimpleStorage*. See the SimpleStorage schema for details. |
| } |   |   |
| **SKU** | string<br><br>*read-only<br>(null)* | The manufacturer SKU for this system. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **Storage** { | object | A reference to the collection of storage devices associated with this system. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Storage*. See the Storage schema for details. |
| } |   |   |
| **SubModel** | string<br><br>*read-only<br>(null)* | The sub-model for this system. |
| **SystemType** | string<br>(enum)<br><br>*read-only* | The type of computer system represented by this resource. *For the possible property values, see SystemType in Property Details.* |
| **TrustedModules** [ { | array | This object describes the array of Trusted Modules in the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | The firmware version of this Trusted Module. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion2** | string<br><br>*read-only<br>(null)* | The 2nd firmware version of this Trusted Module, if applicable. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InterfaceType** | string<br>(enum)<br><br>*read-only<br>(null)* | This property indicates the interface type of the Trusted Module. *For the possible property values, see InterfaceType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InterfaceTypeSelection** | string<br>(enum)<br><br>*read-only<br>(null)* | The Interface Type selection supported by this Trusted Module. *For the possible property values, see InterfaceTypeSelection in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| } ] |   |   |
| **UUID** | string<br><br>*read-only<br>(null)* | The universal unique identifier (UUID) for this system. |

### Actions

### Reset


This action is used to reset the system.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResetType** | string<br>(enum)<br><br>*read-write* | The type of reset to be performed. *For the possible property values, see ResetType in Property Details.* |
| } |   |   |   |

### SetDefaultBootOrder


This action is used to set the Boot Order to the default settings.

**URIs**:


(This action takes no parameters.)


### Property Details

### BootSourceOverrideEnabled:


Describes the state of the Boot Source Override feature.

| string | Description |
| --- | --- |
| Continuous | The system will boot to the target specified in the BootSourceOverrideTarget until this property is set to Disabled. |
| Disabled | The system will boot normally. |
| Once | On its next boot cycle, the system will boot (one time) to the Boot Source Override Target. The value of BootSourceOverrideEnabled is then reset back to Disabled. |

### BootSourceOverrideMode:


The BIOS Boot Mode (either Legacy or UEFI) to be used when BootSourceOverrideTarget boot source is booted from.

| string | Description |
| --- | --- |
| Legacy | The system will boot in non-UEFI boot mode to the Boot Source Override Target. |
| UEFI | The system will boot in UEFI boot mode to the Boot Source Override Target. |

### BootSourceOverrideTarget:


The current boot source to be used at next boot instead of the normal boot device, if BootSourceOverrideEnabled is true.

| string | Description |
| --- | --- |
| BiosSetup | Boot to the BIOS Setup Utility. |
| Cd | Boot from the CD/DVD disc. |
| Diags | Boot the manufacturer's Diagnostics program. |
| Floppy | Boot from the floppy disk drive. |
| Hdd | Boot from a hard drive. |
| None | Boot from the normal boot device. |
| Pxe | Boot from the Pre-Boot EXecution (PXE) environment. |
| RemoteDrive | Boot from a remote drive (e.g. iSCSI). |
| SDCard | Boot from an SD Card. |
| UefiBootNext | Boot to the UEFI Device specified in the BootNext property. |
| UefiHttp | Boot from a UEFI HTTP network location. |
| UefiShell | Boot to the UEFI Shell. |
| UefiTarget | Boot to the UEFI Device specified in the UefiTargetBootSourceOverride property. |
| Usb | Boot from a USB device as specified by the system BIOS. |
| Utilities | Boot the manufacturer's Utilities program(s). |

### HostingRoles:


The hosing roles that this computer system supports. The enumerations of HostingRoles specify different features that the hosting ComputerSystem supports.

| string | Description |
| --- | --- |
| ApplicationServer | The system hosts functionality that supports general purpose applications. |
| StorageServer | The system hosts functionality that supports the system acting as a storage server. |
| Switch | The system hosts functionality that supports the system acting as a switch. |

### IndicatorLED:


The state of the indicator LED, used to identify the system.

| string | Description |
| --- | --- |
| Blinking | The Indicator LED is blinking. |
| Lit | The Indicator LED is lit. |
| Off | The Indicator LED is off. |
| Unknown | The state of the Indicator LED cannot be determined. *This value has been Deprecated in favor of returning null if the state is unknown.* |

### InterfaceType:


This property indicates the interface type of the Trusted Module.

| string | Description |
| --- | --- |
| TCM1_0 | Trusted Cryptography Module (TCM) 1.0. |
| TPM1_2 | Trusted Platform Module (TPM) 1.2. |
| TPM2_0 | Trusted Platform Module (TPM) 2.0. |

### InterfaceTypeSelection:


The Interface Type selection supported by this Trusted Module.

| string | Description |
| --- | --- |
| BiosSetting | The TrustedModule supports switching InterfaceType via platform software, such as a BIOS configuration Attribute. |
| FirmwareUpdate | The TrustedModule supports switching InterfaceType via a firmware update. |
| None | The TrustedModule does not support switching the InterfaceType. |
| OemMethod | The TrustedModule supports switching InterfaceType via an OEM proprietary mechanism. |

### MemoryMirroring:


The ability and type of memory mirroring supported by this system.

| string | Description |
| --- | --- |
| DIMM | The system supports DIMM mirroring at the DIMM level.  Individual DIMMs can be mirrored. |
| Hybrid | The system supports a hybrid mirroring at the system and DIMM levels.  Individual DIMMs can be mirrored. |
| None | The system does not support DIMM mirroring. |
| System | The system supports DIMM mirroring at the System level.  Individual DIMMs are not paired for mirroring in this mode. |

### PowerState:


This is the current power state of the system.

| string | Description |
| --- | --- |
| Off | The system is powered off, although some components may continue to have AUX power such as management controller. |
| On | The system is powered on. |
| PoweringOff | A temporary state between On and Off. The power off action can take time while the OS is in the shutdown process. |
| PoweringOn | A temporary state between Off and On. This temporary state can be very short. |

### ResetType:


The type of reset to be performed.

| string | Description |
| --- | --- |
| ForceOff | Turn the unit off immediately (non-graceful shutdown). |
| ForceOn | Turn the unit on immediately. |
| ForceRestart | Perform an immediate (non-graceful) shutdown, followed by a restart. |
| GracefulRestart | Perform a graceful shutdown followed by a restart of the system. |
| GracefulShutdown | Perform a graceful shutdown and power off. |
| Nmi | Generate a Diagnostic Interrupt (usually an NMI on x86 systems) to cease normal operations, perform diagnostic actions and typically halt the system. |
| On | Turn the unit on. |
| PowerCycle | Perform a power cycle of the unit. |
| PushPowerButton | Simulate the pressing of the physical power button on this unit. |

### SystemType:


The type of computer system represented by this resource.

| string | Description |
| --- | --- |
| Composed | A computer system that has been created by binding resource blocks together. |
| OS | An operating system instance. |
| Physical | A computer system. |
| PhysicallyPartitioned | A hardware-based partition of a computer system. |
| Virtual | A virtual machine instance running on this system. |
| VirtuallyPartitioned | A virtual or software-based partition of a computer system. |

### TimeoutAction:


This property indicates the action to perform when the Watchdog Timer reaches its timeout value.

| string | Description |
| --- | --- |
| None | No action taken. |
| OEM | Perform an OEM-defined action. |
| PowerCycle | Power cycle the system. |
| PowerDown | Power down the system. |
| ResetSystem | Reset the system. |

### WarningAction:


This property indicates the action to perform when the Watchdog Timer is close (typically 3-10 seconds) to reaching its timeout value.

| string | Description |
| --- | --- |
| DiagnosticInterrupt | Raise a (typically non-maskable) Diagnostic Interrupt. |
| MessagingInterrupt | Raise a legacy IPMI messaging interrupt. |
| None | No action taken. |
| OEM | Perform an OEM-defined action. |
| SCI | Raise an interrupt using the ACPI System Control Interrupt (SCI). |
| SMI | Raise a Systems Management Interrupt (SMI). |


## Drive 1.4.0

The Drive schema represents a single physical disk drive for a system, including links to associated Volumes.

|     |     |     |
| --- | --- | --- |
| **Assembly** {} | object | A reference to the Assembly resource associated with this drive. See the *Assembly* schema for details on this property. |
| **AssetTag** | string<br><br>*read-write<br>(null)* | The user assigned asset tag for this drive. |
| **BlockSizeBytes** | number<br>(Bytes)<br><br>*read-only<br>(null)* | The size of the smallest addressible unit (Block) of this drive in bytes. |
| **CapableSpeedGbs** | number<br>(Gbit/s)<br><br>*read-only<br>(null)* | The speed which this drive can communicate to a storage controller in ideal conditions in Gigabits per second. |
| **CapacityBytes** | number<br>(Bytes)<br><br>*read-only<br>(null)* | The size in bytes of this Drive. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EncryptionAbility** | string<br>(enum)<br><br>*read-only<br>(null)* | The encryption abilities of this drive. *For the possible property values, see EncryptionAbility in Property Details.* |
| **EncryptionStatus** | string<br>(enum)<br><br>*read-only<br>(null)* | The status of the encrytion of this drive. *For the possible property values, see EncryptionStatus in Property Details.* |
| **FailurePredicted** | boolean<br><br>*read-only<br>(null)* | Is this drive currently predicting a failure in the near future. |
| **HotspareType** | string<br>(enum)<br><br>*read-only<br>(null)* | The type of hotspare this drive is currently serving as. *For the possible property values, see HotspareType in Property Details.* |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Identifiers** [ { } ] | array (object) | The Durable names for the drive. This type describes any additional identifiers for a resource. See the *Resource* schema for details on this property. |
| **IndicatorLED** | string<br>(enum)<br><br>*read-write<br>(null)* | The state of the indicator LED, used to identify the drive. *For the possible property values, see IndicatorLED in Property Details.* |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Chassis** { | object | A reference to the Chassis which contains this Drive. See the *Chassis* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Endpoints** [ { } ] | array (object) | An array of references to the endpoints that connect to this drive. This is the schema definition for the Endpoint resource. It represents the properties of an entity that sends or receives protocol defined messages over a transport. See the *Endpoint* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Volumes** [ { | array | An array of references to the volumes contained in this drive. This will reference Volumes that are either wholly or only partly contained by this drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Volume resource. See the Links section and the *Volume* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **Location** [ { } ] | array (object) | The Location of the drive. This type describes the location of a resource. See the *Resource* schema for details on this property. |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | This is the manufacturer of this drive. |
| **MediaType** | string<br>(enum)<br><br>*read-only<br>(null)* | The type of media contained in this drive. *For the possible property values, see MediaType in Property Details.* |
| **Model** | string<br><br>*read-only<br>(null)* | This is the model number for the drive. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NegotiatedSpeedGbs** | number<br>(Gbit/s)<br><br>*read-only<br>(null)* | The speed which this drive is currently communicating to the storage controller in Gigabits per second. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Operations** [ { | array | The operations currently running on the Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AssociatedTask** { | object | A reference to the task associated with the operation if any. See the *Task* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Task resource. See the Links section and the *Task* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OperationName** | string<br><br>*read-only<br>(null)* | The name of the operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PercentageComplete** | number<br><br>*read-only<br>(null)* | The percentage of the operation that has been completed. |
| } ] |   |   |
| **PartNumber** | string<br><br>*read-only<br>(null)* | The part number for this drive. |
| **PhysicalLocation** {} | object | The Location of the drive. See the *Resource* schema for details on this property. |
| **PredictedMediaLifeLeftPercent** | number<br><br>*read-only<br>(null)* | The percentage of reads and writes that are predicted to still be available for the media. |
| **Protocol** | string<br>(enum)<br><br>*read-only<br>(null)* | The protocol this drive is using to communicate to the storage controller. *For the possible property values, see Protocol in Property Details.* |
| **Revision** | string<br><br>*read-only<br>(null)* | The revision of this Drive. This is typically the firmware/hardware version of the drive. |
| **RotationSpeedRPM** | number<br>(RPM)<br><br>*read-only<br>(null)* | The rotation speed of this Drive in Revolutions per Minute (RPM). |
| **SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number for this drive. |
| **SKU** | string<br><br>*read-only<br>(null)* | This is the SKU for this drive. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **StatusIndicator** | string<br>(enum)<br><br>*read-write<br>(null)* | The state of the status indicator, used to communicate status information about this drive. *For the possible property values, see StatusIndicator in Property Details.* |

### Actions

### SecureErase


This action is used to securely erase the contents of the drive.

**URIs**:


(This action takes no parameters.)


### Property Details

### EncryptionAbility:


The encryption abilities of this drive.

| string | Description |
| --- | --- |
| None | The drive is not capable of self encryption. |
| Other | The drive is capable of self encryption through some other means. |
| SelfEncryptingDrive | The drive is capable of self encryption per the Trusted Computing Group's Self Encrypting Drive Standard. |

### EncryptionStatus:


The status of the encrytion of this drive.

| string | Description |
| --- | --- |
| Foreign | The drive is currently encrypted, the data is not accessible to the user, and the system requires user intervention to expose the data. |
| Locked | The drive is currently encrypted and the data is not accessible to the user, however the system has the ability to unlock the drive automatically. |
| Unecrypted | The drive is not currently encrypted. *This value has been Deprecated in favor of Unencrypted.* |
| Unencrypted | The drive is not currently encrypted. |
| Unlocked | The drive is currently encrypted but the data is accessible to the user unencrypted. |

### HotspareType:


The type of hotspare this drive is currently serving as.

| string | Description |
| --- | --- |
| Chassis | The drive is currently serving as a hotspare for all other drives in the chassis. |
| Dedicated | The drive is currently serving as a hotspare for a user defined set of drives. |
| Global | The drive is currently serving as a hotspare for all other drives in the storage system. |
| None | The drive is not currently a hotspare. |

### IndicatorLED:


The state of the indicator LED, used to identify the drive.

| string | Description |
| --- | --- |
| Blinking | The Indicator LED is blinking. |
| Lit | The Indicator LED is lit. |
| Off | The Indicator LED is off. |

### MediaType:


The type of media contained in this drive.

| string | Description |
| --- | --- |
| HDD | The drive media type is traditional magnetic platters. |
| SMR | The drive media type is shingled magnetic recording. |
| SSD | The drive media type is solid state or flash memory. |

### Protocol:


The protocol this drive is using to communicate to the storage controller.

| string | Description |
| --- | --- |
| AHCI | Advanced Host Controller Interface. |
| FC | Fibre Channel. |
| FCoE | Fibre Channel over Ethernet. |
| FCP | Fibre Channel Protocol for SCSI. |
| FICON | FIbre CONnection (FICON). |
| FTP | File Transfer Protocol. |
| HTTP | Hypertext Transport Protocol. |
| HTTPS | Secure Hypertext Transport Protocol. |
| iSCSI | Internet SCSI. |
| iWARP | Internet Wide Area Remote Direct Memory Access Protocol. |
| NFSv3 | Network File System version 3. |
| NFSv4 | Network File System version 4. |
| NVMe | Non-Volatile Memory Express. |
| NVMeOverFabrics | NVMe over Fabrics. |
| OEM | OEM specific. |
| PCIe | PCI Express (Vendor Proprietary). |
| RoCE | RDMA over Converged Ethernet Protocol. |
| RoCEv2 | RDMA over Converged Ethernet Protocol Version 2. |
| SAS | Serial Attached SCSI. |
| SATA | Serial AT Attachment. |
| SFTP | Secure File Transfer Protocol. |
| SMB | Server Message Block (aka CIFS Common Internet File System). |
| UHCI | Universal Host Controller Interface. |
| USB | Universal Serial Bus. |

### StatusIndicator:


The state of the status indicator, used to communicate status information about this drive.

| string | Description |
| --- | --- |
| Fail | The drive has failed. |
| Hotspare | The drive is marked to be automatically rebuilt and used as a replacement for a failed drive. |
| InACriticalArray | The array that this drive is a part of is degraded. |
| InAFailedArray | The array that this drive is a part of is failed. |
| OK | The drive is OK. |
| PredictiveFailureAnalysis | The drive is still working but predicted to fail soon. |
| Rebuild | The drive is being rebuilt. |


## EthernetInterface 1.4.0

The EthernetInterface schema represents a single, logical ethernet interface or network interface controller (NIC).

|     |     |     |
| --- | --- | --- |
| **AutoNeg** | boolean<br><br>*read-write<br>(null)* | This indicates if the speed and duplex are automatically negotiated and configured on this interface. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **DHCPv4** { | object<br><br>*<br>(null)* | DHCPv4 configuration for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DHCPEnabled** | boolean<br><br>*read-write<br>(null)* | Determines whether DHCPv4 is enabled on this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDNSServers** | boolean<br><br>*read-write<br>(null)* | Determines whether to use DHCPv4-supplied DNS servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDomainName** | boolean<br><br>*read-write<br>(null)* | Determines whether to use a DHCPv4-supplied domain name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseGateway** | boolean<br><br>*read-write<br>(null)* | Determines whether to use a DHCPv4-supplied gateway. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseNTPServers** | boolean<br><br>*read-write<br>(null)* | Determines whether to use DHCPv4-supplied NTP servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseStaticRoutes** | boolean<br><br>*read-write<br>(null)* | Determines whether to use DHCPv4-supplied static routes. |
| } |   |   |
| **DHCPv6** { | object<br><br>*<br>(null)* | DHCPv6 configuration for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OperatingMode** | string<br>(enum)<br><br>*read-write<br>(null)* | Determines the DHCPv6 operating mode for this interface. *For the possible property values, see OperatingMode in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDNSServers** | boolean<br><br>*read-write<br>(null)* | When enabled, DNS server addresses supplied through DHCPv6 stateless mode will be used. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDomainName** | boolean<br><br>*read-write<br>(null)* | When enabled, the domain name supplied through DHCPv6 stateless mode will be used. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseNTPServers** | boolean<br><br>*read-write<br>(null)* | When enabled, NTP server addresses supplied through DHCPv6 stateless mode will be used. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseRapidCommit** | boolean<br><br>*read-write<br>(null)* | Determines whether to use DHCPv6 rapid commit mode for stateful mode address assignments. Do not enable in networks where more than one DHCPv6 server is configured to provide address assignments. |
| } |   |   |
| **FQDN** | string<br><br>*read-write<br>(null)* | This is the complete, fully qualified domain name obtained by DNS for this interface. |
| **FullDuplex** | boolean<br><br>*read-write<br>(null)* | This indicates if the interface is in Full Duplex mode or not. |
| **HostName** | string<br><br>*read-write<br>(null)* | The DNS Host Name, without any domain information. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **InterfaceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this interface is enabled. |
| **IPv4Addresses** [ { } ] | array (object) | The IPv4 addresses currently assigned to this interface. This type describes an IPv4 Address. See the *IPAddresses* schema for details on this property. |
| **IPv4StaticAddresses** [ { } ] | array (object) | The IPv4 static addresses assigned to this interface. This type describes an IPv4 Address. See the *IPAddresses* schema for details on this property. |
| **IPv6Addresses** [ { } ] | array (object) | Enumerates in an array all of the currently assigned IPv6 addresses on this interface. This type describes an IPv6 Address. See the *IPAddresses* schema for details on this property. |
| **IPv6AddressPolicyTable** [ { | array | An array representing the RFC 6724 Address Selection Policy Table. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Label** | number<br><br>*read-write<br>(null)* | The IPv6 Label (as defined in RFC 6724 section 2.1). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Precedence** | number<br><br>*read-write<br>(null)* | The IPv6 Precedence (as defined in RFC 6724 section 2.1. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Prefix** | string<br><br>*read-write<br>(null)* | The IPv6 Address Prefix (as defined in RFC 6724 section 2.1). |
| } ] |   |   |
| **IPv6DefaultGateway** | string<br><br>*read-only<br>(null)* | This is the IPv6 default gateway address that is currently in use on this interface. |
| **IPv6StaticAddresses** [ { } ] | array (object) | Represents in an array all of the IPv6 static addresses to be assigned on this interface. This object represents a single IPv6 static address to be assigned on a network interface. See the *IPAddresses* schema for details on this property. |
| **IPv6StaticDefaultGateways** [ { } ] | array (object) | The IPv6 static default gateways for this interface. This object represents a single IPv6 static address to be assigned on a network interface. See the *IPAddresses* schema for details on this property. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Chassis** { | object | A reference to the Chassis which contains this Ethernet Interface. See the *Chassis* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Endpoints** [ { } ] | array (object) | An array of references to the endpoints that connect to this ethernet interface. This is the schema definition for the Endpoint resource. It represents the properties of an entity that sends or receives protocol defined messages over a transport. See the *Endpoint* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HostInterface** {} | object | This is a reference to a Host Interface that is associated with this Ethernet Interface. See the *HostInterface* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **LinkStatus** | string<br>(enum)<br><br>*read-only<br>(null)* | The link status of this interface (port). *For the possible property values, see LinkStatus in Property Details.* |
| **MACAddress** | string<br><br>*read-write<br>(null)* | This is the currently configured MAC address of the (logical port) interface. |
| **MaxIPv6StaticAddresses** | number<br><br>*read-only<br>(null)* | This indicates the maximum number of Static IPv6 addresses that can be configured on this interface. |
| **MTUSize** | number<br><br>*read-write<br>(null)* | This is the currently configured Maximum Transmission Unit (MTU) in bytes on this interface. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NameServers** [ ] | array (string)<br><br>*read-only* | This represents DNS name servers that are currently in use on this interface. |
| **NameServersIPv6** [ ] | array (string, null)<br><br>*read-only* | The IPV6 DNS name servers to be used for retrieving the host name. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PermanentMACAddress** | string<br><br>*read-only<br>(null)* | This is the permanent MAC address assigned to this interface (port). |
| **SpeedMbps** | number<br>(Mbit/s)<br><br>*read-write<br>(null)* | This is the current speed in Mbps of this interface. |
| **StatelessAddressAutoConfig** { | object<br><br>*<br>(null)* | Stateless Address Automatic Configuration (SLAAC) parameters for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv4AutoConfigEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates whether IPv4 SLAAC is enabled for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv6AutoConfigEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates whether IPv6 SLAAC is enabled for this interface. |
| } |   |   |
| **StaticNameServers** [ ] | array (string)<br><br>*read-write* | A statically defined set of DNS server IP addresses (both IPv4 and IPv6). |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **UefiDevicePath** | string<br><br>*read-only<br>(null)* | The UEFI device path for this interface. |
| **VLAN** {} | object<br><br>*<br>(null)* | If this Network Interface supports more than one VLAN, this property is not present. VLANs collections appear in the Link section of this resource. See the *VLanNetworkInterface* schema for details on this property. |
| **VLANs** { | object | This is a reference to a collection of VLANs and is only used if the interface supports more than one VLANs. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *VLanNetworkInterface*. See the VLanNetworkInterface schema for details. |
| } |   |   |

### Property Details

### LinkStatus:


The link status of this interface (port).

| string | Description |
| --- | --- |
| LinkDown | There is no link on this interface, but the interface is connected. |
| LinkUp | The link is available for communication on this interface. |
| NoLink | There is no link or connection detected on this interface. |

### OperatingMode:


Determines the DHCPv6 operating mode for this interface.

| string | Description |
| --- | --- |
| Disabled | DHCPv6 is disabled. |
| Stateful | DHCPv6 stateful mode. |
| Stateless | DHCPv6 stateless mode. |


## Event 1.2.1

The Event schema describes the JSON payload received by an Event Destination (which has subscribed to event notification) when events occurs.  This resource contains data about event(s), including descriptions, severity and MessageId reference to a Message Registry that can be accessed for further information.

|     |     |     |
| --- | --- | --- |
| **Context** | string<br><br>*read-only* | A context can be supplied at subscription time.  This property is the context value supplied by the subscriber. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Events** [ { | array<br><br>* required* | Each event in this array has a set of properties that describe the event.  Since this is an array, more than one event can be sent simultaneously. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Actions** {} | object | The available actions for this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Context** | string<br><br>*read-only* | A context can be supplied at subscription time.  This property is the context value supplied by the subscriber. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EventId** | string<br><br>*read-only* | This is a unique instance identifier of an event. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EventTimestamp** | string<br><br>*read-only* | This is time the event occurred. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EventType** | string<br>(enum)<br><br>*read-only required* | This indicates the type of event sent, according to the definitions in the EventService. *For the possible property values, see EventType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemberId** | string<br><br>*read-only* | This is the identifier for the member within the collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Message** | string<br><br>*read-only* | This is the human readable message, if provided. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MessageArgs** [ ] | array (string)<br><br>*read-only* | This array of message arguments are substituted for the arguments in the message when looked up in the message registry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MessageId** | string<br><br>*read-only required* | This is the key for this message which can be used to look up the message in a message registry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OriginOfCondition** { | object | This indicates the resource that originated the condition that caused the event to be generated. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Severity** | string<br><br>*read-only* | This is the severity of the event. |
| } ] |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |

### Property Details

### EventType:


This indicates the type of event sent, according to the definitions in the EventService.

| string | Description |
| --- | --- |
| Alert | A condition exists which requires attention. |
| ResourceAdded | A resource has been added. |
| ResourceRemoved | A resource has been removed. |
| ResourceUpdated | The value of this resource has been updated. |
| StatusChange | The status of this resource has changed. |


## EventDestination 1.3.0

An Event Destination desribes the target of an event subscription, including the types of events subscribed and context to provide to the target in the Event payload.

|     |     |     |
| --- | --- | --- |
| **Context** | string<br><br>*read-write required<br>(null)* | A client-supplied string that is stored with the event destination subscription. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Destination** | string<br><br>*read-only required on create* | The URI of the destination Event Service. |
| **EventTypes** [ ] | array (string<br>(enum))<br><br>*read-only* | This property shall contain the types of events that shall be sent to the desination. *For the possible property values, see EventTypes in Property Details.* |
| **HttpHeaders** [ { | array | This is for setting HTTP headers, such as authorization information.  This object will be null on a GET. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**(pattern)** | string<br><br>*read-write* | Property names follow regular expression pattern "^\[^:\\\\s\]\+$" |
| } ] |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **MessageIds** [ ] | array (string, null)<br><br>*read-only* | A list of MessageIds that the service will only send.  If this property is absent or the array is empty, then Events with any MessageId will be sent to the subscriber. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **OriginResources** [ { | array | A list of resources for which the service will only send related events.  If this property is absent or the array is empty, then Events originating from any resource will be sent to the subscriber. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } ] |   |   |
| **Protocol** | string<br>(enum)<br><br>*read-only required on create* | The protocol type of the event connection. *For the possible property values, see Protocol in Property Details.* |
| **SubscriptionType** | string<br>(enum)<br><br>*read-only required<br>(null)* | Indicates the subscription type for events. *For the possible property values, see SubscriptionType in Property Details.* |

### Property Details

### EventTypes:


This property shall contain the types of events that shall be sent to the desination.

| string | Description |
| --- | --- |
| Alert | A condition exists which requires attention. |
| ResourceAdded | A resource has been added. |
| ResourceRemoved | A resource has been removed. |
| ResourceUpdated | The value of this resource has been updated. |
| StatusChange | The status of this resource has changed. |

### Protocol:


The protocol type of the event connection.

| string | Description |
| --- | --- |
| Redfish | The destination follows the Redfish specification for event notifications. |

### SubscriptionType:


Indicates the subscription type for events.

| string | Description |
| --- | --- |
| RedfishEvent | The subscription follows the Redfish specification for event notifications, which is done by a service sending an HTTP POST to the subscriber's destination URI. |
| SSE | The subscription follows the HTML5 Server-Sent Event definition for event notifications. |


## EventService 1.1.0

The Event Service resource contains properties for managing event subcriptions and generates the events sent to subscribers.  The resource has links to the actual collection of subscriptions (called Event Destinations).

|     |     |     |
| --- | --- | --- |
| **DeliveryRetryAttempts** | number<br><br>*read-write* | This is the number of attempts an event posting is retried before the subscription is terminated.  This retry is at the service level, meaning the HTTP POST to the Event Destination was returned by the HTTP operation as unsuccessful (4xx or 5xx return code) or an HTTP timeout occurred this many times before the Event Destination subscription is terminated. |
| **DeliveryRetryIntervalSeconds** | number<br>(seconds)<br><br>*read-write* | This represents the number of seconds between retry attempts for sending any given Event. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EventTypesForSubscription** [ ] | array (string<br>(enum))<br><br>*read-only* | This is the types of Events that can be subscribed to. *For the possible property values, see EventTypesForSubscription in Property Details.* |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **ServerSentEventUri** | string<br><br>*read-only* | Link to a URI for receiving Sever Sent Event representations of the events generated by this service. |
| **ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **Subscriptions** { | object | This is a reference to a collection of Event Destination resources. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *EventDestination*. See the EventDestination schema for details. |
| } |   |   |

### Actions

### SubmitTestEvent


This action is used to generate a test event.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EventId** | string<br><br>*read-write required* | This is the ID of event to be added. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EventTimestamp** | string<br><br>*read-write required* | This is the time stamp of event to be added. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EventType** | string<br>(enum)<br><br>*read-write* | This is the type of event to be added. *For the possible property values, see EventType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Message** | string<br><br>*read-write required* | This is the human readable message of event to be added. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MessageArgs** [ ] | array (string)<br><br>*read-write required* | This is the array of message arguments of the event to be added. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MessageId** | string<br><br>*read-write required* | This is the message ID of event to be added. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OriginOfCondition** | string<br><br>*read-write required* | This is the OriginOfCondition property of event to be added. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Severity** | string<br><br>*read-write required* | This is the Severity of event to be added. |
| } |   |   |   |

### Property Details

### EventType:


This is the type of event to be added.

| string | Description |
| --- | --- |
| Alert | A condition exists which requires attention. |
| ResourceAdded | A resource has been added. |
| ResourceRemoved | A resource has been removed. |
| ResourceUpdated | The value of this resource has been updated. |
| StatusChange | The status of this resource has changed. |

### EventTypesForSubscription:


This is the types of Events that can be subscribed to.

| string | Description |
| --- | --- |
| Alert | A condition exists which requires attention. |
| ResourceAdded | A resource has been added. |
| ResourceRemoved | A resource has been removed. |
| ResourceUpdated | The value of this resource has been updated. |
| StatusChange | The status of this resource has changed. |


## HpeFwRev

|     |     |     |
| --- | --- | --- |
| **Backup** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumber** | integer<br><br>*read-only* | The build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumberString** | string<br><br>*read-only* | The string version of the build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Date** | string<br><br>*read-only* | The build date of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DebugBuild** | boolean<br><br>*read-only* | True if the firmware is a debug build; False if it is not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Family** | string<br><br>*read-only* | The family of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MajorVersion** | integer<br><br>*read-only* | The major version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinorVersion** | integer<br><br>*read-only* | The minor version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Time** | string<br><br>*read-only* | The build time of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VersionString** | string<br><br>*read-only<br>(null)* | The version string of the firmware. This value might be null if VersionString is unavailable. |
| } |   |   |
| **Bootblock** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumber** | integer<br><br>*read-only* | The build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumberString** | string<br><br>*read-only* | The string version of the build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Date** | string<br><br>*read-only* | The build date of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DebugBuild** | boolean<br><br>*read-only* | True if the firmware is a debug build; False if it is not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Family** | string<br><br>*read-only* | The family of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MajorVersion** | integer<br><br>*read-only* | The major version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinorVersion** | integer<br><br>*read-only* | The minor version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Time** | string<br><br>*read-only* | The build time of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VersionString** | string<br><br>*read-only<br>(null)* | The version string of the firmware. This value might be null if VersionString is unavailable. |
| } |   |   |
| **Current** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumber** | integer<br><br>*read-only* | The build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumberString** | string<br><br>*read-only* | The string version of the build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Date** | string<br><br>*read-only* | The build date of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DebugBuild** | boolean<br><br>*read-only* | True if the firmware is a debug build; False if it is not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Family** | string<br><br>*read-only* | The family of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MajorVersion** | integer<br><br>*read-only* | The major version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinorVersion** | integer<br><br>*read-only* | The minor version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Time** | string<br><br>*read-only* | The build time of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VersionString** | string<br><br>*read-only<br>(null)* | The version string of the firmware. This value might be null if VersionString is unavailable. |
| } |   |   |
| **Pending** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumber** | integer<br><br>*read-only* | The build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumberString** | string<br><br>*read-only* | The string version of the build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Date** | string<br><br>*read-only* | The build date of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DebugBuild** | boolean<br><br>*read-only* | True if the firmware is a debug build; False if it is not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Family** | string<br><br>*read-only* | The family of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MajorVersion** | integer<br><br>*read-only* | The major version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinorVersion** | integer<br><br>*read-only* | The minor version of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Time** | string<br><br>*read-only* | The build time of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VersionString** | string<br><br>*read-only<br>(null)* | The version string of the firmware. This value might be null if VersionString is unavailable. |
| } |   |   |

## HpeHttpsCert

This is the schema definition for HpeHttpsCert.

|     |     |     |
| --- | --- | --- |
| **CertificateSigningRequest** | string<br><br>*read-only<br>(null)* | When a GenerateCSR action is performed, this field contains the generated CSR (in Base64 format). Contains a public and private key pair. |
| **CertificateSigningRequestInformation** { | object | The Country, State, City, OrgName, OrgUnit and CommonName with which the CSR was generated. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**City** | string<br><br>*read-only* | The city or locality where the company or organization that owns this device is located. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CommonName** | string<br><br>*read-only* | The FQDN of this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Country** | string<br><br>*read-only* | The two-character country code where the company or organization that owns this device is located. Eg: US |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OrgName** | string<br><br>*read-only* | The name of the company or organization that owns this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OrgUnit** | string<br><br>*read-only* | The unit within the company or organization that owns this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only* | The state where the company or organization that owns this device is located. |
| } |   |   |
| **Id** | string<br><br>*read-write* | Uniquely identifies the resource within the collection of like resources. |
| **X509CertificateInformation** { | object | Contains the X509 Certificate Information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Issuer** | string<br><br>*read-only* | The Certificate Authority that issued the certificate. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only* | The serial number that the Certificate Authority assigned to the certificate. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Subject** | string<br><br>*read-only* | The entity to which the certificate was issued. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ValidNotAfter** | string<br><br>*read-only* | The date on which the certificate validity period ends. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ValidNotBefore** | string<br><br>*read-only* | The date on which the certificate validity period begins. |
| } |   |   |

### Actions

### GenerateCSR




**URIs**:


(This action takes no parameters.)


### GenerateSelfSignedCertificate




**URIs**:


(This action takes no parameters.)


### ImportCACertificate




**URIs**:


(This action takes no parameters.)


### ImportCertificate




**URIs**:


(This action takes no parameters.)


## HpeMemoryExt

This is the schema definition for HpeMemoryExt.

|     |     |     |
| --- | --- | --- |
| **DIMMStatus** | string<br>(enum)<br><br>*read-only<br>(null)* | Specifies memory module status and whether the module in use. *For the possible property values, see DIMMStatus in Property Details.* |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Type** | <br><br>*read-write* |  |

### Property Details

### DIMMStatus:


Specifies memory module status and whether the module in use.

| string | Description |
| --- | --- |
| AddedButUnused | DIMM is added but currently unused. |
| ConfigurationError | Configuration error in DIMM. |
| Degraded | DIMM state is degraded. |
| DoesNotMatch | DIMM type does not match. |
| ExpectedButMissing | DIMM is expected but missing. |
| GoodInUse | DIMM is functioning properly and currently in use. |
| GoodPartiallyInUse | DIMM is functioning properly but partially in use. |
| None |  |
| NotPresent | DIMM is not present. |
| NotSupported | DIMM is not supported. |
| Other | DIMM status that does not fit any of these definitions. |
| PresentSpare | DIMM is present but used as spare. |
| PresentUnused | DIMM is present but unused. |
| Unknown | The status of the DIMM is unknown. |
| UpgradedButUnused | DIMM is upgraded but currently unused. |


## HpeProcessorsExt

This is the schema definition for HpeProcessorsExt.

|     |     |     |
| --- | --- | --- |
| **CoresEnabled** | integer<br><br>*read-only<br>(null)* | The number of enabled cores in the processor. |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Type** | <br><br>*read-write* |  |

## HpeSecurityService

This is the schema definition for a HpeSecurityService.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Links** { | object | The links array contains the links to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HttpsCaCerts** { | object | The value of this property shall be a reference to a resource of Type HpeWfmHttpsCaCerts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HttpsCert** { | object | The value of this property shall be a reference to a resource of Type HpeHttpsCert. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |
| **Oem** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hpe** | <br><br>*read-write* |  |
| } |   |   |
| **Type** | <br><br>*read-write* |  |

## HpeWfmAccountExt

This is the schema definition for HpeWfmAccountExt.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **DisplayName** | string<br><br>*read-write* | Descriptive display name that helps to easily identify the owner of each user name. The display name does not have to be the same as the user name and must use printable characters. The maximum length for a display name is 127 characters. |
| **Enabled** | boolean<br><br>*read-write* | Indicates whether the user account is enabled or not. |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Privilege** | string<br>(enum)<br><br>*read-write* | This privilege enables a user to log in to management processor. All local accounts have the login privilege. This privilege is added automatically if it is not specified. *For the possible property values, see Privilege in Property Details.* |

### Property Details

### Privilege:


This privilege enables a user to log in to management processor. All local accounts have the login privilege. This privilege is added automatically if it is not specified.

| string | Description |
| --- | --- |
| Device | Allows configuring and performing actions on devices includes login privilege |
| Login | Read operations allowed like viewing discovered nodes and groups and generate reports |
| Manager | All operations allowed |
| Security |  |
| User | Allows configuring users with device privilege |


## HpeWfmAccountServiceExt

This is the schema definition for HpeWfmAccountServiceExt.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **MinPasswordLength** | number<br><br>*read-write* | The minimum password length for this service. |

## HpeWfmActivityLogs

This is the schema definition for a HpeWfmActivityLogs.

|     |     |     |
| --- | --- | --- |
| **ActivityLogsLocation** [ ] | array (string)<br><br>*read-only* | List of the activity log files.  |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |

### Actions

### ClearLog




**URIs**:


(This action takes no parameters.)


## HpeWfmAddOnServices

This is the schema definition for HpeWfmAddOnServices.

|     |     |     |
| --- | --- | --- |
| **AddOnServiceId** | string<br><br>*read-write* | Describes the ID of the add-on service available in iLO Amplifier. |
| **AddOnServiceVersion** | string<br><br>*read-only* | This property contains the add-on service version as defined by the developer for the associated service. |
| **Description** | string<br><br>*read-only* | Brief description about the add-on service available in iLO Amplifier |
| **Id** | <br><br>*read-write* |  |
| **Name** | string<br><br>*read-only* | Describes the name of the add-on service available in iLO Amplifier. |
| **Oem** | <br><br>*read-write* |  |
| **PackageName** | string<br><br>*read-only* | Describes the package name of the add-on service available in iLO Amplifier. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

## HpeWfmAddOnServicesManager

This is the schema definition for HpeWfmAddOnServicesManager.

|     |     |     |
| --- | --- | --- |
| **AddOnServiceAvailableVersion** | string<br><br>*read-only* | Describes the new version of the add-on service available in iLO Amplifier. |
| **AddOnServiceId** | string<br><br>*read-only* | Describes the ID of the add-on service available in iLO Amplifier. |
| **AddOnServiceVersion** | string<br><br>*read-only* | Describes the installed version of the add-on service in iLO Amplifier. |
| **BinaryPath** | string<br><br>*read-only* | The path where the binary to be used for the installation of the add-on service is available in iLO Amplifier. |
| **Description** | string<br><br>*read-only* | Brief description about the add-on service available in iLO Amplifier |
| **Id** | <br><br>*read-write* |  |
| **InstallationStatus** | string<br>(enum)<br><br>*read-only* | Describes the current installation status of the add-on service. *For the possible property values, see InstallationStatus in Property Details.* |
| **MenuHtmlRef** | string<br><br>*read-only* | Describes the menu html reference and js file of the add-on service installed in iLO Amplifier |
| **MenuName** | string<br><br>*read-only* | Describes the menu name of the add-on service installed in iLO Amplifier |
| **Name** | string<br><br>*read-only* | Describes the name of the add-on service available in iLO Amplifier. |
| **Oem** | <br><br>*read-write* |  |
| **PackageName** | string<br><br>*read-only* | Describes the package name of the add-on service available in iLO Amplifier. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

### Actions

### Reset


The reset action to reset the specified add-on service.

**URIs**:


(This action takes no parameters.)


### Start


The start action to start the specified add-on service.

**URIs**:


(This action takes no parameters.)


### Stop


The stop action to start the specified add-on service.

**URIs**:


(This action takes no parameters.)


### Property Details

### InstallationStatus:


Describes the current installation status of the add-on service.

| string |
| --- |
| Installed | 
| NotInstalled | 


## HpeWfmAggregatorService

This is the schema definition for HpeWfmAggregatorService.

|     |     |     |
| --- | --- | --- |
| **ActionStatus** { | object | The detailed and collated status of the action performed |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DiscoverServersFromCSV** { | object | The detailed and collated status of discovering multiple servers added through csv file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DiscoveryStatus** | string<br>(enum)<br><br>*read-only* | The status of the discovery process. *For the possible property values, see DiscoveryStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProgressPercent** | integer<br><br>*read-only* | The progress percent of the discovery process. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DiscoverServersInRange** { | object | The detailed and collated status of discovering multiple servers |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DiscoveryStatus** | string<br>(enum)<br><br>*read-only* | The status of the discovery process. *For the possible property values, see DiscoveryStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EndAddress** | string<br><br>*read-only* | The ending address at which the discovery process stops. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProgressPercent** | integer<br><br>*read-only* | The progress percent of the discovery process. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StartAddress** | string<br><br>*read-only* | The starting address at which the discovery process begins. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RefreshAll** { | object | The detailed and collated status of refreshing multiple servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsUserInitiated** | boolean<br><br>*read-only* | The flag indicates whether the refresh is initiated by user. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProgressPercent** | integer<br><br>*read-only* | The progress percent of the Refresh process. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RefreshStatus** | string<br>(enum)<br><br>*read-only* | The status of the refresh process. *For the possible property values, see RefreshStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **AggregatedHealth** { | object | The aggregated health of all systems managed by this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Critical** | integer<br><br>*read-only* | The number of systems with Critical health status that are managed by this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OK** | integer<br><br>*read-only* | The number of systems with OK health status that are managed by this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Unknown** | integer<br><br>*read-only* | The number of systems with Unknown health status that are managed by this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning** | integer<br><br>*read-only* | The number of systems with Warning health status that are managed by this device. |
| } |   |   |
| **AllowAlertBasedRefresh** | boolean<br><br>*read-write* | If enabled, servers will be refreshed on alerts on the managed Nodes. |
| **AutoRefreshMode** | boolean<br><br>*read-write* | If enabled, servers will be refreshed automatically in intervals based on the total number of managed Nodes. |
| **ContinousDiscovery** | boolean<br><br>*read-write* | If enabled, the information of nodes and groups are refreshed at a regular interval. The regular interval is specified by RefreshInterval. |
| **Description** | <br><br>*read-write* |  |
| **FederationGroups** { | object | This property references a resource of type Collection with a MemberType of Federation groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **Id** | <br><br>*read-write required* |  |
| **Links** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Dashboard** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Alerts** { | object | The value of this property shall be a reference to a resource of Type Alerts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Assets** { | object | The value of this property shall be a reference to a resource of Type Assets. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Compliance** { | object | The value of this property shall be a reference to a resource of Type Compliance. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServerGroups** { | object | The value of this property shall be a reference to a resource of Type Server Groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LicenseInfo** { | object | The value of this property shall be a reference to a resource of Type LicenseInfo. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LogServices** { | object | The value of this property shall be resource of type LogServices. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedGroups** { | object | The value of this property shall be a reference to a resource of Type ManagedGroups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedServerGroups** { | object | The value of this property shall be a reference to a resource of Type ManagedServerGroups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedSystems** { | object | The value of this property shall be a reference to a resource of Type ManagedSystems. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedSystemsSummary** { | object | The value of this property shall be a reference to a resource of Type ManagedSystemsSummary. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Reports** { | object | The value of this property shall be a reference to a resource of Type Reports. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | <br><br>*read-write required* |  |
| **RefreshIntervalInHours** | integer<br>(enum)<br><br>*read-write* | The time interval in minutes when refresh of information of nodes and groups are initiated again. *For the possible property values, see RefreshIntervalInHours in Property Details.* |
| **ServerGroups** { | object | This property references a resource of type Collection with a MemberType of Server groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **Systems** { | object | This property references a resource of type Collection with a MemberType of Systems. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **SystemsCount** | integer<br><br>*read-only* | The number of systems managed by Central Management Device. |

### Actions

### DiscoverServersFromCSV




**URIs**:


(This action takes no parameters.)


### DiscoverServersInRange




**URIs**:


(This action takes no parameters.)


### RefreshAll




**URIs**:


(This action takes no parameters.)


### Property Details

### DiscoveryStatus:


The status of the discovery process.

| string | Description |
| --- | --- |
| Failed | Discovery process is completed and is failed |
| InProgress | Discovery process is in progress |
| NotInitiated | Discovery process is not initiated |
| PartiallySuccessful | Discovery process is partially successful and completed |
| Queued | Discovery process is queued |
| Successful | Discovery process is successfully completed |

### RefreshIntervalInHours:


The time interval in minutes when refresh of information of nodes and groups are initiated again.

| integer |
| --- |
| 6 | 
| 8 | 
| 12 | 
| 24 | 

### RefreshStatus:


The status of the refresh process.

| string | Description |
| --- | --- |
| Failed | Refresh process is completed and is failed |
| InProgress | Refresh process is in progress |
| NotInitiated | Refresh process is not initiated |
| Successful | Refresh process is successfully completed |


## HpeWfmAlertService

This is the schema definition for a HpeWfmAlertService.

|     |     |     |
| --- | --- | --- |
| **AlertMail** { | object | AlertMail options. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Authentication** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EmailAddress** | string<br><br>*read-write* | The Email Address to which Mail Alerts are sent. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enabled** | boolean<br><br>*read-write* | Specifies whether Alert Mail is enabled or not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MailServer** { | object | Specifies the configurations for Mail Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DomainName** | string<br><br>*read-write* | Specifies the DomainName of the Mail Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HostName** | string<br><br>*read-write* | Specifies the HostName of the Mail Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | integer<br><br>*read-write* | Specifies the port number to be used for Mail Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecureMailServerEnabled** | boolean<br><br>*read-write* | Indicates whether to use secure alert mail server relay. When enabled, alert mail server is connected using secure protocol |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NotificationCategory** { | object | The properties of the object specify the category of alerts for which the mails will be sent when AlertMail is Enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Administration** | boolean<br><br>*read-write* | All alerts related to Administration are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**All** | boolean<br><br>*read-write* | All alerts are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GeneralFailure** | boolean<br><br>*read-write* | All alerts related to General Failure are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HardwareFailure** | boolean<br><br>*read-write* | All alerts related to Hardware Failure are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Maintenance** | boolean<br><br>*read-write* | All alerts related to Maintenance are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Other** | boolean<br><br>*read-write* | All other alerts are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Security** | boolean<br><br>*read-write* | All alerts related to Security are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Storage** | boolean<br><br>*read-write* | All alerts related to Storage are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NotificationSeverity** { | object | The properties of the object specify the severity of alerts for which the mails will be sent when AlertMail is Enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Critical** | boolean<br><br>*read-write* | All alerts with severity Critical are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Info** | boolean<br><br>*read-write* | All alerts with severity Info are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning** | boolean<br><br>*read-write* | All alerts with severity Warning are sent to the configured Mail address if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **IFTTT** { | object | IFTTT options. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enabled** | boolean<br><br>*read-write* | Specifies whether IFTTT is enabled or not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Key** | string<br><br>*read-write* | IFTTT Key. |
| } |   |   |
| **Links** { | object | The URIs for the resources related to the alert mail service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AlertLogs** { | object | The URI for alert logs resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |
| **SensorThreshold** { | object | Specifies the threshold configuration of several hardware sensors. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AltitudeSensor** { | object | Specifies the threshold configuration of altitude sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsAlertEnabled** | boolean<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxThreshold** | integer<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinThreshold** | integer<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UserConfig** | string<br>(enum)<br><br>*read-write* |  *For the possible property values, see UserConfig in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HumiditySensor** { | object | Specifies the threshold configuration of humidity sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsAlertEnabled** | boolean<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxThreshold** | integer<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinThreshold** | integer<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UserConfig** | string<br>(enum)<br><br>*read-write* |  *For the possible property values, see UserConfig in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TempratureSensor** { | object | Specifies the threshold configuration of temprature sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsAlertEnabled** | boolean<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxThreshold** | integer<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinThreshold** | integer<br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UserConfig** | string<br>(enum)<br><br>*read-write* |  *For the possible property values, see UserConfig in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **WolframAlertsEnabled** | boolean<br><br>*read-write* | Specifies whether Wolfram Alerts are enabled or not. |

### Actions

### SendTestAlertMail


Send a test Alert mail to the configured mail address.

**URIs**:


(This action takes no parameters.)


### Property Details

### UserConfig:

| string | Description |
| --- | --- |
| Celsius | It specifies that measuring unit of temperature is Celsius. |
| Fahrenheit | It specifies that measuring unit of temperature is Fahrenheit. |
| None | It specifies that no measuring unit has been configured for temperature. |


## HpeWfmBaseline

This is the schema definition for HpeWfmBaseline.

|     |     |     |
| --- | --- | --- |
| **BaselineState** | string<br>(enum)<br><br>*read-only* | This property indicates the state of inventory for this resource. *For the possible property values, see BaselineState in Property Details.* |
| **Components** { | object | The URI refers to collection of components in the baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **RelatedTask** { | object | The URI refers to the task which is created to import this baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **SizeInMB** | integer<br><br>*read-only* | Space on disk (in MB) used by this baseline. |
| **Version** | string<br><br>*read-only* | The version of the Baseline. |

### Property Details

### BaselineState:


This property indicates the state of inventory for this resource.

| string | Description |
| --- | --- |
| ImportFailed | Import of the baseline failed. |
| ImportInProgress | Import of the baseline is in progress. |
| ImportSuccess | Import of the baseline was completed successfully. |


## HpeWfmBaselineComponents

This is the schema definition for a HpeWfmBaselineComponents.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Recommendation** | string<br>(enum)<br><br>*read-only* | This property indicates the upgrade recommendataion for the component. *For the possible property values, see Recommendation in Property Details.* |
| **Version** | string<br><br>*read-only* | The version of this component. |

### Property Details

### Recommendation:


This property indicates the upgrade recommendation for the component.

| string | Description |
| --- | --- |
| Critical | HPE requires users update to this version immediately. |
| Optional | Users should update to this version if their system is affected by one of the documented fixes or if there is a desire to utilize any of the enhanced functionality provided by this version. |
| Recommended | HPE recommends users update to this version at their earliest convenience. |
| Unknown | Unknown recommendation |


## HpeWfmBaselineService

This is the schema definition for HpeWfmBaselineService.

|     |     |     |
| --- | --- | --- |
| **Baselines** { | object | This property references a collection resource of imported baselines. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **DateTime** | string<br><br>*read-only<br>(null)* | The current DateTime (with offset) setting that the task service is using. |
| **Description** | <br><br>*read-write* |  |
| **FreeSpaceInMB** | integer<br><br>*read-only* | Free space of disk (in MB) remaining for importing baselines . |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Oem** | <br><br>*read-write* | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. |
| **ServiceEnabled** | boolean<br><br>*read-only<br>(null)* | This indicates whether this service is enabled. |
| **Status** | <br><br>*read-write* |  |
| **TotalSpaceInMB** | integer<br><br>*read-only* | Total space of disk (in MB) allocated for importing baselines. |

## HpeWfmComputerSystem

This is the schema definition for HpeWfmComputerSystem.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Links** { | object | The URIs for the resources related to the date time service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareInventory** { | object | The URI for for Firmware Inventory of Computer System. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SoftwareInventory** { | object | The URI for Software Inventory of Computer System. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |

## HpeWfmDashboardAlerts

|     |     |     |
| --- | --- | --- |
| **AlertsInfo** { | object | This indicates the count of various categories of alerts received from managed systems. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Critical** | integer<br><br>*read-only<br>(null)* | Count of Critical alerts received from managed systems. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OK** | integer<br><br>*read-only<br>(null)* | Count of Info alerts received from managed systems. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Security** | integer<br><br>*read-only<br>(null)* | Count of Security alerts received from managed systems. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning** | integer<br><br>*read-only<br>(null)* | Count of Warning alerts received from managed systems. |
| } |   |   |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Monitoring** { | object | Indicates information about servers being monitored by iLO Amplifier Pack. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MonitoredCount** | integer<br><br>*read-only<br>(null)* | Count of servers being monitored by iLO Amplifier Pack. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalServersCount** | integer<br><br>*read-only<br>(null)* | Total Count of managed servers. |
| } |   |   |
| **Name** | <br><br>*read-write* |  |

## HpeWfmDashboardAssets

|     |     |     |
| --- | --- | --- |
| **AggregatedHealth** { | object | This indicates the aggregated health status of all the servers managed by iLO Amplifier Pack. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Critical** | integer<br><br>*read-only<br>(null)* | Count of all the servers whose health status is Critical. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OK** | integer<br><br>*read-only<br>(null)* | Count of all the servers whose health status is Ok. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Security** | integer<br><br>*read-only<br>(null)* | Count of all the security related events/alerts recieved from managed servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning** | integer<br><br>*read-only<br>(null)* | Count of all the servers whose health status is Warning. |
| } |   |   |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **ServerGenerations** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | This indicates the total count of servers of a server generation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | This indicates the server generation's name. |
| } ] |   |   |
| **ServerModels** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | This indicates the total count of servers of a server model. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | This indicates the server model's name. |
| } ] |   |   |
| **ServerPlatforms** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | This indicates the total count of servers of a server platform. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | This indicates the name of a server platform. |
| } ] |   |   |

## HpeWfmDashboardCompliance

|     |     |     |
| --- | --- | --- |
| **BaselineComplianceTasks** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineId** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineName** | string<br><br>*read-only<br>(null)* | Indicates the name of this firmware baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineVersion** | string<br><br>*read-only<br>(null)* | Indicates the version of this firmware baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CompliantCount** | integer<br><br>*read-only<br>(null)* | Indicates the number of servers compliant to this firmware baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NotCompliantCount** | integer<br><br>*read-only<br>(null)* | Count of servers not compliant to this firmware baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TaskId** | <br><br>*read-write* |  |
| } ] |   |   |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **NotRunCount** | integer<br><br>*read-only<br>(null)* | Count of servers for which compliance has never been run for any imported firmware baseline. |
| **TotalServersCount** | integer<br><br>*read-only<br>(null)* | Total number of servers managed by this iLO Amp. |

## HpeWfmDashboardServerGroups

|     |     |     |
| --- | --- | --- |
| **ActionStatus** { | object | The detailed and collated status of action performed |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServerGroupsHealthStatus** { | object | The status of task initiated for fetching details of health status of various servers in all server groups managed by iLO Amplifier. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthActionStatus** | string<br>(enum)<br><br>*read-only* | The status of the getting process. *For the possible property values, see HealthActionStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProgressPercent** | integer<br><br>*read-only* | The progress percent of the HealthStatus process. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **ServerGroupsInfo** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Critical** | integer<br><br>*read-only<br>(null)* | Count of all the servers whose health status is Critical. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Indicates the server group name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OK** | integer<br><br>*read-only<br>(null)* | Count of all the servers whose health status is Ok. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Unknown** | integer<br><br>*read-only<br>(null)* | Count of all the servers whose health status is Unknown. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning** | integer<br><br>*read-only<br>(null)* | Count of all the servers whose health status is Warning. |
| } ] |   |   |

### Actions

### ServerGroupsHealthStatus




**URIs**:


(This action takes no parameters.)


### Property Details

### HealthActionStatus:


The status of the process.

| string | Description |
| --- | --- |
| Failed | HealthStatus process is completed and is failed |
| InProgress | HealthStatus process is in progress |
| NotInitiated | HealthStatus process is not initiated |
| PartiallySuccessful | HealthStatus process is partially successful and completed |
| Queued | HealthStatus process is queued |
| Successful | HealthStatus process is successfully completed |


## HpeWfmDateTime

This is the schema definition for HpeWfmDateTime.

|     |     |     |
| --- | --- | --- |
| **ConfigurationSettings** | string<br>(enum)<br><br>*read-only* | The state of the currently displayed configuration settings. *For the possible property values, see ConfigurationSettings in Property Details.* |
| **DateTime** | string<br><br>*read-only* | The date and time used by management processor. |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Modified** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **NTPServers** [ ] | array (string)<br><br>*read-only* | The NTP servers, in order of preference. |
| **StaticNTPServers** [ ] | array (string)<br><br>*read-write* | The static NTP servers, in order of preference. |
| **StaticNTPServersEnabled** | boolean<br><br>*read-write* | Specifies whether manually specified NTP servers are enabled or not. |
| **TimeZone** { | object | The currently selected time zone. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Index** | number<br><br>*read-write* | The index of the current time zone. To set a new time zone, specify a different time zone index. This property can be set only when DHCPv4 or DHCPv6 supplied time settings are disabled. Since the time zone list might vary from one firmware version to another (which often leads to differences in time zone indices), setting the time zone by name is recommended over setting by index, for better compatibility. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only* | The name of the current time zone. Patch this field to set the time zone by name - recommended over patching the index. When this field is specified in the patch, the Index field, if specified, will be ignored. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UtcOffset** | string<br><br>*read-only* | The UTC offset of the current time zone, in the format {+/-}hh:mm |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Value** | string<br><br>*read-only* | The environment variable value. |
| } |   |   |
| **TimeZoneList** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Index** | number<br><br>*read-only* | The time zone index. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only* | The time zone name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UtcOffset** | string<br><br>*read-only* | The UTC offset of the time zone, in the format {+/-}hh:mm |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Value** | string<br><br>*read-only* | The environment variable value. |
| } ] |   |   |

### Property Details

### ConfigurationSettings:


The state of the currently displayed configuration settings.

| string |
| --- |
| Current | 
| SomePendingReset | 


## HpeWfmDirectory

This is the schema definition for HpeWfmDirectory.

|     |     |     |
| --- | --- | --- |
| **BaseDN** | string<br><br>*read-write* | The group identifier in LDAP Server. |
| **DirectoryAddress** | string<br><br>*read-write* | The IP Address of the LDAP Server. |
| **DirectoryEnabled** | boolean<br><br>*read-write* | LDAP login status |
| **DirectoryName** | string<br><br>*read-write* | The name of the LDAP Server. |
| **DirectoryPort** | integer<br><br>*read-write* | The port number of LDAP Server. |
| **DirectorySecureConnection** | boolean<br><br>*read-write* | LDAP secure connection |
| **DirectoryType** | string<br><br>*read-write* | The type of the LDAP Server. |
| **DirectoryVersion** | integer<br><br>*read-write* | The version number of the LDAP server. |
| **Id** | <br><br>*read-write* |  |
| **Links** { | object | The links array contains the related resource URIs. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Groups** [ { | array | The groups URI associated with this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |
| **OrganizationalUnit** | string<br><br>*read-write* | The organizational unit which the LDAP Server is part of. |
| **UserNamingAttribute** | string<br><br>*read-write* | The user naming attribute of the LDAP Server. |

## HpeWfmDirectoryAccessService

This is the schema definition for a HpeWfmDirectoryAccessService.

|     |     |     |
| --- | --- | --- |
| **Directories** { | object | This property references a resource of type Collection with a MemberType of directories. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **ServiceEnabled** | boolean<br><br>*read-write* | This indicates whether this service is enabled. |

## HpeWfmDirectoryGroup

This is the schema definition for a HpeWfmDirectoryGroup.

|     |     |     |
| --- | --- | --- |
| **GroupEnabled** | boolean<br><br>*read-write* | This indicates whether this group is enabled. |
| **GroupName** | string<br><br>*read-write* | The name of the group in the LDAP Server. |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **privilege** | string<br><br>*read-write* | The type of privilege this group is entitled to. |

## HpeWfmEthernetNetworkInterface

This is the schema definition for a HpeWfmEthernetNetworkInterface.

|     |     |     |
| --- | --- | --- |
| **ConfigurationSettings** | string<br>(enum)<br><br>*read-only* | The state of the currently displayed configuration settings. *For the possible property values, see ConfigurationSettings in Property Details.* |
| **Description** | <br><br>*read-write* |  |
| **DHCPv4** { | object | DHCPv4 options. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enabled** | boolean<br><br>*read-write* | Determines whether DHCPv4 is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDNSServers** | boolean<br><br>*read-write* | Determines whether to use DHCPv4-supplied DNS servers. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDomainName** | boolean<br><br>*read-write* | Determines whether to use a DHCPv4-supplied domain name. Can only be enabled when DHCPv4 is also enabled; otherwis,e this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseGateway** | boolean<br><br>*read-write* | Determines whether to use a DHCPv4-supplied gateway. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseNTPServers** | boolean<br><br>*read-write* | Determines whether to use DHCPv4-supplied NTP servers. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseStaticRoutes** | boolean<br><br>*read-write* | Determines whether to use DHCPv4-supplied static routes. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseWINSServers** | boolean<br><br>*read-write* | Determines whether to use DHCPv4-supplied WINS servers. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only. |
| } |   |   |
| **DHCPv6** { | object | DHCPv6 options. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enabled** | boolean<br><br>*read-write* | Determines whether DHCPv6 is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDNSServers** | boolean<br><br>*read-write* | Determines whether to use DHCPv6-supplied DNS servers. Can only be enabled when DHCPv6 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseDomainName** | boolean<br><br>*read-write* | Determines whether to use a DHCPv6-supplied domain name. Can only be enabled when DHCPv6 is also enabled; otherwis,e this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseGateway** | boolean<br><br>*read-write* | Determines whether to use a DHCPv6-supplied gateway. Can only be enabled when DHCPv6 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseNTPServers** | boolean<br><br>*read-write* | Determines whether to use DHCPv6-supplied NTP servers. Can only be enabled when DHCPv6 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseStaticRoutes** | boolean<br><br>*read-write* | Determines whether to use DHCPv6-supplied static routes. Can only be enabled when DHCPv6 is also enabled; otherwise, this property will be set to false and will be read-only. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UseWINSServers** | boolean<br><br>*read-write* | Determines whether to use DHCPv6-supplied WINS servers. Can only be enabled when DHCPv6 is also enabled; otherwise, this property will be set to false and will be read-only. |
| } |   |   |
| **DomainName** | string<br><br>*read-write* | Domain name of the network to which this management processor belongs. This property can only be modified when the management processor is not configured to use a DHCP supplied domain name; otherwise this property is read-only indicating the value is provided by DHCP. |
| **HostName** | string<br><br>*read-write* | The management processor host name. |
| **Id** | <br><br>*read-write* |  |
| **IPv4** { | object | The Management Processor IPv4 Configuration Settings. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentStaticRoutes** [ { | array | The current configured IPv4 static routes. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Destination** | string<br><br>*read-only* | An IPv4 static route destination. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Gateway** | string<br><br>*read-only* | An IPv4 static route gateway. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SubnetMask** | string<br><br>*read-only* | An IPv4 static route subnet mask. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DDNSRegistration** | boolean<br><br>*read-write* | Determines whether DDNS registration is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DNSSearch** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AvailableSettings** | string<br><br>*read-only* | Currently configured IPv4 DNS Domain servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentSettings** | string<br><br>*read-write* | Currently configured IPv4 DNS Domain servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DNSServers** [ ] | array (string)<br><br>*read-write* | Currently configured IPv4 DNS servers in order of descending preference. Static values when not configured to use DHCPv4-supplied DNS servers; otherwise this property is read-only indicating the values are provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv4Addresses** [ { | array | The IPv4 connection characteristics for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Address** | string<br><br>*read-write<br>(null)* | The IPv4 Address. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Gateway** | string<br><br>*read-write<br>(null)* | The IPv4 gateway for this address. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SubnetMask** | string<br><br>*read-write<br>(null)* | The IPv4 Subnet mask. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StaticRoutes** [ { | array | The current configured IPv4 static routes. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Destination** | string<br><br>*read-write* | An IPv4 static route destination. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Gateway** | string<br><br>*read-write* | An IPv4 static route gateway. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SubnetMask** | string<br><br>*read-write* | An IPv4 static route subnet mask. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WINSRegistration** | boolean<br><br>*read-write* | Determines whether WINS registration is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WINSServers** [ ] | array (string)<br><br>*read-write* | Currently configured WINS servers in order of descending preference. Static values when not configured to use DHCPv4-supplied WINS servers; otherwise this property is read-only indicating the values are provided by DHCPv4 |
| } |   |   |
| **IPv6** { | object | The Management Processor IPv6 Configuration Settings. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentStaticRoutes** [ { | array | The current configured IPv6 static routes. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Destination** | string<br><br>*read-only* | An IPv6 static route destination. Only writeable when use of DHCPv6-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv6. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Gateway** | string<br><br>*read-only* | An IPv6 static route gateway. Only writeable when use of DHCPv6-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv6. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrefixLength** | integer<br><br>*read-only* | Prefix Length |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DNSSearch** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AvailableSettings** | string<br><br>*read-only* | Currently configured IPv6 DNS Domain servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentSettings** | string<br><br>*read-write* | Currently configured IPv6 DNS Domain servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DNSServers** [ ] | array (string)<br><br>*read-write* | Currently configured IPv6 DNS servers in order of descending preference. Static values when not configured to use DHCPv4-supplied DNS servers; otherwise this property is read-only indicating the values are provided by DHCPv4. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv6Addresses** [ { | array | The IPv6 connection characteristics for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Address** | string<br><br>*read-write<br>(null)* | The IPv6 Address. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Gateway** | string<br><br>*read-write<br>(null)* | The IPv6 gateway for this address. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrefixLength** | integer<br><br>*read-write<br>(null)* | Prefix Length |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StaticRoutes** [ { | array | The current configured IPv6 static routes. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Destination** | string<br><br>*read-write<br>(null)* | An IPv6 static route destination. Only writeable when use of DHCPv6-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv6. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Gateway** | string<br><br>*read-write<br>(null)* | An IPv6 static route gateway. Only writeable when use of DHCPv6-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv6. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrefixLength** | integer<br><br>*read-write<br>(null)* | Prefix Length |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **Links** { | object | The URIs for the resources related to the date time service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DateTimeService** { | object | The URI for this date time service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |
| **NICEnabled** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AvailableSettings** | boolean<br><br>*read-only* | Determines whether this NIC is enabled or disabled. Enabling one NIC will disable the others. If no NIC is enabled, this management processor is not accessible over the network. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentSettings** | boolean<br><br>*read-write* | Determines whether this NIC is enabled or disabled. Enabling one NIC will disable the others. If no NIC is enabled, this management processor is not accessible over the network. |
| } |   |   |
| **PreferredMode** | string<br>(enum)<br><br>*read-write<br>(null)* | Determines which is the IP Address for receiving Alerts. *For the possible property values, see PreferredMode in Property Details.* |
| **PreferredNIC** | string<br>(enum)<br><br>*read-write<br>(null)* | Determines which NIC is the preferred NIC for receiving Alerts. *For the possible property values, see PreferredNIC in Property Details.* |

### Property Details

### ConfigurationSettings:


The state of the currently displayed configuration settings.

| string | Description |
| --- | --- |
| Current | All configuration settings for this NIC are currently in use. |
| SomePendingReset | One or more configuration settings on this NIC are not yet in use.  They require a reset of this management processor in order to take effect. |

### PreferredMode:


Determines which IP Address is used for receiving Alerts.

| string | Description |
| --- | --- |
| IPv4 | IPv4 Address will be used |
| IPv6 | IPv6 Address will be used |

### PreferredNIC:


Determines which NIC is the preferred NIC for receiving Alerts.

| string | Description |
| --- | --- |
| NIC1 | NIC1 is the preferred NIC |
| NIC2 | NIC2 is the preferred NIC |


## HpeWfmEventDestinationExt

This is the schema definition for HpeWfmEventDestinationExt.

|     |     |     |
| --- | --- | --- |
| **DeliveryRetryAttempts** | integer<br><br>*read-write* | Specifies number of delivery retry attempts that will be made while forwarding events. |
| **DeliveryRetryIntervalSeconds** | integer<br><br>*read-write* | Specifies number of seconds after which a retry will be made for forwarding the events. |
| **EnableActivityAlerts** | boolean<br><br>*read-write* | Flag to be enabled to allow forwarding of iLO Amplifier Alerts to the subscriber. By default, it is set to false. |
| **NotificationCategory** { | object | The properties of the object specify the category of alerts for which the events will be sent. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Administration** | boolean<br><br>*read-write* | All alerts related to Administration are sent to the configured subscription destination if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GeneralFailure** | boolean<br><br>*read-write* | All alerts related to General Failure are sent to the configured subscription destination if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HardwareFailure** | boolean<br><br>*read-write* | All alerts related to Hardware Failure are sent to the configured subscription destination if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Maintenance** | boolean<br><br>*read-write* | All alerts related to Maintenance are sent to the configured subscription destination if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Other** | boolean<br><br>*read-write* | All other alerts are sent to the configured subscription destination if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Security** | boolean<br><br>*read-write* | All alerts related to Security are sent to the configured subscription destination if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Storage** | boolean<br><br>*read-write* | All alerts related to Storage are sent to the configured subscription destination if it is set to true. |
| } |   |   |
| **NotificationSeverity** { | object | The properties of the object specify the severity of alerts for which the events will be sent. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Critical** | boolean<br><br>*read-write* | All alerts with severity Critical are sent to the configured subscription destination, if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Info** | boolean<br><br>*read-write* | All alerts with severity Info are sent to the configured subscription destination, if it is set to true. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning** | boolean<br><br>*read-write* | All alerts with severity Warning are sent to the configured subscription destination, if it is set to true. |
| } |   |   |

## HpeWfmFederationGroup

This is the schema definition for HpeWfmFederationGroup.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Systems** { | object | This property references a resource of type Collection with a MemberType of Systems in the federation groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |

## HpeWfmFederationGroupJobResults

This is the schema definition for HpeWfmFederationGroupJobResults.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **FederationGroupJobInfo** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**JobStatus** | string<br><br>*read-only* | Progress message associated with the job. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerAddress** | string<br><br>*read-only* | The Manager address of the Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StatusMessage** | string<br><br>*read-only* | Progress message associated with the job. |
| } ] |   |   |
| **Name** | <br><br>*read-write* |  |

## HpeWfmHttpsCert

This is the schema definition for HpeWfmHttpsCert.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **X509CACertificateInformation** { | object | Contains the X509 Certificate Information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Issuer** | string<br><br>*read-only* | The Certificate Authority that issued the certificate. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only* | The serial number that the Certificate Authority assigned to the certificate. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Subject** | string<br><br>*read-only* | The entity to which the certificate was issued. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ValidNotAfter** | string<br><br>*read-only* | The date on which the certificate validity period ends. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ValidNotBefore** | string<br><br>*read-only* | The date on which the certificate validity period begins. |
| } |   |   |

## HpeWfmInfosightAggregation

This is the schema definition for HpeWfmInfosightAggregation.

|     |     |     |
| --- | --- | --- |
| **AHSDownloadErrorCount** | integer<br><br>*read-only* | This is the number of errors that happened during AHS Downloads for all servers in the current cycle(24 hours). |
| **AHSScheduleStartTime** | integer<br><br>*read-write* | This is the AHS Schedule Start time in seconds. |
| **AHSUploadErrorCount** | integer<br><br>*read-only* | This is the number of errors that happened during AHS Uploads for all servers in the current cycle(24 hours). |
| **ApplianceSerialNumber** | string<br><br>*read-only<br>(null)* | This is the unqiue iLO Amplifier Serial Number. |
| **AverageAHSFileSize** | integer<br><br>*read-only* | The average file size in KB of an AHS file in the current cyle for all servers (in a day). |
| **ClaimId** | string<br><br>*read-only<br>(null)* | Claim Id from the claim token |
| **ClaimToken** | string<br><br>*read-write<br>(null)* | Claim token associated with the user |
| **ClaimTokenValidationStatus** | string<br>(enum)<br><br>*read-only* | This property shows the current status of the connection to HPE Infosight from this device. *For the possible property values, see ClaimTokenValidationStatus in Property Details.* |
| **CompletedAHSDownloadCount** | integer<br><br>*read-only* | This is the number of AHS downloads completed in the current cycle (a day). |
| **CompletedAHSUploadCount** | integer<br><br>*read-only* | This is the number of AHS Uploads completed in the current cycle (a day). |
| **CompletedHeartBeatUploadCount** | integer<br><br>*read-only* | This is the number of HeartBeat Uploads completed in the current cycle(10 mins). |
| **ConcurrentAHSDownloadCount** | integer<br><br>*read-only* | This is the number of AHS Downloads happening concurrently. |
| **ConcurrentAHSUploadCount** | integer<br><br>*read-only* | This is the number of AHS Uploads happening concurrently. |
| **ConnectionStatus** | string<br>(enum)<br><br>*read-only* | This property shows the current status of the connection to HPE Infosight from this device. *For the possible property values, see ConnectionStatus in Property Details.* |
| **ConnectionStatusErrorDetails** | string<br><br>*read-only<br>(null)* | Detailed error string in case of connection failure |
| **DatacenterLocation** | string<br><br>*read-write<br>(null)* | Location of the Datacenter |
| **Description** | <br><br>*read-write* |  |
| **HeartBeatUploadErrorCount** | integer<br><br>*read-only* | This is the number of errors that happened during HeartBeat Uploads for all servers in the current cycle (10mins). |
| **Id** | <br><br>*read-write* |  |
| **MaxAHSFileSize** | integer<br><br>*read-only* | The largest file size in KB of an AHS file in the current cycle for all servers (in a day). |
| **Name** | <br><br>*read-write* |  |
| **NewAHSCycleStartTime** | string<br><br>*read-only<br>(null)* | Time at which the AHS download and upload was started for all servers. |
| **PreviousHeartBeatCycleCompleteTime** | string<br><br>*read-only<br>(null)* | Time at which the HeartBeat upload was completed for all the servers in the previous cycle. |
| **ServerPIIDataEnabled** | boolean<br><br>*read-write* | Indicates if sending the Server Identifiable Information like IP address and Hostname in the heartbeat is enabled. |
| **ServiceEnabled** | boolean<br><br>*read-write* | Indicates if HPE InfoSight Integration is enabled. |
| **TenantName** | string<br><br>*read-only<br>(null)* | Tenant Name from the claim token |

### Property Details

### ClaimTokenValidationStatus:


This property shows the current status of the connection to HPE InfoSight from this device.

| string | Description |
| --- | --- |
| ConnectionFailed | Connection to HPE InfoSight failed. |
| NotInitiated | Validation of claim token was  not initiated. |
| TokenExpired | The claim token has expired. |
| ValidationFailed | The claim token entered is not a valid claim token. |
| ValidationInProgress | Validation of the entered claim token is being attempted. |
| ValidationSuccess |  |

### ConnectionStatus:


This property shows the current status of the connection to HPE InfoSight from this device.

| string | Description |
| --- | --- |
| Connected | Connection to HPE InfoSight was successful . |
| Connecting | Connection to HPE InfoSight is being attempted. |
| ConnectionFailed | Connection to HPE InfoSight failed. |
| NotInitiated | Connection to HPE InfoSight was not initiated. |


## HpeWfmJobResults

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **OutputDownloadFile** | <br><br>*read-only* | The URI for the output download file after a successfull run. |
| **Results** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |

## HpeWfmJobServiceExt

This is the schema definition for HpeWfmJobServiceExt.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |

### Actions

### AhsDownloadJobs


Download AHS Jobs.

**URIs**:


(This action takes no parameters.)


### ApplyConfigurationBaselineJobs


Apply Configuration Baseline jobs.

**URIs**:


(This action takes no parameters.)


### AssignRecoveryPolicyJob


Assign Recovery Policy.

**URIs**:


(This action takes no parameters.)


### ConfigureRemoteSyslogJobs


Setting Indicator LED.

**URIs**:


(This action takes no parameters.)


### CreateGroupJobs


Creating group jobs.

**URIs**:


(This action takes no parameters.)


### DeleteCompletedJobs


Delete all the completed Jobs.

**URIs**:


(This action takes no parameters.)


### DeleteJobs


Delete Server.

**URIs**:


(This action takes no parameters.)


### DownloadAuditLogsJobs


Download Audit jobs.

**URIs**:


(This action takes no parameters.)


### DownloadReportJobs


Download Report jobs.

**URIs**:


(This action takes no parameters.)


### ExcludeServersFromInfoSight


Exclude servers from InfoSight.

**URIs**:


(This action takes no parameters.)


### ImportBaselineJobs


Import Baseline jobs.

**URIs**:


(This action takes no parameters.)


### ImportConfigurationBaselineJobs


Import Configuration Baseline jobs.

**URIs**:


(This action takes no parameters.)


### ImportOSBaselineJobs


Import Baseline jobs.

**URIs**:


(This action takes no parameters.)


### ManualRecoveryJobs


Manual Recovery.

**URIs**:


(This action takes no parameters.)


### OnDemandAhsJobs


Download AHS Jobs.

**URIs**:


(This action takes no parameters.)


### QuarantineActionJobs


Quarantine Action.

**URIs**:


(This action takes no parameters.)


### RefreshJob


Server Refresh.

**URIs**:


(This action takes no parameters.)


### ResetSystemJobs


Resetting Systems.

**URIs**:


(This action takes no parameters.)


### ServerGroupActionJobs


Delete Server.

**URIs**:


(This action takes no parameters.)


### ServerGroupJobs


Server group jobs.

**URIs**:


(This action takes no parameters.)


### ServerUpdateJobs


Server Updatejobs.

**URIs**:


(This action takes no parameters.)


### SetIndicatorLedJobs


Setting Indicator LED.

**URIs**:


(This action takes no parameters.)


### SppComplianceJobs


SPP Compliance jobs.

**URIs**:


(This action takes no parameters.)


### UnAssignRecoveryPolicyJob


Unassign Recovery Policy.

**URIs**:


(This action takes no parameters.)


### UpdateFirmwareJobs


Updating firmwares on servers.

**URIs**:


(This action takes no parameters.)


### VirtualMediaJobs


Mounting Virtual Media.

**URIs**:


(This action takes no parameters.)


## HpeWfmLicense

This is the schema definition for HpeWfmLicense.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **License** | string<br><br>*read-only* | Describes the name of the license installed on management processor. |
| **LicensedNoOfServers** | integer<br><br>*read-only* | Indicates the number of servers that can be managed. |
| **LicenseFirstName** | string<br><br>*read-only* | First name. |
| **LicenseKey** | string<br><br>*read-write<br>(null)* | The installed license key.Will be set to NULL on read. |
| **LicenseLastName** | string<br><br>*read-only* | Last name. |
| **LicenseMailID** | string<br><br>*read-only* | Users email ID . |
| **LicenseOrganization** | string<br><br>*read-only* | Organization name. |
| **LicenseType** | string<br><br>*read-only* | Indicates whether the license is Perpetual or Evaluation. |
| **Name** | <br><br>*read-write* |  |
| **Oem** | <br><br>*read-write* |  |

## HpeWfmLicenseInfo

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **LicenseInfo** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | This indicates the total count of servers that hold this license. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | This indicates the license name. |
| } ] |   |   |
| **Name** | <br><br>*read-write* |  |

## HpeWfmLogEntry

This is the schema definition for HpeWfmLogEntry.

|     |     |     |
| --- | --- | --- |
| **ActionRequired** | string<br><br>*read-only* | The ActionRequired is to be done in order to possibly resolve the problem occured. |
| **Category** | string<br><br>*read-only* | The log entry category. |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **iLoIPAddress** | string<br><br>*read-only* | The IP address of the iLO. |
| **Name** | <br><br>*read-write* |  |
| **Summary** | string<br><br>*read-only* | The log entry summary. |
| **Updated** | string<br><br>*read-only* | The date and time of the latest log entry update, for example, 2014-04-15T00:38:00Z. |

## HpeWfmManagedGroup

This is the schema definition for HpeWfmManagedGroup.

|     |     |     |
| --- | --- | --- |
| **AggregatedHealth** { | object | The aggregated health of all systems in the Federation group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Critical** | integer<br><br>*read-only* | The number of systems with Critical health status in the Federation group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OK** | integer<br><br>*read-only* | The number of systems with OK health status in the Federation group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Unknown** | integer<br><br>*read-only* | The number of systems with unknown health status in the Federation group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Warning** | integer<br><br>*read-only* | The number of systems with Warning health status in the Federation group. |
| } |   |   |
| **Description** | <br><br>*read-write* |  |
| **Discovery** | <br><br>*read-write* |  |
| **FirmwareUpdateRequired** | boolean<br><br>*read-only* | The group has servers with incompatible iLO firmware versions. Hence a firmware update is required |
| **Id** | <br><br>*read-write* |  |
| **LastTaskStatus** | <br><br>*read-write* |  |
| **Links** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedSystems** { | object | The value of this property shall be a reference to a resource of Type ManagedSystems for this group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedSystemsSummary** { | object | The value of this property shall be a reference to a resource of Type ManagedSystemsSummary for this group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Reports** { | object | The value of this property shall be a reference to a resource of Type ReportsSummary for this group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **ManagerAddressWithCredentials** | <br><br>*read-write* |  |
| **Name** | string<br><br>*read-only* | The name of the Federation Group. |
| **RefreshRequired** | boolean<br><br>*read-only* | The group is newly formed / a server is newly added to the group. |
| **SystemsCount** | integer<br><br>*read-only* | The number of systems in the Federation group. |

## HpeWfmManagedGroupSession

This is the schema definition for HpeWfmManagedGroupSession.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Password** | string<br><br>*read-write* | The password for the managed system. |
| **SessionKey** | string<br><br>*read-only* | The session key for the managed system. |
| **SessionURL** | string<br><br>*read-only* | The session URL for the managed system. |
| **UserName** | string<br><br>*read-write* | The username for the managed system. |

## HpeWfmManagedServerGroups

This is the schema definition for HpeWfmManagedServerGroups.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Discovery** | <br><br>*read-write* |  |
| **FirmwareUpdateRequired** | boolean<br><br>*read-only* | The group has servers with incompatible iLO firmware versions. Hence a firmware update is required. |
| **GroupDescription** | string<br><br>*read-write* | The description of the Server Group. |
| **Id** | <br><br>*read-write* |  |
| **LastTaskStatus** | <br><br>*read-write* |  |
| **Links** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedSystems** { | object | The value of this property shall be a reference to a resource of Type ManagedSystems for this group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagedSystemsSummary** { | object | The value of this property shall be a reference to a resource of Type ManagedSystemsSummary for this group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Reports** { | object | The value of this property shall be a reference to a resource of Type ReportsSummary for this group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | string<br><br>*read-only* | The name of the Server Group. |
| **RefreshRequired** | boolean<br><br>*read-only* | The group is newly formed / a server is newly added to the group. |
| **SystemsCount** | integer<br><br>*read-only* | The number of systems in the server group. |

## HpeWfmManagedSystem

This is the schema definition for HpeWfmManagedSystem.

|     |     |     |
| --- | --- | --- |
| **ArrayControllers** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CacheMemorySizeMiB** | integer<br><br>*read-only* | Indicates the Cache Memory size of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only* | Indicates the Firmware Version of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br><br>*read-only* | Indicates the Health Status of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** | string<br><br>*read-only* | Indicates the Location of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LocationFormat** | string<br><br>*read-only* | Indicates the Location format of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LogicalDrives** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CapacityMiB** | integer<br><br>*read-only<br>(null)* | Capacity of the Logical Drive in MiB. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br><br>*read-only<br>(null)* | Health Status of the Logical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LogicalDriveEncryption** | boolean<br><br>*read-only<br>(null)* | Logical Drive Encryption is Enabled on the Drive if True, Disabled if False. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LogicalDriveNumber** | integer<br><br>*read-only<br>(null)* | Number of the Logical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LogicalDriveType** | string<br><br>*read-only<br>(null)* | Type of the Logical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Name of the Logical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Raid** | string<br><br>*read-only<br>(null)* | Raid level of the Logical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only<br>(null)* | State of the Logical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VolumeUniqueIdentifier** | string<br><br>*read-only<br>(null)* | Volume Unique Identifier of the Logical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only* | Indicates the Model of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only* | Indicates the Name of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PhysicalDrives** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CapacityGB** | integer<br><br>*read-only<br>(null)* | Capacity of the Physical Drive in GB. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CapacityMiB** | integer<br><br>*read-only<br>(null)* | Capacity of the Physical Drive in MiB. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | Firmware Version of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br><br>*read-only<br>(null)* | Health Status of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InterfaceSpeedMbps** | integer<br><br>*read-only<br>(null)* | Interface Speed of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InterfaceType** | string<br><br>*read-only<br>(null)* | Interface Type of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** | string<br><br>*read-only<br>(null)* | Location of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LocationFormat** | string<br><br>*read-only<br>(null)* | Location Format of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MediaType** | string<br><br>*read-only<br>(null)* | Media Type of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | Model of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RotationalSpeedRpm** | integer<br><br>*read-only<br>(null)* | Rotational Speed of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only<br>(null)* | Serial Number of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only<br>(null)* | State of the Physical Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only* | Indicates the Serial Number of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only* | Indicates the State of the Array Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StorageEnclosures** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DriveBayCount** | integer<br><br>*read-only<br>(null)* | Drive Bay Count of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | Firmware Version of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br><br>*read-only<br>(null)* | Health Status of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** | string<br><br>*read-only<br>(null)* | Location of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LocationFormat** | string<br><br>*read-only<br>(null)* | Location Format of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Name of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only<br>(null)* | Serial Number of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only<br>(null)* | State of the Storage Enclosure. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } ] |   |   |
| **Description** | <br><br>*read-write* |  |
| **DeviceInventory** [ { | array | The information relating to the Manager of this system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | <br><br>*read-write* |  |
| } ] |   |   |
| **FansSummary** { | object | This object describes the system's fan details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | The number of fans in the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Details** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentReading** | integer<br><br>*read-only<br>(null)* | The current speed of the fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FanName** | string<br><br>*read-only<br>(null)* | The name of the fan sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ReadingRPM** | integer<br><br>*read-only<br>(null)* | The current speed of the fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Units** | string<br>(enum)<br><br>*read-only<br>(null)* | Units for the CurrentReading. *For the possible property values, see Units in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **FirmwareInventory** [ { | array | The information relating to the Manager of this system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | <br><br>*read-write* |  |
| } ] |   |   |
| **HealthSummary** { | object | This object describes the health status of the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AgentlessManagementService** | string<br><br>*read-only<br>(null)* | The status of the Agentless Management Service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BiosOrHardwareHealth** | string<br><br>*read-only<br>(null)* | The Health status of the Bios or Hardware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FanRedundancy** | string<br><br>*read-only<br>(null)* | This is the fan redundancy state of the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Fans** | string<br><br>*read-only<br>(null)* | The Health status of the Fans. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**iLOHealth** | string<br><br>*read-only<br>(null)* | The status of the iLO Health. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Memory** | string<br><br>*read-only<br>(null)* | The Health status of the Memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Network** | string<br><br>*read-only<br>(null)* | The Health status of the Network. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerSupplies** | string<br><br>*read-only<br>(null)* | The Health status of the Power Supplies. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerSupplyRedundancy** | string<br><br>*read-only<br>(null)* | This is the power supply redundancy state of the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Processors** | string<br><br>*read-only<br>(null)* | The Health status of the Processors. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SmartStorageBattery** | string<br><br>*read-only<br>(null)* | The Smart Storage Battery state of the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Storage** | string<br><br>*read-only<br>(null)* | The Health status of the Storage. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Temperatures** | string<br><br>*read-only<br>(null)* | The Health status of Temperatures. |
| } |   |   |
| **HostBusAdapters** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Drives** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CapacityMiB** | integer<br><br>*read-only<br>(null)* | Capacity of the drive in MiB. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | Firmware Version of the Disk Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br><br>*read-only<br>(null)* | Health Status of the Disk. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** | string<br><br>*read-only<br>(null)* | Location of the Disk Drive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | Model of the Disk. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Name of the Disk. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only<br>(null)* | Serial Number of the Disk. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only<br>(null)* | State of the Disk. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only* | Indicates the Firmware Version of the Host Bus Adapter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br><br>*read-only* | Indicates the Health Status of the Host Bus Adapter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** | string<br><br>*read-only* | Indicates the Location of the Host Bus Adapter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only* | Indicates the Model of the Host Bus Adapter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only* | Indicates the Name of the Host Bus Adapter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only* | Indicates the Serial Number of the Host Bus Adapter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only* | Indicates the State of the Host Bus Adapter. |
| } ] |   |   |
| **Id** | <br><br>*read-write* |  |
| **InfoSightMetrics** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AHSData** { | object | Indicates the AHS download and upload status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AHSDownloadErrorDetails** | string<br><br>*read-only* | Indicates the error details of why the AHS Download Failed. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AHSFileSizeKB** | integer<br><br>*read-only* | The Size of the AHS File Downloaded in KB. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DownloadEndTime** | string<br><br>*read-only* | Indicates the end time of the last AHS file downloaded for this node. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DownloadStartTime** | string<br><br>*read-only* | Indicates the start time of the last AHS file downloaded for this node. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DownloadStatus** | string<br>(enum)<br><br>*read-only* | Indicates the status of the last AHS file downloaded for this node. *For the possible property values, see DownloadStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UploadEndTime** | string<br><br>*read-only* | Indicates the end time of the last AHS file uploaded to InfoSight for this node. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UploadStartTime** | string<br><br>*read-only* | Indicates the start time of the last AHS file uploaded to InfoSight for this node. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UploadStatus** | string<br>(enum)<br><br>*read-only* | Indicates the status of the last AHS file uploaded to InfoSight for this node. *For the possible property values, see UploadStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HeartBeatLastUpdated** | string<br><br>*read-only* | Indicates the last updated heartbeat timestamp. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InventoryLastUpdated** | string<br><br>*read-only* | Indicates the last updated inventory timestamp. |
| } |   |   |
| **Manager** { | object | The information relating to the Manager of this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Credentials** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DateTime** | string<br><br>*read-only* | iLO Date and Time |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | The firmware version of this Manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**License** { | object | The information relating to the Manager license of this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LicenseKey** | string<br><br>*read-only* | The license key installed on this management processor. License keys are 25 characters in length and contain both letters and numbers. Use POST method to collection of membertype HpiLOLicense to install / update the license. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LicenseType** | string<br>(enum)<br><br>*read-only* | The type of license installed on this management processor. *For the possible property values, see LicenseType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only* | The name of the license installed on this management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerEthernetAddresses** [ { | array | This array of objects is used to represent the IPv4 connection characteristics for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv4Address** | string<br><br>*read-only* | Indicates the IPv4 Address of the Manager Ethernet Interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv6Address1** | string<br><br>*read-only* | Indicates the IPv6 Address of the Manager Ethernet Interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv6Address2** | string<br><br>*read-only* | Indicates the IPv6 Address of the Manager Ethernet Interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv6Address3** | string<br><br>*read-only* | Indicates the IPv6 Address of the Manager Ethernet Interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv6Address4** | string<br><br>*read-only* | Indicates the IPv6 Address of the Manager Ethernet Interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerFQDN** | string<br><br>*read-only* | Indicates the FQDN of the Manager Ethernet Interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NICEnabled** | boolean<br><br>*read-only* | Indicates whether the NIC is enabled or not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerType** | string<br>(enum)<br><br>*read-only* | This property is the manager type for this resource. *For the possible property values, see ManagerType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | Model name of the manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteSyslog** { | object | The information relating to the remote syslog configuration of the Manager of this system |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enabled** | boolean<br><br>*read-write* | Indicates whether Remote Syslog is enabled. When enabled, management processor sends notification messages to the specified Syslog server. This can be enabled only when the property RemoteSyslogServer is set or not empty. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | integer<br><br>*read-write* | The port number through which the Syslog server is listening. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Server** | string<br><br>*read-write* | The IP address, FQDN, IPv6 name, or short name of the server running the Syslog service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpdateService** { | object | The information relating to the update service of the Manager of this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Details** | string<br><br>*read-only* | Details about the current firmware flash status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Flags** | string<br>(enum)<br><br>*read-only* | Other flags. *For the possible property values, see Flags in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ImageType** | string<br>(enum)<br><br>*read-only* | Firmware flash image type. *For the possible property values, see ImageType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProgressPercent** | integer<br><br>*read-only* | Firmware flash progress. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br>(enum)<br><br>*read-only* | Current state of the firmware flash. *For the possible property values, see State in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UUID** | string<br><br>*read-only<br>(null)* | The universal unique identifier for this Manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VirtualMedia** { | object | The information relating to the Manager virtual media of this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ConnectedVia** | string<br>(enum)<br><br>*read-only<br>(null)* | Specifies how the virtual media is connected to the server. *For the possible property values, see ConnectedVia in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **MemorySummary** { | object | This object describes the central memory of the system in general detail. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | The number of processors in the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Details** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DIMMStatus** | string<br>(enum)<br><br>*read-only<br>(null)* | Specifies memory module status and whether the module in use. *For the possible property values, see DIMMStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DIMMTechnology** | string<br>(enum)<br><br>*read-only<br>(null)* | The memory module technology type. *For the possible property values, see DIMMTechnology in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DIMMType** | string<br>(enum)<br><br>*read-only<br>(null)* | The type of memory DIMM used in this system. *For the possible property values, see DIMMType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaximumFrequencyMHz** | integer<br><br>*read-only<br>(null)* | Identifies the maximum, capable speed of the device in megahertz (MHz). If the value is null, the speed is unknown. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SizeMB** | integer<br><br>*read-only<br>(null)* | The size of the memory device in megabytes. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SocketLocator** | string<br><br>*read-only<br>(null)* | The socket of this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalSystemMemoryGiB** | integer<br><br>*read-only<br>(null)* | This is the total amount of memory in the system measured in GiB. |
| } |   |   |
| **Name** | <br><br>*read-write* |  |
| **NetworkAdapters** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | Network Adapter firmware version |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Network Adapter name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PhysicalPorts** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FullDuplex** | boolean<br><br>*read-only<br>(null)* | Full-duplex data transmission allows data to be transmitted in both directions on a signal carrier at the same time. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv4Addresses** [ { | array | This array of objects is used to represent the IPv4 connection characteristics for this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Address** | string<br><br>*read-only<br>(null)* | This is the IPv4 Address. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPv6Addresses** [ { | array | This array of objects enumerates all of the currently assigned IPv6 addresses on this interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Address** | string<br><br>*read-only<br>(null)* | This is the IPv6 Address. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MacAddress** | string<br><br>*read-only<br>(null)* | The port MAC address. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SpeedMbps** | integer<br><br>*read-only<br>(null)* | An estimate of the interface's current bandwidth in Megabits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } ] |   |   |
| **PCIDeviceSummary** [ { | array | The information relating to the PCI Devices of the Manager of this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeviceID** | integer<br><br>*read-write* | Indicates the Device ID of the PCI Device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeviceLocation** | string<br><br>*read-write* | Indicates the location of the PCI Device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeviceType** | string<br><br>*read-write* | Indicates the device type of the PCI Device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeviceVersion** | string<br><br>*read-write* | Indicates the device Version of the PCI Device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only* | Indicates the name of the PCI Device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SubsystemDeviceID** | integer<br><br>*read-only* | Indicates the Subsystem Device ID of the PCI Device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SubsystemVendorID** | integer<br><br>*read-write* | Indicates the Subsystem Vendor ID of the PCI Device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VendorID** | integer<br><br>*read-only* | Indicates the Vendor ID of the PCI Device. |
| } ] |   |   |
| **Persona** { | object | The information relating to the profile or persona applied on this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AppliedDetails** { | object | The result of the persona applied on this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LastApplied** | string<br><br>*read-only* | The date and time when the persona was applied on this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PersonaId** | integer<br><br>*read-only* | The name of the presona that was applied on this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | string<br>(enum)<br><br>*read-only* | The status result of the persona that was applied on this system. *For the possible property values, see Status in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ValidationDetails** { | object | The results of the persona validation performed on this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LastValidated** | string<br><br>*read-only* | The date and time when the persona was validated on this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PersonaId** | integer<br><br>*read-only* | The name of the presona that was validated on this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | string<br>(enum)<br><br>*read-only* | The status result of the persona validation that was applied on this system. *For the possible property values, see Status in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **PowerSummary** { | object | This object describes the power supplies of the system in general detail. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | The number of power supplies in the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerConsumedWatts** | integer<br><br>*read-only<br>(null)* | The amount of power consumed in Watts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerSupplies** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BayNumber** | integer<br><br>*read-only<br>(null)* | The bay number of this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | The Firmware version of the power supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br><br>*read-only<br>(null)* | The health status of the power supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HotplugCapable** | boolean<br><br>*read-only* | The Firmware version of the power supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | The product model of this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | The Name of the power supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerCapacityWatts** | integer<br><br>*read-only<br>(null)* | The total Power Capacity in Watts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerSupplyStatus** | string<br><br>*read-only<br>(null)* | The Status of the power supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only<br>(null)* | The power supply Serial Number. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SparePartNumber** | string<br><br>*read-only<br>(null)* | The power supply Spare Part Number. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only<br>(null)* | The state of the power supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **ProcessorSummary** { | object | This object describes the central processors of the system in general detail. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Count** | integer<br><br>*read-only<br>(null)* | The number of processors in the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Details** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CoresEnabled** | integer<br><br>*read-only<br>(null)* | The total number of cores enabled in this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Manufacturer** | string<br><br>*read-only<br>(null)* | The processor manufacturer. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | The product model number of this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Socket** | string<br><br>*read-only<br>(null)* | The socket of this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SpeedMHz** | integer<br><br>*read-only<br>(null)* | The maximum clock speed of the processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalCores** | integer<br><br>*read-only<br>(null)* | The total number of cores contained in this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalThreads** | integer<br><br>*read-only<br>(null)* | The total number of execution threads supported by this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | The processor model for the primary or majority of processors in this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | <br><br>*read-write* |  |
| } |   |   |
| **ServerGroups** [ ] | array (string)<br><br>*read-only* |  |
| **SmartStorageBatterySummary** [ { | array | This object describes the Smart Storage Battery details of the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ChargeLevelPercent** | integer<br><br>*read-only* | Charge Level Percent of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only* | Firmware Version of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HealthStatus** | string<br>(enum)<br><br>*read-only* | This represents the health status of the system *For the possible property values, see HealthStatus in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Index** | integer<br><br>*read-only* | Index of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaximumCapWatts** | integer<br><br>*read-only* | Maximum Capacity of Smart Storage Battery in Watts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only* | Model name of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProductName** | string<br><br>*read-only* | Product name of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemainingChargeTimeSeconds** | integer<br><br>*read-only* | Remaining Charge Time Seconds of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only* | Serial Number of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SparePartNumber** | string<br><br>*read-only* | Spare Part Number of Smart Storage Battery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only* | Indicates the State of the System. |
| } ] |   |   |
| **SoftwareInventory** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Description** | string<br><br>*read-only* | Indicates the description about the Software. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only* | Indicates the Name of the Software. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SoftwareId** | integer<br><br>*read-only* | Indicates the ID of the Software. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Version** | string<br><br>*read-only* | Indicates the Version of the Software. |
| } ] |   |   |
| **SystemSummary** | <br><br>*read-write* |  |
| **TaskHistory** [ { | array | Contains the members of this collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } ] |   |   |

### Property Details

### ConnectedVia:


Specifies how the virtual media is connected to the server.

| string | Description |
| --- | --- |
| Applet | Connected to a client application. |
| None |  |
| NotConnected | No current connection. |
| URI | Connected to a URI location. |

### DIMMStatus:


Specifies memory module status and whether the module in use.

| string | Description |
| --- | --- |
| AddedButUnused | DIMM is added but currently unused. |
| ConfigurationError | Configuration error in DIMM. |
| Degraded | DIMM state is degraded. |
| DoesNotMatch | DIMM type does not match. |
| ExpectedButMissing | DIMM is expected but missing. |
| GoodInUse | DIMM is functioning properly and currently in use. |
| GoodPartiallyInUse | DIMM is functioning properly but partially in use. |
| None |  |
| NotPresent | DIMM is not present. |
| NotSupported | DIMM is not supported. |
| Other | DIMM status that does not fit any of these definitions. |
| PresentSpare | DIMM is present but used as spare. |
| PresentUnused | DIMM is present but unused. |
| Unknown | The status of the DIMM is unknown. |
| UpgradedButUnused | DIMM is upgraded but currently unused. |

### DIMMTechnology:


The memory module technology type.

| string |
| --- |
| None | 
| BurstEDO | 
| FastPage | 
| Synchronous | 
| EDO | 
| LRDIMM | 
| RDRAM | 
| RDIMM | 
| UDIMM | 
| NVDIMM | 
| RNVDIMM | 
| LRNVDIMM | 
| Unknown | 

### DIMMType:


The type of memory DIMM used in this system.

| string |
| --- |
| None | 
| DDR | 
| DDR2 | 
| DDR3 | 
| DDR4 | 
| FBD2 | 
| LPDD3 | 
| LPDDR | 
| LPDDR2 | 
| LPDDR4 | 

### DownloadStatus:


Indicates the status of the last AHS file downloaded for this node.

| string |
| --- |
| Pending | 
| Running | 
| Done | 
| Failed | 

### Flags:


Other flags.

| string |
| --- |
| NONE | 
| RESET_ILO | 
| REQUEST_SYSTEM_COLD_BOOT | 
| REQUEST_SYSTEM_WARM_BOOT | 
| DEFERRED_AUX_PWR_CYCLE | 

### HealthStatus:


This represents the health status of the system

| string | Description |
| --- | --- |
| Critical | A critical condition exists that requires immediate attention |
| OK | Normal |
| Warning | A condition exists that requires attention |

### ImageType:


Firmware flash image type.

| string |
| --- |
| NO_DEVICE | 
| ILO_DEVICE | 
| ILO_DEVICE_FIRMWARE | 
| ILO_DEVICE_LANGPK | 
| ILO_DEVICE_DEBUGGER | 
| BIOS_DEVICE | 
| SCD_DEVICE | 
| CPLD_DEVICE | 
| CARB_DEVICE | 
| PM_DEVICE | 
| UNKNOWN | 

### LicenseType:


The type of license installed on this management processor.

| string |
| --- |
| Unlicensed | 
| Evaluation | 
| Perpetual | 
| Subscription | 
| Internal | 
| Duration | 
| Expired | 

### ManagerType:


This property is the manager type for this resource.

| string | Description |
| --- | --- |
| BMC | A controller which provides management functions for a single computer system. |
| EnclosureManager | A controller which provides management functions for a chassis or group of devices or systems. |
| ManagementController | A controller used primarily to monitor or manage the operation of a device or system. |

### State:


Current state of the firmware flash.

| string |
| --- |
| IDLE | 
| UPLOADING | 
| PROGRESSING | 
| COMPLETED | 
| ERROR | 

### Status:


The status result of the persona validation that was applied on this system.

| string |
| --- |
| NotInitiated | 
| Queued | 
| InProgress | 
| Failed | 
| Aborted | 
| Successful | 
| PartiallySuccessful | 
| NotSuccessful | 
| Unknown | 

### Units:


Units for the CurrentReading.

| string |
| --- |
| None | 
| RPM | 
| Percent | 

### UploadStatus:


Indicates the status of the last AHS file uploaded to InfoSight for this node.

| string |
| --- |
| Pending | 
| Running | 
| Done | 
| Failed | 

## HpeWfmManagerExt

This is the schema definition for HpeWfmManagerExt.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Firmware** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **License** | <br><br>*read-write* |  |
| **Links** { | object | The links array contains the links to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AddOnServicesManager** { | object | The URI for the add-on services manager resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineService** { | object | The URI for this security service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DateTimeService** { | object | The URI for this date time service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InfosightAggregationPolicy** { | object | Reference to a resource of InfoSight Aggregation Policy. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LicenseService** { | object | The URI for this license service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LoggerPolicy** { | object | Reference to a resource of Debug LoggerPolicy. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecurityService** { | object | The URI for this security service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Telemetry** { | object | The URI for telemetry service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpdateService** { | object | The URI for this update service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |
| **SerialCLISpeed** | integer<br>(enum)<br><br>*read-write* | Serial command line interface speed in bits/second. *For the possible property values, see SerialCLISpeed in Property Details.* |
| **SerialCLIStatus** | string<br>(enum)<br><br>*read-write<br>(null)* | Status of serial command line interface. *For the possible property values, see SerialCLIStatus in Property Details.* |
| **Type** | <br><br>*read-write* |  |
| **WatchdogTimerActive** | boolean<br><br>*read-write* | Specifies whether Watchdog is enabled or not. |

### Actions

### Backup




**URIs**:


(This action takes no parameters.)


### ResetToFactoryDefaults




**URIs**:


(This action takes no parameters.)


### Restore




**URIs**:


(This action takes no parameters.)


### Shutdown




**URIs**:


(This action takes no parameters.)


### Property Details

### SerialCLISpeed:


Serial command line interface speed in bits/second.

| integer |
| --- |
| 9600 | 
| 19200 | 
| 38400 | 
| 57600 | 
| 115200 | 

### SerialCLIStatus:


Status of serial command line interface.

| string | Description |
| --- | --- |
| Disabled | Serial command line interface is disabled. |
| EnabledAuthReq | Serial command line interface is enabled with authentication required. |
| EnabledNoAuth | Serial command line interface is enabled with no authentication required. |
| None |  |


## HpeWfmManagerNetworkService

This is the schema definition for HpeWfmManagerNetworkService.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Links** { | object | The resource URIs related to the network services managed by this manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EthernetInterfaces** { | object | The URIs of the Ethernet NICs. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |
| **ProxyServer** { | object | Proxy Server options. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BypassProxyEnabled** | boolean<br><br>*read-write* | Indicates whether to bypass the proxy or not. When enabled, management processor sends alerts without using the proxy server otherwise it will use the proxy server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BypassProxyServers** | string<br><br>*read-write* | Bypass Proxy Servers list. The list should be comma separated values. The valid entries are ipv4/ipv6 address, FQDN, Domain name, CIDR format like 15.146.0.0/12 and domain name prefixed with "." to match *.domain names (.hpe.com)  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enabled** | boolean<br><br>*read-write* | Indicates whether to use proxy server or not. When enabled, management processor sends alerts via proxy server otherwise it will not use the proxy server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | integer<br><br>*read-write* | The port number through which the Proxy server is listening. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProxyPassword** | string<br><br>*read-write* | Password for proxy server authentication. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProxyUsername** | string<br><br>*read-write* | Username for proxy server authentication. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecureProxyEnabled** | boolean<br><br>*read-write* | Indicates whether to connect to proxy server securely. When enabled, proxy server is connected via https, else uses http. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Server** | string<br><br>*read-write* | The IP address, FQDN, IPv6 name, or short name of the Proxy server. |
| } |   |   |
| **RemoteSyslog** { | object | Remote Syslog options. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enabled** | boolean<br><br>*read-write* | Indicates whether Remote Syslog is enabled. When enabled, management processor sends notification messages to the specified Syslog server. This can be enabled only when the property RemoteSyslogServer is set or not empty. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | integer<br><br>*read-write* | The port number through which the Syslog server is listening. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryServer** | string<br><br>*read-write* | The IP address, FQDN, IPv6 name, or short name of the server running the Syslog service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryServer** | string<br><br>*read-write* | The IP address, FQDN, IPv6 name, or short name of the server running the Syslog service. |
| } |   |   |
| **TestConnectionResults** { | object | Results of the last run test. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DetailString** | string<br><br>*read-only* | Detailed message string for the status of connection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LastTestRunDate** | string<br><br>*read-only<br>(null)* | Time at which the tests were run last time. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | string<br>(enum)<br><br>*read-only* | Status of the last run test *For the possible property values, see Status in Property Details.* |
| } |   |   |

### Actions

### SendTestSyslog




**URIs**:


(This action takes no parameters.)


### TestConnection


Test Connectivity to HPE InfoSight Backend.

**URIs**:


(This action takes no parameters.)


### Property Details

### Status:


Status of the last run test

| string | Description |
| --- | --- |
| Failed | Test connection failed. |
| NotInitiated | Test was not initiated. |
| PartialSuccess | Partial success. See DetailString. |
| Success | Test connection succeeded. |
| Testing | Testing in progress |


## HpeWfmManualRecoveryJobResults

This is the schema definition for HpeWfmManualRecoveryJobResults.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **InstallSetInfo** { | object | The Install Set Details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InstallSetComponents** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentInfo** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ActiveVersion** | string<br><br>*read-write* | The component active version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AvailableVersion** | string<br><br>*read-write* | The component version available for update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentDescription** | string<br><br>*read-write* | The component description of the install component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentName** | string<br><br>*read-write* | The component name of the install component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentType** | string<br><br>*read-write* | The component type(Firmware/Driver etc.) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentVersion** | string<br><br>*read-write* | The component current version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DependencyFailed** | boolean<br><br>*read-write* | The component install dependency failed flag. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeploymentResult** | string<br><br>*read-write* | The result after the deployment. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InstalledVersion** | string<br><br>*read-write* | The final installed version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsForcedFlag** | boolean<br><br>*read-write* | The component isForced flag. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsSelectedFlag** | boolean<br><br>*read-write* | The component isSelected flag. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PreviousInstalledVersion** | string<br><br>*read-write* | The previous installed version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProductFamilyName** | string<br><br>*read-write* | The component product family name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StatusMessage** | string<br><br>*read-write* | The component install status message. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerAddress** | string<br><br>*read-write* | The IP address of the  Managed Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalErrors** | integer<br><br>*read-write* | Gives the total errors/failed dependencies during the calculate Install set for the Managed Node. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |

## HpeWfmNonFedGroupJobResults

This is the schema definition for HpeWfmNonFedGroupJobResults.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **ServerGroupJobInfo** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**JobStatus** | string<br><br>*read-only* | Progress message associated with the job. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerAddress** | string<br><br>*read-only* | The Manager address of the Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StatusMessage** | string<br><br>*read-only* | Progress message associated with the job. |
| } ] |   |   |

## HpeWfmOSBaseline

This is the schema definition for HpeWfmOSBaseline.

|     |     |     |
| --- | --- | --- |
| **BaselineState** | string<br>(enum)<br><br>*read-only* | This property indicates the state of inventory for this resource. *For the possible property values, see BaselineState in Property Details.* |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **RelatedTask** { | object | The URI refers to the task which is created to import this OS baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **SizeInMB** | integer<br><br>*read-only* | Space on disk (in MB) used by this OS baseline. |

### Property Details

### BaselineState:


This property indicates the state of inventory for this resource.

| string | Description |
| --- | --- |
| ImportFailed | Import of the OS baseline failed. |
| ImportInProgress | Import of the OS baseline is in progress. |
| ImportSuccess | Import of the OS baseline was completed successfully. |


## HpeWfmOSBaselineService

This is the schema definition for HpeWfmOSBaselineService.

|     |     |     |
| --- | --- | --- |
| **DateTime** | string<br><br>*read-only<br>(null)* | The current DateTime (with offset) setting that the task service is using. |
| **Description** | <br><br>*read-write* |  |
| **FreeSpaceInMB** | integer<br><br>*read-only* | Free space of disk (in MB) remaining for importing OS baselines . |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Oem** | <br><br>*read-write* | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. |
| **OSBaselines** { | object | This property references a collection resource of imported OS baselines. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **ServiceEnabled** | boolean<br><br>*read-only<br>(null)* | This indicates whether this service is enabled. |
| **Status** | <br><br>*read-write* |  |
| **TotalSpaceInMB** | integer<br><br>*read-only* | Total space of disk (in MB) allocated for importing OS baselines . |

## HpeWfmRecoveryPolicy

This is the schema definition for HpeWfmRecoveryPolicy.

|     |     |     |
| --- | --- | --- |
| **BaselineID** | integer<br><br>*read-write* | The Baseline ID used for this recovery policy. |
| **CreatedBy** | string<br><br>*read-only* | The name of the user that created the recovery policy. |
| **CreatedTime** | string<br><br>*read-only* | The recovery policy creation time. |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **LastUpdatedBy** | string<br><br>*read-only* | The name of the user that last updated the recovery policy. |
| **LastUpdatedTime** | string<br><br>*read-only* | The recovery policy modification time. |
| **Name** | string<br><br>*read-write* | The name of the recovery policy. |
| **OperatingSystemID** | integer<br><br>*read-write* | The Operating System ID used for this recovery policy. |
| **PersonaID** | integer<br><br>*read-write* | The Persona ID used for this recovery policy. |
| **Type** | <br><br>*read-write* |  |
| **UseNANDBackupRestoreIfAvailable** | boolean<br><br>*read-write* | Describes whether we should use the iLO Backup and Restore feature. |
| **Version** | integer<br><br>*read-only* | The recovery policy version. |

## HpeWfmSecurityServiceExt

This is the schema definition for HpeWfmSecurityServiceExt.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **LoginBanner** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsEnabled** | boolean<br><br>*read-write* | The login security banner message that is displayed on the management processor Login page. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Message** | string<br><br>*read-write* | The is to enable the message that is displayed on the management processor Login page. |
| } |   |   |
| **Name** | <br><br>*read-write* |  |

## HpeWfmServerGroups

This is the schema definition for HpeWfmServerGroups.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Systems** { | object | This property references a resource of type Collection with a MemberType of Systems in the server groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |

## HpeWfmServiceExt

This is the schema definition for HpeWfmServiceExt.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Language** | string<br><br>*read-write* | Specifies the Language to be used. |
| **Links** { | object | The links array contains the links to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AggregatorService** { | object | The URI to this Aggregator service resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResourceDirectory** { | object | The URI for the  resource directory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Manager** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FQDN** | string<br><br>*read-only* | Fully qualified domain name of the management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HostName** | string<br><br>*read-only* | The name of management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerFirmwareVersion** | string<br><br>*read-only* | The major and minor management processor version numbers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerFirmwareVersionPass** | string<br><br>*read-only* | The build or pass number of the management processor version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br>(enum)<br><br>*read-only* | The type of the service manager. *For the possible property values, see Model in Property Details.* |
| } ] |   |   |
| **Name** | <br><br>*read-write* |  |
| **Sessions** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CertCommonName** | string<br><br>*read-only* | The name of the management processor as it appears in the digital certificate when a secure web GUI session is established to the management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**KerberosEnabled** | boolean<br><br>*read-only* | Specifies whether Kerberos login is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LDAPAuthLicenced** | boolean<br><br>*read-only* | Specifies whether a valid license is installed for LDAP use. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LDAPEnabled** | boolean<br><br>*read-only* | Specifies whether LDAP login is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LocalLoginEnabled** | boolean<br><br>*read-only* | Specifies whether local users can log in. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LoginFailureDelay** | integer<br><br>*read-only* | The delay (seconds) when a management processor login attempt has failed. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LoginHint** { | object |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint** | string<br><br>*read-only* | The information on how to log in to the management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HintPOSTData** { | object | The POST information on how to log in to the management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Password** | string<br><br>*read-only* | The password for logging in to the management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UserName** | string<br><br>*read-only* | The user name for logging in to the management processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecurityMessage** | string<br><br>*read-only* | The login security banner message that is displayed on the management processor Login page. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecurityOverride** | boolean<br><br>*read-only* | Specifies whether the security override switch is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServerName** | string<br><br>*read-only* | The name of the server that this management processor is managing. |
| } |   |   |

## HpeWfmSessionExt

This is the schema definition for HpeWfmSessionExt.

|     |     |     |
| --- | --- | --- |
| **AccessTime** | string<br><br>*read-only* | User session last-access time |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **LoginTime** | string<br><br>*read-only* | User session login time |
| **MySession** | boolean<br><br>*read-only* | Indicates whether this is a session you own. |
| **Name** | <br><br>*read-write* |  |
| **Privilege** | string<br>(enum)<br><br>*read-write* | Account privileges available for the user *For the possible property values, see Privilege in Property Details.* |
| **Type** | <br><br>*read-write* |  |
| **UserAccount** | string<br><br>*read-only* | Login details of the user |
| **UserExpires** | string<br><br>*read-only* | User session expire time |
| **UserIP** | string<br><br>*read-only* | IP address of the user |
| **UserTag** | string<br>(enum)<br><br>*read-only* | Session source *For the possible property values, see UserTag in Property Details.* |
| **UserType** | string<br>(enum)<br><br>*read-only* | User type *For the possible property values, see UserType in Property Details.* |

### Property Details

### Privilege:


Account privileges available for the user

| string | Description |
| --- | --- |
| Device | Allows configuring and performing actions on devices includes login privilege |
| Login | Read operations allowed like viewing discovered nodes and groups and generate reports |
| Manager | All operations allowed |
| User | Allows configuring users with device privilege |

### UserTag:


Session source

| string |
| --- |
| Web UI | 
| SSH | 
| Console | 
| Unknown | 

### UserType:


User type

| string |
| --- |
| Local | 
| Directory | 
| Single Sign On | 
| Kerberos | 
| Trusted Key | 
| Security Override | 
| System | 
| Federation | 


## HpeWfmSoftwareInventory

This is the schema definition for HpeWfmSoftwareInventory.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **DeviceClass** | string<br><br>*read-only* | The Device Class of the firmware. |
| **DeviceContext** | string<br><br>*read-only* | The Device Context of the firmware. |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **OSType** | string<br><br>*read-only* | The OS type for the driver/software. |

## HpeWfmSppComplianceJobResults

This is the schema definition for HpeWfmSppComplianceJobResults.

|     |     |     |
| --- | --- | --- |
| **BaselineComplianceInfo** { | object | The Install Set Details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentInfo** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AvailableVersion** | string<br><br>*read-only* | The component version available in the baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentDescription** | string<br><br>*read-only* | The component description of the install component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentName** | string<br><br>*read-only* | The component name of the install component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InstalledVersion** | string<br><br>*read-only* | The current component version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** | string<br><br>*read-only* | Status of the component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsCompliantFlag** | boolean<br><br>*read-only* | The Server compliance flag. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsFirmwareOnly** | boolean<br><br>*read-only* | This describes whether the compliance is only for firmware or not. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerAddress** | string<br><br>*read-only* | The IP address of the Managed Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StatusMessage** | string<br><br>*read-only* | Progress message associated with the job. |
| } |   |   |
| **Description** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **Results** { | object | Result for the compliance run. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**JobStatusMessage** | string<br><br>*read-only* | Progress message associated with the job. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OutputCsvFile** | <br><br>*read-only* | The URI for the output CSV file after a successfull run. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResultSummary** [ { | array | Summary results for each node |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DetailedResultsUri** | string<br><br>*read-only* | The url for Detailed Results. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IpAddress** | string<br><br>*read-only* | The system/group on which the job is applied. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsCompliant** | boolean<br><br>*read-only* | Specifies whether the server is compliant with the baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StatusMessage** | string<br><br>*read-only* | Progress message associated with the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |

## HpeWfmSystemSummary

This is the schema definition for HpeWfmSystemSummary.

|     |     |     |
| --- | --- | --- |
| **ActionCapabilities** { | object | This object describes the Actions that can be performed on the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AbsarokaOfflineUpdate** | boolean<br><br>*read-only* | The Action capability for Absaroka Offline Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AbsarokaOnlineUpdate** | boolean<br><br>*read-only* | The Action capability for Absaroka Online Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AHSDownload** | boolean<br><br>*read-only* | The Action capability for AHS Download. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AssignRecovery** | boolean<br><br>*read-only* | The Action capability for Assign Recovery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineAutomaticUpdate** | boolean<br><br>*read-only* | The Action capability for Baseline Automatic Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Delete** | boolean<br><br>*read-only* | The Action capability for Delete. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeployUpdate** | boolean<br><br>*read-only* | The Action capability for Deploy Capable Servers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ExcludeFromInfoSight** | boolean<br><br>*read-only* | This property indicates whether the server is excluded from sending data to InfoSight. If set to true the data is not sent to InfoSight, if set to false the data is sent to InfoSight. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareUpdate** | boolean<br><br>*read-only* | The Action capability for Firmware Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GroupManage** | boolean<br><br>*read-only* | The Action capability for Group Manage. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ImportConfigBaseline** | boolean<br><br>*read-only* | The Action capability for Import config baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManualRecovery** | boolean<br><br>*read-only* | The Action capability for Manual Recovery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OfflineFirmwareUpdate** | boolean<br><br>*read-only* | The Action capability for Offline Firmware Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OnlineFirmwareUpdate** | boolean<br><br>*read-only* | The Action capability for Online Firmware Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Power** | boolean<br><br>*read-only* | The Action capability for Power. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Refresh** | boolean<br><br>*read-only* | The Action capability for Refresh. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemoteSyslog** | boolean<br><br>*read-only* | The Action capability for Remote Syslog. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UID** | boolean<br><br>*read-only* | The Action capability for UID. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UnAssignRecovery** | boolean<br><br>*read-only* | The Action capability for Unassign Recovery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VirtualMedia** | boolean<br><br>*read-only* | The Action capability for Virtual Media. |
| } |   |   |
| **ActionErrorMessage** { | object | This object describes the Actions that can be performed on the system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AbsarokaOfflineUpdate** | string<br><br>*read-only* | The error message for Absaroka Offline Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AbsarokaOnlineUpdate** | string<br><br>*read-only* | The error message for Absaroka Online Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AssignRecovery** | string<br><br>*read-only* | The error message for Assign Recovery. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineAutomaticUpdate** | string<br><br>*read-only* | The error message for Baseline Automatic Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GroupManage** | string<br><br>*read-only* | The error message for Manage Group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ImportConfigBaseline** | string<br><br>*read-only* | The error message for Import Config Baseline. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OfflineFirmwareUpdate** | string<br><br>*read-only* | The error message for Offline Firmware Update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OnlineFirmwareUpdate** | string<br><br>*read-only* | The error message for Online Firmware Update. |
| } |   |   |
| **AllowActions** | boolean<br><br>*read-only* | Indicates if the action is allowed on a server. |
| **AMSStatus** | string<br><br>*read-only* | Gives the status of AMS. |
| **ChassisType** | string<br><br>*read-only* | The chassis type. |
| **Description** | <br><br>*read-write* |  |
| **Discovery** | <br><br>*read-write* |  |
| **EncryptionSecurityState** | string<br>(enum)<br><br>*read-only* | Indicates the Encryption Security State of the Server.  *For the possible property values, see EncryptionSecurityState in Property Details.* |
| **FederationActionGroupName** | string<br><br>*read-only* | Gives the name of the Federation Group the server belongs to. |
| **FederationEnabled** | boolean<br><br>*read-only* | Indicates whether management processor Federation management is enabled or disabled. |
| **FederationSupported** | boolean<br><br>*read-only* | Indicates whether management processor Federation is supported. |
| **GatewayManaged** | boolean<br><br>*read-only* | Indicates if the Server is Gateway Managed (Federation Group). |
| **HealthStatus** | string<br>(enum)<br><br>*read-only* | This represents the health status of the system. *For the possible property values, see HealthStatus in Property Details.* |
| **HostName** | string<br><br>*read-only* | The DNS Host Name, without any domain information. |
| **HostOSDescription** | string<br><br>*read-only* | Gives description about OS on the Host. |
| **HostOSName** | string<br><br>*read-only* | Gives the OS Name of the Host. |
| **HostOSType** | integer<br><br>*read-only* | Gives the OS Type of the Host. |
| **HostOSVersion** | string<br><br>*read-only* | Gives the OS Version of the Host. |
| **Id** | <br><br>*read-write* |  |
| **iLOBackupFileForRestore** | string<br><br>*read-only* | Indicates the date on which the backup was created on the iLO NAND. Otherwise says No. |
| **iLOHealth** | string<br><br>*read-only* | The status of the iLO Health. |
| **iLOType** | string<br><br>*read-only* | The iLO type of this Manager. |
| **iLOUUID** | string<br><br>*read-only* | The universal unique identifier for the iLO. |
| **IndicatorLED** | string<br>(enum)<br><br>*read-write* | The state of the indicator LED. *For the possible property values, see IndicatorLED in Property Details.* |
| **LastTaskStatus** | <br><br>*read-write* |  |
| **ManagerAddress** | string<br><br>*read-only* | The IP address or DNS of the manager which was added by user. |
| **ManagerFirmwareVersion** | string<br><br>*read-only* | Gives the Firmware Version of the manager. |
| **ManagerFQDN** | string<br><br>*read-only* | The fully qualified domain name of the manager. |
| **ManagerIPAddress** | string<br><br>*read-only* | The IPv4 address of the manager. |
| **ManagerIPv6Address1** | string<br><br>*read-only* | The IPv6 address of the manager. |
| **ManagerIPv6Address2** | string<br><br>*read-only* | The IPv6 address of the manager. |
| **ManagerIPv6Address3** | string<br><br>*read-only* | The IPv6 address of the manager. |
| **ManagerIPv6Address4** | string<br><br>*read-only* | The IPv6 address of the manager. |
| **ManagerLicense** | string<br><br>*read-only* | Gives the License of the manager. |
| **ManagerSSLPort** | integer<br><br>*read-only* | The Web Server SSL Port of the manager. |
| **ManagerVirtualMediaImage** | string<br><br>*read-write* | The valid URI indicating the image that is mounted on this server. A null value indicates that no image exists. |
| **ManualRecoveryFlag** | boolean<br><br>*read-only* | Indicates if the Server is set for Manual or Automatic Recovery. |
| **Manufacturer** | string<br><br>*read-only* | The manufacturer of the system. |
| **MasterManagerType** | string<br><br>*read-only* | The type of the manager. |
| **MasterManagerTypeUrl** | string<br><br>*read-only* | The url of the master manager type. |
| **Model** | string<br><br>*read-only* | The model information that the manufacturer uses to refer to this system. |
| **Name** | <br><br>*read-write* |  |
| **NumOfGrpsNodeBelongs** | integer<br><br>*read-only* | Gives the number of Federation Groups this iLO is part of. |
| **PowerState** | string<br>(enum)<br><br>*read-only* | This is the current power state of the system. *For the possible property values, see PowerState in Property Details.* |
| **ProductID** | string<br><br>*read-only* | The system product ID. |
| **RecoveryAction** | string<br><br>*read-only* | Indicates the Action that is set for recovery. |
| **RecoveryPolicyId** | integer<br><br>*read-only* | Gives the Recovery Policy Id. |
| **RecoveryPolicyName** | string<br><br>*read-only* | Indicates the Recovery Persona Applied on the System. |
| **RecoveryStatus** | string<br><br>*read-only* | Indicates the Status of the System. If the recovery install set is applied or not,  and its status once recovery starts. |
| **SecurityState** | string<br><br>*read-only* | Indicates the Security State of the System. |
| **SerialNumber** | string<br><br>*read-only* | The system serial number. |
| **ServerPlatformType** | string<br>(enum)<br><br>*read-only* | This property is the server platform type for this resource. *For the possible property values, see ServerPlatformType in Property Details.* |
| **ServerUpdateInfo** { | object | This object describes the status of the update operations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineId** | integer<br><br>*read-only* | The baseline that is applied for the server update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineName** | string<br><br>*read-only* | The name of the baseline that the server was staged with. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br>(enum)<br><br>*read-only* | The state field indicates whether the server is staged/deployed etc. *For the possible property values, see State in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StoredSUTMode** | string<br><br>*read-only* | The previous SUT mode before starting the update. |
| } |   |   |
| **StandAloneManaged** | boolean<br><br>*read-only* | Indicates if the Server is Standalone Managed with Credentials. |
| **StatusState** | string<br><br>*read-only* | Indicates the State of the System. |
| **SummaryForSystem** { | object | Link to the Managed System with detailed information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **SUTMode** | string<br><br>*read-only* | Gives the Mode of HPSUT. |
| **SUTServiceState** | string<br><br>*read-only* | Gives the Service state of HPSUT. |
| **SUTServiceVersion** | string<br><br>*read-only* | Gives the Service Version of HPSUT. |
| **SystemCategory** | string<br>(enum)<br><br>*read-only* | The category of the system based on discovery. *For the possible property values, see SystemCategory in Property Details.* |
| **SystemType** | string<br><br>*read-only* | The system type. |
| **TPMModuleType** | string<br><br>*read-only* | Gives the Module Type of TPM on the Server. |
| **TPMStatus** | string<br><br>*read-only* | Gives the Status of TPM on the Server. |
| **UUID** | string<br><br>*read-only* | The universal unique identifier for this system. |

### Property Details

### EncryptionSecurityState:


Indicates the Encryption Security State of the Server. 

| string |
| --- |
| Production | 
| HighSecurity | 
| FIPS | 

### HealthStatus:


This represents the health status of the system.

| string | Description |
| --- | --- |
| Critical | A critical condition exists that requires immediate attention |
| OK | Normal |
| Warning | A condition exists that requires attention |

### IndicatorLED:


The state of the indicator LED.

| string | Description |
| --- | --- |
| Blinking | The Indicator LED is blinking. |
| Lit | The Indicator LED is lit. |
| Off | The Indicator LED is off. |
| Unknown | The state of the Indicator LED cannot be determined. |

### PowerState:


This is the current power state of the system.

| string |
| --- |
| On | 
| Off | 
| Unknown | 
| Reset | 

### ServerPlatformType:


This property is the server platform type for this resource.

| string |
| --- |
| Edgeline | 
| Proliant | 
| Apollo | 
| Synergy | 

### State:


The state field indicates whether the server is staged/deployed etc.

| string | Description |
| --- | --- |
| Deployed | Server is successfully Deployed. |
| DeployFailed | Server deployment failed. |
| NotInitiated | No server update initiated. |
| Staged | Server is successfully Staged. |
| StageFailed | Server staging failed. |

### SystemCategory:


The category of the system based on discovery.

| string |
| --- |
| Discovered | 
| Managed | 
| NotReachable | 


## HpeWfmTaskExt

This is the schema definition for HpeWfmTaskExt.

|     |     |     |
| --- | --- | --- |
| **CreatedBy** | string<br><br>*read-only* | The name of the user that created this task. |
| **Description** | <br><br>*read-write* |  |
| **DetailedTaskLink** { | object | Detailed status of the task. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | <br><br>*read-write* |  |
| } |   |   |
| **History** | string<br><br>*read-only* | The history of the task. |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |
| **ProgressMessages** [ ] | array (string)<br><br>*read-only* | This is an array of messages associated with the task. |
| **ProgressPercent** | integer<br><br>*read-only* | The progress percent of this task. |
| **SelectedAddress** [ ] | array (string)<br><br>*read-only* | This is an array of IP addresses associated with the task. |
| **SelectedGroups** [ { | array | This is the list of the groups associated with the task, if any. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**allSystemsInGroup** | boolean<br><br>*read-only* | The flag suggests whether all the servers in the group are selected. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GroupName** | string<br><br>*read-only* | The Group name of the selected group. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SelectedAddress** [ ] | array (string)<br><br>*read-only* | This is an array of IP addresses selected within the group. |
| } ] |   |   |
| **SubTaskCount** | integer<br><br>*read-only* | Number of subtasks for this task. |
| **TaskIdentifier** | integer<br><br>*read-only* | A unique task identifier number for this task. |

## HpeWfmTaskServiceExt

This is the schema definition for HpeWfmTaskServiceExt.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **Name** | <br><br>*read-write* |  |

### Actions

### DeleteCompletedTasks


Delete all the completed Tasks.

**URIs**:


(This action takes no parameters.)


## HpeWfmUpdateJobResults

This is the schema definition for HpeWfmUpdateJobResults.

|     |     |     |
| --- | --- | --- |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **InstallSetInfo** { | object | The Install Set Details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InstallSetComponents** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BaselineName** | string<br><br>*read-write* | The Baseline name with which the server is updated. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentInfo** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ActiveVersion** | string<br><br>*read-write* | The component active version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AvailableVersion** | string<br><br>*read-write* | The component version available for update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentDescription** | string<br><br>*read-write* | The component description of the install component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentName** | string<br><br>*read-write* | The component name of the install component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ComponentType** | string<br><br>*read-write* | The component type(Firmware/Driver etc.) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CurrentVersion** | string<br><br>*read-write* | The component current version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DependencyFailed** | boolean<br><br>*read-write* | The component install dependency failed flag. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeploymentResult** | string<br><br>*read-write* | The result after the deployment. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InstalledVersion** | string<br><br>*read-write* | The final installed version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsForcedFlag** | boolean<br><br>*read-write* | The component isForced flag. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IsSelectedFlag** | boolean<br><br>*read-write* | The component isSelected flag. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PreviousInstalledVersion** | string<br><br>*read-write* | The previous installed version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProductFamilyName** | string<br><br>*read-write* | The component product family name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StagingResult** | string<br><br>*read-write* | The result after the staging. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StatusMessage** | string<br><br>*read-write* | The component install status message. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VersionInBaseline** | string<br><br>*read-write* | The previous installed version. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HostOSType** | string<br><br>*read-write* | The Host OS Type of the Managed Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerAddress** | string<br><br>*read-write* | The IP address Managed Server. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TotalErrors** | integer<br><br>*read-write* | Gives the total errors/failed dependencies during the calculate Install set for the Managed Node |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **Name** | <br><br>*read-write* |  |

## HpeWfmUpdateService

This is the schema definition for HpeWfmUpdateService.

|     |     |     |
| --- | --- | --- |
| **AddOnServiceStatusInfo** { | object | Status of add-on service installation and uninstallation action |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProgressPercent** | integer<br><br>*read-only* | The progress percentage of add-on service installation/uninstallation action. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State** | string<br><br>*read-only* | The state of add-on service installation/ uninstallation action. |
| } |   |   |
| **AddOnServicesUpdatesAvailable** | boolean<br><br>*read-only* | Indicates if add-on services updates are available. |
| **AddOnServicesUpdatesDismissed** | boolean<br><br>*read-write* | Indicates if add-on services updates have been disabled by the user. |
| **AutoUpdateFeatureEnabled** | boolean<br><br>*read-write* | Indicates if Automatic Self Update of iLO Amplifier Pack Feature is enabled by the user. |
| **AutoUpdatePackageInfo** { | object | The Automatic Self Update Firmware Package Details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BuildNumber** | integer<br><br>*read-only* | The build number of the firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Filename** | string<br><br>*read-only* | The Filename of the new firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinimumVersionString** | string<br><br>*read-only<br>(null)* | The minimum version string of the firmware required to perform the self update. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ReadmeLocation** { | object | The Automatic Self Update Firmware Package Readme file link location. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**extref** | string<br><br>*read-only* | The file path of the ReadMe file. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Recommendation** | string<br><br>*read-only* | The update recommendation of the new firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ReleaseDate** | string<br><br>*read-only* | The build date of the new firmware. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VersionString** | string<br><br>*read-only<br>(null)* | The version string of the firmware. This value might be null if VersionString is unavailable. |
| } |   |   |
| **AutoUpdateStatus** | string<br>(enum)<br><br>*read-only* | This property shows the current status of the automatic self update. *For the possible property values, see AutoUpdateStatus in Property Details.* |
| **AutoUpdateStatusErrorDetails** | string<br><br>*read-only<br>(null)* | Detailed string describing the auto self update status. |
| **Description** | <br><br>*read-write* |  |
| **Id** | <br><br>*read-write* |  |
| **MidwayConnectionStatus** | string<br>(enum)<br><br>*read-only* | This property shows the current status of the connection to HPE Midway from this device. *For the possible property values, see MidwayConnectionStatus in Property Details.* |
| **MidwayConnectionStatusErrorDetails** | string<br><br>*read-only<br>(null)* | Detailed error string in case of connection failure. |
| **Name** | <br><br>*read-write* |  |
| **ProgressPercent** | integer<br><br>*read-only* | The progress percentage of firmware update. |
| **SelfUpdateMethod** | string<br>(enum)<br><br>*read-write* | Specifies the Automatic Self Update Method *For the possible property values, see SelfUpdateMethod in Property Details.* |
| **State** | string<br>(enum)<br><br>*read-only* | The State of firmware update. *For the possible property values, see State in Property Details.* |

### Actions

### AddOnServiceInstallation




**URIs**:


(This action takes no parameters.)


### AddOnServiceUnInstallation


The uninstall action to uninstall the specified add-on service.

**URIs**:


(This action takes no parameters.)


### CheckForUpdates




**URIs**:


(This action takes no parameters.)


### ManagerUpdate




**URIs**:


(This action takes no parameters.)


### Property Details

### AutoUpdateStatus:


This property shows the current status of the automatic self update.

| string | Description |
| --- | --- |
| Already Up-to-date | iLO Amplifier Pack is already updated to the latest version. |
| Automatic Update Completed | Automatic update of iLO Amplifier Pack Completed. |
| Automatic Update In Progress | Automatic update of iLO Amplifier Pack In Progress. |
| Automatic Update Initiated | Automatic update of iLO Amplifier Pack Initiated. |
| New Update Available | New version of iLO Amplifier Pack is available for update. |
| Not Available | Update Status information not available. |

### MidwayConnectionStatus:


This property shows the current status of the connection to HPE Midway from this device.

| string | Description |
| --- | --- |
| Connected | Connection to HPE Midway was successful . |
| Connecting | Connection to HPE Midway is being attempted. |
| ConnectionFailed | Connection to HPE Midway failed. |
| NotInitiated | Connection to HPE Midway was not initiated. |

### SelfUpdateMethod:


Specifies the Automatic Self Update Method

| string |
| --- |
| CheckForUpdatesOnly | 
| FullAutomaticUpdate | 

### State:


The State of firmware update.

| string |
| --- |
| Idle | 
| In Progress | 
| Completed | 
| Error | 


## Job 1.0.1

|     |
| --- |
| *v1.0* |
| 2018.2 |
This resource contains information about a specific Job scheduled  or being executed by a Redfish service's Job Service.

**URIs**:

/redfish/v1/JobService/Jobs/*{JobId}*
/redfish/v1/JobService/Jobs/*{JobId}*/Steps/*{JobId2}*

|     |     |     |
| --- | --- | --- |
| **CreatedBy** | string<br><br>*read-only* | The person or program that created this job entry. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EndTime** | string<br><br>*read-only<br>(null)* | The date-time stamp that the job was completed. |
| **HidePayload** | boolean<br><br>*read-only* | Indicates that the contents of the Payload should be hidden from view after the Job has been created.  When set to True, the Payload object will not be returned on GET. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **JobState** | string<br>(enum)<br><br>*read-write* | The state of the job. *For the possible property values, see JobState in Property Details.* |
| **JobStatus** | string<br>(enum)<br><br>*read-only* | The status of the job. *For the possible property values, see JobStatus in Property Details.* |
| **MaxExecutionTime** | string<br><br>*read-write<br>(null)* | The maximum amount of time the job is allowed to execute. |
| **Messages** [ { } ] | array (object) | This is an array of messages associated with the job. This type describes a Message returned by the Redfish service. See the *Message* schema for details on this property. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Payload** { | object | The HTTP and JSON payload details for this job. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HttpHeaders** [ ] | array (string)<br><br>*read-only* | This represents the HTTP headers used in the operation of this job. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HttpOperation** | string<br><br>*read-only* | The HTTP operation to perform to execute this job. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**JsonBody** | string<br><br>*read-only* | This property contains the JSON payload to use in the execution of this Job. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TargetUri** | string<br><br>*read-only* | The URI of the target for this job. |
| } |   |   |
| **PercentComplete** | integer<br>(%)<br><br>*read-only<br>(null)* | The completion percentage of this job. |
| **Schedule** {} | object | The Schedule Settings for this Job. See the *Schedule* schema for details on this property. |
| **StartTime** | string<br><br>*read-only* | The date-time stamp that the job was started or is scheduled to start. |
| **StepOrder** [ ] | array (string)<br><br>*read-only* | This represents the serialized execution order of the Job Steps. |
| **Steps** { | object | A link to a collection of Steps for this Job. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Job*. See the Job schema for details. |
| } |   |   |

### Property Details

### JobState:


The state of the job.

| string | Description |
| --- | --- |
| Cancelled | Job was cancelled.. |
| Completed | Job has completed. |
| Continue | Job is to resume operation. |
| Exception | Job has stopped due to an exception condition. |
| Interrupted | Job has been interrupted. |
| New | A new job. |
| Pending | Job is pending and has not started. |
| Running | Job is running normally. |
| Service | Job is running as a service. |
| Starting | Job is starting. |
| Stopping | Job is in the process of stopping. |
| Suspended | Job has been suspended. |
| UserIntervention | Job is waiting for user intervention. |

### JobStatus:


The status of the job.

| string | Description |
| --- | --- |
| Critical | A critical condition exists that requires immediate attention. |
| OK | Normal. |
| Warning | A condition exists that requires attention. |


## JobService 1.0.0

This is the schema definition for the Job Service.  It represents the properties for the service itself and has links to the actual list of tasks.

**URIs**:

/redfish/v1/JobService

|     |     |     |
| --- | --- | --- |
| **DateTime** | string<br><br>*read-only<br>(null)* | The current DateTime (with offset) setting that the job service is using. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Jobs** { | object | References to the Jobs collection. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Job*. See the Job schema for details. |
| } |   |   |
| **Log** { | object | This is a reference to a Log Service used by the Job Service. See the *LogService* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a LogService resource. See the Links section and the *LogService* schema for details. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **ServiceCapabilities** { | object | This object describes the supported capabilities of this Job Service implementation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxJobs** | integer<br><br>*read-only<br>(null)* | Maximum number of Jobs supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxSteps** | integer<br><br>*read-only<br>(null)* | Maximum number of Job Steps supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Scheduling** | boolean<br><br>*read-only<br>(null)* | Indicates whether scheduling of Jobs is supported. |
| } |   |   |
| **ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled. |
| **Status** {} | object | This property describes the status and health of the resource and its children. See the *Resource* schema for details on this property. |

## JsonSchemaFile 1.1.0

This is the schema definition for the Schema File locator resource.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Languages** [ ] | array (string)<br><br>*read-only required* | Language codes for the schemas available. |
| **Location** [ { | array<br><br>* required* | Location information for this schema file. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ArchiveFile** | string<br><br>*read-only* | If the schema is hosted on the service in an archive file, this is the name of the file within the archive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ArchiveUri** | string<br><br>*read-only* | If the schema is hosted on the service in an archive file, this is the link to the archive file. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Language** | string<br><br>*read-only* | The language code for the file the schema is in. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PublicationUri** | string<br><br>*read-only* | Link to publicly available (canonical) URI for schema. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Uri** | string<br><br>*read-only* | Link to locally available URI for schema. |
| } ] |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Schema** | string<br><br>*read-only required* | The @odata.type name this schema describes. |

## LogEntry 1.3.0

This resource defines the record format for a log.  It is designed to be used for SEL logs (from IPMI) as well as Event Logs and OEM-specific log formats.  The EntryType field indicates the type of log and the resource includes several additional properties dependent on the EntryType.

|     |     |     |
| --- | --- | --- |
| **Created** | string<br><br>*read-only* | The time the log entry was created. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EntryCode** | string<br>(enum)<br><br>*read-only<br>(null)* | If the EntryType is SEL, this will have the entry code for the log entry. *For the possible property values, see EntryCode in Property Details.* |
| **EntryType** | string<br>(enum)<br><br>*read-only required* | his is the type of log entry. *For the possible property values, see EntryType in Property Details.* |
| **EventId** | string<br><br>*read-only* | This is a unique instance identifier of an event. |
| **EventTimestamp** | string<br><br>*read-only* | This is time the event occurred. |
| **EventType** | string<br>(enum)<br><br>*read-only* | This indicates the type of an event recorded in this log. *For the possible property values, see EventType in Property Details.* |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OriginOfCondition** { | object | This is the URI of the resource that caused the log entry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Message** | string<br><br>*read-only<br>(null)* | This property decodes from EntryType:  If it is Event then it is a message string.  Otherwise, it is SEL or Oem specific.  In most cases, this will be the actual Log Entry. |
| **MessageArgs** [ ] | array (string)<br><br>*read-only* | The values of this property shall be any arguments for the message. |
| **MessageId** | string<br><br>*read-only* | This property decodes from EntryType:  If it is Event then it is a message id.  Otherwise, it is SEL or Oem specific.  This value is only used for registries - for more information, see the specification. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **OemLogEntryCode** | string<br><br>*read-only<br>(null)* | If the LogEntryCode type is OEM, this will contain the OEM-specific entry code. |
| **OemRecordFormat** | string<br><br>*read-only<br>(null)* | If the entry type is Oem, this will contain more information about the record format from the Oem. |
| **OemSensorType** | string<br><br>*read-only<br>(null)* | If the Sensor Type is OEM, this will contain the OEM-specific sensor type. |
| **SensorNumber** | number<br><br>*read-only<br>(null)* | This property decodes from EntryType:  If it is SEL, it is the sensor number; if Event then the count of events.  Otherwise, it is Oem specific. |
| **SensorType** | string<br>(enum)<br><br>*read-only<br>(null)* | If the EntryType is SEL, this will have the sensor type that the log entry pertains to. *For the possible property values, see SensorType in Property Details.* |
| **Severity** | string<br>(enum)<br><br>*read-only<br>(null)* | This is the severity of the log entry. *For the possible property values, see Severity in Property Details.* |

### Property Details

### EntryCode:


If the EntryType is SEL, this will have the entry code for the log entry.

| string | Description |
| --- | --- |
| Assert | The condition has been asserted. |
| D0 Power State | The ACPI defined D0 Power State. |
| D1 Power State | The ACPI defined D1 Power State. |
| D2 Power State | The ACPI defined D2 Power State. |
| D3 Power State | The ACPI defined D3 Power State. |
| Deassert | The condition has been deasserted. |
| Device Disabled | A device has been disabled. |
| Device Enabled | A device has been enabled. |
| Device Inserted / Device Present | A device has been inserted or is now present. |
| Device Removed / Device Absent | A device has been removed or is now absent. |
| Fully Redundant | Indicates that full redundancy has been regained. |
| Informational | An Informational event. |
| Install Error | An Install Error has been detected. |
| Limit Exceeded | A limit has been exceeded. |
| Limit Not Exceeded | A limit has not been exceeded. |
| Lower Critical - going high | The reading crossed the Lower Critical threshold while going high. |
| Lower Critical - going low | The reading crossed the Lower Critical threshold while going low. |
| Lower Non-critical - going high | The reading crossed the Lower Non-critical threshold while going high. |
| Lower Non-critical - going low | The reading crossed the Lower Non-critical threshold while going low. |
| Lower Non-recoverable - going high | The reading crossed the Lower Non-recoverable threshold while going high. |
| Lower Non-recoverable - going low | The reading crossed the Lower Non-recoverable threshold while going low. |
| Monitor | A Monitor event. |
| Non-redundant:Insufficient Resources | Unit is non-redundant and has insufficient resource to maintain normal operation. |
| Non-redundant:Sufficient Resources from Insufficient Resources | Unit has regianed minimum resources needed for normal operation. |
| Non-redundant:Sufficient Resources from Redundant | Redundancy has been lost but unit is functioning with minimum resources needed for normal operation. |
| OEM | An OEM defined event. |
| Performance Lags | Performance does not meet expectations. |
| Performance Met | Performance meets expectations. |
| Predictive Failure asserted | A Predictive Failure has been detected. |
| Predictive Failure deasserted | A Predictive Failure is no longer present. |
| Redundancy Degraded | Redundancy still exists, but at less than full level. |
| Redundancy Degraded from Fully Redundant | Unit has lost some redundant resource(s) but is still in a redundant state. |
| Redundancy Degraded from Non-redundant | Unit has regained some resource(s) and is redundant but not fully redundant. |
| Redundancy Lost | Entered any non-redundant state, including Non-redundant: Insufficient Resources. |
| State Asserted | The state has been asserted. |
| State Deasserted | The state has been deasserted. |
| Transition to Active | The state transitioned to active. |
| Transition to Busy | The state transitioned to busy. |
| Transition to Critical from less severe | A state has changed to Critical from less severe. |
| Transition to Critical from Non-recoverable | A state has changed to Critical from Non-recoverable. |
| Transition to Degraded | A state has transitioned to Degraded. |
| Transition to Idle | The state transitioned to idle. |
| Transition to In Test | A state has transitioned to In Test. |
| Transition to Non-Critical from more severe | A state has changed to Non-Critical from more severe. |
| Transition to Non-Critical from OK | A state has changed to Non-Critical from OK. |
| Transition to Non-recoverable | A state has changed to Non-recoverable. |
| Transition to Non-recoverable from less severe | A state has changed to Non-recoverable from less severe. |
| Transition to Off Duty | A state has transitioned to Off Duty. |
| Transition to Off Line | A state has transitioned to Off Line. |
| Transition to OK | A state has changed to OK. |
| Transition to On Line | A state has transitioned to On Line. |
| Transition to Power Off | A state has transitioned to Power Off. |
| Transition to Power Save | A state has transitioned to Power Save. |
| Transition to Running | A state has transitioned to Running. |
| Upper Critical - going high | The reading crossed the Upper Critical threshold while going high. |
| Upper Critical - going low | The reading crossed the Upper Critical threshold while going low. |
| Upper Non-critical - going high | The reading crossed the Upper Non-critical threshold while going high. |
| Upper Non-critical - going low | The reading crossed the Upper Non-critical threshold while going low. |
| Upper Non-recoverable - going high | The reading crossed the Upper Non-recoverable threshold while going high. |
| Upper Non-recoverable - going low | The reading crossed the Upper Non-recoverable threshold while going low. |

### EntryType:


his is the type of log entry.

| string | Description |
| --- | --- |
| Event | Contains a Redfish-defined message (event). |
| Oem | Contains an entry in an OEM-defined format. |
| SEL | Contains a legacy IPMI System Event Log (SEL) entry. |

### EventType:


This indicates the type of an event recorded in this log.

| string | Description |
| --- | --- |
| Alert | A condition exists which requires attention. |
| ResourceAdded | A resource has been added. |
| ResourceRemoved | A resource has been removed. |
| ResourceUpdated | The value of this resource has been updated. |
| StatusChange | The status of this resource has changed. |

### SensorType:


If the EntryType is SEL, this will have the sensor type that the log entry pertains to.

| string | Description |
| --- | --- |
| Add-in Card | A sensor for an add-in card. |
| BaseOSBoot/InstallationStatus | A sensor for a base OS boot or installation status event. |
| Battery | A sensor for a battery. |
| Boot Error | A sensor for a boot error event. |
| Button/Switch | A sensor for a button or switch. |
| Cable/Interconnect | A sensor for a cable or interconnect type of device. |
| Chassis | A sensor for a chassis. |
| ChipSet | A sensor for a chipset. |
| CoolingDevice | A sensor for a cooling device. |
| Critical Interrupt | A sensor for a critical interrupt event. |
| Current | A current sensor. |
| Drive Slot/Bay | A sensor for a drive slot or bay. |
| Entity Presence | A sensor for an entity presence event. |
| Event Logging Disabled | A sensor for the event log. |
| Fan | A fan sensor. |
| FRUState | A sensor for a FRU state event. |
| LAN | A sensor for a LAN device. |
| Management Subsystem Health | A sensor for a management subsystem health event. |
| Memory | A sensor for a memory device. |
| Microcontroller/Coprocessor | A sensor for a microcontroller or coprocessor. |
| Module/Board | A sensor for a module or board. |
| Monitor ASIC/IC | A sensor for a monitor ASIC or IC. |
| OEM | An OEM defined sensor. |
| OS Stop/Shutdown | A sensor for an OS stop or shutdown event |
| Other FRU | A sensor for an other type of FRU. |
| Other Units-based Sensor | A sensor for a miscellaneous analog sensor. |
| Physical Chassis Security | A physical security sensor. |
| Platform Alert | A sensor for a platform alert event. |
| Platform Security Violation Attempt | A platform security sensor. |
| POST Memory Resize | A sensor for a POST memory resize event. |
| Power Supply / Converter | A sensor for a power supply or DC-to-DC converter. |
| PowerUnit | A sensor for a power unit. |
| Processor | A sensor for a processor. |
| Session Audit | A sensor for a session audit event. |
| Slot/Connector | A sensor for a slot or connector. |
| System ACPI PowerState | A sensor for an ACPI power state event. |
| System Event | A sensor for a system event. |
| System Firmware Progress | A sensor for a system firmware progress event. |
| SystemBoot/Restart | A sensor for a system boot or restart event. |
| Temperature | A temperature sensor. |
| Terminator | A sensor for a terminator. |
| Version Change | A sensor for a version change event. |
| Voltage | A voltage sensor. |
| Watchdog | A sensor for a watchdog event. |

### Severity:


This is the severity of the log entry.

| string | Description |
| --- | --- |
| Critical | A critical condition requiring immediate attention. |
| OK | Informational or operating normally. |
| Warning | A condition requiring attention. |


## LogService 1.1.0

This resource represents the log service for the resource or service to which it is associated.

|     |     |     |
| --- | --- | --- |
| **DateTime** | string<br><br>*read-write<br>(null)* | The current DateTime (with offset) for the log service, used to set or read time. |
| **DateTimeLocalOffset** | string<br><br>*read-write<br>(null)* | The time offset from UTC that the DateTime property is set to in format: +06:00 . |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Entries** { | object | References to the log entry collection. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *LogEntry*. See the LogEntry schema for details. |
| } |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **LogEntryType** | string<br>(enum)<br><br>*read-only<br>(null)* | The format of the Entries of this log. *For the possible property values, see LogEntryType in Property Details.* |
| **MaxNumberOfRecords** | number<br><br>*read-only* | The maximum number of log entries this service can have. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **OverWritePolicy** | string<br>(enum)<br><br>*read-only* | The overwrite policy for this service that takes place when the log is full. *For the possible property values, see OverWritePolicy in Property Details.* |
| **ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled. |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

### Actions

### ClearLog


This action is used to clear the log for this Log Service.

**URIs**:


(This action takes no parameters.)


### Property Details

### LogEntryType:


The format of the Entries of this log.

| string | Description |
| --- | --- |
| Event | The log contains Redfish-defined messages (events). |
| Multiple | The log contains multiple Log Entry types or a single entry type cannot be guaranteed by the Log Service. |
| OEM | The log contains entries in an OEM-defined format. |
| SEL | The log contains legacy IPMI System Event Log (SEL) entries. |

### OverWritePolicy:


The overwrite policy for this service that takes place when the log is full.

| string | Description |
| --- | --- |
| NeverOverWrites | When full, new entries to the Log will be discarded. |
| Unknown | The overwrite policy is not known or is undefined. |
| WrapsWhenFull | When full, new entries to the Log will overwrite previous entries. |


## Manager 1.4.0

This is the schema definition for a Manager.  Examples of managers are BMCs, Enclosure Managers, Management Controllers and other subsystems assigned managability functions.

|     |     |     |
| --- | --- | --- |
| **AutoDSTEnabled** | boolean<br><br>*read-write* | Indicates whether the manager is configured for automatic DST adjustment. |
| **CommandShell** { | object | Information about the Command Shell service provided by this manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ConnectTypesSupported** [ ] | array (string<br>(enum))<br><br>*read-only* | This object is used to enumerate the Command Shell connection types allowed by the implementation. *For the possible property values, see ConnectTypesSupported in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxConcurrentSessions** | number<br><br>*read-only* | Indicates the maximum number of service sessions, regardless of protocol, this manager is able to support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServiceEnabled** | boolean<br><br>*read-write* | Indicates if the service is enabled for this manager. |
| } |   |   |
| **DateTime** | string<br><br>*read-write<br>(null)* | The current DateTime (with offset) for the manager, used to set or read time. |
| **DateTimeLocalOffset** | string<br><br>*read-write<br>(null)* | The time offset from UTC that the DateTime property is set to in format: +06:00 . |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EthernetInterfaces** { | object | This is a reference to a collection of NICs that this manager uses for network communication.  It is here that clients will find NIC configuration options and settings. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *EthernetInterface*. See the EthernetInterface schema for details. |
| } |   |   |
| **FirmwareVersion** | string<br><br>*read-only<br>(null)* | The firmware version of this Manager. |
| **GraphicalConsole** { | object | The value of this property shall contain the information about the Graphical Console (KVM-IP) service of this manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ConnectTypesSupported** [ ] | array (string<br>(enum))<br><br>*read-only* | This object is used to enumerate the Graphical Console connection types allowed by the implementation. *For the possible property values, see ConnectTypesSupported in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxConcurrentSessions** | number<br><br>*read-only* | Indicates the maximum number of service sessions, regardless of protocol, this manager is able to support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServiceEnabled** | boolean<br><br>*read-write* | Indicates if the service is enabled for this manager. |
| } |   |   |
| **HostInterfaces** { | object | This is a reference to a collection of Host Interfaces that this manager uses for local host communication.  It is here that clients will find Host Interface configuration options and settings. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *HostInterface*. See the HostInterface schema for details. |
| } |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerForChassis** [ { | array | This property is an array of references to the chassis that this manager has control over. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerForServers** [ { | array | This property is an array of references to the systems that this manager has control over. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a ComputerSystem resource. See the Links section and the *ComputerSystem* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerForSwitches** [ { } ] | array (object) | This property is an array of references to the switches that this manager has control over. Switch contains properties describing a simple fabric switch. See the *Switch* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ManagerInChassis** { | object | This property is a reference to the chassis that this manager is located in. See the *Chassis* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **LogServices** { | object | This is a reference to a collection of Logs used by the manager. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *LogService*. See the LogService schema for details. |
| } |   |   |
| **ManagerType** | string<br>(enum)<br><br>*read-only* | This property represents the type of manager that this resource represents. *For the possible property values, see ManagerType in Property Details.* |
| **Model** | string<br><br>*read-only<br>(null)* | The model information of this Manager as defined by the manufacturer. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NetworkProtocol** { | object | This is a reference to the network services and their settings that the manager controls.  It is here that clients will find network configuration options as well as network services. See the *ManagerNetworkProtocol* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a ManagerNetworkProtocol resource. See the Links section and the *ManagerNetworkProtocol* schema for details. |
| } |   |   |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PowerState** | string<br>(enum)<br><br>*read-only<br>(null)* | This is the current power state of the Manager. *For the possible property values, see PowerState in Property Details.* |
| **Redundancy** [ { | array | Redundancy information for the managers of this system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } ] |   |   |
| **SerialConsole** { | object | Information about the Serial Console service provided by this manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ConnectTypesSupported** [ ] | array (string<br>(enum))<br><br>*read-only* | This object is used to enumerate the Serial Console connection types allowed by the implementation. *For the possible property values, see ConnectTypesSupported in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxConcurrentSessions** | number<br><br>*read-only* | Indicates the maximum number of service sessions, regardless of protocol, this manager is able to support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ServiceEnabled** | boolean<br><br>*read-write* | Indicates if the service is enabled for this manager. |
| } |   |   |
| **SerialInterfaces** { | object | This is a reference to a collection of serial interfaces that this manager uses for serial and console communication.  It is here that clients will find serial configuration options and settings. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *SerialInterface*. See the SerialInterface schema for details. |
| } |   |   |
| **ServiceEntryPointUUID** | string<br><br>*read-only<br>(null)* | The UUID of the Redfish Service provided by this manager. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **UUID** | string<br><br>*read-only<br>(null)* | The Universal Unique Identifier (UUID) for this Manager. |
| **VirtualMedia** { | object | This is a reference to the Virtual Media services for this particular manager. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *VirtualMedia*. See the VirtualMedia schema for details. |
| } |   |   |

### Actions

### ForceFailover


The ForceFailover action forces a failover of this manager to the manager used in the parameter.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NewManager** { | object | This parameter specifies the Manager in which to fail over.  In this case, a valid reference is supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another Manager resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |   |

### ModifyRedundancySet


The ModifyRedundancySet operation is used to add or remove members to a redundant group of manager.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Add** [ { | array | This array defines the Managers to add to the redundancy set.  In this case, a valid reference is supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another Manager resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Remove** [ { | array | This array defines the Managers to remove from the redundancy set.  In this case, a valid reference is supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another Manager resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |   |

### Reset


The reset action resets/reboots the manager.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResetType** | string<br>(enum)<br><br>*read-write* | This is the type of reset to be performed. *For the possible property values, see ResetType in Property Details.* |
| } |   |   |   |

### Property Details

### ConnectTypesSupported:


This object is used to enumerate the Serial Console connection types allowed by the implementation.

| string | Description |
| --- | --- |
| IPMI | The controller supports a Serial Console connection using the IPMI Serial-over-LAN (SOL) protocol. |
| Oem | The controller supports a Serial Console connection using an OEM-specific protocol. |
| SSH | The controller supports a Serial Console connection using the SSH protocol. |
| Telnet | The controller supports a Serial Console connection using the Telnet protocol. |

### ManagerType:


This property represents the type of manager that this resource represents.

| string | Description |
| --- | --- |
| AuxiliaryController | A controller which provides management functions for a particular subsystem or group of devices. |
| BMC | A controller which provides management functions for a single computer system. |
| EnclosureManager | A controller which provides management functions for a chassis or group of devices or systems. |
| ManagementController | A controller used primarily to monitor or manage the operation of a device or system. |
| RackManager | A controller which provides management functions for a whole or part of a rack. |
| Service | A software-based service which provides management functions. |

### PowerState:


This is the current power state of the Manager.

| string | Description |
| --- | --- |
| Off | The state is powered Off. |
| On | The state is powered On. |
| PoweringOff | A temporary state between On and Off. |
| PoweringOn | A temporary state between Off and On. |

### ResetType:


This is the type of reset to be performed.

| string | Description |
| --- | --- |
| ForceOff | Turn the unit off immediately (non-graceful shutdown). |
| ForceOn | Turn the unit on immediately. |
| ForceRestart | Perform an immediate (non-graceful) shutdown, followed by a restart. |
| GracefulRestart | Perform a graceful shutdown followed by a restart of the system. |
| GracefulShutdown | Perform a graceful shutdown and power off. |
| Nmi | Generate a Diagnostic Interrupt (usually an NMI on x86 systems) to cease normal operations, perform diagnostic actions and typically halt the system. |
| On | Turn the unit on. |
| PowerCycle | Perform a power cycle of the unit. |
| PushPowerButton | Simulate the pressing of the physical power button on this unit. |


## ManagerAccount 1.1.2

The user accounts, owned by a Manager, are defined in this resource.  Changes to a Manager Account may affect the current Redfish service connection if this manager is responsible for the Redfish service.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Enabled** | boolean<br><br>*read-write* | This property is used by a User Administrator to disable an account w/o having to delet the user information.  When set to true, the user can login.  When set to false, the account is administratively disabled and the user cannot login. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Role** { | object | A reference to the Role object defining Privileges for this account--returned when the resource is read. The ID of the role is the same as property RoleId. See the *Role* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Role resource. See the Links section and the *Role* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Locked** | boolean<br><br>*read-write* | This property indicates that the account has been auto-locked by the account service because the lockout threshold has been exceeded.  When set to true, the account is locked. A user admin can write the property to false to manually unlock, or the account service will unlock it once the lockout duration period has passed. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Password** | string<br><br>*read-write required on create<br>(null)* | This property is used with a PATCH or PUT to write the password for the account.  This property is null on a GET. |
| **RoleId** | string<br><br>*read-write required on create* | This property contains the Role for this account. |
| **UserName** | string<br><br>*read-write required on create* | This property contains the user name for the account. |

## ManagerNetworkProtocol 1.2.0

This resource is used to obtain or modify the network services managed by a given manager.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **DHCP** { | object | Settings for this Manager's DHCP protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **FQDN** | string<br><br>*read-only<br>(null)* | This is the fully qualified domain name for the manager obtained by DNS including the host name and top-level domain name. |
| **HostName** | string<br><br>*read-only<br>(null)* | The DNS Host Name of this manager, without any domain information. |
| **HTTP** { | object | Settings for this Manager's HTTP protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **HTTPS** { | object | Settings for this Manager's HTTPS protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **IPMI** { | object | Settings for this Manager's IPMI-over-LAN protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **KVMIP** { | object | Settings for this Manager's KVM-IP protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NTP** { | object | Settings for this Manager's NTP protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NTPServers** [ ] | array (string, null)<br><br>*read-write* | Indicates to which NTP servers this manager is subscribed. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **SNMP** { | object | Settings for this Manager's SNMP support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **SSDP** { | object | Settings for this Manager's SSDP support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NotifyIPv6Scope** | string<br>(enum)<br><br>*read-write<br>(null)* | Indicates the scope for the IPv6 Notify messages for SSDP. *For the possible property values, see NotifyIPv6Scope in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NotifyMulticastIntervalSeconds** | number<br>(seconds)<br><br>*read-write<br>(null)* | Indicates how often the Multicast is done from this service for SSDP. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NotifyTTL** | number<br><br>*read-write<br>(null)* | Indicates the time to live hop count for SSDPs Notify messages. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **SSH** { | object | Settings for this Manager's SSH (Secure Shell) protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **Telnet** { | object | Settings for this Manager's Telnet protocol support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |
| **VirtualMedia** { | object | Settings for this Manager's Virtual Media support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Port** | number<br><br>*read-write<br>(null)* | Indicates the protocol port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ProtocolEnabled** | boolean<br><br>*read-write<br>(null)* | Indicates if the protocol is enabled or disabled. |
| } |   |   |

### Property Details

### NotifyIPv6Scope:


Indicates the scope for the IPv6 Notify messages for SSDP.

| string | Description |
| --- | --- |
| Link | SSDP Notify messages are sent to addresses in the IPv6 Local Link scope. |
| Organization | SSDP Notify messages are sent to addresses in the IPv6 Local Organization scope. |
| Site | SSDP Notify messages are sent to addresses in the IPv6 Local Site scope. |


## Memory 1.5.0

This is the schema definition for definition of a Memory and its configuration.

|     |     |     |
| --- | --- | --- |
| **AllocationAlignmentMiB** | number<br><br>*read-only<br>(null)* | The boundary which memory regions are allocated on, measured in mebibytes (MiB). |
| **AllocationIncrementMiB** | number<br><br>*read-only<br>(null)* | The size of the smallest unit of allocation for a memory region in mebibytes (MiB). |
| **AllowedSpeedsMHz** [ ] | array (number)<br><br>*read-only* | Speed bins supported by this Memory. |
| **Assembly** {} | object | A reference to the Assembly resource associated with this memory. See the *Assembly* schema for details on this property. |
| **BaseModuleType** | string<br>(enum)<br><br>*read-only<br>(null)* | The base module type of Memory. *For the possible property values, see BaseModuleType in Property Details.* |
| **BusWidthBits** | number<br><br>*read-only<br>(null)* | Bus Width in bits. |
| **CacheSizeMiB** | number<br>(MiBy)<br><br>*read-only<br>(null)* | Total size of the cache portion memory in MiB. |
| **CapacityMiB** | number<br>(MiBy)<br><br>*read-only<br>(null)* | Memory Capacity in mebibytes (MiB). |
| **DataWidthBits** | number<br><br>*read-only<br>(null)* | Data Width in bits. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **DeviceID** | string<br><br>*read-only<br>(null)* | Device ID. |
| **DeviceLocator** | string<br><br>*read-only<br>(null)* | Location of the Memory in the platform. |
| **ErrorCorrection** | string<br>(enum)<br><br>*read-only<br>(null)* | Error correction scheme supported for this memory. *For the possible property values, see ErrorCorrection in Property Details.* |
| **FirmwareApiVersion** | string<br><br>*read-only<br>(null)* | Version of API supported by the firmware. |
| **FirmwareRevision** | string<br><br>*read-only<br>(null)* | Revision of firmware on the Memory controller. |
| **FunctionClasses** [ ] | array (string)<br><br>*read-only* | Function Classes by the Memory. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **IsRankSpareEnabled** | boolean<br><br>*read-only<br>(null)* | Rank spare enabled status. |
| **IsSpareDeviceEnabled** | boolean<br><br>*read-only<br>(null)* | Spare device enabled status. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Chassis** { | object | A reference to the Chassis which contains this Memory. See the *Chassis* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| **LogicalSizeMiB** | number<br>(MiBy)<br><br>*read-only<br>(null)* | Total size of the logical memory in MiB. |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | The Memory manufacturer. |
| **MaxTDPMilliWatts** [ ] | array (number)<br><br>*read-only* | Maximum TDPs in milli Watts. |
| **MemoryDeviceType** | string<br>(enum)<br><br>*read-only<br>(null)* | Type details of the Memory. *For the possible property values, see MemoryDeviceType in Property Details.* |
| **MemoryLocation** { | object | Memory connection information to sockets and memory controllers. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Channel** | number<br><br>*read-only<br>(null)* | Channel number in which Memory is connected. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemoryController** | number<br><br>*read-only<br>(null)* | Memory controller number in which Memory is connected. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Slot** | number<br><br>*read-only<br>(null)* | Slot number in which Memory is connected. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Socket** | number<br><br>*read-only<br>(null)* | Socket number in which Memory is connected. |
| } |   |   |
| **MemoryMedia** [ ] | array (string<br>(enum))<br><br>*read-only* | Media of this Memory. *For the possible property values, see MemoryMedia in Property Details.* |
| **MemorySubsystemControllerManufacturerID** | string<br><br>*read-only<br>(null)* | The manufacturer ID of the memory subsystem controller of this memory module. |
| **MemorySubsystemControllerProductID** | string<br><br>*read-only<br>(null)* | The product ID of the memory subsystem controller of this memory module. |
| **MemoryType** | string<br>(enum)<br><br>*read-only<br>(null)* | The type of Memory. *For the possible property values, see MemoryType in Property Details.* |
| **Metrics** { | object | A reference to the Metrics associated with this Memory. See the *MemoryMetrics* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a MemoryMetrics resource. See the Links section and the *MemoryMetrics* schema for details. |
| } |   |   |
| **ModuleManufacturerID** | string<br><br>*read-only<br>(null)* | The manufacturer ID of this memory module. |
| **ModuleProductID** | string<br><br>*read-only<br>(null)* | The product ID of this memory module. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NonVolatileSizeMiB** | number<br>(MiBy)<br><br>*read-only<br>(null)* | Total size of the non-volatile portion memory in MiB. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **OperatingMemoryModes** [ ] | array (string<br>(enum))<br><br>*read-only* | Memory modes supported by the Memory. *For the possible property values, see OperatingMemoryModes in Property Details.* |
| **OperatingSpeedMhz** | number<br><br>*read-only<br>(null)* | Operating speed of Memory in MHz or MT/s as appropriate. |
| **PartNumber** | string<br><br>*read-only<br>(null)* | The product part number of this device. |
| **PersistentRegionNumberLimit** | number<br><br>*read-only<br>(null)* | Total number of persistent regions this Memory can support. |
| **PersistentRegionSizeLimitMiB** | number<br><br>*read-only<br>(null)* | Total size of persistent regions in mebibytes (MiB). |
| **PersistentRegionSizeMaxMiB** | number<br><br>*read-only<br>(null)* | Maximum size of a single persistent region in mebibytes (MiB). |
| **PowerManagementPolicy** { | object | Power management policy information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AveragePowerBudgetMilliWatts** | number<br>(mW)<br><br>*read-only<br>(null)* | Average power budget in milli watts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxTDPMilliWatts** | number<br>(mW)<br><br>*read-only<br>(null)* | Maximum TDP in milli watts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PeakPowerBudgetMilliWatts** | number<br>(mW)<br><br>*read-only<br>(null)* | Peak power budget in milli watts. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PolicyEnabled** | boolean<br><br>*read-only<br>(null)* | Power management policy enabled status. |
| } |   |   |
| **RankCount** | number<br><br>*read-only<br>(null)* | Number of ranks available in the Memory. |
| **Regions** [ { | array | Memory regions information within the Memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemoryClassification** | string<br>(enum)<br><br>*read-only<br>(null)* | Classification of memory occupied by the given memory region. *For the possible property values, see MemoryClassification in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OffsetMiB** | number<br>(MiBy)<br><br>*read-only<br>(null)* | Offset with in the Memory that corresponds to the starting of this memory region in mebibytes (MiB). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PassphraseEnabled** | boolean<br><br>*read-only<br>(null)* | Indicates if the passphrase is enabled for this region. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PassphraseState** | boolean<br><br>*read-only<br>(null)* | State of the passphrase for this region. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RegionId** | string<br><br>*read-only<br>(null)* | Unique region ID representing a specific region within the Memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SizeMiB** | number<br>(MiBy)<br><br>*read-only<br>(null)* | Size of this memory region in mebibytes (MiB). |
| } ] |   |   |
| **SecurityCapabilities** { | object | This object contains security capabilities of the Memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxPassphraseCount** | number<br><br>*read-only<br>(null)* | Maximum number of passphrases supported for this Memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PassphraseCapable** | boolean<br><br>*read-only<br>(null)* | Memory passphrase set capability. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecurityStates** [ ] | array (string<br>(enum))<br><br>*read-only* | Security states supported by the Memory. *For the possible property values, see SecurityStates in Property Details.* |
| } |   |   |
| **SerialNumber** | string<br><br>*read-only<br>(null)* | The product serial number of this device. |
| **SpareDeviceCount** | number<br><br>*read-only<br>(null)* | Number of unused spare devices available in the Memory. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **SubsystemDeviceID** | string<br><br>*read-only<br>(null)* | Subsystem Device ID. |
| **SubsystemVendorID** | string<br><br>*read-only<br>(null)* | SubSystem Vendor ID. |
| **VendorID** | string<br><br>*read-only<br>(null)* | Vendor ID. |
| **VolatileRegionNumberLimit** | number<br><br>*read-only<br>(null)* | Total number of volatile regions this Memory can support. |
| **VolatileRegionSizeLimitMiB** | number<br><br>*read-only<br>(null)* | Total size of volatile regions in mebibytes (MiB). |
| **VolatileRegionSizeMaxMiB** | number<br><br>*read-only<br>(null)* | Maximum size of a single volatile region in mebibytes (MiB). |
| **VolatileSizeMiB** | number<br>(MiBy)<br><br>*read-only<br>(null)* | Total size of the volitile portion memory in MiB. |

### Actions

### DisablePassphrase


Disable passphrase for given regions.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Passphrase** | string<br><br>*read-write required* | Passphrase for doing the operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RegionId** | string<br><br>*read-write required* | Memory region ID for which this action to be applied. |
| } |   |   |   |

### SecureEraseUnit


This defines the action for securely erasing given regions.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Passphrase** | string<br><br>*read-write required* | Passphrase for doing the operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RegionId** | string<br><br>*read-write required* | Memory region ID for which this action to be applied. |
| } |   |   |   |

### SetPassphrase


Set passphrase for the given regions.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Passphrase** | string<br><br>*read-write required* | Passphrase for doing the operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RegionId** | string<br><br>*read-write required* | Memory region ID for which this action to be applied. |
| } |   |   |   |

### UnlockUnit


This defines the action for unlocking given regions.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Passphrase** | string<br><br>*read-write required* | Passphrase for doing the operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RegionId** | string<br><br>*read-write required* | Memory region ID for which this action to be applied. |
| } |   |   |   |

### Property Details

### BaseModuleType:


The base module type of Memory.

| string | Description |
| --- | --- |
| LRDIMM | Load Reduced. |
| Mini_RDIMM | Mini_RDIMM. |
| Mini_UDIMM | Mini_UDIMM. |
| RDIMM | Registered DIMM. |
| SO_DIMM | SO_DIMM. |
| SO_DIMM_16b | SO_DIMM_16b. |
| SO_DIMM_32b | SO_DIMM_32b. |
| SO_RDIMM_72b | SO_RDIMM_72b. |
| SO_UDIMM_72b | SO_UDIMM_72b. |
| UDIMM | UDIMM. |

### ErrorCorrection:


Error correction scheme supported for this memory.

| string | Description |
| --- | --- |
| AddressParity | Address Parity errors can be corrected. |
| MultiBitECC | Multi-bit Data errors can be corrected by ECC. |
| NoECC | No ECC available. |
| SingleBitECC | Single bit Data error can be corrected by ECC. |

### MemoryClassification:


Classification of memory occupied by the given memory region.

| string | Description |
| --- | --- |
| Block | Block accesible memory. |
| ByteAccessiblePersistent | Byte accessible persistent memory. |
| Volatile | Volatile memory. |

### MemoryDeviceType:


Type details of the Memory.

| string | Description |
| --- | --- |
| DDR | DDR. |
| DDR2 | DDR2. |
| DDR2_SDRAM | DDR2 SDRAM. |
| DDR2_SDRAM_FB_DIMM | DDR2 SDRAM FB_DIMM. |
| DDR2_SDRAM_FB_DIMM_PROBE | DDR2 SDRAM FB_DIMM PROBE. |
| DDR3 | DDR3. |
| DDR3_SDRAM | DDR3 SDRAM. |
| DDR4 | DDR4. |
| DDR4_SDRAM | DDR4 SDRAM. |
| DDR4E_SDRAM | DDR4E SDRAM. |
| DDR_SDRAM | DDR SDRAM. |
| DDR_SGRAM | DDR SGRAM. |
| EDO | EDO. |
| FastPageMode | Fast Page Mode. |
| Logical | Logical Non-volatile device. |
| LPDDR3_SDRAM | LPDDR3 SDRAM. |
| LPDDR4_SDRAM | LPDDR4 SDRAM. |
| PipelinedNibble | Pipelined Nibble. |
| ROM | ROM. |
| SDRAM | SDRAM. |

### MemoryMedia:


Media of this Memory.

| string | Description |
| --- | --- |
| DRAM | DRAM media. |
| NAND | NAND media. |
| Proprietary | Proprietary media. |

### MemoryType:


The type of Memory.

| string | Description |
| --- | --- |
| DRAM | The memory module is composed of volatile memory. |
| NVDIMM_F | The memory module is composed of non-volatile memory. |
| NVDIMM_N | The memory module is composed of volatile memory backed by non-volatile memory. |
| NVDIMM_P | The memory module is composed of a combination of non-volatile and volatile memory. |

### OperatingMemoryModes:


Memory modes supported by the Memory.

| string | Description |
| --- | --- |
| Block | Block accessible system memory. |
| PMEM | Persistent memory, byte accesible through system address space. |
| Volatile | Volatile memory. |

### SecurityStates:


Security states supported by the Memory.

| string | Description |
| --- | --- |
| Disabled | Secure mode is disabled. |
| Enabled | Secure mode is enabled. |
| Frozen | Secure state is frozen and can not be modified until reset. |
| Locked | Secure mode is enabled and access to the data is locked. |
| Passphraselimit | Number of attempts to unlock the Memory exceeded limit. |
| Unlocked | Secure mode is enabled and access to the data is unlocked. |


## MemoryDomain 1.2.0

This is the schema definition of a Memory Domain and its configuration. Memory Domains are used to indicate to the client which Memory (DIMMs) can be grouped together in Memory Chunks to form interleave sets or otherwise grouped together.

|     |     |     |
| --- | --- | --- |
| **AllowsBlockProvisioning** | boolean<br><br>*read-only<br>(null)* | Indicates if this Memory Domain supports the provisioning of blocks of memory. |
| **AllowsMemoryChunkCreation** | boolean<br><br>*read-only<br>(null)* | Indicates if this Memory Domain supports the creation of Memory Chunks. |
| **AllowsMirroring** | boolean<br><br>*read-only<br>(null)* | Indicates if this Memory Domain supports the creation of Memory Chunks with mirroring enabled. |
| **AllowsSparing** | boolean<br><br>*read-only<br>(null)* | Indicates if this Memory Domain supports the creation of Memory Chunks with sparing enabled. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **InterleavableMemorySets** [ { | array | This is the interleave sets for the memory chunk. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemorySet** [ { | array | This is the collection of memory for a particular interleave set. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Memory resource. See the Links section and the *Memory* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } ] |   |   |
| **MemoryChunks** { | object<br><br>*<br>(null)* | A reference to the collection of Memory Chunks associated with this Memory Domain. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *MemoryChunks*. See the MemoryChunks schema for details. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |

## MemoryMetrics 1.1.3

MemoryMetrics contains usage and health statistics for a single Memory module or device instance.

|     |     |     |
| --- | --- | --- |
| **BlockSizeBytes** | number<br>(Bytes)<br><br>*read-only<br>(null)* | Block size in bytes. |
| **CurrentPeriod** { | object | This object contains the Memory metrics since last reset or ClearCurrentPeriod action. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BlocksRead** | number<br><br>*read-only<br>(null)* | Number of blocks read since reset. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BlocksWritten** | number<br><br>*read-only<br>(null)* | Number of blocks written since reset. |
| } |   |   |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **HealthData** { | object | This object describes the health information of the memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AlarmTrips** { | object | Alarm trip information about the memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AddressParityError** | boolean<br><br>*read-only<br>(null)* | Address parity error detected status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CorrectableECCError** | boolean<br><br>*read-only<br>(null)* | Correctable data error threshold crossing alarm trip detected status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SpareBlock** | boolean<br><br>*read-only<br>(null)* | Spare block capacity crossing alarm trip detected status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Temperature** | boolean<br><br>*read-only<br>(null)* | Temperature threshold crossing alarm trip detected status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UncorrectableECCError** | boolean<br><br>*read-only<br>(null)* | Uncorrectable data error threshold crossing alarm trip detected status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DataLossDetected** | boolean<br><br>*read-only<br>(null)* | Data loss detection status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LastShutdownSuccess** | boolean<br><br>*read-only<br>(null)* | Status of last shutdown. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PerformanceDegraded** | boolean<br><br>*read-only<br>(null)* | Performance degraded mode status. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PredictedMediaLifeLeftPercent** | number<br><br>*read-only<br>(null)* | The percentage of reads and writes that are predicted to still be available for the media. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RemainingSpareBlockPercentage** | number<br><br>*read-only<br>(null)* | Remaining spare blocks in percentage. |
| } |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **LifeTime** { | object | This object contains the Memory metrics for the lifetime of the Memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BlocksRead** | number<br><br>*read-only<br>(null)* | Number of blocks read for the lifetime of the Memory. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BlocksWritten** | number<br><br>*read-only<br>(null)* | Number of blocks written for the lifetime of the Memory. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |

### Actions

### ClearCurrentPeriod


This sets the CurrentPeriod object values to zero.

**URIs**:


(This action takes no parameters.)


## MessageRegistry 1.1.1

This is the schema definition for all Message Registries.  It represents the properties for the registries themselves.  The MessageId is formed per the Redfish specification.  It consists of the RegistryPrefix concatenated with the version concatenated with the unique identifier for the message registry entry.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Language** | string<br><br>*read-only required* | This is the RFC 5646 compliant language code for the registry. |
| **Messages** { | object<br><br>* required* | The pattern property indicates that a free-form string is the unique identifier for the message within the registry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**(pattern)** { | object | Property names follow regular expression pattern "\[A\-Za\-z0\-9\]\+" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Description** | string<br><br>*read-only required* | This is a short description of how and when this message is to be used. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Message** | string<br><br>*read-only required* | The actual message. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NumberOfArgs** | number<br><br>*read-only required* | The number of arguments to be expected to be passed in as MessageArgs for this message. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ParamTypes** [ ] | array (string<br>(enum))<br><br>*read-only* | The MessageArg types, in order, for the message. *For the possible property values, see ParamTypes in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Resolution** | string<br><br>*read-only required* | Used to provide suggestions on how to resolve the situation that caused the error. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Severity** | string<br><br>*read-only required* | This is the severity of the message. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**(pattern)** {} [ ] | array, boolean, number, object, string<br><br>*<br>(null)* | Property names follow regular expression pattern "^\(\[a\-zA\-Z\_\]\[a\-zA\-Z0\-9\_\]\*\)?@\(odata\|Redfish\|Message\|Privileges\)\\\.\[a\-zA\-Z\_\]\[a\-zA\-Z0\-9\_\.\]\+$" |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **OwningEntity** | string<br><br>*read-only required* | This is the organization or company that publishes this registry. |
| **RegistryPrefix** | string<br><br>*read-only required* | This is the single word prefix used to form a messageID structure. |
| **RegistryVersion** | string<br><br>*read-only required* | This is the message registry version which is used in the middle portion of a messageID. |

### Property Details

### ParamTypes:


The MessageArg types, in order, for the message.

| string | Description |
| --- | --- |
| number | The parameter is a number. |
| string | The parameter is a string. |


## MessageRegistryFile 1.1.0

This is the schema definition for the Schema File locator resource.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Languages** [ ] | array (string)<br><br>*read-only required* | Language codes for the schemas available. |
| **Location** [ { | array<br><br>* required* | Location information for this schema file. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ArchiveFile** | string<br><br>*read-only* | If the schema is hosted on the service in an archive file, this is the name of the file within the archive. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ArchiveUri** | string<br><br>*read-only* | If the schema is hosted on the service in an archive file, this is the link to the archive file. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Language** | string<br><br>*read-only* | The language code for the file the schema is in. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PublicationUri** | string<br><br>*read-only* | Link to publicly available (canonical) URI for schema. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Uri** | string<br><br>*read-only* | Link to locally available URI for schema. |
| } ] |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Registry** | string<br><br>*read-only required* | The Registry Name, Major and Minor version used in MessageID construction. |

## NetworkAdapter 1.1.0

A NetworkAdapter represents the physical network adapter capable of connecting to a computer network.  Examples include but are not limited to Ethernet, Fibre Channel, and converged network adapters.

|     |     |     |
| --- | --- | --- |
| **Assembly** {} | object | A reference to the Assembly resource associated with this adapter. See the *Assembly* schema for details on this property. |
| **Controllers** [ { | array | The set of network controllers ASICs that make up this NetworkAdapter. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ControllerCapabilities** { | object<br><br>*<br>(null)* | The capabilities of this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DataCenterBridging** { | object<br><br>*<br>(null)* | Data Center Bridging (DCB) for this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Capable** | boolean<br><br>*read-only<br>(null)* | Whether this controller is capable of Data Center Bridging (DCB). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkDeviceFunctionCount** | number<br><br>*read-only<br>(null)* | The maximum number of physical functions available on this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkPortCount** | number<br><br>*read-only<br>(null)* | The number of physical ports on this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NPIV** { | object<br><br>*<br>(null)* | N_Port ID Virtualization (NPIV) capabilties for this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxDeviceLogins** | number<br><br>*read-only<br>(null)* | The maximum number of N_Port ID Virtualization (NPIV) logins allowed simultaneously from all ports on this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxPortLogins** | number<br><br>*read-only<br>(null)* | The maximum number of N_Port ID Virtualization (NPIV) logins allowed per physical port on this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VirtualizationOffload** { | object<br><br>*<br>(null)* | Virtualization offload for this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SRIOV** { | object<br><br>*<br>(null)* | Single-Root Input/Output Virtualization (SR-IOV) capabilities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SRIOVVEPACapable** | boolean<br><br>*read-only<br>(null)* | Whether this controller supports Single Root Input/Output Virtualization (SR-IOV) in Virtual Ethernet Port Aggregator (VEPA) mode. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VirtualFunction** { | object<br><br>*<br>(null)* | A virtual function of a controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeviceMaxCount** | number<br><br>*read-only<br>(null)* | The maximum number of Virtual Functions (VFs) supported by this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinAssignmentGroupSize** | number<br><br>*read-only<br>(null)* | The minimum number of Virtual Functions (VFs) that can be allocated or moved between physical functions for this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkPortMaxCount** | number<br><br>*read-only<br>(null)* | The maximum number of Virtual Functions (VFs) supported per network port for this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwarePackageVersion** | string<br><br>*read-only<br>(null)* | The version of the user-facing firmware package. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Links** { | object | Links. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkDeviceFunctions** [ { | array | Contains the members of this collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkDeviceFunction resource. See the Links section and the *NetworkDeviceFunction* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkPorts** [ { | array | Contains the members of this collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkPort resource. See the Links section and the *NetworkPort* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PCIeDevices** [ { | array | Contains the members of this collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeDevice resource. See the Links section and the *PCIeDevice* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| } ] |   |   |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | The manufacturer or OEM of this network adapter. |
| **Model** | string<br><br>*read-only<br>(null)* | The model string for this network adapter. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NetworkDeviceFunctions** { | object | Contains the members of this collection. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *NetworkDeviceFunction*. See the NetworkDeviceFunction schema for details. |
| } |   |   |
| **NetworkPorts** { | object | Contains the members of this collection. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *NetworkPort*. See the NetworkPort schema for details. |
| } |   |   |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PartNumber** | string<br><br>*read-only<br>(null)* | Part number for this network adapter. |
| **SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number for this network adapter. |
| **SKU** | string<br><br>*read-only<br>(null)* | The manufacturer SKU for this network adapter. |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

### Actions

### ResetSettingsToDefault


This action is to clear the settings back to factory defaults.

**URIs**:


(This action takes no parameters.)


## NetworkDeviceFunction 1.2.1

A Network Device Function represents a logical interface exposed by the network adapter.

|     |     |     |
| --- | --- | --- |
| **AssignablePhysicalPorts** [ { | array | The array of physical port references that this network device function may be assigned to. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkPort resource. See the Links section and the *NetworkPort* schema for details. |
| } ] |   |   |
| **BootMode** | string<br>(enum)<br><br>*read-write<br>(null)* | The boot mode configured for this network device function. *For the possible property values, see BootMode in Property Details.* |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **DeviceEnabled** | boolean<br><br>*read-write<br>(null)* | Whether the network device function is enabled. |
| **Ethernet** { | object<br><br>*<br>(null)* | Ethernet. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MACAddress** | string<br><br>*read-write<br>(null)* | This is the currently configured MAC address of the (logical port) network device function. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MTUSize** | number<br><br>*read-write<br>(null)* | The Maximum Transmission Unit (MTU) configured for this network device function. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PermanentMACAddress** | string<br><br>*read-only<br>(null)* | This is the permanent MAC address assigned to this network device function (physical function). |
| } |   |   |
| **FibreChannel** { | object<br><br>*<br>(null)* | Fibre Channel. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AllowFIPVLANDiscovery** | boolean<br><br>*read-write<br>(null)* | Whether the FCoE Initialization Protocol (FIP) is used for populating the FCoE VLAN Id. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootTargets** [ { | array | An array of Fibre Channel boot targets configured for this network device function. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**BootPriority** | number<br><br>*read-write<br>(null)* | The relative priority for this entry in the boot targets array. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LUNID** | string<br><br>*read-write<br>(null)* | The Logical Unit Number (LUN) ID to boot from on the device referred to by the corresponding WWPN. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WWPN** | string<br><br>*read-write<br>(null)* | The World-Wide Port Name to boot from. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FCoEActiveVLANId** | number<br><br>*read-only<br>(null)* | The active FCoE VLAN ID. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FCoELocalVLANId** | number<br><br>*read-write<br>(null)* | The locally configured FCoE VLAN ID. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PermanentWWNN** | string<br><br>*read-only<br>(null)* | This is the permanent WWNN address assigned to this network device function (physical function). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PermanentWWPN** | string<br><br>*read-only<br>(null)* | This is the permanent WWPN address assigned to this network device function (physical function). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WWNN** | string<br><br>*read-write<br>(null)* | This is the currently configured WWNN address of the network device function (physical function). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WWNSource** | string<br>(enum)<br><br>*read-write<br>(null)* | The configuration source of the WWNs for this connection (WWPN and WWNN). *For the possible property values, see WWNSource in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WWPN** | string<br><br>*read-write<br>(null)* | This is the currently configured WWPN address of the network device function (physical function). |
| } |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **iSCSIBoot** { | object<br><br>*<br>(null)* | iSCSI Boot. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AuthenticationMethod** | string<br>(enum)<br><br>*read-write<br>(null)* | The iSCSI boot authentication method for this network device function. *For the possible property values, see AuthenticationMethod in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CHAPSecret** | string<br><br>*read-write<br>(null)* | The shared secret for CHAP authentication. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CHAPUsername** | string<br><br>*read-write<br>(null)* | The username for CHAP authentication. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InitiatorDefaultGateway** | string<br><br>*read-write<br>(null)* | The IPv6 or IPv4 iSCSI boot default gateway. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InitiatorIPAddress** | string<br><br>*read-write<br>(null)* | The IPv6 or IPv4 address of the iSCSI initiator. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InitiatorName** | string<br><br>*read-write<br>(null)* | The iSCSI initiator name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InitiatorNetmask** | string<br><br>*read-write<br>(null)* | The IPv6 or IPv4 netmask of the iSCSI boot initiator. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPAddressType** | string<br>(enum)<br><br>*read-write<br>(null)* | The type of IP address (IPv6 or IPv4) being populated in the iSCSIBoot IP address fields. *For the possible property values, see IPAddressType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IPMaskDNSViaDHCP** | boolean<br><br>*read-write<br>(null)* | Whether the iSCSI boot initiator uses DHCP to obtain the iniator name, IP address, and netmask. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MutualCHAPSecret** | string<br><br>*read-write<br>(null)* | The CHAP Secret for 2-way CHAP authentication. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MutualCHAPUsername** | string<br><br>*read-write<br>(null)* | The CHAP Username for 2-way CHAP authentication. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryDNS** | string<br><br>*read-write<br>(null)* | The IPv6 or IPv4 address of the primary DNS server for the iSCSI boot initiator. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryLUN** | number<br><br>*read-write<br>(null)* | The logical unit number (LUN) for the primary iSCSI boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryTargetIPAddress** | string<br><br>*read-write<br>(null)* | The IP address (IPv6 or IPv4) for the primary iSCSI boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryTargetName** | string<br><br>*read-write<br>(null)* | The name of the iSCSI primary boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryTargetTCPPort** | number<br><br>*read-write<br>(null)* | The TCP port for the primary iSCSI boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryVLANEnable** | boolean<br><br>*read-write<br>(null)* | This indicates if the primary VLAN is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PrimaryVLANId** | number<br><br>*read-write<br>(null)* | The 802.1q VLAN ID to use for iSCSI boot from the primary target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RouterAdvertisementEnabled** | boolean<br><br>*read-write<br>(null)* | Whether IPv6 router advertisement is enabled for the iSCSI boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryDNS** | string<br><br>*read-write<br>(null)* | The IPv6 or IPv4 address of the secondary DNS server for the iSCSI boot initiator. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryLUN** | number<br><br>*read-write<br>(null)* | The logical unit number (LUN) for the secondary iSCSI boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryTargetIPAddress** | string<br><br>*read-write<br>(null)* | The IP address (IPv6 or IPv4) for the secondary iSCSI boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryTargetName** | string<br><br>*read-write<br>(null)* | The name of the iSCSI secondary boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryTargetTCPPort** | number<br><br>*read-write<br>(null)* | The TCP port for the secondary iSCSI boot target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryVLANEnable** | boolean<br><br>*read-write<br>(null)* | This indicates if the secondary VLAN is enabled. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SecondaryVLANId** | number<br><br>*read-write<br>(null)* | The 802.1q VLAN ID to use for iSCSI boot from the secondary target. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TargetInfoViaDHCP** | boolean<br><br>*read-write<br>(null)* | Whether the iSCSI boot target name, LUN, IP address, and netmask should be obtained from DHCP. |
| } |   |   |
| **Links** { | object | Links. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Endpoints** [ { } ] | array (object) | An array of references to endpoints associated with this network device function. This is the schema definition for the Endpoint resource. It represents the properties of an entity that sends or receives protocol defined messages over a transport. See the *Endpoint* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PCIeFunction** { | object | Contains the members of this collection. See the *PCIeFunction* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeFunction resource. See the Links section and the *PCIeFunction* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **MaxVirtualFunctions** | number<br><br>*read-only<br>(null)* | The number of virtual functions (VFs) that are available for this Network Device Function. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NetDevFuncCapabilities** [ ] | array (string<br>(enum))<br><br>*read-only<br>(null)* | Capabilities of this network device function. *For the possible property values, see NetDevFuncCapabilities in Property Details.* |
| **NetDevFuncType** | string<br>(enum)<br><br>*read-write<br>(null)* | The configured capability of this network device function. *For the possible property values, see NetDevFuncType in Property Details.* |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PhysicalPortAssignment** { | object | The physical port that this network device function is currently assigned to. See the *NetworkPort* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkPort resource. See the Links section and the *NetworkPort* schema for details. |
| } |   |   |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **VirtualFunctionsEnabled** | boolean<br><br>*read-only<br>(null)* | Whether Single Root I/O Virtualization (SR-IOV) Virual Functions (VFs) are enabled for this Network Device Function. |

### Property Details

### AuthenticationMethod:


The iSCSI boot authentication method for this network device function.

| string | Description |
| --- | --- |
| CHAP | iSCSI Challenge Handshake Authentication Protocol (CHAP) authentication is used. |
| MutualCHAP | iSCSI Mutual Challenge Handshake Authentication Protocol (CHAP) authentication is used. |
| None | No iSCSI authentication is used. |

### BootMode:


The boot mode configured for this network device function.

| string | Description |
| --- | --- |
| Disabled | Do not indicate to UEFI/BIOS that this device is bootable. |
| FibreChannel | Boot this device using the embedded Fibre Channel support and configuration.  Only applicable if the NetworkDeviceFunctionType is set to FibreChannel. |
| FibreChannelOverEthernet | Boot this device using the embedded Fibre Channel over Ethernet (FCoE) boot support and configuration.  Only applicable if the NetworkDeviceFunctionType is set to FibreChannelOverEthernet. |
| iSCSI | Boot this device using the embedded iSCSI boot support and configuration.  Only applicable if the NetworkDeviceFunctionType is set to iSCSI. |
| PXE | Boot this device using the embedded PXE support.  Only applicable if the NetworkDeviceFunctionType is set to Ethernet. |

### IPAddressType:


The type of IP address (IPv6 or IPv4) being populated in the iSCSIBoot IP address fields.

| string | Description |
| --- | --- |
| IPv4 | IPv4 addressing is used for all IP-fields in this object. |
| IPv6 | IPv6 addressing is used for all IP-fields in this object. |

### NetDevFuncCapabilities:


Capabilities of this network device function.

| string | Description |
| --- | --- |
| Disabled | Neither enumerated nor visible to the operating system. |
| Ethernet | Appears to the operating system as an Ethernet device. |
| FibreChannel | Appears to the operating system as a Fibre Channel device. |
| FibreChannelOverEthernet | Appears to the operating system as an FCoE device. |
| iSCSI | Appears to the operating system as an iSCSI device. |

### NetDevFuncType:


The configured capability of this network device function.

| string | Description |
| --- | --- |
| Disabled | Neither enumerated nor visible to the operating system. |
| Ethernet | Appears to the operating system as an Ethernet device. |
| FibreChannel | Appears to the operating system as a Fibre Channel device. |
| FibreChannelOverEthernet | Appears to the operating system as an FCoE device. |
| iSCSI | Appears to the operating system as an iSCSI device. |

### WWNSource:


The configuration source of the WWNs for this connection (WWPN and WWNN).

| string | Description |
| --- | --- |
| ConfiguredLocally | The set of FC/FCoE boot targets was applied locally through API or UI. |
| ProvidedByFabric | The set of FC/FCoE boot targets was applied by the Fibre Channel fabric. |


## NetworkInterface 1.1.0

A NetworkInterface contains references linking NetworkAdapter, NetworkPort, and NetworkDeviceFunction resources and represents the functionality available to the containing system.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | Links. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkAdapter** { | object | Contains the members of this collection. See the *NetworkAdapter* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkAdapter resource. See the Links section and the *NetworkAdapter* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NetworkDeviceFunctions** { | object | Contains the members of this collection. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *NetworkDeviceFunction*. See the NetworkDeviceFunction schema for details. |
| } |   |   |
| **NetworkPorts** { | object | Contains the members of this collection. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *NetworkPort*. See the NetworkPort schema for details. |
| } |   |   |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

## NetworkPort 1.1.0

A Network Port represents a discrete physical port capable of connecting to a network.

|     |     |     |
| --- | --- | --- |
| **ActiveLinkTechnology** | string<br>(enum)<br><br>*read-write<br>(null)* | Network Port Active Link Technology. *For the possible property values, see ActiveLinkTechnology in Property Details.* |
| **AssociatedNetworkAddresses** [ ] | array (string, null)<br><br>*read-only* | The array of configured network addresses (MAC or WWN) that are associated with this Network Port, including the programmed address of the lowest numbered Network Device Function, the configured but not active address if applicable, the address for hardware port teaming, or other network addresses. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EEEEnabled** | boolean<br><br>*read-write<br>(null)* | Whether IEEE 802.3az Energy Efficient Ethernet (EEE) is enabled for this network port. |
| **FlowControlConfiguration** | string<br>(enum)<br><br>*read-write<br>(null)* | The locally configured 802.3x flow control setting for this network port. *For the possible property values, see FlowControlConfiguration in Property Details.* |
| **FlowControlStatus** | string<br>(enum)<br><br>*read-only<br>(null)* | The 802.3x flow control behavior negotiated with the link partner for this network port (Ethernet-only). *For the possible property values, see FlowControlStatus in Property Details.* |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **LinkStatus** | string<br>(enum)<br><br>*read-only<br>(null)* | The status of the link between this port and its link partner. *For the possible property values, see LinkStatus in Property Details.* |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **NetDevFuncMaxBWAlloc** [ { | array | The array of maximum bandwidth allocation percentages for the Network Device Functions associated with this port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxBWAllocPercent** | number<br><br>*read-write<br>(null)* | The maximum bandwidth allocation percentage allocated to the corresponding network device function instance. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkDeviceFunction** { | object | Contains the members of this collection. See the *NetworkDeviceFunction* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkDeviceFunction resource. See the Links section and the *NetworkDeviceFunction* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } ] |   |   |
| **NetDevFuncMinBWAlloc** [ { | array | The array of minimum bandwidth allocation percentages for the Network Device Functions associated with this port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinBWAllocPercent** | number<br><br>*read-write<br>(null)* | The minimum bandwidth allocation percentage allocated to the corresponding network device function instance. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkDeviceFunction** { | object | Contains the members of this collection. See the *NetworkDeviceFunction* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkDeviceFunction resource. See the Links section and the *NetworkDeviceFunction* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } ] |   |   |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PhysicalPortNumber** | string<br><br>*read-only<br>(null)* | The physical port number label for this port. |
| **PortMaximumMTU** | number<br><br>*read-only<br>(null)* | The largest maximum transmission unit (MTU) that can be configured for this network port. |
| **SignalDetected** | boolean<br><br>*read-only<br>(null)* | Whether or not the port has detected enough signal on enough lanes to establish link. |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **SupportedEthernetCapabilities** [ ] | array (string<br>(enum))<br><br>*read-only<br>(null)* | The set of Ethernet capabilities that this port supports. *For the possible property values, see SupportedEthernetCapabilities in Property Details.* |
| **SupportedLinkCapabilities** [ { | array | The self-described link capabilities of this port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LinkNetworkTechnology** | string<br>(enum)<br><br>*read-only<br>(null)* | The self-described link network technology capabilities of this port. *For the possible property values, see LinkNetworkTechnology in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LinkSpeedMbps** | number<br><br>*read-only<br>(null)* | The speed of the link in Mbps when this link network technology is active. |
| } ] |   |   |
| **WakeOnLANEnabled** | boolean<br><br>*read-write<br>(null)* | Whether Wake on LAN (WoL) is enabled for this network port. |

### Property Details

### ActiveLinkTechnology:


Network Port Active Link Technology.

| string | Description |
| --- | --- |
| Ethernet | The port is capable of connecting to an Ethernet network. |
| FibreChannel | The port is capable of connecting to a Fibre Channel network. |
| InfiniBand | The port is capable of connecting to an InfiniBand network. |

### FlowControlConfiguration:


The locally configured 802.3x flow control setting for this network port.

| string | Description |
| --- | --- |
| None | No IEEE 802.3x flow control is enabled on this port. |
| RX | IEEE 802.3x flow control may be initiated by the link partner. |
| TX | IEEE 802.3x flow control may be initiated by this station. |
| TX_RX | IEEE 802.3x flow control may be initiated by this station or the link partner. |

### FlowControlStatus:


The 802.3x flow control behavior negotiated with the link partner for this network port (Ethernet-only).

| string | Description |
| --- | --- |
| None | No IEEE 802.3x flow control is enabled on this port. |
| RX | IEEE 802.3x flow control may be initiated by the link partner. |
| TX | IEEE 802.3x flow control may be initiated by this station. |
| TX_RX | IEEE 802.3x flow control may be initiated by this station or the link partner. |

### LinkNetworkTechnology:


The self-described link network technology capabilities of this port.

| string | Description |
| --- | --- |
| Ethernet | The port is capable of connecting to an Ethernet network. |
| FibreChannel | The port is capable of connecting to a Fibre Channel network. |
| InfiniBand | The port is capable of connecting to an InfiniBand network. |

### LinkStatus:


The status of the link between this port and its link partner.

| string | Description |
| --- | --- |
| Down | The port is enabled but link is down. |
| Up | The port is enabled and link is good (up). |

### SupportedEthernetCapabilities:


The set of Ethernet capabilities that this port supports.

| string | Description |
| --- | --- |
| EEE | IEEE 802.3az Energy Efficient Ethernet (EEE) is supported on this port. |
| WakeOnLAN | Wake on LAN (WoL) is supported on this port. |


## PCIeDevice 1.2.0

This is the schema definition for the PCIeDevice resource.  It represents the properties of a PCIeDevice attached to a System.

|     |     |     |
| --- | --- | --- |
| **Assembly** {} | object | A reference to the Assembly resource associated with this PCIe device. See the *Assembly* schema for details on this property. |
| **AssetTag** | string<br><br>*read-write<br>(null)* | The user assigned asset tag for this PCIe device. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **DeviceType** | string<br>(enum)<br><br>*read-only* | The device type for this PCIe device. *For the possible property values, see DeviceType in Property Details.* |
| **FirmwareVersion** | string<br><br>*read-only<br>(null)* | The version of firmware for this PCIe device. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | The links object contains the links to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Chassis** [ { | array | An array of references to the chassis in which the PCIe device is contained. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PCIeFunctions** [ { | array | An array of references to PCIeFunctions exposed by this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeFunction resource. See the Links section and the *PCIeFunction* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | This is the manufacturer of this PCIe device. |
| **Model** | string<br><br>*read-only<br>(null)* | This is the model number for the PCIe device. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PartNumber** | string<br><br>*read-only<br>(null)* | The part number for this PCIe device. |
| **SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number for this PCIe device. |
| **SKU** | string<br><br>*read-only<br>(null)* | This is the SKU for this PCIe device. |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

### Property Details

### DeviceType:


The device type for this PCIe device.

| string | Description |
| --- | --- |
| MultiFunction | A multi-function PCIe device. |
| Simulated | A PCIe device which is not currently physically present, but is being simulated by the PCIe infrastructure. |
| SingleFunction | A single-function PCIe device. |


## PCIeFunction 1.2.0

This is the schema definition for the PCIeFunction resource.  It represents the properties of a PCIeFunction attached to a System.

|     |     |     |
| --- | --- | --- |
| **ClassCode** | string<br><br>*read-only<br>(null)* | The Class Code of this PCIe function. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **DeviceClass** | string<br>(enum)<br><br>*read-only* | The class for this PCIe Function. *For the possible property values, see DeviceClass in Property Details.* |
| **DeviceId** | string<br><br>*read-only<br>(null)* | The Device ID of this PCIe function. |
| **FunctionId** | number<br><br>*read-only<br>(null)* | The the PCIe Function identifier. |
| **FunctionType** | string<br>(enum)<br><br>*read-only* | The type of the PCIe Function. *For the possible property values, see FunctionType in Property Details.* |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | The links object contains the links to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Drives** [ { | array | An array of references to the drives which the PCIe device produces. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Drive resource. See the Links section and the *Drive* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EthernetInterfaces** [ { | array | An array of references to the ethernet interfaces which the PCIe device produces. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a EthernetInterface resource. See the Links section and the *EthernetInterface* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NetworkDeviceFunctions** [ { | array | An array of references to the Network Device Functions which the PCIe device produces. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a NetworkDeviceFunction resource. See the Links section and the *NetworkDeviceFunction* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PCIeDevice** { | object<br><br>*<br>(null)* | A reference to the PCIeDevice on which this function resides. See the *PCIeDevice* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeDevice resource. See the Links section and the *PCIeDevice* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StorageControllers** [ { | array | An array of references to the storage controllers which the PCIe device produces. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a StorageController resource. See the Links section and the *Storage* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **RevisionId** | string<br><br>*read-only<br>(null)* | The Revision ID of this PCIe function. |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **SubsystemId** | string<br><br>*read-only<br>(null)* | The Subsystem ID of this PCIe function. |
| **SubsystemVendorId** | string<br><br>*read-only<br>(null)* | The Subsystem Vendor ID of this PCIe function. |
| **VendorId** | string<br><br>*read-only<br>(null)* | The Vendor ID of this PCIe function. |

### Property Details

### DeviceClass:


The class for this PCIe Function.

| string | Description |
| --- | --- |
| Bridge | A bridge. |
| CommunicationController | A communication controller. |
| Coprocessor | A coprocessor. |
| DisplayController | A display controller. |
| DockingStation | A docking station. |
| EncryptionController | An encryption controller. |
| GenericSystemPeripheral | A generic system peripheral. |
| InputDeviceController | An input device controller. |
| IntelligentController | An intelligent controller. |
| MassStorageController | A mass storage controller. |
| MemoryController | A memory controller. |
| MultimediaController | A multimedia controller. |
| NetworkController | A network controller. |
| NonEssentialInstrumentation | A non-essential instrumentation. |
| Other | A other class. The function Device Class Id needs to be verified. |
| ProcessingAccelerators | A processing accelerators. |
| Processor | A processor. |
| SatelliteCommunicationsController | A satellite communications controller. |
| SerialBusController | A serial bus controller. |
| SignalProcessingController | A signal processing controller. |
| UnassignedClass | An unassigned class. |
| UnclassifiedDevice | An unclassified device. |
| WirelessController | A wireless controller. |

### FunctionType:


The type of the PCIe Function.

| string | Description |
| --- | --- |
| Physical | A physical PCie function. |
| Virtual | A virtual PCIe function. |


## PCIeSlots 1.0.0

This is the schema definition for the PCIe Slot properties.

**URIs**:

/redfish/v1/Chassis/*{ChassisId}*/PCIeSlots

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Slots** [ { | array | An array of PCI Slot information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Lanes** | integer<br><br>*read-only<br>(null)* | This is the number of PCIe lanes supported by this slot. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Links** { | object<br><br>*<br>(null)* | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PCIeDevice** [ { | array | An array of references to the PCIe Devices contained in this slot. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a PCIeDevice resource. See the Links section and the *PCIeDevice* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** {} | object | The Location of the PCIe slot. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PCIeType** | <br><br>*read-only<br>(null)* | This is the PCIe specification supported by this slot. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SlotType** | string<br>(enum)<br><br>*read-only<br>(null)* | This is the PCIe slot type for this slot. *For the possible property values, see SlotType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This property describes the status and health of the resource and its children. See the *Resource* schema for details on this property. |
| } ] |   |   |

### Property Details

### SlotType:


This is the PCIe slot type for this slot.

| string | Description |
| --- | --- |
| FullLength | Full-Length PCIe slot. |
| HalfLength | Half-Length PCIe slot. |
| LowProfile | Low-Profile or Slim PCIe slot. |
| M2 | PCIe M.2 slot. |
| Mini | Mini PCIe slot. |
| OEM | And OEM-specific slot. |


## Port 1.1.0

Port contains properties describing a port of a switch.

|     |     |     |
| --- | --- | --- |
| **CurrentSpeedGbps** | number<br>(Gbit/s)<br><br>*read-only<br>(null)* | The current speed of this port. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AssociatedEndpoints** [ { } ] | array (object) | An array of references to the endpoints that connect to the switch through this port. This is the schema definition for the Endpoint resource. It represents the properties of an entity that sends or receives protocol defined messages over a transport. See the *Endpoint* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ConnectedSwitches** [ { } ] | array (object) | An array of references to the switches that connect to the switch through this port. Switch contains properties describing a simple fabric switch. See the *Switch* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ConnectedSwitchPorts** [ { | array | An array of references to the ports that connect to the switch through this port. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to another Port resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| **MaxSpeedGbps** | number<br>(Gbit/s)<br><br>*read-only<br>(null)* | The maximum speed of this port as currently configured. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PortId** | string<br><br>*read-only<br>(null)* | This is the label of this port on the physical switch package. |
| **PortProtocol** | string<br>(enum)<br><br>*read-only<br>(null)* | The protocol being sent over this port. *For the possible property values, see PortProtocol in Property Details.* |
| **PortType** | string<br>(enum)<br><br>*read-only<br>(null)* | This is the type of this port. *For the possible property values, see PortType in Property Details.* |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **Width** | number<br><br>*read-only<br>(null)* | The number of lanes, phys, or other physical transport links that this port contains. |

### Actions

### Reset


This action is used to reset this port.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResetType** | string<br>(enum)<br><br>*read-write* | The type of reset to be performed. *For the possible property values, see ResetType in Property Details.* |
| } |   |   |   |

### Property Details

### PortProtocol:


The protocol being sent over this port.

| string | Description |
| --- | --- |
| AHCI | Advanced Host Controller Interface. |
| FC | Fibre Channel. |
| FCoE | Fibre Channel over Ethernet. |
| FCP | Fibre Channel Protocol for SCSI. |
| FICON | FIbre CONnection (FICON). |
| FTP | File Transfer Protocol. |
| HTTP | Hypertext Transport Protocol. |
| HTTPS | Secure Hypertext Transport Protocol. |
| iSCSI | Internet SCSI. |
| iWARP | Internet Wide Area Remote Direct Memory Access Protocol. |
| NFSv3 | Network File System version 3. |
| NFSv4 | Network File System version 4. |
| NVMe | Non-Volatile Memory Express. |
| NVMeOverFabrics | NVMe over Fabrics. |
| OEM | OEM specific. |
| PCIe | PCI Express (Vendor Proprietary). |
| RoCE | RDMA over Converged Ethernet Protocol. |
| RoCEv2 | RDMA over Converged Ethernet Protocol Version 2. |
| SAS | Serial Attached SCSI. |
| SATA | Serial AT Attachment. |
| SFTP | Secure File Transfer Protocol. |
| SMB | Server Message Block (aka CIFS Common Internet File System). |
| UHCI | Universal Host Controller Interface. |
| USB | Universal Serial Bus. |

### PortType:


This is the type of this port.

| string | Description |
| --- | --- |
| BidirectionalPort | This port connects to any type of device. |
| DownstreamPort | This port connects to a target device. |
| InterswitchPort | This port connects to another switch. |
| ManagementPort | This port connects to a switch manager. |
| UnconfiguredPort | This port has not yet been configured. |
| UpstreamPort | This port connects to a host device. |

### ResetType:


The type of reset to be performed.

| string | Description |
| --- | --- |
| ForceOff | Turn the unit off immediately (non-graceful shutdown). |
| ForceOn | Turn the unit on immediately. |
| ForceRestart | Perform an immediate (non-graceful) shutdown, followed by a restart. |
| GracefulRestart | Perform a graceful shutdown followed by a restart of the system. |
| GracefulShutdown | Perform a graceful shutdown and power off. |
| Nmi | Generate a Diagnostic Interrupt (usually an NMI on x86 systems) to cease normal operations, perform diagnostic actions and typically halt the system. |
| On | Turn the unit on. |
| PowerCycle | Perform a power cycle of the unit. |
| PushPowerButton | Simulate the pressing of the physical power button on this unit. |


## Power 1.5.0

This is the schema definition for the Power Metrics.  It represents the properties for Power Consumption and Power Limiting.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **PowerControl** [ { | array | This is the definition for power control function (power reading/limiting). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Actions** {} | object | The available actions for this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemberId** | string<br><br>*read-only* | This is the identifier for the member within the collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Power Control Function name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PhysicalContext** | string<br>(enum)<br><br>*read-only* | Describes the area, device, or set of devices to which this power control applies. *For the possible property values, see PhysicalContext in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerAllocatedWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The total amount of power that has been allocated (or budegeted)to  chassis resources. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerAvailableWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The amount of power not already budgeted and therefore available for additional allocation. (powerCapacity - powerAllocated).  This indicates how much reserve power capacity is left. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerCapacityWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The total amount of power available to the chassis for allocation. This may the power supply capacity, or power budget assigned to the chassis from an up-stream chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerConsumedWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The actual power being consumed by the chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerLimit** { | object | Power limit status and configuration information for this chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CorrectionInMs** | number<br>(ms)<br><br>*read-write<br>(null)* | The time required for the limiting process to reduce power consumption to below the limit. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LimitException** | string<br>(enum)<br><br>*read-write<br>(null)* | The action that is taken if the power cannot be maintained below the LimitInWatts. *For the possible property values, see LimitException in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LimitInWatts** | number<br>(W)<br><br>*read-write<br>(null)* | The Power limit in watts. Set to null to disable power capping. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerMetrics** { | object | Power readings for this chassis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AverageConsumedWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The average power level over the measurement window (the last IntervalInMin minutes). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IntervalInMin** | number<br>(min)<br><br>*read-only<br>(null)* | The time interval (or window) in which the PowerMetrics are measured over. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxConsumedWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The highest power consumption level that has occured over the measurement window (the last IntervalInMin minutes). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinConsumedWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The lowest power consumption level over the measurement window (the last IntervalInMin minutes). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerRequestedWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The potential power that the chassis resources are requesting which may be higher than the current level being consumed since requested power includes budget that the chassis resource wants for future use. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RelatedItem** [ { | array | The ID(s) of the resources associated with this Power Limit. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| } ] |   |   |
| **PowerSupplies** [ { | array | Details of the power supplies associated with this system or device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Actions** {} | object | The available actions for this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Assembly** {} | object | A reference to the Assembly resource associated with this power supply. See the *Assembly* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EfficiencyPercent** | number<br>(%)<br><br>*read-only<br>(null)* | The measured efficiency of this Power Supply as a percentage. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | The firmware version for this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HotPluggable** | boolean<br><br>*read-only<br>(null)* | Indicates if this device can be inserted or removed while the equipment is in operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IndicatorLED** | string<br>(enum)<br><br>*read-write<br>(null)* | The state of the indicator LED, used to identify the power supply. *For the possible property values, see IndicatorLED in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InputRanges** [ { | array | This is the input ranges that the power supply can use. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**InputType** | string<br>(enum)<br><br>*read-only<br>(null)* | The Input type (AC or DC). *For the possible property values, see InputType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaximumFrequencyHz** | number<br>(Hz)<br><br>*read-only<br>(null)* | The maximum line input frequency at which this power supply input range is effective. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaximumVoltage** | number<br>(V)<br><br>*read-only<br>(null)* | The maximum line input voltage at which this power supply input range is effective. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinimumFrequencyHz** | number<br>(Hz)<br><br>*read-only<br>(null)* | The minimum line input frequency at which this power supply input range is effective. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinimumVoltage** | number<br>(V)<br><br>*read-only<br>(null)* | The minimum line input voltage at which this power supply input range is effective. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OutputWattage** | number<br>(W)<br><br>*read-only<br>(null)* | The maximum capacity of this Power Supply when operating in this input range. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LastPowerOutputWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The average power output of this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LineInputVoltage** | number<br>(V)<br><br>*read-only<br>(null)* | The line input voltage at which the Power Supply is operating. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LineInputVoltageType** | string<br>(enum)<br><br>*read-only<br>(null)* | The line voltage type supported as an input to this Power Supply. *For the possible property values, see LineInputVoltageType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Manufacturer** | string<br><br>*read-only<br>(null)* | This is the manufacturer of this power supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemberId** | string<br><br>*read-only* | This is the identifier for the member within the collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | The model number for this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | The name of the Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PartNumber** | string<br><br>*read-only<br>(null)* | The part number for this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerCapacityWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The maximum capacity of this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerInputWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The measured input power of this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerOutputWatts** | number<br>(W)<br><br>*read-only<br>(null)* | The measured output power of this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PowerSupplyType** | string<br>(enum)<br><br>*read-only<br>(null)* | The Power Supply type (AC or DC). *For the possible property values, see PowerSupplyType in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Redundancy** [ { | array | This structure is used to show redundancy for power supplies.  The Component ids will reference the members of the redundancy groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RelatedItem** [ { | array | The ID(s) of the resources associated with this Power Limit. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number for this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SparePartNumber** | string<br><br>*read-only<br>(null)* | The spare part number for this Power Supply. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| } ] |   |   |
| **Redundancy** [ { | array | Redundancy information for the power subsystem of this system or device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } ] |   |   |
| **Voltages** [ { | array | This is the definition for voltage sensors. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Actions** {} | object | The available actions for this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdCritical** | number<br>(V)<br><br>*read-only<br>(null)* | Below normal range but not yet fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdFatal** | number<br>(V)<br><br>*read-only<br>(null)* | Below normal range and is fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdNonCritical** | number<br>(V)<br><br>*read-only<br>(null)* | Below normal range. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxReadingRange** | number<br>(V)<br><br>*read-only<br>(null)* | Maximum value for this Voltage sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemberId** | string<br><br>*read-only* | This is the identifier for the member within the collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinReadingRange** | number<br>(V)<br><br>*read-only<br>(null)* | Minimum value for this Voltage sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Voltage sensor name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PhysicalContext** | string<br>(enum)<br><br>*read-only* | Describes the area or device to which this voltage measurement applies. *For the possible property values, see PhysicalContext in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ReadingVolts** | number<br>(V)<br><br>*read-only<br>(null)* | The present reading of the voltage sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RelatedItem** [ { | array | Describes the areas or devices to which this voltage measurement applies. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SensorNumber** | number<br><br>*read-only<br>(null)* | A numerical identifier to represent the voltage sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdCritical** | number<br>(V)<br><br>*read-only<br>(null)* | Above normal range but not yet fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdFatal** | number<br>(V)<br><br>*read-only<br>(null)* | Above normal range and is fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdNonCritical** | number<br>(V)<br><br>*read-only<br>(null)* | Above normal range. |
| } ] |   |   |

### Property Details

### IndicatorLED:


The state of the indicator LED, used to identify the power supply.

| string | Description |
| --- | --- |
| Blinking | The Indicator LED is blinking. |
| Lit | The Indicator LED is lit. |
| Off | The Indicator LED is off. |

### InputType:


The Input type (AC or DC).

| string | Description |
| --- | --- |
| AC | Alternating Current (AC) input range. |
| DC | Direct Current (DC) input range. |

### LimitException:


The action that is taken if the power cannot be maintained below the LimitInWatts.

| string | Description |
| --- | --- |
| HardPowerOff | Turn the power off immediately when the limit is exceeded. |
| LogEventOnly | Log an event when the limit is exceeded, but take no further action. |
| NoAction | Take no action when the limit is exceeded. |
| Oem | Take an OEM-defined action. |

### LineInputVoltageType:


The line voltage type supported as an input to this Power Supply.

| string | Description |
| --- | --- |
| AC120V | AC 120V nominal input. |
| AC240V | AC 240V nominal input. |
| AC277V | AC 277V nominal input. |
| ACandDCWideRange | Wide range AC or DC input. |
| ACHighLine | 277V AC input. *This value has been Deprecated in favor of AC277V.* |
| ACLowLine | 100-127V AC input. *This value has been Deprecated in favor of AC120V.* |
| ACMidLine | 200-240V AC input. *This value has been Deprecated in favor of AC240V.* |
| ACWideRange | Wide range AC input. |
| DC240V | DC 240V nominal input. |
| DC380V | High Voltage DC input (380V). |
| DCNeg48V | -48V DC input. |
| Unknown | The power supply line input voltage type cannot be determined. |

### PhysicalContext:


Describes the area or device to which this voltage measurement applies.

| string | Description |
| --- | --- |
| ASIC | An ASIC device, such as an FPGA or a GPGPU. |
| Back | The back of the chassis. |
| Backplane | A backplane within the chassis. |
| Chassis | The entire chassis. |
| ComputeBay | Within a compute bay. |
| CPU | A Processor (CPU). |
| Exhaust | The air exhaust point of the chassis. |
| ExpansionBay | Within an expansion bay. |
| Fan | A fan. |
| Front | The front of the chassis. |
| GPU | A Graphics Processor (GPU). |
| Intake | The air intake point of the chassis. |
| LiquidInlet | The liquid inlet point of the chassis. |
| LiquidOutlet | The liquid outlet point of the chassis. |
| Lower | The lower portion of the chassis. |
| Memory | A memory device. |
| NetworkBay | Within a networking bay. |
| NetworkingDevice | A networking device. |
| PowerSupply | A power supply. |
| PowerSupplyBay | Within a power supply bay. |
| Room | The room. |
| StorageBay | Within a storage bay. |
| StorageDevice | A storage device. |
| SystemBoard | The system board (PCB). |
| Upper | The upper portion of the chassis. |
| VoltageRegulator | A voltage regulator device. |

### PowerSupplyType:


The Power Supply type (AC or DC).

| string | Description |
| --- | --- |
| AC | Alternating Current (AC) power supply. |
| ACorDC | Power Supply supports both DC or AC. |
| DC | Direct Current (DC) power supply. |
| Unknown | The power supply type cannot be determined. |


## PrivilegeRegistry 1.1.1

This is the schema definition for Operation to Privilege mapping.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Mappings** [ { | array |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Entity** | string<br><br>*read-only* | Indicates entity name. e.g., Manager. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OperationMap** { | object | List mapping between HTTP method and privilege required for entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DELETE** [ { | array | Indicates privilege required for HTTP DELETE operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GET** [ { | array | Indicates privilege required for HTTP GET operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HEAD** [ { | array | Indicates privilege required for HTTP HEAD operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PATCH** [ { | array | Indicates privilege required for HTTP PATCH operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**POST** [ { | array | Indicates privilege required for HTTP POST operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PUT** [ { | array | Indicates privilege required for HTTP PUT operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PropertyOverrides** [ { | array | Indicates privilege overrides of property or element within a entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OperationMap** { | object<br><br>*<br>(null)* | List mapping between HTTP operation and privilege needed to perform operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DELETE** [ { | array | Indicates privilege required for HTTP DELETE operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GET** [ { | array | Indicates privilege required for HTTP GET operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HEAD** [ { | array | Indicates privilege required for HTTP HEAD operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PATCH** [ { | array | Indicates privilege required for HTTP PATCH operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**POST** [ { | array | Indicates privilege required for HTTP POST operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PUT** [ { | array | Indicates privilege required for HTTP PUT operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Targets** [ ] | array (string, null)<br><br>*read-only* | Indicates the URI or Entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ResourceURIOverrides** [ { | array | Indicates privilege overrides of Resource URI. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OperationMap** { | object<br><br>*<br>(null)* | List mapping between HTTP operation and privilege needed to perform operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DELETE** [ { | array | Indicates privilege required for HTTP DELETE operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GET** [ { | array | Indicates privilege required for HTTP GET operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HEAD** [ { | array | Indicates privilege required for HTTP HEAD operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PATCH** [ { | array | Indicates privilege required for HTTP PATCH operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**POST** [ { | array | Indicates privilege required for HTTP POST operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PUT** [ { | array | Indicates privilege required for HTTP PUT operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Targets** [ ] | array (string, null)<br><br>*read-only* | Indicates the URI or Entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SubordinateOverrides** [ { | array | Indicates privilege overrides of subordinate resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OperationMap** { | object<br><br>*<br>(null)* | List mapping between HTTP operation and privilege needed to perform operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DELETE** [ { | array | Indicates privilege required for HTTP DELETE operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**GET** [ { | array | Indicates privilege required for HTTP GET operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HEAD** [ { | array | Indicates privilege required for HTTP HEAD operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PATCH** [ { | array | Indicates privilege required for HTTP PATCH operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**POST** [ { | array | Indicates privilege required for HTTP POST operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PUT** [ { | array | Indicates privilege required for HTTP PUT operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Privilege** [ ] | array (string)<br><br>*read-only* | Lists the privileges that are allowed to perform the given type of HTTP operation on the entity type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Targets** [ ] | array (string, null)<br><br>*read-only* | Indicates the URI or Entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| } ] |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **OEMPrivilegesUsed** [ ] | array (string)<br><br>*read-only* | Lists the set of OEM Priviliges used in building this mapping. |
| **PrivilegesUsed** [ ] | array (string<br>(enum))<br><br>*read-only* | Lists the set of Redfish standard priviliges used in building this mapping. *For the possible property values, see PrivilegesUsed in Property Details.* |

### Property Details

### PrivilegesUsed:


Lists the set of Redfish standard priviliges used in building this mapping.

| string | Description |
| --- | --- |
| ConfigureComponents | Able to configure components managed by this service. |
| ConfigureManager | Able to configure Manager resources. |
| ConfigureSelf | Able to change the password for the current user Account. |
| ConfigureUsers | Able to configure Users and their Accounts. |
| Login | Able to log into the service and read resources. |


## Processor 1.3.0

This is the schema definition for the Processor resource.  It represents the properties of a processor attached to a System.

|     |     |     |
| --- | --- | --- |
| **Assembly** {} | object | A reference to the Assembly resource associated with this processor. See the *Assembly* schema for details on this property. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **InstructionSet** | string<br>(enum)<br><br>*read-only<br>(null)* | The instruction set of the processor. *For the possible property values, see InstructionSet in Property Details.* |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Chassis** { | object | A reference to the Chassis which contains this Processor. See the *Chassis* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | The processor manufacturer. |
| **MaxSpeedMHz** | number<br><br>*read-only<br>(null)* | The maximum clock speed of the processor. |
| **Model** | string<br><br>*read-only<br>(null)* | The product model number of this device. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **ProcessorArchitecture** | string<br>(enum)<br><br>*read-only<br>(null)* | The architecture of the processor. *For the possible property values, see ProcessorArchitecture in Property Details.* |
| **ProcessorId** { | object | Identification information for this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EffectiveFamily** | string<br><br>*read-only<br>(null)* | The effective Family for this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EffectiveModel** | string<br><br>*read-only<br>(null)* | The effective Model for this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IdentificationRegisters** | string<br><br>*read-only<br>(null)* | The contents of the Identification Registers (CPUID) for this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MicrocodeInfo** | string<br><br>*read-only<br>(null)* | The Microcode Information for this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Step** | string<br><br>*read-only<br>(null)* | The Step value for this processor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**VendorId** | string<br><br>*read-only<br>(null)* | The Vendor Identification for this processor. |
| } |   |   |
| **ProcessorType** | string<br>(enum)<br><br>*read-only<br>(null)* | The type of processor. *For the possible property values, see ProcessorType in Property Details.* |
| **Socket** | string<br><br>*read-only<br>(null)* | The socket or location of the processor. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **SubProcessors** { | object | A reference to the collection of Sub-Processors associated with this system, such as cores or threads that are part of a processor. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Processor*. See the Processor schema for details. |
| } |   |   |
| **TotalCores** | number<br><br>*read-only<br>(null)* | The total number of cores contained in this processor. |
| **TotalThreads** | number<br><br>*read-only<br>(null)* | The total number of execution threads supported by this processor. |

### Property Details

### InstructionSet:


The instruction set of the processor.

| string | Description |
| --- | --- |
| ARM-A32 | ARM 32-bit. |
| ARM-A64 | ARM 64-bit. |
| IA-64 | Intel IA-64. |
| MIPS32 | MIPS 32-bit. |
| MIPS64 | MIPS 64-bit. |
| OEM | OEM-defined. |
| x86 | x86 32-bit. |
| x86-64 | x86 64-bit. |

### ProcessorArchitecture:


The architecture of the processor.

| string | Description |
| --- | --- |
| ARM | ARM. |
| IA-64 | Intel Itanium. |
| MIPS | MIPS. |
| OEM | OEM-defined. |
| x86 | x86 or x86-64. |

### ProcessorType:


The type of processor.

| string | Description |
| --- | --- |
| Accelerator | An Accelerator. |
| Core | A Core in a Processor. |
| CPU | A Central Processing Unit. |
| DSP | A Digital Signal Processor. |
| FPGA | A Field Programmable Gate Array. |
| GPU | A Graphics Processing Unit. |
| OEM | An OEM-defined Processing Unit. |
| Thread | A Thread in a Processor. |


## Role 1.2.1

This resource defines a user role to be used in conjunction with a Manager Account.

|     |     |     |
| --- | --- | --- |
| **AssignedPrivileges** [ ] | array (string<br>(enum))<br><br>*read-write* | The redfish privileges that this role includes. *For the possible property values, see AssignedPrivileges in Property Details.* |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **IsPredefined** | boolean<br><br>*read-only* | This property is used to indicate if the Role is one of the Redfish Predefined Roles vs a Custom role. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **OemPrivileges** [ ] | array (string)<br><br>*read-write* | The OEM privileges that this role includes. |
| **RoleId** | string<br><br>*read-only required on create* | This property contains the name of the Role. |

### Property Details

### AssignedPrivileges:


The redfish privileges that this role includes.

| string | Description |
| --- | --- |
| ConfigureComponents | Able to configure components managed by this service. |
| ConfigureManager | Able to configure Manager resources. |
| ConfigureSelf | Able to change the password for the current user Account. |
| ConfigureUsers | Able to configure Users and their Accounts. |
| Login | Able to log into the service and read resources. |

## ServiceRoot 1.3.1

This object represents the root Redfish service.

|     |     |     |
| --- | --- | --- |
| **AccountService** { | object | This is a link to the Account Service. See the *AccountService* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a AccountService resource. See the Links section and the *AccountService* schema for details. |
| } |   |   |
| **Chassis** { | object | This is a link to a collection of Chassis. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Chassis*. See the Chassis schema for details. |
| } |   |   |
| **CompositionService** {} | object | This is a link to the CompositionService. See the *CompositionService* schema for details on this property. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EventService** { | object | This is a link to the EventService. See the *EventService* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a EventService resource. See the Links section and the *EventService* schema for details. |
| } |   |   |
| **Fabrics** { | object | A link to a collection of all fabric entities. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Fabric*. See the Fabric schema for details. |
| } |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **JsonSchemas** { | object | This is a link to a collection of Json-Schema files. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *JsonSchemaFile*. See the JsonSchemaFile schema for details. |
| } |   |   |
| **Links** { | object<br><br>* required* | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Sessions** { | object<br><br>* required* | Link to a collection of Sessions. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Session*. See the Session schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| } |   |   |
| **Managers** { | object | This is a link to a collection of Managers. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Manager*. See the Manager schema for details. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Product** | string<br><br>*read-only* | The product associated with this Redfish service. |
| **ProtocolFeaturesSupported** { | object | Contains information about protocol features supported by the service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ExpandQuery** { | object | Contains information about the use of $expand in the service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ExpandAll** | boolean<br><br>*read-only* | This indicates whether the expand support of asterisk (expand all entries) is supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Levels** | boolean<br><br>*read-only* | This indicates whether the expand support of the $levels qualifier is supported by the service. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Links** | boolean<br><br>*read-only* | This indicates whether the expand support of tilde (expand only entries in the Links section) is supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxLevels** | number<br><br>*read-only* | This indicates the maximum number value of the $levels qualifier in expand operations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**NoLinks** | boolean<br><br>*read-only* | This indicates whether the expand support of period (expand only entries not in the Links section) is supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FilterQuery** | boolean<br><br>*read-only* | This indicates whether the filter query parameter is supported. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SelectQuery** | boolean<br><br>*read-only* | This indicates whether the select query parameter is supported. |
| } |   |   |
| **RedfishVersion** | string<br><br>*read-only* | The version of the Redfish service. |
| **Registries** { | object | This is a link to a collection of Registries. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *MessageRegistryFile*. See the MessageRegistryFile schema for details. |
| } |   |   |
| **SessionService** { | object | This is a link to the Sessions Service. See the *SessionService* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a SessionService resource. See the Links section and the *SessionService* schema for details. |
| } |   |   |
| **StorageServices** { | object | A link to a collection of all storage service entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } |   |   |
| **StorageSystems** { | object | This is a link to a collection of storage systems. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } |   |   |
| **Systems** { | object | This is a link to a collection of Systems. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *ComputerSystem*. See the ComputerSystem schema for details. |
| } |   |   |
| **Tasks** { | object | This is a link to the Task Service. See the *TaskService* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a TaskService resource. See the Links section and the *TaskService* schema for details. |
| } |   |   |
| **UpdateService** { | object | This is a link to the UpdateService. See the *UpdateService* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a UpdateService resource. See the Links section and the *UpdateService* schema for details. |
| } |   |   |
| **UUID** | string<br><br>*read-only<br>(null)* | Unique identifier for a service instance. When SSDP is used, this value should be an exact match of the UUID value returned in a 200OK from an SSDP M-SEARCH request during discovery. |

## Session 1.1.0

The Session resource describes a single connection (session) between a client and a Redfish service instance.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Password** | string<br><br>*read-only required on create<br>(null)* | This property is used in a POST to specify a password when creating a new session.  This property is null on a GET. |
| **UserName** | string<br><br>*read-only required on create<br>(null)* | The UserName for the account for this session. |

## SessionService 1.1.3

This is the schema definition for the Session Service.  It represents the properties for the service itself and has links to the actual list of sessions.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled.  If set to false, the Session Service is disabled and any attempt to access it will fail.  This means new sessions cannot be created, old sessions cannot be deleted though established sessions may continue operating. |
| **Sessions** { | object | Link to a collection of Sessions. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Session*. See the Session schema for details. |
| } |   |   |
| **SessionTimeout** | number<br>(seconds)<br><br>*read-write* | This is the number of seconds of inactivity that a session may have before the session service closes the session due to inactivity. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

## SimpleStorage 1.2.0

This is the schema definition for the Simple Storage resource.  It represents the properties of a storage controller and its directly-attached devices.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Devices** [ { | array | The storage devices associated with this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**CapacityBytes** | number<br>(Bytes)<br><br>*read-only<br>(null)* | The size of the storage device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Manufacturer** | string<br><br>*read-only<br>(null)* | The name of the manufacturer of this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | The product model number of this device. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| } ] |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Chassis** { | object | A reference to the Chassis which contains this Simple Storage. See the *Chassis* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **UefiDevicePath** | string<br><br>*read-only<br>(null)* | The UEFI device path used to access this storage controller. |

## SoftwareInventory 1.2.0

This schema defines an inventory of software components.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **LowestSupportedVersion** | string<br><br>*read-only<br>(null)* | A string representing the lowest supported version of this software. |
| **Manufacturer** | string<br><br>*read-only<br>(null)* | A string representing the manufacturer/producer of this software. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **RelatedItem** [ { | array | The ID(s) of the resources associated with this software inventory item. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } ] |   |   |
| **ReleaseDate** | string<br><br>*read-only<br>(null)* | Release date of this software. |
| **SoftwareId** | string<br><br>*read-only* | A string representing the implementation-specific ID for identifying this software. |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **UefiDevicePaths** [ ] | array (string, null)<br><br>*read-only* | A list of strings representing the UEFI Device Path(s) of the component(s) associated with this software inventory item. |
| **Updateable** | boolean<br><br>*read-only<br>(null)* | Indicates whether this software can be updated by the update service. |
| **Version** | string<br><br>*read-only<br>(null)* | A string representing the version of this software. |

## Storage 1.4.0

This schema defines a storage subsystem and its respective properties.  A storage subsystem represents a set of storage controllers (physical or virtual) and the resources such as volumes that can be accessed from that subsystem.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Drives** [ { | array | The set of drives attached to the storage controllers represented by this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Drive resource. See the Links section and the *Drive* schema for details. |
| } ] |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Enclosures** [ { | array | An array of references to the chassis to which this storage subsystem is attached. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Chassis resource. See the Links section and the *Chassis* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Redundancy** [ { | array | Redundancy information for the storage subsystem. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } ] |   |   |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **StorageControllers** [ { | array | The set of storage controllers represented by this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Actions** {} | object | The available actions for this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Assembly** {} | object | A reference to the Assembly resource associated with this Storage Controller. See the *Assembly* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AssetTag** | string<br><br>*read-write<br>(null)* | The user assigned asset tag for this storage controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FirmwareVersion** | string<br><br>*read-only<br>(null)* | The firmware version of this storage Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Identifiers** [ { } ] | array (object) | The Durable names for the storage controller. This type describes any additional identifiers for a resource. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Endpoints** [ { } ] | array (object) | An array of references to the endpoints that connect to this controller. This is the schema definition for the Endpoint resource. It represents the properties of an entity that sends or receives protocol defined messages over a transport. See the *Endpoint* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**StorageServices** [ { | array | An array of references to the StorageServices that connect to this controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Manufacturer** | string<br><br>*read-only<br>(null)* | This is the manufacturer of this storage controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemberId** | string<br><br>*read-only* | This is the identifier for the member within the collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | This is the model number for the storage controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | The name of the Storage Controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PartNumber** | string<br><br>*read-only<br>(null)* | The part number for this storage controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number for this storage controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SKU** | string<br><br>*read-only<br>(null)* | This is the SKU for this storage controller. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SpeedGbps** | number<br>(Gbit/s)<br><br>*read-only<br>(null)* | The speed of the storage controller interface. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SupportedControllerProtocols** [ ] | array (string<br>(enum))<br><br>*read-only* | This represents the protocols by which this storage controller can be communicated to. *For the possible property values, see SupportedControllerProtocols in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SupportedDeviceProtocols** [ ] | array (string<br>(enum))<br><br>*read-only* | This represents the protocols which the storage controller can use to communicate with attached devices. *For the possible property values, see SupportedDeviceProtocols in Property Details.* |
| } ] |   |   |
| **Volumes** { | object | The set of volumes produced by the storage controllers represented by this resource. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Volume*. See the Volume schema for details. |
| } |   |   |

### Actions

### SetEncryptionKey


This action is used to set the encryption key for the storage subsystem.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EncryptionKey** | string<br><br>*read-write required* | The encryption key to set on the storage subsytem. |
| } |   |   |   |

### Property Details

### SupportedControllerProtocols:


This represents the protocols by which this storage controller can be communicated to.

| string | Description |
| --- | --- |
| AHCI | Advanced Host Controller Interface. |
| FC | Fibre Channel. |
| FCoE | Fibre Channel over Ethernet. |
| FCP | Fibre Channel Protocol for SCSI. |
| FICON | FIbre CONnection (FICON). |
| FTP | File Transfer Protocol. |
| HTTP | Hypertext Transport Protocol. |
| HTTPS | Secure Hypertext Transport Protocol. |
| iSCSI | Internet SCSI. |
| iWARP | Internet Wide Area Remote Direct Memory Access Protocol. |
| NFSv3 | Network File System version 3. |
| NFSv4 | Network File System version 4. |
| NVMe | Non-Volatile Memory Express. |
| NVMeOverFabrics | NVMe over Fabrics. |
| OEM | OEM specific. |
| PCIe | PCI Express (Vendor Proprietary). |
| RoCE | RDMA over Converged Ethernet Protocol. |
| RoCEv2 | RDMA over Converged Ethernet Protocol Version 2. |
| SAS | Serial Attached SCSI. |
| SATA | Serial AT Attachment. |
| SFTP | Secure File Transfer Protocol. |
| SMB | Server Message Block (aka CIFS Common Internet File System). |
| UHCI | Universal Host Controller Interface. |
| USB | Universal Serial Bus. |

### SupportedDeviceProtocols:


This represents the protocols which the storage controller can use to communicate with attached devices.

| string | Description |
| --- | --- |
| AHCI | Advanced Host Controller Interface. |
| FC | Fibre Channel. |
| FCoE | Fibre Channel over Ethernet. |
| FCP | Fibre Channel Protocol for SCSI. |
| FICON | FIbre CONnection (FICON). |
| FTP | File Transfer Protocol. |
| HTTP | Hypertext Transport Protocol. |
| HTTPS | Secure Hypertext Transport Protocol. |
| iSCSI | Internet SCSI. |
| iWARP | Internet Wide Area Remote Direct Memory Access Protocol. |
| NFSv3 | Network File System version 3. |
| NFSv4 | Network File System version 4. |
| NVMe | Non-Volatile Memory Express. |
| NVMeOverFabrics | NVMe over Fabrics. |
| OEM | OEM specific. |
| PCIe | PCI Express (Vendor Proprietary). |
| RoCE | RDMA over Converged Ethernet Protocol. |
| RoCEv2 | RDMA over Converged Ethernet Protocol Version 2. |
| SAS | Serial Attached SCSI. |
| SATA | Serial AT Attachment. |
| SFTP | Secure File Transfer Protocol. |
| SMB | Server Message Block (aka CIFS Common Internet File System). |
| UHCI | Universal Host Controller Interface. |
| USB | Universal Serial Bus. |


## Task 1.2.0

This resource contains information about a specific Task scheduled by or being executed by a Redfish service's Task Service.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **EndTime** | string<br><br>*read-only* | The date-time stamp that the task was last completed. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Messages** [ { } ] | array (object) | This is an array of messages associated with the task. This type describes a Message returned by the Redfish service. See the *Message* schema for details on this property. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **StartTime** | string<br><br>*read-only* | The date-time stamp that the task was last started. |
| **TaskMonitor** | string<br><br>*read-only* | The URI of the Task Monitor for this task. |
| **TaskState** | string<br>(enum)<br><br>*read-only* | The state of the task. *For the possible property values, see TaskState in Property Details.* |
| **TaskStatus** | string<br>(enum)<br><br>*read-only* | This is the completion status of the task. *For the possible property values, see TaskStatus in Property Details.* |

### Property Details

### TaskState:


The state of the task.

| string | Description |
| --- | --- |
| Cancelled | Task has been cancelled by an operator or internal process. |
| Cancelling | Task is in the process of being cancelled. |
| Completed | Task has completed. |
| Exception | Task has stopped due to an exception condition. |
| Interrupted | Task has been interrupted. |
| Killed | Task was terminated. *This value has been deprecated and is being replaced by the value Cancelled which has more determinate semantics.* |
| New | A new task. |
| Pending | Task is pending and has not started. |
| Running | Task is running normally. |
| Service | Task is running as a service. |
| Starting | Task is starting. |
| Stopping | Task is in the process of stopping. |
| Suspended | Task has been suspended. |

### TaskStatus:


This is the completion status of the task.

| string | Description |
| --- | --- |
| Critical | A critical condition exists that requires immediate attention. |
| OK | Normal. |
| Warning | A condition exists that requires attention. |


## TaskService 1.1.1

This is the schema definition for the Task Service.  It represents the properties for the service itself and has links to the actual list of tasks.

|     |     |     |
| --- | --- | --- |
| **CompletedTaskOverWritePolicy** | string<br>(enum)<br><br>*read-only* | Overwrite policy of completed tasks. *For the possible property values, see CompletedTaskOverWritePolicy in Property Details.* |
| **DateTime** | string<br><br>*read-only<br>(null)* | The current DateTime (with offset) setting that the task service is using. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **LifeCycleEventOnTaskStateChange** | boolean<br><br>*read-only* | Send an Event upon Task State Change. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **Tasks** { | object | References to the Tasks collection. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *Task*. See the Task schema for details. |
| } |   |   |

### Property Details

### CompletedTaskOverWritePolicy:


Overwrite policy of completed tasks.

| string | Description |
| --- | --- |
| Manual | Completed tasks are not automatically overwritten. |
| Oldest | Oldest completed tasks are overwritten. |


## Thermal 1.4.0

This is the schema definition for the Thermal properties.  It represents the properties for Temperature and Cooling.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Fans** [ { | array | This is the definition for fans. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Actions** {} | object | The available actions for this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Assembly** {} | object | A reference to the Assembly resource associated with this fan. See the *Assembly* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**FanName** | string<br><br>*read-only<br>(null)* | Name of the fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HotPluggable** | boolean<br><br>*read-only<br>(null)* | Indicates if this device can be inserted or removed while the equipment is in operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**IndicatorLED** | string<br>(enum)<br><br>*read-write<br>(null)* | The state of the indicator LED, used to identify this Fan. *For the possible property values, see IndicatorLED in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Location** {} | object | This type describes the location of a resource. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdCritical** | number<br><br>*read-only<br>(null)* | Below normal range but not yet fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdFatal** | number<br><br>*read-only<br>(null)* | Below normal range and is fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdNonCritical** | number<br><br>*read-only<br>(null)* | Below normal range. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Manufacturer** | string<br><br>*read-only<br>(null)* | This is the manufacturer of this Fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxReadingRange** | number<br><br>*read-only<br>(null)* | Maximum value for Reading. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemberId** | string<br><br>*read-only* | This is the identifier for the member within the collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinReadingRange** | number<br><br>*read-only<br>(null)* | Minimum value for Reading. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Model** | string<br><br>*read-only<br>(null)* | The model number for this Fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Name of the fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PartNumber** | string<br><br>*read-only<br>(null)* | The part number for this Fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PhysicalContext** | string<br>(enum)<br><br>*read-only* | Describes the area or device associated with this fan. *For the possible property values, see PhysicalContext in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Reading** | number<br><br>*read-only<br>(null)* | Current fan speed. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ReadingUnits** | string<br>(enum)<br><br>*read-only<br>(null)* | Units in which the reading and thresholds are measured. *For the possible property values, see ReadingUnits in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Redundancy** [ { | array | This structure is used to show redundancy for fans.  The Component ids will reference the members of the redundancy groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RelatedItem** [ { | array | The ID(s) of the resources serviced with this fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SerialNumber** | string<br><br>*read-only<br>(null)* | The serial number for this Fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SparePartNumber** | string<br><br>*read-only<br>(null)* | The spare part number for this Fan. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdCritical** | number<br><br>*read-only<br>(null)* | Above normal range but not yet fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdFatal** | number<br><br>*read-only<br>(null)* | Above normal range and is fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdNonCritical** | number<br><br>*read-only<br>(null)* | Above normal range. |
| } ] |   |   |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Redundancy** [ { | array | This structure is used to show redundancy for fans.  The Component ids will reference the members of the redundancy groups. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| } ] |   |   |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **Temperatures** [ { | array | This is the definition for temperature sensors. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Actions** {} | object | The available actions for this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AdjustedMaxAllowableOperatingValue** | number<br>(Cel)<br><br>*read-only<br>(null)* | Adjusted maximum allowable operating temperature for this equipment based on the current environmental conditions present. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AdjustedMinAllowableOperatingValue** | number<br>(Cel)<br><br>*read-only<br>(null)* | Adjusted minimum allowable operating temperature for this equipment based on the current environmental conditions present. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeltaPhysicalContext** | string<br>(enum)<br><br>*read-only* | Describes the area or device to which the DeltaReadingCelsius temperature measurement applies, relative to PhysicalContext. *For the possible property values, see DeltaPhysicalContext in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**DeltaReadingCelsius** | number<br>(Cel)<br><br>*read-only<br>(null)* | Delta Temperature reading. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdCritical** | number<br>(Cel)<br><br>*read-only<br>(null)* | Below normal range but not yet fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdFatal** | number<br>(Cel)<br><br>*read-only<br>(null)* | Below normal range and is fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**LowerThresholdNonCritical** | number<br>(Cel)<br><br>*read-only<br>(null)* | Below normal range. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxAllowableOperatingValue** | number<br>(Cel)<br><br>*read-only<br>(null)* | Maximum allowable operating temperature for this equipment. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MaxReadingRangeTemp** | number<br>(Cel)<br><br>*read-only<br>(null)* | Maximum value for ReadingCelsius. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MemberId** | string<br><br>*read-only* | This is the identifier for the member within the collection. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinAllowableOperatingValue** | number<br>(Cel)<br><br>*read-only<br>(null)* | Minimum allowable operating temperature for this equipment. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MinReadingRangeTemp** | number<br>(Cel)<br><br>*read-only<br>(null)* | Minimum value for ReadingCelsius. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name** | string<br><br>*read-only<br>(null)* | Temperature sensor name. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PhysicalContext** | string<br>(enum)<br><br>*read-only* | Describes the area or device to which this temperature measurement applies. *For the possible property values, see PhysicalContext in Property Details.* |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ReadingCelsius** | number<br>(Cel)<br><br>*read-only<br>(null)* | Temperature. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RelatedItem** [ { | array | Describes the areas or devices to which this temperature measurement applies. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | The unique identifier for a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**SensorNumber** | number<br><br>*read-only<br>(null)* | A numerical identifier to represent the temperature sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdCritical** | number<br>(Cel)<br><br>*read-only<br>(null)* | Above normal range but not yet fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdFatal** | number<br>(Cel)<br><br>*read-only<br>(null)* | Above normal range and is fatal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**UpperThresholdNonCritical** | number<br>(Cel)<br><br>*read-only<br>(null)* | Above normal range. |
| } ] |   |   |

### Property Details

### DeltaPhysicalContext:


Describes the area or device to which the DeltaReadingCelsius temperature measurement applies, relative to PhysicalContext.

| string | Description |
| --- | --- |
| ASIC | An ASIC device, such as an FPGA or a GPGPU. |
| Back | The back of the chassis. |
| Backplane | A backplane within the chassis. |
| Chassis | The entire chassis. |
| ComputeBay | Within a compute bay. |
| CPU | A Processor (CPU). |
| Exhaust | The air exhaust point of the chassis. |
| ExpansionBay | Within an expansion bay. |
| Fan | A fan. |
| Front | The front of the chassis. |
| GPU | A Graphics Processor (GPU). |
| Intake | The air intake point of the chassis. |
| LiquidInlet | The liquid inlet point of the chassis. |
| LiquidOutlet | The liquid outlet point of the chassis. |
| Lower | The lower portion of the chassis. |
| Memory | A memory device. |
| NetworkBay | Within a networking bay. |
| NetworkingDevice | A networking device. |
| PowerSupply | A power supply. |
| PowerSupplyBay | Within a power supply bay. |
| Room | The room. |
| StorageBay | Within a storage bay. |
| StorageDevice | A storage device. |
| SystemBoard | The system board (PCB). |
| Upper | The upper portion of the chassis. |
| VoltageRegulator | A voltage regulator device. |

### IndicatorLED:


The state of the indicator LED, used to identify this Fan.

| string | Description |
| --- | --- |
| Blinking | The Indicator LED is blinking. |
| Lit | The Indicator LED is lit. |
| Off | The Indicator LED is off. |

### PhysicalContext:


Describes the area or device to which this temperature measurement applies.

| string | Description |
| --- | --- |
| ASIC | An ASIC device, such as an FPGA or a GPGPU. |
| Back | The back of the chassis. |
| Backplane | A backplane within the chassis. |
| Chassis | The entire chassis. |
| ComputeBay | Within a compute bay. |
| CPU | A Processor (CPU). |
| Exhaust | The air exhaust point of the chassis. |
| ExpansionBay | Within an expansion bay. |
| Fan | A fan. |
| Front | The front of the chassis. |
| GPU | A Graphics Processor (GPU). |
| Intake | The air intake point of the chassis. |
| LiquidInlet | The liquid inlet point of the chassis. |
| LiquidOutlet | The liquid outlet point of the chassis. |
| Lower | The lower portion of the chassis. |
| Memory | A memory device. |
| NetworkBay | Within a networking bay. |
| NetworkingDevice | A networking device. |
| PowerSupply | A power supply. |
| PowerSupplyBay | Within a power supply bay. |
| Room | The room. |
| StorageBay | Within a storage bay. |
| StorageDevice | A storage device. |
| SystemBoard | The system board (PCB). |
| Upper | The upper portion of the chassis. |
| VoltageRegulator | A voltage regulator device. |

### ReadingUnits:


Units in which the reading and thresholds are measured.

| string | Description |
| --- | --- |
| Percent | Indicates that the fan reading and thresholds are measured in percentage. |
| RPM | Indicates that the fan reading and thresholds are measured in rotations per minute. |



## UpdateService 1.2.1

This is the schema definition for the Update Service. It represents the properties for the service itself and has links to collections of firmware and software inventory.

|     |     |     |
| --- | --- | --- |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **FirmwareInventory** { | object<br><br>*<br>(null)* | An inventory of firmware. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *SoftwareInventory*. See the SoftwareInventory schema for details. |
| } |   |   |
| **HttpPushUri** | string<br><br>*read-only* | The URI used to perform an HTTP or HTTPS push update to the Update Service. |
| **HttpPushUriTargets** [ ] | array (string, null)<br><br>*read-write* | The array of URIs indicating the target for applying the update image. |
| **HttpPushUriTargetsBusy** | boolean<br><br>*read-write<br>(null)* | This represents if the HttpPushUriTargets property is reserved by any client. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **ServiceEnabled** | boolean<br><br>*read-write<br>(null)* | This indicates whether this service is enabled. |
| **SoftwareInventory** { | object<br><br>*<br>(null)* | An inventory of software. Contains a link to a resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to Collection of *SoftwareInventory*. See the SoftwareInventory schema for details. |
| } |   |   |
| **Status** {} | object<br><br>*<br>(null)* | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |

### Actions

### SimpleUpdate


This action is used to update software components.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**ImageURI** | string<br><br>*read-write required* | The URI of the software image to be installed. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Targets** [ ] | array (string)<br><br>*read-write* | The array of URIs indicating where the update image is to be applied. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**TransferProtocol** | string<br>(enum)<br><br>*read-write* | The network protocol used by the Update Service to retrieve the software image file located at the URI provided in ImageURI, if the URI does not contain a scheme. *For the possible property values, see TransferProtocol in Property Details.* |
| } |   |   |   |

### Property Details

### TransferProtocol:


The network protocol used by the Update Service to retrieve the software image file located at the URI provided in ImageURI, if the URI does not contain a scheme.

| string | Description |
| --- | --- |
| CIFS | Common Internet File System protocol. |
| FTP | File Transfer Protocol. |
| HTTP | Hypertext Transfer Protocol. |
| HTTPS | HTTP Secure protocol. |
| NSF | Network File System protocol. |
| OEM | A protocol defined by the manufacturer. |
| SCP | Secure File Copy protocol. |
| SFTP | Secure File Transfer Protocol. |
| TFTP | Trivial File Transfer Protocol. |


## VirtualMedia 1.2.0

The VirtualMedia schema contains properties related to monitoring and control of an instance of virtual media such as a remote CD, DVD, or USB device. Virtual media functionality is provided by a Manager for a system or device.

|     |     |     |
| --- | --- | --- |
| **ConnectedVia** | string<br>(enum)<br><br>*read-only<br>(null)* | Current virtual media connection methods. *For the possible property values, see ConnectedVia in Property Details.* |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Image** | string<br><br>*read-write<br>(null)* | A URI providing the location of the selected image. |
| **ImageName** | string<br><br>*read-only<br>(null)* | The current image name. |
| **Inserted** | boolean<br><br>*read-write<br>(null)* | Indicates if virtual media is inserted in the virtual device. |
| **MediaTypes** [ ] | array (string<br>(enum))<br><br>*read-only* | This is the media types supported as virtual media. *For the possible property values, see MediaTypes in Property Details.* |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **WriteProtected** | boolean<br><br>*read-write<br>(null)* | Indicates the media is write protected. |

### Actions

### EjectMedia


This action is used to detach remote media from virtual media.

**URIs**:


(This action takes no parameters.)


### InsertMedia


This action is used to attach remote media to virtual media.

**URIs**:


The following table shows the parameters for the action which are included in the POST body to the URI shown in the "target" property of the Action.

|     |     |     |
| --- | --- | --- |
| { |   |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Image** | string<br><br>*read-write required* | The URI of the remote media to attach to the virtual media. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Inserted** | boolean<br><br>*read-write* | Indicates if the image is to be treated as inserted upon completion of the action. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**WriteProtected** | boolean<br><br>*read-write* | Indicates if the remote media is supposed to be treated as write protected. |
| } |   |   |   |

### Property Details

### ConnectedVia:


Current virtual media connection methods.

| string | Description |
| --- | --- |
| Applet | Connected to a client application. |
| NotConnected | No current connection. |
| Oem | Connected via an OEM-defined method. |
| URI | Connected to a URI location. |

### MediaTypes:


This is the media types supported as virtual media.

| string | Description |
| --- | --- |
| CD | A CD-ROM format (ISO) image. |
| DVD | A DVD-ROM format image. |
| Floppy | A floppy disk image. |
| USBStick | An emulation of a USB storage device. |


## Volume 1.0.3

Volume contains properties used to describe a volume, virtual disk, LUN, or other logical storage entity for any system.

|     |     |     |
| --- | --- | --- |
| **BlockSizeBytes** | number<br>(Bytes)<br><br>*read-only<br>(null)* | The size of the smallest addressible unit (Block) of this volume in bytes. |
| **CapacityBytes** | number<br>(Bytes)<br><br>*read-only<br>(null)* | The size in bytes of this Volume. |
| **Description** | string<br><br>*read-only<br>(null)* | Provides a description of this resource and is used for commonality  in the schema definitions. |
| **Encrypted** | boolean<br><br>*read-write<br>(null)* | Is this Volume encrypted. |
| **EncryptionTypes** [ ] | array (string<br>(enum))<br><br>*read-write* | The types of encryption used by this Volume. *For the possible property values, see EncryptionTypes in Property Details.* |
| **Id** | string<br><br>*read-only required* | Uniquely identifies the resource within the collection of like resources. |
| **Identifiers** [ { } ] | array (object) | The Durable names for the volume. See the *v1_1_0.v1_1_0* schema for details on this property. |
| **Links** { | object | Contains references to other resources that are related to this resource. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Drives** [ { | array | An array of references to the drives which contain this volume. This will reference Drives that either wholly or only partly contain this volume. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Drive resource. See the Links section and the *Drive* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} ] |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Oem** {} | object | Oem extension object. See the *Resource* schema for details on this property. |
| } |   |   |
| **Name** | string<br><br>*read-only required* | The name of the resource or array element. |
| **Oem** {} | object | This is the manufacturer/provider specific extension moniker used to divide the Oem object into sections. See the *Resource* schema for details on this property. |
| **Operations** [ { | array | The operations currently running on the Volume. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**AssociatedTask** { | object | A reference to the task associated with the operation if any. See the *Task* schema for details on this property. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**@odata.id** | string<br><br>*read-only* | Link to a Task resource. See the Links section and the *Task* schema for details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} |   |   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**OperationName** | string<br><br>*read-only<br>(null)* | The name of the operation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**PercentageComplete** | number<br><br>*read-only<br>(null)* | The percentage of the operation that has been completed. |
| } ] |   |   |
| **OptimumIOSizeBytes** | number<br>(Bytes)<br><br>*read-only<br>(null)* | The size in bytes of this Volume's optimum IO size. |
| **Status** {} | object | This type describes the status and health of a resource and its children. See the *Resource* schema for details on this property. |
| **VolumeType** | string<br>(enum)<br><br>*read-only<br>(null)* | The type of this volume. *For the possible property values, see VolumeType in Property Details.* |

### Actions

### Initialize


This action is used to prepare the contents of the volume for use by the system.

**URIs**:


(This action takes no parameters.)


### Property Details

### EncryptionTypes:


The types of encryption used by this Volume.

| string | Description |
| --- | --- |
| ControllerAssisted | The volume is being encrypted by the storage controller entity. |
| NativeDriveEncryption | The volume is utilizing the native drive encryption capabilities of the drive hardware. |
| SoftwareAssisted | The volume is being encrypted by software running on the system or the operating system. |

### VolumeType:


The type of this volume.

| string | Description |
| --- | --- |
| Mirrored | The volume is a mirrored device. |
| NonRedundant | The volume is a non-redundant storage device. |
| RawDevice | The volume is a raw physical device without any RAID or other virtualization applied. |
| SpannedMirrors | The volume is a spanned set of mirrored devices. |
| SpannedStripesWithParity | The volume is a spanned set of devices which uses parity to retain redundant information. |
| StripedWithParity | The volume is a device which uses parity to retain redundant information. |



Text in this section is placed at the end of the document, following all of the schema sections.


