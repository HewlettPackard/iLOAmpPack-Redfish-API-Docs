## AccountService.v1_0_4.AccountService
```@odata.type: "#AccountService.v1_0_4.AccountService"```

This is the schema definition for the Account service. It represents the properties for this service and has links to the list of accounts.

### Managing User Accounts with the Accounts Collection

**JSONPath**: `/Accounts/@odata.id`

The destination of this link is a collection of user accounts (see ManagerAccount).

* You may create a new user account by POSTing a new account description the the Accounts collection.  See ManagerAccount for details.
> e.g. `POST https://{iLO}/redfish/v1/accountservice/accounts/ with new account description`
* You may modify an existing user by PATCHing properties to the user account resource.  See ManagerAccount for details.
> e.g. `PATCH https://{iLO}/redfish/v1/accountservice/accounts/{item} with different properties`
* You may remove a user account by DELETEing the resources representing the user
> e.g. `DELETE https://{iLO}/redfish/v1/accountservice/accounts/{item}`

### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/accountservice```|GET PATCH |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```PrivilegeMap```|[PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)|
|```Roles```|Collection of [Role](#role-v1_0_0-role)|
|```Accounts```|Collection of [ManagerAccount](#manageraccount-v1_0_3-manageraccount)|

### AccountLockoutCounterResetAfter
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)

| | |
|---|---|
|Description|The interval of time in seconds since the last failed login attempt at which point the lockout threshold counter for the account is reset to zero. Must be less than or equal to AccountLockoutDuration.|
|Type|number|
|Read Only|False|

### AccountLockoutDuration
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)

| | |
|---|---|
|Description|The time in seconds an account is locked after the account lockout threshold is met. Must be >= AccountLockoutResetAfter. If set to 0, no lockout will occur.|
|Type|number or null|
|Read Only|False|

### AccountLockoutThreshold
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)

| | |
|---|---|
|Description|The number of failed login attempts before a user account is locked for a specified duration (0=never locked).|
|Type|number or null|
|Read Only|False|

### Accounts
This property references a resource of type Collection with a MemberType of ManagerAccount.
### AuthFailureLoggingThreshold
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)

| | |
|---|---|
|Description|This is the number of authorization failures that need to occur before the failure attempt is logged to the manager log.|
|Type|number|
|Read Only|False|

### MaxPasswordLength
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)

| | |
|---|---|
|Description|This is the maximum password length for this service.|
|Type|number|
|Read Only|True|

### MinPasswordLength
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)

| | |
|---|---|
|Description|This is the minimum password length for this service.|
|Type|number|
|Read Only|False|

### PrivilegeMap
A reference to the Privilege mapping that defines the privileges needed to perform a requested operation on a URI associated with this service.
### Roles
This property shall contain the link to a collection of type RoleCollection.
### ServiceEnabled
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)

| | |
|---|---|
|Description|This indicates whether this service is enabled.|
|Type|boolean or null|
|Read Only|False|

### Status
Member of [AccountService.v1_0_4.AccountService](#accountservice-v1_0_4-accountservice)
See the Redfish standard schema and specification for information on common Status object.

## Chassis.v1_4_0.Chassis
```@odata.type: "#Chassis.v1_4_0.Chassis"```
ERROR: No instances found for resource type #Chassis.v1_4_0.Chassis in the resource map.

The schema definition for the Chassis resource represents the properties for physical components for any system. This object represents racks, rack mount servers, blades, standalone, modular systems, enclosures, and all other containers. The non-CPU/device-centric parts of the schema are accessed either directly or indirectly through this resource.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #Chassis.v1_4_0.Chassis in the resource map.
## ComputerSystem.v1_3_0.ComputerSystem
```@odata.type: "#ComputerSystem.v1_3_0.ComputerSystem"```

This is the schema definition for a ComputerSystem.  Examples of ComputerSystem are BMCs, Enclosure Managers, Management Controllers and other subsystems assigned manageability functions.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/systems/{item}```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Memory```|Collection of [Memory](#memory-v1_2_0-memory)|
|```Oem/Hpe/Links/FirmwareInventory```|SoftwareInventoryCollection|
|```EthernetInterfaces```|Collection of [EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)|
|```Processors```|Collection of [Processor](#processor-v1_1_0-processor)|
|```PCIeDevices```|Collection of [PCIeDevice](#pciedevice-v1_1_0-pciedevice)|
|```Storage```|Collection of [Storage](#storage-v1_2_0-storage)|
|```Oem/Hpe/Links/SoftwareInventory```|SoftwareInventoryCollection|

### EthernetInterfaces
This is a reference to a collection of NICs that this System uses for network communication.  It is here that clients will find NIC configuration options and settings.
### HostName
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The DNS Host Name, without any domain information|
|Type|string or null|
|Read Only|True|

### IndicatorLED
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The state of the indicator LED.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Unknown```|The state of the Indicator LED cannot be determined.|
|```Lit```|The Indicator LED is lit.|
|```Blinking```|The Indicator LED is blinking.|
|```Off```|The Indicator LED is off.|

### LogServices
The LogService collection URI for this resource.
### Manufacturer
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The manufacturer or OEM of this system.|
|Type|string or null|
|Read Only|True|

### Memory
The central memory in the system.
### MemorySummary
**MemorySummary.Status**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)
See the Redfish standard schema and specification for information on common Status object.

**MemorySummary.TotalSystemMemoryGiB**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|This is the total amount of memory in the system measured in GiB.|
|Type|integer or null|
|Read Only|True|

### Model
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The model information that the manufacturer uses to refer to this system.|
|Type|string or null|
|Read Only|True|

### Oem.Hpe.Type
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

### PCIeDevices
A reference to a collection of PCIe Devices used by this computer system.
### PCIeFunctions
A reference to a collection of PCIe Functions used by this computer system.
### PartNumber
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The manufacturer's system part number.|
|Type|string or null|
|Read Only|True|

### PowerState
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|This is the current power state of the system|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Null```|
|```On```|
|```Off```|
|```Unknown```|
|```Reset```|

### ProcessorSummary
**ProcessorSummary.Count**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The number of processors in the system.|
|Type|integer or null|
|Read Only|True|

**ProcessorSummary.Model**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The processor model for the primary or majority of processors in this system.|
|Type|string or null|
|Read Only|True|

**ProcessorSummary.Status**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)
See the Redfish standard schema and specification for information on common Status object.

### Processors
The central processors in the system.
### SKU
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|SKU for this system.|
|Type|string or null|
|Read Only|True|

### SecureBoot
A reference to the UEFI SecureBoot resource associated with this system.
### SerialNumber
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The system serial number.|
|Type|string or null|
|Read Only|True|

### Status
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)
See the Redfish standard schema and specification for information on common Status object.

### Storage
A reference to the collection of storage devices associated with this system.
### SystemType
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The type of computer system that this resource represents.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Physical```|A computer system|
|```Virtual```|A virtual machine instance running on this system|
|```OS```|An operating system instance|
|```PhysicallyPartitioned```|A hardware-based partition of a computer system|
|```VirtuallyPartitioned```|A virtual or software-based partition of a computer system|

### TrustedModules (array)
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)
```TrustedModules``` is an array containing elements of:

**TrustedModules[{item}].FirmwareVersion**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The firmware version of this Trusted Module|
|Type|string or null|
|Read Only|True|

**TrustedModules[{item}].InterfaceType**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|This property indicates the interface type of the Trusted Module.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```TM1_0```|Trusted Module (TM) 1.0|
|```TPM1_2```|Trusted Platform Module (TPM) 1.2|
|```TPM2_0```|Trusted Platform Module (TPM) 2.0|

**TrustedModules[{item}].Status**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)
See the Redfish standard schema and specification for information on common Status object.

### UUID
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)

| | |
|---|---|
|Description|The universal unique identifier for this system.|
|Type|string or null|
|Read Only|True|

### Actions

**Reset**
Member of [ComputerSystem.v1_3_0.ComputerSystem](#computersystem-v1_3_0-computersystem)
There are no parameters for this action.
## Drive.v1_2_0.Drive
```@odata.type: "#Drive.v1_2_0.Drive"```

Drive contains properties describing a single physical disk drive for any system, along with links to associated Volumes.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/systems/{item}/storage/{item}/drives/{item}```|GET |

### AssetTag
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The user assigned asset tag for this drive.|
|Type|string or null|
|Read Only|False|

### BlockSizeBytes
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The size of the smallest addressible unit (Block) of this drive in bytes.|
|Type|number or null|
|Read Only|True|

### CapableSpeedGbs
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The speed which this drive can communicate to a storage controller in ideal conditions in Gigabits per second.|
|Type|number or null|
|Read Only|True|

### CapacityBytes
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The size in bytes of this Drive.|
|Type|number or null|
|Read Only|True|

### EncryptionAbility
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The encryption abilities of this drive.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```None```|The drive is not capable of self encryption.|
|```SelfEncryptingDrive```|The drive is capable of self encryption per the Trusted Computing Group's Self Encrypting Drive Standard.|
|```Other```|The drive is capable of self encryption through some other means.|

### EncryptionStatus
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The status of the encrytion of this drive.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Unecrypted```|The drive is not currently encrypted.|
|```Unlocked```|The drive is currently encrypted but the data is accessible to the user unencrypted.|
|```Locked```|The drive is currently encrypted and the data is not accessible to the user, however the system has the ability to unlock the drive automatically.|
|```Foreign```|The drive is currently encrypted, the data is not accessible to the user, and the system requires user intervention to expose the data.|
|```Unencrypted```|The drive is not currently encrypted.|

### FailurePredicted
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|Is this drive currently predicting a failure in the near future.|
|Type|boolean or null|
|Read Only|True|

### HotspareType
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The type of hotspare this drive is currently serving as.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```None```|The drive is not currently a hotspare.|
|```Global```|The drive is currently serving as a hotspare for all other drives in the storage system.|
|```Chassis```|The drive is currently serving as a hotspare for all other drives in the chassis.|
|```Dedicated```|The drive is currently serving as a hotspare for a user defined set of drives.|

### Identifiers (array)
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)
```Identifiers``` is an array containing elements of:

**Identifiers[{item}].DurableName**
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|This indicates the world wide, persistent name of the resource.|
|Type|string or null|
|Read Only|True|

**Identifiers[{item}].DurableNameFormat**
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|This represents the format of the DurableName property.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```NAA```|Name Address Authority Format.|
|```iQN```|iSCSI Qualified Name.|
|```FC_WWN```|Fibre Channel World Wide Name.|
|```UUID```|Universally Unique Identifier.|
|```EUI```|IEEE-defined 64-bit Extended Unique Identifier.|

### IndicatorLED
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The state of the indicator LED, used to identify the drive.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Lit```|The Indicator LED is lit.|
|```Blinking```|The Indicator LED is blinking.|
|```Off```|The Indicator LED is off.|

### Location (array)
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)
```Location``` is an array containing elements of:

**Location[{item}].Info**
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|This indicates the location of the resource.|
|Type|string or null|
|Read Only|True|

**Location[{item}].InfoFormat**
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|This represents the format of the Info property.|
|Type|string or null|
|Read Only|True|

### Manufacturer
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|This is the manufacturer of this drive.|
|Type|string or null|
|Read Only|True|

### MediaType
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The type of media contained in this drive.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```HDD```|The drive media type is traditional magnetic platters.|
|```SSD```|The drive media type is solid state or flash memory.|
|```SMR```|The drive media type is shingled magnetic recording.|

### Model
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|This is the model number for the drive.|
|Type|string or null|
|Read Only|True|

### NegotiatedSpeedGbs
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The speed which this drive is currently communicating to the storage controller in Gigabits per second.|
|Type|number or null|
|Read Only|True|

### PartNumber
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The part number for this drive.|
|Type|string or null|
|Read Only|True|

### PredictedMediaLifeLeftPercent
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The percentage of reads and writes that are predicted to still be available for the media.|
|Type|number or null|
|Read Only|True|

### Protocol (array)
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)
```Protocol``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```PCIe```|PCI Express (Vendor Proprietary).|
|```AHCI```|Advanced Host Controller Interface.|
|```UHCI```|Universal Host Controller Interface.|
|```SAS```|Serial Attached SCSI.|
|```SATA```|Serial AT Attachment.|
|```USB```|Universal Serial Bus.|
|```NVMe```|Non-Volatile Memory Express.|
|```FC```|Fibre Channel.|
|```iSCSI```|Internet SCSI.|
|```FCoE```|Fibre Channel over Ethernet.|
|```FCP```|Fibre Channel Protocol for SCSI.|
|```FICON```|FIbre CONnection (FICON).|
|```NVMeOverFabrics```|NVMe over Fabrics.|
|```SMB```|Server Message Block (aka CIFS Common Internet File System).|
|```NFSv3```|Network File System version 3.|
|```NFSv4```|Network File System version 4.|
|```HTTP```|Hypertext Transport Protocol.|
|```HTTPS```|Secure Hypertext Transport Protocol.|
|```FTP```|File Transfer Protocol.|
|```SFTP```|Secure File Transfer Protocol.|

### Revision
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The revision of this Drive. This is typically the firmware/hardware version of the drive.|
|Type|string or null|
|Read Only|True|

### RotationSpeedRPM
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The rotation speed of this Drive in Revolutions per Minute (RPM).|
|Type|number or null|
|Read Only|True|

### SKU
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|This is the SKU for this drive.|
|Type|string or null|
|Read Only|True|

### SerialNumber
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The serial number for this drive.|
|Type|string or null|
|Read Only|True|

### Status
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)
See the Redfish standard schema and specification for information on common Status object.

### StatusIndicator
Member of [Drive.v1_2_0.Drive](#drive-v1_2_0-drive)

| | |
|---|---|
|Description|The state of the status indicator, used to communicate status information about this drive.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```OK```|The drive is OK.|
|```Fail```|The drive has failed.|
|```Rebuild```|The drive is being rebuilt.|
|```PredictiveFailureAnalysis```|The drive is still working but predicted to fail soon.|
|```Hotspare```|The drive is marked to be automatically rebuilt and used as a replacement for a failed drive.|
|```InACriticalArray```|The array that this drive is a part of is degraded.|
|```InAFailedArray```|The array that this drive is a part of is failed.|

## EthernetInterface.v1_2_0.EthernetInterface
```@odata.type: "#EthernetInterface.v1_2_0.EthernetInterface"```

The schema definition of a simple Ethernet NIC resource.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/ethernetinterfaces/{item}```|GET PATCH |
|```/redfish/v1/systems/{item}/ethernetinterfaces/{item}```|GET POST PATCH |

### AutoNeg
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|This indicates if the speed and duplex is automatically configured by the NIC.|
|Type|boolean or null|
|Read Only|True|

### FQDN
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|This is the complete, fully qualified domain name obtained by DNS for this interface.|
|Type|string or null|
|Read Only|False|

### FrameSize
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The MAC frame size (bytes).|
|Type|integer or null|
|Read Only|False|

### FullDuplex
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The connection duplex status. If Autosense is enabled, this property cannot be modified. Autosense is only applicable and modifiable for a dedicated network port and cannot be modified for blade servers.|
|Type|boolean or null|
|Read Only|True|

### HostName
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The DNS Host Name, without any domain information.|
|Type|string or null|
|Read Only|False|

### IPv4Addresses (array)
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```IPv4Addresses``` is an array containing elements of:

**IPv4Addresses[{item}].Address**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv4 Address.|
|Type|string or null|
|Read Only|False|

**IPv4Addresses[{item}].AddressOrigin**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|How the address was determined.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```DHCP```|The address is provided by a DHCP service.|
|```Static```|A static address as configured by the user.|

**IPv4Addresses[{item}].Gateway**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv4 gateway for this address.|
|Type|string or null|
|Read Only|False|

**IPv4Addresses[{item}].SubnetMask**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv4 Subnet mask.|
|Type|string or null|
|Read Only|False|

### IPv6AddressPolicyTable (array)
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```IPv6AddressPolicyTable``` is an array containing elements of:

**IPv6AddressPolicyTable[{item}].Label**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The label value for this table entry, as defined in RFC3484 section 2.1.|
|Type|integer or null|
|Read Only|False|

**IPv6AddressPolicyTable[{item}].Precedence**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The precedence value for this table entry as defined in RFC3484 section 2.1.|
|Type|integer or null|
|Read Only|False|

**IPv6AddressPolicyTable[{item}].Prefix**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv6 Address Prefix for this table entry as defined in RFC3484 section 2.1.|
|Type|string or null|
|Read Only|False|

### IPv6Addresses (array)
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```IPv6Addresses``` is an array containing elements of:

**IPv6Addresses[{item}].Address**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv6 Address.|
|Type|string or null|
|Read Only|True|

**IPv6Addresses[{item}].AddressOrigin**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|How the address was determined.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```DHCP```|The address is provided by a DHCP service.|
|```Static```|A static address as configured by the user.|
|```SLAAC```|The address is provided by a Stateless Address AutoConfiguration (SLAAC) service.|

**IPv6Addresses[{item}].AddressState**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The current state of this address as defined in RFC 4862.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```Preferred```|This address is currently within both its valid and preferred lifetimes as defined in RFC 4862.|
|```Deprecated```|This address is currently within its valid lifetime, but the address is now outside of its preferred lifetime as defined in RFC 4862.|
|```Tentative```|This address is currently undergoing Duplicate Address Detection testing as defined in RFC 4862 section 5.4.|
|```Failed```|This address has a problem with Duplicate Address Detection testing as defined in RFC 4862 section 5.4 and is not currently in use.|

**IPv6Addresses[{item}].PrefixLength**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv6 Address Prefix Length.|
|Type|integer or null|
|Read Only|True|

### IPv6DefaultGateway
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv6 default gateway address that is currently in use on this interface.|
|Type|string or null|
|Read Only|True|

### IPv6StaticAddresses (array)
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```IPv6StaticAddresses``` is an array containing elements of:

**IPv6StaticAddresses[{item}].Address**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|A valid IPv6 address.|
|Type|string or null|
|Read Only|False|

**IPv6StaticAddresses[{item}].PrefixLength**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The Prefix Length of this IPv6 address.|
|Type|integer or null|
|Read Only|False|

### InterfaceEnabled
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|This indicates whether this interface is enabled.|
|Type|boolean or null|
|Read Only|False|

### LinkStatus
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The link status of this interface (port).|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```LinkUp```|The link is available for communication on this interface.|
|```NoLink```|There is no link or connection detected on this interface.|
|```LinkDown```|There is no link on this interface, but the interface is connected.|

### MACAddress
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The effective current MAC address. If the assignable MAC address is not supported, this is a read-only alias of FactoryMacAddress.|
|Type|string or null|
|Read Only|True|

### MTUSize
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|This is the currently configured Maximum Transmission Unit (MTU) in bytes on this interface.|
|Type|number or null|
|Read Only|False|

### MaxIPv6StaticAddresses
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|This indicates the maximum number of Static IPv6 addresses that can be configured on this interface.|
|Type|number or null|
|Read Only|True|

### NameServers (array)
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```NameServers``` is an array containing elements of:


| | |
|---|---|
|Type|string or null|
|Read Only|True|

### Oem.Hpe.ConfigurationSettings
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The state of the currently displayed configuration settings.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Current```|All configuration settings for this NIC are currently in use.|
|```SomePendingReset```|One or more configuration settings on this NIC are not yet in use.  They require a reset of this management processor in order to take effect.|

### Oem.Hpe.DHCPv4
**Oem.Hpe.DHCPv4.Enabled**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether DHCPv4 is enabled.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.DHCPv4.UseDNSServers**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether to use DHCPv4-supplied DNS servers. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.DHCPv4.UseDomainName**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether to use a DHCPv4-supplied domain name. Can only be enabled when DHCPv4 is also enabled; otherwis,e this property will be set to false and will be read-only.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.DHCPv4.UseGateway**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether to use a DHCPv4-supplied gateway. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.DHCPv4.UseNTPServers**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether to use DHCPv4-supplied NTP servers. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.DHCPv4.UseStaticRoutes**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether to use DHCPv4-supplied static routes. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.DHCPv4.UseWINSServers**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether to use DHCPv4-supplied WINS servers. Can only be enabled when DHCPv4 is also enabled; otherwise, this property will be set to false and will be read-only.|
|Type|boolean|
|Read Only|False|

### Oem.Hpe.DomainName
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Domain name of the network to which this management processor belongs. This property can only be modified when the management processor is not configured to use a DHCP supplied domain name; otherwise this property is read-only indicating the value is provided by DHCP.|
|Type|string|
|Read Only|False|

### Oem.Hpe.HostName
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The management processor host name.|
|Type|string|
|Read Only|False|

### Oem.Hpe.IPv4
**Oem.Hpe.IPv4.DDNSRegistration**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether DDNS registration is enabled.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.IPv4.DNSSearch**
**Oem.Hpe.IPv4.DNSSearch.AvailableSettings**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Currently configured IPv4 DNS Domain servers.|
|Type|string|
|Read Only|True|

**Oem.Hpe.IPv4.DNSSearch.CurrentSettings**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Currently configured IPv4 DNS Domain servers.|
|Type|string|
|Read Only|False|

**Oem.Hpe.IPv4.DNSServers (array)**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```DNSServers``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Oem.Hpe.IPv4.IPv4Addresses (array)**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```IPv4Addresses``` is an array containing elements of:

**IPv4Addresses[{item}].Address**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv4 Address.|
|Type|string or null|
|Read Only|False|

**IPv4Addresses[{item}].Gateway**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv4 gateway for this address.|
|Type|string or null|
|Read Only|False|

**IPv4Addresses[{item}].SubnetMask**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The IPv4 Subnet mask.|
|Type|string or null|
|Read Only|False|

**Oem.Hpe.IPv4.StaticRoutes (array)**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```StaticRoutes``` is an array containing elements of:

**StaticRoutes[{item}].Destination**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|An IPv4 static route destination. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4.|
|Type|string|
|Read Only|False|

**StaticRoutes[{item}].Gateway**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|An IPv4 static route gateway. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4.|
|Type|string|
|Read Only|False|

**StaticRoutes[{item}].SubnetMask**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|An IPv4 static route subnet mask. Only writeable when use of DHCPv4-supplied static routes is disabled; otherwise this property is read-only indicating the value is provided by DHCPv4.|
|Type|string|
|Read Only|False|

**Oem.Hpe.IPv4.WINSRegistration**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether WINS registration is enabled.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.IPv4.WINSServers (array)**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
```WINSServers``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

### Oem.Hpe.NICEnabled
**Oem.Hpe.NICEnabled.AvailableSettings**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether this NIC is enabled or disabled. Enabling one NIC will disable the others. If no NIC is enabled, this management processor is not accessible over the network.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.NICEnabled.CurrentSettings**
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines whether this NIC is enabled or disabled. Enabling one NIC will disable the others. If no NIC is enabled, this management processor is not accessible over the network.|
|Type|boolean|
|Read Only|False|

### Oem.Hpe.PreferredNIC
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|Determines which NIC is the preferred NIC for receiving Alerts.|
|Type|string or null|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```NIC1```|NIC1 is the preferred NIC|
|```NIC2```|NIC2 is the preferred NIC|

### Oem.Hpe.Type
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

### PermanentMACAddress
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|This is the MAC address assigned to this NIC at the factory.|
|Type|string or null|
|Read Only|True|

### SpeedMbps
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The link speed of the Ethernet interface in megabits per second. If Autosense is enabled, this property cannot be modified. This property can only be modified on a dedicated network port. It cannot be modified for blade servers.|
|Type|integer or null|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Null```|
|```1000```|
|```100```|
|```10```|

### Status
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)
See the Redfish standard schema and specification for information on common Status object.

### UefiDevicePath
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|The UEFI device path for this interface.|
|Type|string or null|
|Read Only|True|

### VLAN
Member of [EthernetInterface.v1_2_0.EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)

| | |
|---|---|
|Description|If this Network Interface supports more than one VLAN, this property will not be present and the client should look for VLANs collection in the link section of this resource.|
|Type|string|
|Read Only|True|

## HpeFwRev.v1_0_0.HpeFwRev
```@odata.type: "#HpeFwRev.v1_0_0.HpeFwRev"```
ERROR: No instances found for resource type #HpeFwRev.v1_0_0.HpeFwRev in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeFwRev.v1_0_0.HpeFwRev in the resource map.
## HpeHttpsCert.v1_0_0.HpeHttpsCert
```@odata.type: "#HpeHttpsCert.v1_0_0.HpeHttpsCert"```

This is the schema definition for the X509 Certificate.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/securityservice/httpscert```|GET POST |

### CertificateSigningRequest
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|When a GenerateCSR action is performed, this field contains the generated CSR (in Base64 format). Contains a public and private key pair.|
|Type|string or null|
|Read Only|True|

### CertificateSigningRequestInformation
**CertificateSigningRequestInformation.City**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The city or locality where the company or organization that owns this device is located.|
|Type|string|
|Read Only|True|

**CertificateSigningRequestInformation.CommonName**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The FQDN of this device.|
|Type|string|
|Read Only|True|

**CertificateSigningRequestInformation.Country**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The two-character country code where the company or organization that owns this device is located. Eg: US|
|Type|string|
|Read Only|True|

**CertificateSigningRequestInformation.OrgName**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The name of the company or organization that owns this device.|
|Type|string|
|Read Only|True|

**CertificateSigningRequestInformation.OrgUnit**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The unit within the company or organization that owns this device.|
|Type|string|
|Read Only|True|

**CertificateSigningRequestInformation.State**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The state where the company or organization that owns this device is located.|
|Type|string|
|Read Only|True|

### Type
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

### X509CertificateInformation
**X509CertificateInformation.Issuer**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The Certificate Authority that issued the certificate.|
|Type|string|
|Read Only|True|

**X509CertificateInformation.SerialNumber**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The serial number that the Certificate Authority assigned to the certificate.|
|Type|string|
|Read Only|True|

**X509CertificateInformation.Subject**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The entity to which the certificate was issued.|
|Type|string|
|Read Only|True|

**X509CertificateInformation.ValidNotAfter**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The date on which the certificate validity period ends.|
|Type|string|
|Read Only|True|

**X509CertificateInformation.ValidNotBefore**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

| | |
|---|---|
|Description|The date on which the certificate validity period begins.|
|Type|string|
|Read Only|True|

### Actions

**GenerateSelfSignedCertificate**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)
Imports a Trusted Certificate and resets the device.

There are no parameters for this action.

**ImportCertificate**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)
Imports a Trusted Certificate and resets the device.


**Parameters:**

**Certificate (string)**

Contains PEM formatted X509 certificate (Base64 encoded).

**GenerateCSR**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)

**Parameters:**

**City (string)**

The city or locality where the company or organization that owns this device is located.

**OrgName (string)**

The name of the company or organization that owns this device.

**Country (string)**

The two-character country code where the company or organization that owns this device is located. Eg: US

**CommonName (string)**

The FQDN of this device.

**OrgUnit (string)**

The unit within the company or organization that owns this device.

**State (string)**

The state where the company or organization that owns this device is located.

**ImportCACertificate**
Member of [HpeHttpsCert.v1_0_0.HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)
Imports a Trusted Certificate and resets the device.


**Parameters:**

**Certificate (string)**

Contains PEM formatted X509 certificate (Base64 encoded).
## HpeProcessorExt.v1_0_0.HpeProcessorExt
```@odata.type: "#HpeProcessorExt.v1_0_0.HpeProcessorExt"```
ERROR: No instances found for resource type #HpeProcessorExt.v1_0_0.HpeProcessorExt in the resource map.

HPE CPU Information
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeProcessorExt.v1_0_0.HpeProcessorExt in the resource map.
## HpeSecurityService.v1_0_0.HpeSecurityService
```@odata.type: "#HpeSecurityService.v1_0_0.HpeSecurityService"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/securityservice```|GET PATCH |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Links/HttpsCaCerts```|HpWfmHttpsCertCollection|
|```Links/HttpsCert```|[HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)|

### Oem.Hpe.LoginBanner
**Oem.Hpe.LoginBanner.IsEnabled**
Member of [HpeSecurityService.v1_0_0.HpeSecurityService](#hpesecurityservice-v1_0_0-hpesecurityservice)

| | |
|---|---|
|Description|The login security banner message that is displayed on the management processor Login page.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.LoginBanner.Message**
Member of [HpeSecurityService.v1_0_0.HpeSecurityService](#hpesecurityservice-v1_0_0-hpesecurityservice)

| | |
|---|---|
|Description|The is to enable message that is displayed on the management processor Login page.|
|Type|string|
|Read Only|False|

### Type
Member of [HpeSecurityService.v1_0_0.HpeSecurityService](#hpesecurityservice-v1_0_0-hpesecurityservice)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

## HpeWfmAbsarokaOfflineUpdateTask.v1_0_0.HpeWfmAbsarokaOfflineUpdateTask
```@odata.type: "#HpeWfmAbsarokaOfflineUpdateTask.v1_0_0.HpeWfmAbsarokaOfflineUpdateTask"```
ERROR: No instances found for resource type #HpeWfmAbsarokaOfflineUpdateTask.v1_0_0.HpeWfmAbsarokaOfflineUpdateTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAbsarokaOfflineUpdateTask.v1_0_0.HpeWfmAbsarokaOfflineUpdateTask in the resource map.
## HpeWfmAbsarokaOfflineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOfflineUpdateTaskResults
```@odata.type: "#HpeWfmAbsarokaOfflineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOfflineUpdateTaskResults"```
ERROR: No instances found for resource type #HpeWfmAbsarokaOfflineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOfflineUpdateTaskResults in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAbsarokaOfflineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOfflineUpdateTaskResults in the resource map.
## HpeWfmAbsarokaOnlineUpdateTask.v1_0_0.HpeWfmAbsarokaOnlineUpdateTask
```@odata.type: "#HpeWfmAbsarokaOnlineUpdateTask.v1_0_0.HpeWfmAbsarokaOnlineUpdateTask"```
ERROR: No instances found for resource type #HpeWfmAbsarokaOnlineUpdateTask.v1_0_0.HpeWfmAbsarokaOnlineUpdateTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAbsarokaOnlineUpdateTask.v1_0_0.HpeWfmAbsarokaOnlineUpdateTask in the resource map.
## HpeWfmAbsarokaOnlineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOnlineUpdateTaskResults
```@odata.type: "#HpeWfmAbsarokaOnlineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOnlineUpdateTaskResults"```
ERROR: No instances found for resource type #HpeWfmAbsarokaOnlineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOnlineUpdateTaskResults in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAbsarokaOnlineUpdateTaskResults.v1_0_0.HpeWfmAbsarokaOnlineUpdateTaskResults in the resource map.
## HpeWfmAccountExt.v1_0_0.HpeWfmAccountExt
```@odata.type: "#HpeWfmAccountExt.v1_0_0.HpeWfmAccountExt"```
ERROR: No instances found for resource type #HpeWfmAccountExt.v1_0_0.HpeWfmAccountExt in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAccountExt.v1_0_0.HpeWfmAccountExt in the resource map.
## HpeWfmActivityLogs.v1_0_0.HpeWfmActivityLogs
```@odata.type: "#HpeWfmActivityLogs.v1_0_0.HpeWfmActivityLogs"```
ERROR: No instances found for resource type #HpeWfmActivityLogs.v1_0_0.HpeWfmActivityLogs in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmActivityLogs.v1_0_0.HpeWfmActivityLogs in the resource map.
## HpeWfmAggregatorService.v1_0_0.HpeWfmAggregatorService
```@odata.type: "#HpeWfmAggregatorService.v1_0_0.HpeWfmAggregatorService"```

This is the schema definition for the Aggregator service. It represents the properties for this service and has links to the Systems and federation groups managed by iLO Amplifier Pack.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/aggregatorservice```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```FederationGroups```|[ERROR_UNKNOWN](#error_unknown-v0_0_0-error_unknown)|
|```Systems```|[ERROR_UNKNOWN](#error_unknown-v0_0_0-error_unknown)|

### FederationGroups
This property references a resource of type Collection with a MemberType of Federation groups.
### Systems
This property references a resource of type Collection with a MemberType of Systems.
## HpeWfmAhsDownloadTask.v1_0_0.HpeWfmAhsDownloadTask
```@odata.type: "#HpeWfmAhsDownloadTask.v1_0_0.HpeWfmAhsDownloadTask"```
ERROR: No instances found for resource type #HpeWfmAhsDownloadTask.v1_0_0.HpeWfmAhsDownloadTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAhsDownloadTask.v1_0_0.HpeWfmAhsDownloadTask in the resource map.
## HpeWfmAlertService.v1_0_0.HpeWfmAlertService
```@odata.type: "#HpeWfmAlertService.v1_0_0.HpeWfmAlertService"```
ERROR: No instances found for resource type #HpeWfmAlertService.v1_0_0.HpeWfmAlertService in the resource map.

The Alert Service Settings.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAlertService.v1_0_0.HpeWfmAlertService in the resource map.
## HpeWfmApplyConfigurationBaselineTask.v1_0_0.HpeWfmApplyConfigurationBaselineTask
```@odata.type: "#HpeWfmApplyConfigurationBaselineTask.v1_0_0.HpeWfmApplyConfigurationBaselineTask"```
ERROR: No instances found for resource type #HpeWfmApplyConfigurationBaselineTask.v1_0_0.HpeWfmApplyConfigurationBaselineTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmApplyConfigurationBaselineTask.v1_0_0.HpeWfmApplyConfigurationBaselineTask in the resource map.
## HpeWfmAssignRecoveryPersonaTask.v1_0_0.HpeWfmAssignRecoveryPersonaTask
```@odata.type: "#HpeWfmAssignRecoveryPersonaTask.v1_0_0.HpeWfmAssignRecoveryPersonaTask"```
ERROR: No instances found for resource type #HpeWfmAssignRecoveryPersonaTask.v1_0_0.HpeWfmAssignRecoveryPersonaTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmAssignRecoveryPersonaTask.v1_0_0.HpeWfmAssignRecoveryPersonaTask in the resource map.
## HpeWfmBaseline.v1_0_0.HpeWfmBaseline
```@odata.type: "#HpeWfmBaseline.v1_0_0.HpeWfmBaseline"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/baselineservice/baselines/{item}```|GET DELETE |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Components```|[ERROR_UNKNOWN](#error_unknown-v0_0_0-error_unknown)|

### BaselineState
Member of [HpeWfmBaseline.v1_0_0.HpeWfmBaseline](#hpewfmbaseline-v1_0_0-hpewfmbaseline)

| | |
|---|---|
|Description|This property indicates the state of inventory for this resource.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```ImportInProgress```|Import of the baseline is in progress.|
|```ImportSuccess```|Import of the baseline was completed successfully.|
|```ImportFailed```|Import of the baseline failed.|

### Components
The URI refers to collection of components in the baseline.
### RelatedTask
The URI refers to the task which is created to import this baseline.
### SizeInMB
Member of [HpeWfmBaseline.v1_0_0.HpeWfmBaseline](#hpewfmbaseline-v1_0_0-hpewfmbaseline)

| | |
|---|---|
|Description|Space on disk (in MB) used by this baseline.|
|Type|integer|
|Read Only|True|

### Version
Member of [HpeWfmBaseline.v1_0_0.HpeWfmBaseline](#hpewfmbaseline-v1_0_0-hpewfmbaseline)

| | |
|---|---|
|Description|The version of the Baseline|
|Type|string|
|Read Only|True|

## HpeWfmBaselineComponents.v1_0_0.HpeWfmBaselineComponents
```@odata.type: "#HpeWfmBaselineComponents.v1_0_0.HpeWfmBaselineComponents"```
ERROR: No instances found for resource type #HpeWfmBaselineComponents.v1_0_0.HpeWfmBaselineComponents in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmBaselineComponents.v1_0_0.HpeWfmBaselineComponents in the resource map.
## HpeWfmBaselineService.v1_0_0.HpeWfmBaselineService
```@odata.type: "#HpeWfmBaselineService.v1_0_0.HpeWfmBaselineService"```

This is the schema definition for the Baseline Service.  It represents the properties for the service itself and has links to the various baselines that are imported.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/baselineservice```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Baselines```|Collection of [HpeWfmBaseline](#hpewfmbaseline-v1_0_0-hpewfmbaseline)|

### Baselines
This property references a collection resource of imported baselines.
### DateTime
Member of [HpeWfmBaselineService.v1_0_0.HpeWfmBaselineService](#hpewfmbaselineservice-v1_0_0-hpewfmbaselineservice)

| | |
|---|---|
|Description|The current DateTime (with offset) setting that the task service is using.|
|Type|string or null|
|Read Only|True|

### FreeSpaceInMB
Member of [HpeWfmBaselineService.v1_0_0.HpeWfmBaselineService](#hpewfmbaselineservice-v1_0_0-hpewfmbaselineservice)

| | |
|---|---|
|Description|Free space of disk (in MB) remaining for importing baselines .|
|Type|integer|
|Read Only|True|

### ServiceEnabled
Member of [HpeWfmBaselineService.v1_0_0.HpeWfmBaselineService](#hpewfmbaselineservice-v1_0_0-hpewfmbaselineservice)

| | |
|---|---|
|Description|This indicates whether this service is enabled.|
|Type|boolean or null|
|Read Only|True|

### Status
Member of [HpeWfmBaselineService.v1_0_0.HpeWfmBaselineService](#hpewfmbaselineservice-v1_0_0-hpewfmbaselineservice)
See the Redfish standard schema and specification for information on common Status object.

### TotalSpaceInMB
Member of [HpeWfmBaselineService.v1_0_0.HpeWfmBaselineService](#hpewfmbaselineservice-v1_0_0-hpewfmbaselineservice)

| | |
|---|---|
|Description|Total space of disk (in MB) allocated for importing baselines .|
|Type|integer|
|Read Only|True|

## HpeWfmComputerSystem.v1_0_0.HpeWfmComputerSystem
```@odata.type: "#HpeWfmComputerSystem.v1_0_0.HpeWfmComputerSystem"```
ERROR: No instances found for resource type #HpeWfmComputerSystem.v1_0_0.HpeWfmComputerSystem in the resource map.

The Management Processor General Network Settings.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmComputerSystem.v1_0_0.HpeWfmComputerSystem in the resource map.
## HpeWfmConfigureRemoteSyslogTask.v1_0_0.HpeWfmConfigureRemoteSyslogTask
```@odata.type: "#HpeWfmConfigureRemoteSyslogTask.v1_0_0.HpeWfmConfigureRemoteSyslogTask"```
ERROR: No instances found for resource type #HpeWfmConfigureRemoteSyslogTask.v1_0_0.HpeWfmConfigureRemoteSyslogTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmConfigureRemoteSyslogTask.v1_0_0.HpeWfmConfigureRemoteSyslogTask in the resource map.
## HpeWfmCreateGroupTask.v1_0_0.HpeWfmCreateGroupTask
```@odata.type: "#HpeWfmCreateGroupTask.v1_0_0.HpeWfmCreateGroupTask"```
ERROR: No instances found for resource type #HpeWfmCreateGroupTask.v1_0_0.HpeWfmCreateGroupTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmCreateGroupTask.v1_0_0.HpeWfmCreateGroupTask in the resource map.
## HpeWfmDateTime.v1_0_0.HpeWfmDateTime
```@odata.type: "#HpeWfmDateTime.v1_0_0.HpeWfmDateTime"```

The management processor date and time.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/datetime```|GET PATCH |

### ConfigurationSettings
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The state of the currently displayed configuration settings.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Current```|
|```SomePendingReset```|

### DateTime
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The date and time used by management processor.|
|Type|string|
|Read Only|True|

### Modified
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|This property has been deprecated. It indicates the last time the resource was modified.|
|Type|string|
|Read Only|True|

### NTPServers (array)
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)
```NTPServers``` is an array containing elements of:


| | |
|---|---|
|Description|The current NTP server's IPv4 address, IPv6 address, or FQDN. The value either comes from DHCP or is static depending on the DHCP settings.|
|Type|string|
|Read Only|True|

### StaticNTPServers (array)
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)
```StaticNTPServers``` is an array containing elements of:


| | |
|---|---|
|Description|The static NTP server's IPv4 address, IPv6 address, or FQDN. To set this property, management processor must not be configured to use NTP servers provided by DHCPv4 or DHCPv6.|
|Type|string|
|Read Only|True|

### StaticNTPServersEnabled
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|Specifies whether manually specified NTP servers are enabled or not.|
|Type|boolean|
|Read Only|False|

### TimeZone
**TimeZone.Index**
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The index of the current time zone. To set a new time zone, specify a different time zone index. This property can be set only when DHCPv4 or DHCPv6 supplied time settings are disabled. Since the time zone list might vary from one firmware version to another (which often leads to differences in time zone indices), setting the time zone by name is recommended over setting by index, for better compatibility.|
|Type|number|
|Read Only|False|

**TimeZone.UtcOffset**
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The UTC offset of the current time zone, in the format {+/-}hh:mm|
|Type|string|
|Read Only|True|

**TimeZone.Value**
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The environment variable value.|
|Type|string|
|Read Only|True|

### TimeZoneList (array)
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)
```TimeZoneList``` is an array containing elements of:

**TimeZoneList[{item}].Index**
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The time zone index.|
|Type|number|
|Read Only|True|

**TimeZoneList[{item}].UtcOffset**
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The UTC offset of the time zone, in the format {+/-}hh:mm|
|Type|string|
|Read Only|True|

**TimeZoneList[{item}].Value**
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|The environment variable value.|
|Type|string|
|Read Only|True|

### Type
Member of [HpeWfmDateTime.v1_0_0.HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

## HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs
```@odata.type: "#HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs"```

 
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/debuglogpolicy```|GET POST PATCH |

### DownloadStatus
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)

| | |
|---|---|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```DownloadInProgress```|Downloading log files is in progress|
|```Idle```|There is no ongoing download.|

### LogPolicy (array)
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)
```LogPolicy``` is an array containing elements of:

**LogPolicy[{item}].logLevel**
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)

| | |
|---|---|
|Description|Log level for a particular module|
|Type|string|
|Read Only|False|

**LogPolicy[{item}].module**
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)

| | |
|---|---|
|Description|Module name being referred to change log policy|
|Type|string|
|Read Only|False|

### Modified
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)

| | |
|---|---|
|Description|This property has been deprecated. It indicates the last time the resource was modified.|
|Type|string|
|Read Only|True|

### Type
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

### WritePolicy
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)

| | |
|---|---|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```WriteImmediately```|The Log write policy is Write Immediately|
|```WriteDaily```|The Log write policy is Write Daily|
|```WriteTimely```|The Log write policy is Write Timely|

### Actions

**CollateLogs**
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)
There are no parameters for this action.

**AuditLogs**
Member of [HpeWfmDebugLogs.v1_0_0.HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)
There are no parameters for this action.
## HpeWfmDeleteTask.v1_0_0.HpeWfmDeleteTask
```@odata.type: "#HpeWfmDeleteTask.v1_0_0.HpeWfmDeleteTask"```
ERROR: No instances found for resource type #HpeWfmDeleteTask.v1_0_0.HpeWfmDeleteTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmDeleteTask.v1_0_0.HpeWfmDeleteTask in the resource map.
## HpeWfmDirectory.v1_0_0.HpeWfmDirectory
```@odata.type: "#HpeWfmDirectory.v1_0_0.HpeWfmDirectory"```
ERROR: No instances found for resource type #HpeWfmDirectory.v1_0_0.HpeWfmDirectory in the resource map.

This is the schema definition for the Directory Access service. It represents the properties for this service and has links to the list of directories.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmDirectory.v1_0_0.HpeWfmDirectory in the resource map.
## HpeWfmDirectoryAccessService.v1_0_0.HpeWfmDirectoryAccessService
```@odata.type: "#HpeWfmDirectoryAccessService.v1_0_0.HpeWfmDirectoryAccessService"```
ERROR: No instances found for resource type #HpeWfmDirectoryAccessService.v1_0_0.HpeWfmDirectoryAccessService in the resource map.

This is the schema definition for the Directory Access service. It represents the properties for this service and has links to the list of directories.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmDirectoryAccessService.v1_0_0.HpeWfmDirectoryAccessService in the resource map.
## HpeWfmDirectoryGroup.v1_0_0.HpeWfmDirectoryGroup
```@odata.type: "#HpeWfmDirectoryGroup.v1_0_0.HpeWfmDirectoryGroup"```
ERROR: No instances found for resource type #HpeWfmDirectoryGroup.v1_0_0.HpeWfmDirectoryGroup in the resource map.

This is the schema definition for the Directory Access service. It represents the properties for this service and has links to the list of directories.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmDirectoryGroup.v1_0_0.HpeWfmDirectoryGroup in the resource map.
## HpeWfmDiscoverFederationGroup.v1_0_0.HpeWfmDiscoverFederationGroup
```@odata.type: "#HpeWfmDiscoverFederationGroup.v1_0_0.HpeWfmDiscoverFederationGroup"```
ERROR: No instances found for resource type #HpeWfmDiscoverFederationGroup.v1_0_0.HpeWfmDiscoverFederationGroup in the resource map.

Discover federation groups that are part of Manager.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmDiscoverFederationGroup.v1_0_0.HpeWfmDiscoverFederationGroup in the resource map.
## HpeWfmDownloadReportsTask.v1_0_0.HpeWfmDownloadReportsTask
```@odata.type: "#HpeWfmDownloadReportsTask.v1_0_0.HpeWfmDownloadReportsTask"```
ERROR: No instances found for resource type #HpeWfmDownloadReportsTask.v1_0_0.HpeWfmDownloadReportsTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmDownloadReportsTask.v1_0_0.HpeWfmDownloadReportsTask in the resource map.
## HpeWfmEnvironmentMetrics.v1_0_0.HpeWfmEnvironmentMetrics
```@odata.type: "#HpeWfmEnvironmentMetrics.v1_0_0.HpeWfmEnvironmentMetrics"```
ERROR: No instances found for resource type #HpeWfmEnvironmentMetrics.v1_0_0.HpeWfmEnvironmentMetrics in the resource map.

This resource contains the data about a sensor environment.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmEnvironmentMetrics.v1_0_0.HpeWfmEnvironmentMetrics in the resource map.
## HpeWfmEnvironmentMetricsExt.v1_0_0.HpeWfmEnvironmentMetricsExt
```@odata.type: "#HpeWfmEnvironmentMetricsExt.v1_0_0.HpeWfmEnvironmentMetricsExt"```
ERROR: No instances found for resource type #HpeWfmEnvironmentMetricsExt.v1_0_0.HpeWfmEnvironmentMetricsExt in the resource map.

This resource contains the data about a sensor environment.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmEnvironmentMetricsExt.v1_0_0.HpeWfmEnvironmentMetricsExt in the resource map.
## HpeWfmEthernetNetworkInterface.v1_0_0.HpeWfmEthernetNetworkInterface
```@odata.type: "#HpeWfmEthernetNetworkInterface.v1_0_0.HpeWfmEthernetNetworkInterface"```
ERROR: No instances found for resource type #HpeWfmEthernetNetworkInterface.v1_0_0.HpeWfmEthernetNetworkInterface in the resource map.

The Management Processor General Network Settings.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmEthernetNetworkInterface.v1_0_0.HpeWfmEthernetNetworkInterface in the resource map.
## HpeWfmFederationGroup.v1_0_0.HpeWfmFederationGroup
```@odata.type: "#HpeWfmFederationGroup.v1_0_0.HpeWfmFederationGroup"```
ERROR: No instances found for resource type #HpeWfmFederationGroup.v1_0_0.HpeWfmFederationGroup in the resource map.

This is the schema definition for the Aggregator service. It represents the properties for this service and has links to the Systems and federation groups managed by iLO Amplifier Pack.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmFederationGroup.v1_0_0.HpeWfmFederationGroup in the resource map.
## HpeWfmHttpsCert.v1_0_0.HpeWfmHttpsCert
```@odata.type: "#HpeWfmHttpsCert.v1_0_0.HpeWfmHttpsCert"```
ERROR: No instances found for resource type #HpeWfmHttpsCert.v1_0_0.HpeWfmHttpsCert in the resource map.

This is the schema definition for the X509 Certificate.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmHttpsCert.v1_0_0.HpeWfmHttpsCert in the resource map.
## HpeWfmImportBaselineTask.v1_0_0.HpeWfmImportBaselineTask
```@odata.type: "#HpeWfmImportBaselineTask.v1_0_0.HpeWfmImportBaselineTask"```
ERROR: No instances found for resource type #HpeWfmImportBaselineTask.v1_0_0.HpeWfmImportBaselineTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmImportBaselineTask.v1_0_0.HpeWfmImportBaselineTask in the resource map.
## HpeWfmImportConfigurationBaselineTask.v1_0_0.HpeWfmImportConfigurationBaselineTask
```@odata.type: "#HpeWfmImportConfigurationBaselineTask.v1_0_0.HpeWfmImportConfigurationBaselineTask"```
ERROR: No instances found for resource type #HpeWfmImportConfigurationBaselineTask.v1_0_0.HpeWfmImportConfigurationBaselineTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmImportConfigurationBaselineTask.v1_0_0.HpeWfmImportConfigurationBaselineTask in the resource map.
## HpeWfmImportOSBaselineTask.v1_0_0.HpeWfmImportOSBaselineTask
```@odata.type: "#HpeWfmImportOSBaselineTask.v1_0_0.HpeWfmImportOSBaselineTask"```
ERROR: No instances found for resource type #HpeWfmImportOSBaselineTask.v1_0_0.HpeWfmImportOSBaselineTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmImportOSBaselineTask.v1_0_0.HpeWfmImportOSBaselineTask in the resource map.
## HpeWfmInstallLicenseTask.v1_0_0.HpeWfmInstallLicenseTask
```@odata.type: "#HpeWfmInstallLicenseTask.v1_0_0.HpeWfmInstallLicenseTask"```
ERROR: No instances found for resource type #HpeWfmInstallLicenseTask.v1_0_0.HpeWfmInstallLicenseTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmInstallLicenseTask.v1_0_0.HpeWfmInstallLicenseTask in the resource map.
## HpeWfmLicense.v1_0_0.HpeWfmLicense
```@odata.type: "#HpeWfmLicense.v1_0_0.HpeWfmLicense"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/licenseservice/{item}```|GET |

### License
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|Describes the name of the license installed on management processor.|
|Type|string|
|Read Only|True|

### LicenseFirstName
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|First name.|
|Type|string|
|Read Only|True|

### LicenseKey
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|The installed license key.Will be set to NULL on read.|
|Type|string or null|
|Read Only|False|

### LicenseLastName
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|Last name.|
|Type|string|
|Read Only|True|

### LicenseMailID
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|Users email ID .|
|Type|string|
|Read Only|True|

### LicenseOrganization
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|Organization name.|
|Type|string|
|Read Only|True|

### LicenseType
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|Indicates whether the license is Perpetual or Evaluation.|
|Type|string|
|Read Only|True|

### LicensedNoOfServers
Member of [HpeWfmLicense.v1_0_0.HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)

| | |
|---|---|
|Description|Indicates the number of servers that can be managed.|
|Type|integer|
|Read Only|True|

## HpeWfmLogEntry.v1_0_0.HpeWfmLogEntry
```@odata.type: "#HpeWfmLogEntry.v1_0_0.HpeWfmLogEntry"```
ERROR: No instances found for resource type #HpeWfmLogEntry.v1_0_0.HpeWfmLogEntry in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmLogEntry.v1_0_0.HpeWfmLogEntry in the resource map.
## HpeWfmManagedGroup.v1_0_0.HpeWfmManagedGroup
```@odata.type: "#HpeWfmManagedGroup.v1_0_0.HpeWfmManagedGroup"```
ERROR: No instances found for resource type #HpeWfmManagedGroup.v1_0_0.HpeWfmManagedGroup in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManagedGroup.v1_0_0.HpeWfmManagedGroup in the resource map.
## HpeWfmManagedGroupSession.v1_0_0.HpeWfmManagedGroupSession
```@odata.type: "#HpeWfmManagedGroupSession.v1_0_0.HpeWfmManagedGroupSession"```
ERROR: No instances found for resource type #HpeWfmManagedGroupSession.v1_0_0.HpeWfmManagedGroupSession in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManagedGroupSession.v1_0_0.HpeWfmManagedGroupSession in the resource map.
## HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes
```@odata.type: "#HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managednodes```|GET POST PATCH |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Links/ManagedGroups```|HpeWfmManagedGroupCollection|
|```Links/ManagedSystems```|HpeWfmManagedSystemCollection|
|```Links/RedfishSystems```|HpeWfmManagedSystemCollection|
|```Links/ManagedSystemsSummary```|HpeWfmSystemSummaryCollection|
|```Links/RedfishSystemsSummary```|HpeWfmSystemSummaryCollection|
|```Links/ReportsSummary```|Collection of [HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)|
|```Links/LogServices```|Collection of [LogService](#logservice-v1_0_3-logservice)|

### ActionStatus
**ActionStatus.DiscoverServersFromCSV**
**ActionStatus.DiscoverServersFromCSV.DiscoveryStatus**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The status of the discovery process.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```NotInitiated```|Discovery process is not initiated|
|```Queued```|Discovery process is queued|
|```InProgress```|Discovery process is in progress|
|```Successful```|Discovery process is successfully completed|
|```PartiallySuccessful```|Discovery process is partially successful and completed|
|```Failed```|Discovery process is completed and is failed|

**ActionStatus.DiscoverServersFromCSV.ProgressPercent**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The progress percent of the discovery process.|
|Type|integer|
|Read Only|True|

**ActionStatus.DiscoverServersInRange**
**ActionStatus.DiscoverServersInRange.DiscoveryStatus**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The status of the discovery process.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```NotInitiated```|Discovery process is not initiated|
|```Queued```|Discovery process is queued|
|```InProgress```|Discovery process is in progress|
|```Successful```|Discovery process is successfully completed|
|```PartiallySuccessful```|Discovery process is partially successful and completed|
|```Failed```|Discovery process is completed and is failed|

**ActionStatus.DiscoverServersInRange.EndAddress**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The ending address at which the discovery process stops.|
|Type|string|
|Read Only|True|

**ActionStatus.DiscoverServersInRange.ProgressPercent**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The progress percent of the discovery process.|
|Type|integer|
|Read Only|True|

**ActionStatus.DiscoverServersInRange.StartAddress**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The starting address at which the discovery process begins.|
|Type|string|
|Read Only|True|

**ActionStatus.RefreshAll**
**ActionStatus.RefreshAll.IsUserInitiated**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The flag indicates whether the refresh is initiated by user.|
|Type|boolean|
|Read Only|True|

**ActionStatus.RefreshAll.ProgressPercent**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The progress percent of the Refresh process.|
|Type|integer|
|Read Only|True|

**ActionStatus.RefreshAll.RefreshStatus**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The status of the refresh process.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```NotInitiated```|Refresh process is not initiated|
|```InProgress```|Refresh process is in progress|
|```Successful```|Refresh process is successfully completed|
|```Failed```|Refresh process is completed and is failed|

### AggregatedHealth
**AggregatedHealth.Critical**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The number of systems with Critical health status that are managed by this device.|
|Type|integer|
|Read Only|True|

**AggregatedHealth.OK**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The number of systems with OK health status that are managed by this device.|
|Type|integer|
|Read Only|True|

**AggregatedHealth.Unknown**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The number of systems with unknown health status that are managed by this device.|
|Type|integer|
|Read Only|True|

**AggregatedHealth.Warning**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The number of systems with Warning health status that are managed by this device.|
|Type|integer|
|Read Only|True|

### AutoRefreshMode
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|If enabled, servers will be refreshed automatically in intervals based on the total number of managed Nodes.|
|Type|boolean|
|Read Only|False|

### ContinousDiscovery
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|If enabled, the information of nodes and groups are refreshed at a regular interval. The regular interval is specified by RefreshInterval.|
|Type|boolean|
|Read Only|False|

### IntelligentPriovisioningEULA
**IntelligentPriovisioningEULA.extref**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The URI of an external resource.|
|Type|string|
|Read Only|True|

### RefreshIntervalInHours
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The time interval in minutes when refresh of information of nodes and groups are initiated again.|
|Type|integer|
|Read Only|False|

The following are the supported values:

|Value|
|---|
|```6```|
|```8```|
|```12```|
|```24```|

### SystemsCount
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

| | |
|---|---|
|Description|The number of systems managed by Central Management Device.|
|Type|integer|
|Read Only|True|

### Actions

**RefreshAll**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)
There are no parameters for this action.

**DiscoverServersFromCSV**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

**Parameters:**

**File (string)**

CSV file content

**DiscoverServersInRange**
Member of [HpeWfmManagedNodes.v1_0_0.HpeWfmManagedNodes](#hpewfmmanagednodes-v1_0_0-hpewfmmanagednodes)

**Parameters:**

**UserName (string)**

**EndAddress (string)**

**StartAddress (string)**

**PortNumber (integer)**

**Password (string)**
## HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem
```@odata.type: "#HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem"```
ERROR: No instances found for resource type #HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem in the resource map.
## HpeWfmManagedSystemSession.v1_0_0.HpeWfmManagedSystemSession
```@odata.type: "#HpeWfmManagedSystemSession.v1_0_0.HpeWfmManagedSystemSession"```
ERROR: No instances found for resource type #HpeWfmManagedSystemSession.v1_0_0.HpeWfmManagedSystemSession in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManagedSystemSession.v1_0_0.HpeWfmManagedSystemSession in the resource map.
## HpeWfmManagerExt.v1_0_0.HpeWfmManagerExt
```@odata.type: "#HpeWfmManagerExt.v1_0_0.HpeWfmManagerExt"```
ERROR: No instances found for resource type #HpeWfmManagerExt.v1_0_0.HpeWfmManagerExt in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManagerExt.v1_0_0.HpeWfmManagerExt in the resource map.
## HpeWfmManagerNetworkService.v1_0_0.HpeWfmManagerNetworkService
```@odata.type: "#HpeWfmManagerNetworkService.v1_0_0.HpeWfmManagerNetworkService"```
ERROR: No instances found for resource type #HpeWfmManagerNetworkService.v1_0_0.HpeWfmManagerNetworkService in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManagerNetworkService.v1_0_0.HpeWfmManagerNetworkService in the resource map.
## HpeWfmManualRecoveryTask.v1_0_0.HpeWfmManualRecoveryTask
```@odata.type: "#HpeWfmManualRecoveryTask.v1_0_0.HpeWfmManualRecoveryTask"```
ERROR: No instances found for resource type #HpeWfmManualRecoveryTask.v1_0_0.HpeWfmManualRecoveryTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManualRecoveryTask.v1_0_0.HpeWfmManualRecoveryTask in the resource map.
## HpeWfmManualRecoveryTaskResults.v1_0_0.HpeWfmManualRecoveryTaskResults
```@odata.type: "#HpeWfmManualRecoveryTaskResults.v1_0_0.HpeWfmManualRecoveryTaskResults"```
ERROR: No instances found for resource type #HpeWfmManualRecoveryTaskResults.v1_0_0.HpeWfmManualRecoveryTaskResults in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmManualRecoveryTaskResults.v1_0_0.HpeWfmManualRecoveryTaskResults in the resource map.
## HpeWfmNiOnlineUpdateTaskResults.v1_0_0.HpeWfmNiOnlineUpdateTaskResults
```@odata.type: "#HpeWfmNiOnlineUpdateTaskResults.v1_0_0.HpeWfmNiOnlineUpdateTaskResults"```
ERROR: No instances found for resource type #HpeWfmNiOnlineUpdateTaskResults.v1_0_0.HpeWfmNiOnlineUpdateTaskResults in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmNiOnlineUpdateTaskResults.v1_0_0.HpeWfmNiOnlineUpdateTaskResults in the resource map.
## HpeWfmNonInteractiveOnlineUpdateTask.v1_0_0.HpeWfmNonInteractiveOnlineUpdateTask
```@odata.type: "#HpeWfmNonInteractiveOnlineUpdateTask.v1_0_0.HpeWfmNonInteractiveOnlineUpdateTask"```
ERROR: No instances found for resource type #HpeWfmNonInteractiveOnlineUpdateTask.v1_0_0.HpeWfmNonInteractiveOnlineUpdateTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmNonInteractiveOnlineUpdateTask.v1_0_0.HpeWfmNonInteractiveOnlineUpdateTask in the resource map.
## HpeWfmOfflineUpdateTask.v1_0_0.HpeWfmOfflineUpdateTask
```@odata.type: "#HpeWfmOfflineUpdateTask.v1_0_0.HpeWfmOfflineUpdateTask"```
ERROR: No instances found for resource type #HpeWfmOfflineUpdateTask.v1_0_0.HpeWfmOfflineUpdateTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOfflineUpdateTask.v1_0_0.HpeWfmOfflineUpdateTask in the resource map.
## HpeWfmOfflineUpdateTaskResults.v1_0_0.HpeWfmOfflineUpdateTaskResults
```@odata.type: "#HpeWfmOfflineUpdateTaskResults.v1_0_0.HpeWfmOfflineUpdateTaskResults"```
ERROR: No instances found for resource type #HpeWfmOfflineUpdateTaskResults.v1_0_0.HpeWfmOfflineUpdateTaskResults in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOfflineUpdateTaskResults.v1_0_0.HpeWfmOfflineUpdateTaskResults in the resource map.
## HpeWfmOnlineSppUpdateTask.v1_0_0.HpeWfmOnlineSppUpdateTask
```@odata.type: "#HpeWfmOnlineSppUpdateTask.v1_0_0.HpeWfmOnlineSppUpdateTask"```
ERROR: No instances found for resource type #HpeWfmOnlineSppUpdateTask.v1_0_0.HpeWfmOnlineSppUpdateTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOnlineSppUpdateTask.v1_0_0.HpeWfmOnlineSppUpdateTask in the resource map.
## HpeWfmOnlineSppUpdateTaskResults.v1_0_0.HpeWfmOnlineSppUpdateTaskResults
```@odata.type: "#HpeWfmOnlineSppUpdateTaskResults.v1_0_0.HpeWfmOnlineSppUpdateTaskResults"```
ERROR: No instances found for resource type #HpeWfmOnlineSppUpdateTaskResults.v1_0_0.HpeWfmOnlineSppUpdateTaskResults in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOnlineSppUpdateTaskResults.v1_0_0.HpeWfmOnlineSppUpdateTaskResults in the resource map.
## HpeWfmOnlineUpdateTask.v1_0_0.HpeWfmOnlineUpdateTask
```@odata.type: "#HpeWfmOnlineUpdateTask.v1_0_0.HpeWfmOnlineUpdateTask"```
ERROR: No instances found for resource type #HpeWfmOnlineUpdateTask.v1_0_0.HpeWfmOnlineUpdateTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOnlineUpdateTask.v1_0_0.HpeWfmOnlineUpdateTask in the resource map.
## HpeWfmOSBaseline.v1_0_0.HpeWfmOSBaseline
```@odata.type: "#HpeWfmOSBaseline.v1_0_0.HpeWfmOSBaseline"```
ERROR: No instances found for resource type #HpeWfmOSBaseline.v1_0_0.HpeWfmOSBaseline in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOSBaseline.v1_0_0.HpeWfmOSBaseline in the resource map.
## HpeWfmOSBaselineService.v1_0_0.HpeWfmOSBaselineService
```@odata.type: "#HpeWfmOSBaselineService.v1_0_0.HpeWfmOSBaselineService"```
ERROR: No instances found for resource type #HpeWfmOSBaselineService.v1_0_0.HpeWfmOSBaselineService in the resource map.

This is the schema definition for the Baseline Service.  It represents the properties for the service itself and has links to the various baselines that are imported.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOSBaselineService.v1_0_0.HpeWfmOSBaselineService in the resource map.
## HpeWfmOsProvisioningTask.v1_0_0.HpeWfmOsProvisioningTask
```@odata.type: "#HpeWfmOsProvisioningTask.v1_0_0.HpeWfmOsProvisioningTask"```
ERROR: No instances found for resource type #HpeWfmOsProvisioningTask.v1_0_0.HpeWfmOsProvisioningTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmOsProvisioningTask.v1_0_0.HpeWfmOsProvisioningTask in the resource map.
## HpeWfmQuarantineSystemTask.v1_0_0.HpeWfmQuarantineSystemTask
```@odata.type: "#HpeWfmQuarantineSystemTask.v1_0_0.HpeWfmQuarantineSystemTask"```
ERROR: No instances found for resource type #HpeWfmQuarantineSystemTask.v1_0_0.HpeWfmQuarantineSystemTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmQuarantineSystemTask.v1_0_0.HpeWfmQuarantineSystemTask in the resource map.
## HpeWfmRecoveryPolicy.v1_0_0.HpeWfmRecoveryPolicy
```@odata.type: "#HpeWfmRecoveryPolicy.v1_0_0.HpeWfmRecoveryPolicy"```
ERROR: No instances found for resource type #HpeWfmRecoveryPolicy.v1_0_0.HpeWfmRecoveryPolicy in the resource map.

This is the schema definition for the Recovery Policy.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmRecoveryPolicy.v1_0_0.HpeWfmRecoveryPolicy in the resource map.
## HpeWfmRefreshTask.v1_0_0.HpeWfmRefreshTask
```@odata.type: "#HpeWfmRefreshTask.v1_0_0.HpeWfmRefreshTask"```
ERROR: No instances found for resource type #HpeWfmRefreshTask.v1_0_0.HpeWfmRefreshTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmRefreshTask.v1_0_0.HpeWfmRefreshTask in the resource map.
## HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary
```@odata.type: "#HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managednodes/managedsystems/{item}/reportssummary```|GET |

### BasicDeviceInventory
**BasicDeviceInventory.HealthStatus**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|This represents the health status of the system|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```OK```|Normal|
|```Warning```|A condition exists that requires attention|
|```Critical```|A critical condition exists that requires immediate attention|

**BasicDeviceInventory.HostOSName**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Gives the OS Name of the Host.|
|Type|string|
|Read Only|True|

**BasicDeviceInventory.HostOSType**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Gives the OS Type of the Host.|
|Type|integer|
|Read Only|True|

**BasicDeviceInventory.HostOSVersion**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Gives the OS Version of the Host.|
|Type|string|
|Read Only|True|

**BasicDeviceInventory.ManagerFirmwareVersion**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Gives the Firmware Version of the manager.|
|Type|string|
|Read Only|True|

**BasicDeviceInventory.SystemRomActive**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Gives the Active system ROM.|
|Type|string|
|Read Only|True|

### FirmwareInventory
**FirmwareInventory.ArrayControllers (array)**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)
```ArrayControllers``` is an array containing elements of:

**ArrayControllers[{item}].FirmwareVersion**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Indicates the Firmware Version of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].Model**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Indicates the Model of the Array Controller.|
|Type|string|
|Read Only|True|

**FirmwareInventory.FirmwareInvItems (array)**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)
```FirmwareInvItems``` is an array containing elements of:

**FirmwareInvItems[{item}].DeviceClass**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The device class of the item.|
|Type|string or null|
|Read Only|True|

**FirmwareInvItems[{item}].FirmwareId**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The ID of the item.|
|Type|integer|
|Read Only|True|

**FirmwareInvItems[{item}].Key**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The family-specific key of the firmware item used for correlation to a component database.|
|Type|string or null|
|Read Only|True|

**FirmwareInvItems[{item}].Location**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The location of the item.|
|Type|string or null|
|Read Only|True|

**FirmwareInvItems[{item}].Targets (array)**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)
```Targets``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**FirmwareInvItems[{item}].VersionString**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The user-displayable version of the firmware item in string format|
|Type|string or null|
|Read Only|True|

**FirmwareInventory.HostBusAdapters (array)**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)
```HostBusAdapters``` is an array containing elements of:

**HostBusAdapters[{item}].FirmwareVersion**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Indicates the Firmware Version of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

**HostBusAdapters[{item}].Model**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Indicates the Model of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

**FirmwareInventory.NetworkAdapters (array)**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)
```NetworkAdapters``` is an array containing elements of:

**NetworkAdapters[{item}].FirmwareVersion**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Network Adapter firmware version|
|Type|string or null|
|Read Only|True|

**FirmwareInventory.PCIDeviceSummary (array)**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)
```PCIDeviceSummary``` is an array containing elements of:

**PCIDeviceSummary[{item}].DeviceLocation**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Indicates the location of the PCI Device.|
|Type|string|
|Read Only|False|

**PCIDeviceSummary[{item}].DeviceVersion**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|Indicates the device Version of the PCI Device.|
|Type|string|
|Read Only|False|

### HardwareInventory
**HardwareInventory.MemoryStatus**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```OK```|Normal|
|```Warning```|A condition exists that requires attention|
|```Critical```|A critical condition exists that requires immediate attention|

**HardwareInventory.NoOfDimms**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The total number of DIMMs contained in the System.|
|Type|integer or null|
|Read Only|True|

**HardwareInventory.NoOfFans**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The total number of Fans contained in the System.|
|Type|integer or null|
|Read Only|True|

**HardwareInventory.NoOfPowerSupplies**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The total number of PowerSupplies contained in the System.|
|Type|integer or null|
|Read Only|True|

**HardwareInventory.ProcessorCount**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The number of processors in the system.|
|Type|integer or null|
|Read Only|True|

**HardwareInventory.ProcessorModel**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The processor model for the primary or majority of processors in this system.|
|Type|string or null|
|Read Only|True|

**HardwareInventory.ProcessorStatus**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```OK```|Normal|
|```Warning```|A condition exists that requires attention|
|```Critical```|A critical condition exists that requires immediate attention|

**HardwareInventory.TotalCores**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The total number of cores contained in this processor|
|Type|integer or null|
|Read Only|True|

**HardwareInventory.TotalSystemMemoryGiB**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|This is the total amount of memory in the system measured in GiB.|
|Type|integer or null|
|Read Only|True|

### LicenseInventory
**LicenseInventory.LicenseKey**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The license key installed on this management processor. License keys are 25 characters in length and contain both letters and numbers.Use POST method to collection of membertype HpiLOLicense to install / update the license|
|Type|string|
|Read Only|True|

**LicenseInventory.LicenseType**
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The type of license installed on this management processor.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Unlicensed```|
|```Evaluation```|
|```Perpetual```|
|```Subscription```|
|```Internal```|
|```Duration```|
|```Expired```|

### ManagerAddress
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The IP address or DNS of the manager which was added by user.|
|Type|string|
|Read Only|True|

### ManagerFQDN
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The fully qualified domain name of the manager.|
|Type|string|
|Read Only|True|

### ManagerSSLPort
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The Web Server SSL Port of the manager.|
|Type|integer|
|Read Only|True|

### Model
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The model information that the manufacturer uses to refer to this system.|
|Type|string|
|Read Only|True|

### ProductID
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The system product ID.|
|Type|string|
|Read Only|True|

### SerialNumber
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The system serial number.|
|Type|string|
|Read Only|True|

### ServerHostName
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The DNS Host Name, without any domain information|
|Type|string|
|Read Only|True|

### SystemCategory
Member of [HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)

| | |
|---|---|
|Description|The category of the system based on discovery.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Discovered```|
|```Managed```|
|```NotReachable```|

## HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask
```@odata.type: "#HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask"```
ERROR: No instances found for resource type #HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask in the resource map.
## HpeWfmResource.v1_0_0.HpeWfmResource
```@odata.type: "#HpeWfmResource.v1_0_0.HpeWfmResource"```
ERROR: No instances found for resource type #HpeWfmResource.v1_0_0.HpeWfmResource in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmResource.v1_0_0.HpeWfmResource in the resource map.
## HpeWfmSampleTask.v1_0_0.HpeWfmSampleTask
```@odata.type: "#HpeWfmSampleTask.v1_0_0.HpeWfmSampleTask"```
ERROR: No instances found for resource type #HpeWfmSampleTask.v1_0_0.HpeWfmSampleTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmSampleTask.v1_0_0.HpeWfmSampleTask in the resource map.
## HpeWfmSecurityServiceExt.v1_0_0.HpeWfmSecurityServiceExt
```@odata.type: "#HpeWfmSecurityServiceExt.v1_0_0.HpeWfmSecurityServiceExt"```
ERROR: No instances found for resource type #HpeWfmSecurityServiceExt.v1_0_0.HpeWfmSecurityServiceExt in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmSecurityServiceExt.v1_0_0.HpeWfmSecurityServiceExt in the resource map.
## HpeWfmServerProvisioningTask.v1_0_0.HpeWfmServerProvisioningTask
```@odata.type: "#HpeWfmServerProvisioningTask.v1_0_0.HpeWfmServerProvisioningTask"```
ERROR: No instances found for resource type #HpeWfmServerProvisioningTask.v1_0_0.HpeWfmServerProvisioningTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmServerProvisioningTask.v1_0_0.HpeWfmServerProvisioningTask in the resource map.
## HpeWfmServiceExt.v1_0_0.HpeWfmServiceExt
```@odata.type: "#HpeWfmServiceExt.v1_0_0.HpeWfmServiceExt"```
ERROR: No instances found for resource type #HpeWfmServiceExt.v1_0_0.HpeWfmServiceExt in the resource map.

This object represents the extended HP RESTful API root service.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmServiceExt.v1_0_0.HpeWfmServiceExt in the resource map.
## HpeWfmSessionExt.v1_0_0.HpeWfmSessionExt
```@odata.type: "#HpeWfmSessionExt.v1_0_0.HpeWfmSessionExt"```
ERROR: No instances found for resource type #HpeWfmSessionExt.v1_0_0.HpeWfmSessionExt in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmSessionExt.v1_0_0.HpeWfmSessionExt in the resource map.
## HpeWfmSetIndicatorLedTask.v1_0_0.HpeWfmSetIndicatorLedTask
```@odata.type: "#HpeWfmSetIndicatorLedTask.v1_0_0.HpeWfmSetIndicatorLedTask"```
ERROR: No instances found for resource type #HpeWfmSetIndicatorLedTask.v1_0_0.HpeWfmSetIndicatorLedTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmSetIndicatorLedTask.v1_0_0.HpeWfmSetIndicatorLedTask in the resource map.
## HpeWfmSoftwareInventory.v1_0_0.HpeWfmSoftwareInventory
```@odata.type: "#HpeWfmSoftwareInventory.v1_0_0.HpeWfmSoftwareInventory"```
ERROR: No instances found for resource type #HpeWfmSoftwareInventory.v1_0_0.HpeWfmSoftwareInventory in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmSoftwareInventory.v1_0_0.HpeWfmSoftwareInventory in the resource map.
## HpeWfmSppComplianceTask.v1_0_0.HpeWfmSppComplianceTask
```@odata.type: "#HpeWfmSppComplianceTask.v1_0_0.HpeWfmSppComplianceTask"```
ERROR: No instances found for resource type #HpeWfmSppComplianceTask.v1_0_0.HpeWfmSppComplianceTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmSppComplianceTask.v1_0_0.HpeWfmSppComplianceTask in the resource map.
## HpeWfmSppComplianceTaskResults.v1_0_0.HpeWfmSppComplianceTaskResults
```@odata.type: "#HpeWfmSppComplianceTaskResults.v1_0_0.HpeWfmSppComplianceTaskResults"```
ERROR: No instances found for resource type #HpeWfmSppComplianceTaskResults.v1_0_0.HpeWfmSppComplianceTaskResults in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmSppComplianceTaskResults.v1_0_0.HpeWfmSppComplianceTaskResults in the resource map.
## HpeWfmStorageDef.v1_0_0.HpeWfmStorageDef
```@odata.type: "#HpeWfmStorageDef.v1_0_0.HpeWfmStorageDef"```
ERROR: No instances found for resource type #HpeWfmStorageDef.v1_0_0.HpeWfmStorageDef in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmStorageDef.v1_0_0.HpeWfmStorageDef in the resource map.
## HpeWfmStorageManager.v1_0_0.HpeWfmStorageManager
```@odata.type: "#HpeWfmStorageManager.v1_0_0.HpeWfmStorageManager"```
ERROR: No instances found for resource type #HpeWfmStorageManager.v1_0_0.HpeWfmStorageManager in the resource map.

 
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmStorageManager.v1_0_0.HpeWfmStorageManager in the resource map.
## HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary
```@odata.type: "#HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managednodes/managedsystems/{item}/summary```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```SummaryForSystem```|[HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)|

### AMSStatus
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the status of AMS.|
|Type|string|
|Read Only|True|

### ActionCapabilities
**ActionCapabilities.AHSDownload**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for AHS Download.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.AbsarokaOfflineUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Absaroka Offline Update.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.AbsarokaOnlineUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Absaroka Online Update.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.AssignRecovery**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Assign Recovery.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.BaselineAutomaticUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Baseline Automatic Update.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.Delete**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Delete.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.FirmwareUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Firmware Update.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.GroupManage**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Group Manage.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.ImportConfigBaseline**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Import config baseline.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.ManualRecovery**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Manual Recovery.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.OfflineFirmwareUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Offline Firmware Update.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.OnlineFirmwareUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Online Firmware Update.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.Power**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Power.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.Refresh**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Refresh.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.RemoteSyslog**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Remote Syslog.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.UID**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for UID.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.UnAssignRecovery**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Unassign Recovery.|
|Type|boolean|
|Read Only|True|

**ActionCapabilities.VirtualMedia**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Action capability for Virtual Media.|
|Type|boolean|
|Read Only|True|

### ActionErrorMessage
**ActionErrorMessage.AbsarokaOfflineUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Absaroka Offline Update.|
|Type|string|
|Read Only|True|

**ActionErrorMessage.AbsarokaOnlineUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Absaroka Online Update.|
|Type|string|
|Read Only|True|

**ActionErrorMessage.AssignRecovery**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Assign Recovery.|
|Type|string|
|Read Only|True|

**ActionErrorMessage.BaselineAutomaticUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Baseline Automatic Update.|
|Type|string|
|Read Only|True|

**ActionErrorMessage.GroupManage**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Manage Group.|
|Type|string|
|Read Only|True|

**ActionErrorMessage.ImportConfigBaseline**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Import Config Baseline.|
|Type|string|
|Read Only|True|

**ActionErrorMessage.OfflineFirmwareUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Offline Firmware Update.|
|Type|string|
|Read Only|True|

**ActionErrorMessage.OnlineFirmwareUpdate**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The error message for Online Firmware Update.|
|Type|string|
|Read Only|True|

### Discovery
**Discovery.LastRefreshed**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Last refreshed timestamp|
|Type|string|
|Read Only|True|

**Discovery.ProgressPercent**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The progress percent of the discovery|
|Type|integer|
|Read Only|True|

**Discovery.State**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The discovery state|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```NotInitiated```|
|```Processing```|
|```InProgress```|
|```Complete```|
|```NotResponding```|
|```NotReachable```|
|```FirmwareUpdateInProgress```|
|```Discovered```|
|```Refreshing```|

**Discovery.StateDescription**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The description of the state|
|Type|string|
|Read Only|True|

### EncryptionSecurityState
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates the Encryption Security State of the Server |
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Production```|
|```HighSecurity```|
|```FIPS```|

### FederationActionGroupName
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the name of the Group server belongs to.|
|Type|string|
|Read Only|True|

### FederationEnabled
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates whether management processor federation management is enabled or disabled.|
|Type|boolean|
|Read Only|True|

### FederationSupported
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates whether management processor federation is supported.|
|Type|boolean|
|Read Only|True|

### GatewayManaged
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates if the Server is Gateway Managed(Federation Group)|
|Type|boolean|
|Read Only|True|

### HealthStatus
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|This represents the health status of the system|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```OK```|Normal|
|```Warning```|A condition exists that requires attention|
|```Critical```|A critical condition exists that requires immediate attention|

### HostName
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The DNS Host Name, without any domain information|
|Type|string|
|Read Only|True|

### HostOSDescription
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives description about OS on the Host.|
|Type|string|
|Read Only|True|

### HostOSName
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the OS Name of the Host.|
|Type|string|
|Read Only|True|

### HostOSType
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the OS Type of the Host.|
|Type|integer|
|Read Only|True|

### HostOSVersion
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the OS Version of the Host.|
|Type|string|
|Read Only|True|

### IndicatorLED
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The state of the indicator LED.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Unknown```|The state of the Indicator LED cannot be determined.|
|```Lit```|The Indicator LED is lit.|
|```Blinking```|The Indicator LED is blinking.|
|```Off```|The Indicator LED is off.|

### LastTaskStatus
**LastTaskStatus.EndTime**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The date-time stamp that the task was last completed.|
|Type|string|
|Read Only|True|

**LastTaskStatus.Messages (array)**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)
```Messages``` is an array containing elements of:

**Messages[{item}].Message**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|This is the human readable message, if provided.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].MessageArgs (array)**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)
```MessageArgs``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].MessageId**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|This is the key for this message which can be used to look up the message in a message registry.|
|Type|string|
|Read Only|True|

**Messages[{item}].RelatedProperties (array)**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)
```RelatedProperties``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].Resolution**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Used to provide suggestions on how to resolve the situation that caused the error.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].Severity**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|This is the severity of the errors.|
|Type|string or null|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.CreatedBy**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The name of the user that created this task.|
|Type|string|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.DetailedTaskLink**
Detailed status of the task.
**LastTaskStatus.Oem.Hpe.History**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The history of the task.|
|Type|string|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.ProgressMessages (array)**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)
```ProgressMessages``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.ProgressPercent**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The progress percent of this task.|
|Type|integer|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.SelectedAddress (array)**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.SelectedGroups (array)**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)
```SelectedGroups``` is an array containing elements of:

**SelectedGroups[{item}].GroupName**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Group name of the selected group.|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].SelectedAddress (array)**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].allSystemsInGroup**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The flag suggests whether all the servers in the group are selected.|
|Type|boolean|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.SubTaskCount**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Number of subtasks for this task.|
|Type|integer|
|Read Only|True|

**LastTaskStatus.Oem.Hpe.TaskIdentifier**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|A unique task identifier number for this task.|
|Type|integer|
|Read Only|True|

**LastTaskStatus.StartTime**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The date-time stamp that the task was last started.|
|Type|string|
|Read Only|True|

**LastTaskStatus.TaskState**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The state of the task.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```New```|A new task|
|```Starting```|Task is starting|
|```Running```|Task is running normally|
|```Suspended```|Task has been suspended|
|```Interrupted```|Task has been interrupted|
|```Pending```|Task is pending and has not started|
|```Stopping```|Task is in the process of stopping|
|```Completed```|Task has completed|
|```Killed```|Task was terminated|
|```Exception```|Task has stopped due to an exception condition|
|```Service```|Task is running as a service|

**LastTaskStatus.TaskStatus**
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|This is the completion status of the task.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```OK```|Normal|
|```Warning```|A condition exists that requires attention|
|```Critical```|A critical condition exists that requires immediate attention|

### ManagerAddress
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The IP address or DNS of the manager which was added by user.|
|Type|string|
|Read Only|True|

### ManagerFQDN
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The fully qualified domain name of the manager.|
|Type|string|
|Read Only|True|

### ManagerFirmwareVersion
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the Firmware Version of the manager.|
|Type|string|
|Read Only|True|

### ManagerIPAddress
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The IPv4 address of the manager.|
|Type|string|
|Read Only|True|

### ManagerLicense
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the License of the manager.|
|Type|string|
|Read Only|True|

### ManagerSSLPort
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The Web Server SSL Port of the manager.|
|Type|integer|
|Read Only|True|

### ManagerVirtualMediaImage
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The valid URI indicating the image that is mounted on this server. A null value indicates that no image exists.|
|Type|string|
|Read Only|False|

### ManualRecoveryFlag
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates if the Server is set for Manual or Automatic Recovery|
|Type|boolean|
|Read Only|True|

### Manufacturer
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The manaufacturer of the system.|
|Type|string|
|Read Only|True|

### MasterManagerType
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The type of the manager.|
|Type|string|
|Read Only|True|

### Model
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The model information that the manufacturer uses to refer to this system.|
|Type|string|
|Read Only|True|

### NumOfGrpsNodeBelongs
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the number of Federation Groups this iLO is part of.|
|Type|integer|
|Read Only|True|

### PowerState
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|This is the current power state of the system|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```On```|
|```Off```|
|```Unknown```|
|```Reset```|

### ProductID
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The system product ID.|
|Type|string|
|Read Only|True|

### RecoveryAction
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates the Action that is set for recovery|
|Type|string|
|Read Only|True|

### RecoveryPolicyId
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the Recovery Policy Id.|
|Type|integer|
|Read Only|True|

### RecoveryPolicyName
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates the Recovery Persona Applied on the System.|
|Type|string|
|Read Only|True|

### RecoveryStatus
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates the Status of the System.If the recovery install set is applied or not and once recovery starts , its status|
|Type|string|
|Read Only|True|

### SUTMode
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the Mode of HPSUT.|
|Type|string|
|Read Only|True|

### SUTServiceState
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the Service state of HPSUT.|
|Type|string|
|Read Only|True|

### SUTServiceVersion
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the Service Version of HPSUT.|
|Type|string|
|Read Only|True|

### SecurityState
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates the Security State of the System.|
|Type|string|
|Read Only|True|

### SerialNumber
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The system serial number.|
|Type|string|
|Read Only|True|

### StandAloneManaged
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates if the Server is Standalone Managed with Credentials|
|Type|boolean|
|Read Only|True|

### StatusState
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Indicates the State of the System.|
|Type|string|
|Read Only|True|

### SummaryForSystem
Link to the Managed System with detailed information.
### SystemCategory
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The category of the system based on discovery.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Discovered```|
|```Managed```|
|```NotReachable```|

### SystemType
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The system type.|
|Type|string|
|Read Only|True|

### TPMModuleType
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the Module Type of TPM on the Server.|
|Type|string|
|Read Only|True|

### TPMStatus
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|Gives the Status of TPM on the Server.|
|Type|string|
|Read Only|True|

### UUID
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The universal unique identifier for this system.|
|Type|string|
|Read Only|True|

### iLOType
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The iLO type of this Manager|
|Type|string|
|Read Only|True|

### iLOUUID
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The universal unique identifier for the iLO.|
|Type|string|
|Read Only|True|

## HpeWfmTaskExt.v1_0_0.HpeWfmTaskExt
```@odata.type: "#HpeWfmTaskExt.v1_0_0.HpeWfmTaskExt"```
ERROR: No instances found for resource type #HpeWfmTaskExt.v1_0_0.HpeWfmTaskExt in the resource map.

This is the schema definition for a Task resource.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmTaskExt.v1_0_0.HpeWfmTaskExt in the resource map.
## HpeWfmTaskServiceExt.v1_0_0.HpeWfmTaskServiceExt
```@odata.type: "#HpeWfmTaskServiceExt.v1_0_0.HpeWfmTaskServiceExt"```
ERROR: No instances found for resource type #HpeWfmTaskServiceExt.v1_0_0.HpeWfmTaskServiceExt in the resource map.

This is the schema definition for a Task resource.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmTaskServiceExt.v1_0_0.HpeWfmTaskServiceExt in the resource map.
## HpeWfmTelemetryInfo.v1_0_0.HpeWfmTelemetryInfo
```@odata.type: "#HpeWfmTelemetryInfo.v1_0_0.HpeWfmTelemetryInfo"```

The Telemetry Service Settings.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/telemetry```|GET |

### CpuLoadAverage
Member of [HpeWfmTelemetryInfo.v1_0_0.HpeWfmTelemetryInfo](#hpewfmtelemetryinfo-v1_0_0-hpewfmtelemetryinfo)

| | |
|---|---|
|Description|Specifies average load on CPU.|
|Type|integer|
|Read Only|True|

### CpuUsage
Member of [HpeWfmTelemetryInfo.v1_0_0.HpeWfmTelemetryInfo](#hpewfmtelemetryinfo-v1_0_0-hpewfmtelemetryinfo)

| | |
|---|---|
|Description|Specifies CPU usage in KB.|
|Type|integer|
|Read Only|True|

### CurrentTime
Member of [HpeWfmTelemetryInfo.v1_0_0.HpeWfmTelemetryInfo](#hpewfmtelemetryinfo-v1_0_0-hpewfmtelemetryinfo)

| | |
|---|---|
|Description|Specifies current time.|
|Type|string|
|Read Only|True|

### MemUtilizationKB
Member of [HpeWfmTelemetryInfo.v1_0_0.HpeWfmTelemetryInfo](#hpewfmtelemetryinfo-v1_0_0-hpewfmtelemetryinfo)

| | |
|---|---|
|Description|Specifies memory utilization usage in KB.|
|Type|integer|
|Read Only|True|

### TotalMemoryKB
Member of [HpeWfmTelemetryInfo.v1_0_0.HpeWfmTelemetryInfo](#hpewfmtelemetryinfo-v1_0_0-hpewfmtelemetryinfo)

| | |
|---|---|
|Description|Specifies total available memory in KB.|
|Type|integer|
|Read Only|True|

## HpeWfmUnassignRecoveryPolicyTask.v1_0_0.HpeWfmUnassignRecoveryPolicyTask
```@odata.type: "#HpeWfmUnassignRecoveryPolicyTask.v1_0_0.HpeWfmUnassignRecoveryPolicyTask"```
ERROR: No instances found for resource type #HpeWfmUnassignRecoveryPolicyTask.v1_0_0.HpeWfmUnassignRecoveryPolicyTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmUnassignRecoveryPolicyTask.v1_0_0.HpeWfmUnassignRecoveryPolicyTask in the resource map.
## HpeWfmUpdateFirmwareTask.v1_0_0.HpeWfmUpdateFirmwareTask
```@odata.type: "#HpeWfmUpdateFirmwareTask.v1_0_0.HpeWfmUpdateFirmwareTask"```
ERROR: No instances found for resource type #HpeWfmUpdateFirmwareTask.v1_0_0.HpeWfmUpdateFirmwareTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmUpdateFirmwareTask.v1_0_0.HpeWfmUpdateFirmwareTask in the resource map.
## HpeWfmUpdateService.v1_0_0.HpeWfmUpdateService
```@odata.type: "#HpeWfmUpdateService.v1_0_0.HpeWfmUpdateService"```
ERROR: No instances found for resource type #HpeWfmUpdateService.v1_0_0.HpeWfmUpdateService in the resource map.

The schema definition of a simple Ethernet NIC resource.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmUpdateService.v1_0_0.HpeWfmUpdateService in the resource map.
## HpeWfmValidatePersonaTask.v1_0_0.HpeWfmValidatePersonaTask
```@odata.type: "#HpeWfmValidatePersonaTask.v1_0_0.HpeWfmValidatePersonaTask"```
ERROR: No instances found for resource type #HpeWfmValidatePersonaTask.v1_0_0.HpeWfmValidatePersonaTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmValidatePersonaTask.v1_0_0.HpeWfmValidatePersonaTask in the resource map.
## HpeWfmVirtualMediaTask.v1_0_0.HpeWfmVirtualMediaTask
```@odata.type: "#HpeWfmVirtualMediaTask.v1_0_0.HpeWfmVirtualMediaTask"```
ERROR: No instances found for resource type #HpeWfmVirtualMediaTask.v1_0_0.HpeWfmVirtualMediaTask in the resource map.
### Resource Instances
|Uri|HTTP Allow|
|---|---|

ERROR: No instances found for resource type #HpeWfmVirtualMediaTask.v1_0_0.HpeWfmVirtualMediaTask in the resource map.
## LogEntry.v1_1_1.LogEntry
```@odata.type: "#LogEntry.v1_1_1.LogEntry"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/logservices/devicealertlog/entries/{item}```|GET |

### Created
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The date and time when the log entry was created, for example, 2014-04-15T00:38:00Z.|
|Type|string|
|Read Only|True|

### EntryCode
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|If the EntryType is SEL, this will have the entry code for the log entry.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Assert```|
|```Deassert```|
|```Lower Non-critical - going low```|
|```Lower Non-critical - going high```|
|```Lower Critical - going low```|
|```Lower Critical - going high```|
|```Lower Non-recoverable - going low```|
|```Lower Non-recoverable - going high```|
|```Upper Non-critical - going low```|
|```Upper Non-critical - going high```|
|```Upper Critical - going low```|
|```Upper Critical - going high```|
|```Upper Non-recoverable - going low```|
|```Upper Non-recoverable - going high```|
|```Transition to Idle```|
|```Transition to Active```|
|```Transition to Busy```|
|```State Deasserted```|
|```State Asserted```|
|```Predictive Failure deasserted```|
|```Predictive Failure asserted```|
|```Limit Not Exceeded```|
|```Limit Exceeded```|
|```Performance Met```|
|```Performance Lags```|
|```Transition to OK```|
|```Transition to Non-Critical from OK```|
|```Transition to Critical from less severe```|
|```Transition to Non-recoverable from less severe```|
|```Transition to Non-Critical from more severe```|
|```Transition to Critical from Non-recoverable```|
|```Transition to Non-recoverable```|
|```Monitor```|
|```Informational```|
|```Device Removed / Device Absent```|
|```Device Inserted / Device Present```|
|```Device Disabled```|
|```Device Enabled```|
|```Transition to Running```|
|```Transition to In Test```|
|```Transition to Power Off```|
|```Transition to On Line```|
|```Transition to Off Line```|
|```Transition to Off Duty```|
|```Transition to Degraded```|
|```Transition to Power Save```|
|```Install Error```|
|```Fully Redundant```|
|```Redundancy Lost```|
|```Redundancy Degraded```|
|```Non-redundant:Sufficient Resources from Redundant```|
|```Non-redundant:Sufficient Resources from Insufficient Resources```|
|```Non-redundant:Insufficient Resources```|
|```Redundancy Degraded from Fully Redundant```|
|```Redundancy Degraded from Non-redundant```|
|```D0 Power State```|
|```D1 Power State```|
|```D2 Power State```|
|```D3 Power State```|

### EntryType
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The log entry type.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Event```|
|```SEL```|
|```Oem```|

### EventId
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|This is a unique instance identifier of an event.|
|Type|string|
|Read Only|True|

### EventTimestamp
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|This is time the event occurred.|
|Type|string|
|Read Only|True|

### EventType
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|This indicates the type of an event recorded in this log.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```StatusChange```|The status of this resource has changed.|
|```ResourceUpdated```|The value of this resource has been updated.|
|```ResourceAdded```|A resource has been added.|
|```ResourceRemoved```|A resource has been removed.|
|```Alert```|A condition exists which requires attention.|

### Message
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|This property decodes from EntryType:  If it is Event then it is a message string.  Otherwise, it is SEL or Oem specific.  In most cases, this will be the actual Log Entry.|
|Type|string or null|
|Read Only|True|

### MessageArgs (array)
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)
```MessageArgs``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

### MessageId
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|This property decodes from EntryType:  If it is Event then it is a message id.  Otherwise, it is SEL or Oem specific.  This value is only used for registries - for more information, see the specification.|
|Type|string|
|Read Only|True|

### Oem.Hpe.ActionRequired
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The ActionRequired is to be done in order to possibly resolve the problem occured.|
|Type|string|
|Read Only|True|

### Oem.Hpe.Category
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The log entry category.|
|Type|string|
|Read Only|True|

### Oem.Hpe.Summary
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The log entry summary.|
|Type|string|
|Read Only|True|

### Oem.Hpe.Updated
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The date and time of the latest log entry update, for example, 2014-04-15T00:38:00Z.|
|Type|string|
|Read Only|True|

### Oem.Hpe.iLoIPAddress
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The IP address of iLo.|
|Type|string|
|Read Only|True|

### OemRecordFormat
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|If the entry type is Oem, this will contain more information about the record format from the Oem.|
|Type|string or null|
|Read Only|True|

### SensorNumber
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|This property decodes from EntryType:  If it is SEL, it is the sensor number; if Event then the count of events.  Otherwise, it is Oem specific.|
|Type|number or null|
|Read Only|True|

### SensorType
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|If the EntryType is SEL, this will have the sensor type that the log entry pertains to.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Platform Security Violation Attempt```|
|```Temperature```|
|```Voltage```|
|```Current```|
|```Fan```|
|```Physical Chassis Security```|
|```Processor```|
|```Power Supply / Converter```|
|```PowerUnit```|
|```CoolingDevice```|
|```Other Units-based Sensor```|
|```Memory```|
|```Drive Slot/Bay```|
|```POST Memory Resize```|
|```System Firmware Progress```|
|```Event Logging Disabled```|
|```System Event```|
|```Critical Interrupt```|
|```Button/Switch```|
|```Module/Board```|
|```Microcontroller/Coprocessor```|
|```Add-in Card```|
|```Chassis```|
|```ChipSet```|
|```Other FRU```|
|```Cable/Interconnect```|
|```Terminator```|
|```SystemBoot/Restart```|
|```Boot Error```|
|```BaseOSBoot/InstallationStatus```|
|```OS Stop/Shutdown```|
|```Slot/Connector```|
|```System ACPI PowerState```|
|```Watchdog```|
|```Platform Alert```|
|```Entity Presence```|
|```Monitor ASIC/IC```|
|```LAN```|
|```Management Subsystem Health```|
|```Battery```|
|```Session Audit```|
|```Version Change```|
|```FRUState```|

### Severity
Member of [LogEntry.v1_1_1.LogEntry](#logentry-v1_1_1-logentry)

| | |
|---|---|
|Description|The log entry severity.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```OK```|
|```Warning```|
|```Critical```|

## LogService.v1_0_3.LogService
```@odata.type: "#LogService.v1_0_3.LogService"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managednodes/logservices/alertlog```|GET POST |
|```/redfish/v1/managers/iloamplifier/logservices/devicealertlog```|GET POST |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Entries```|LogEntryCollection|

### DateTime
Member of [LogService.v1_0_3.LogService](#logservice-v1_0_3-logservice)

| | |
|---|---|
|Description|The current DateTime (with offset) for the log service, used to set or read time.|
|Type|string or null|
|Read Only|False|

### DateTimeLocalOffset
Member of [LogService.v1_0_3.LogService](#logservice-v1_0_3-logservice)

| | |
|---|---|
|Description|The time offset from UTC that the DateTime property is set to in format: +06:00 .|
|Type|string or null|
|Read Only|False|

### Entries
The URI to this log entries collection resource.
### MaxNumberOfRecords
Member of [LogService.v1_0_3.LogService](#logservice-v1_0_3-logservice)

| | |
|---|---|
|Description|The maximum number of log entries.|
|Type|integer|
|Read Only|True|

### OverWritePolicy
Member of [LogService.v1_0_3.LogService](#logservice-v1_0_3-logservice)

| | |
|---|---|
|Description|When the log is full, the overwrite policy is enforced.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Unknown```|The overwrite policy is not known or is undefined.|
|```WrapsWhenFull```|When the log is full, new entries will overwrite previous entries.|
|```NeverOverwrites```|When the log is full, new entries are discarded.|

### ServiceEnabled
Member of [LogService.v1_0_3.LogService](#logservice-v1_0_3-logservice)

| | |
|---|---|
|Description|This indicates whether this service is enabled.|
|Type|boolean or null|
|Read Only|False|

### Status
Member of [LogService.v1_0_3.LogService](#logservice-v1_0_3-logservice)
See the Redfish standard schema and specification for information on common Status object.

### Actions

**ClearLog**
Member of [LogService.v1_0_3.LogService](#logservice-v1_0_3-logservice)
There are no parameters for this action.
