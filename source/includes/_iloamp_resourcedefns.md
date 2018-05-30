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

## HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService
```@odata.type: "#HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService"```

This is the schema definition for the Aggregator service. It represents the properties for this service and has links to the Systems and federation groups managed by iLO Amplifier Pack.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/aggregatorservice```|GET POST PATCH |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```FederationGroups```|HpeWfmFederationGroupCollection|
|```Links/ManagedGroups```|HpeWfmManagedGroupCollection|
|```Links/ManagedSystems```|Collection of [HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)|
|```Links/ReportsSummary```|HpeWfmReportsSummaryCollection|
|```Links/ManagedSystemsSummary```|HpeWfmSystemSummaryCollection|
|```Links/LogServices```|Collection of [LogService](#logservice-v1_0_3-logservice)|
|```Systems```|Collection of [ComputerSystem](#computersystem-v1_3_0-computersystem)|

### ActionStatus
**ActionStatus.DiscoverServersFromCSV**
**ActionStatus.DiscoverServersFromCSV.DiscoveryStatus**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

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
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The progress percent of the discovery process.|
|Type|integer|
|Read Only|True|

**ActionStatus.DiscoverServersInRange**
**ActionStatus.DiscoverServersInRange.DiscoveryStatus**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

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
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The ending address at which the discovery process stops.|
|Type|string|
|Read Only|True|

**ActionStatus.DiscoverServersInRange.ProgressPercent**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The progress percent of the discovery process.|
|Type|integer|
|Read Only|True|

**ActionStatus.DiscoverServersInRange.StartAddress**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The starting address at which the discovery process begins.|
|Type|string|
|Read Only|True|

**ActionStatus.RefreshAll**
**ActionStatus.RefreshAll.IsUserInitiated**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The flag indicates whether the refresh is initiated by user.|
|Type|boolean|
|Read Only|True|

**ActionStatus.RefreshAll.ProgressPercent**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The progress percent of the Refresh process.|
|Type|integer|
|Read Only|True|

**ActionStatus.RefreshAll.RefreshStatus**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

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
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The number of systems with Critical health status that are managed by this device.|
|Type|integer|
|Read Only|True|

**AggregatedHealth.OK**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The number of systems with OK health status that are managed by this device.|
|Type|integer|
|Read Only|True|

**AggregatedHealth.Unknown**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The number of systems with unknown health status that are managed by this device.|
|Type|integer|
|Read Only|True|

**AggregatedHealth.Warning**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The number of systems with Warning health status that are managed by this device.|
|Type|integer|
|Read Only|True|

### AutoRefreshMode
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|If enabled, servers will be refreshed automatically in intervals based on the total number of managed Nodes.|
|Type|boolean|
|Read Only|False|

### ContinousDiscovery
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|If enabled, the information of nodes and groups are refreshed at a regular interval. The regular interval is specified by RefreshInterval.|
|Type|boolean|
|Read Only|False|

### FederationGroups
This property references a resource of type Collection with a MemberType of Federation groups.
### RefreshIntervalInHours
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

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

### Systems
This property references a resource of type Collection with a MemberType of Systems.
### SystemsCount
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

| | |
|---|---|
|Description|The number of systems managed by Central Management Device.|
|Type|integer|
|Read Only|True|

### Actions

**RefreshAll**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)
There are no parameters for this action.

**DiscoverServersFromCSV**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

**Parameters:**

**File (string)**

CSV file content

**DiscoverServersInRange**
Member of [HpeWfmAggregatorService.v1_1_0.HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)

**Parameters:**

**UserName (string)**

**EndAddress (string)**

**StartAddress (string)**

**PortNumber (integer)**

**Password (string)**
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

## HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem
```@odata.type: "#HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/aggregatorservice/managedsystems/{item}```|GET POST DELETE |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```SystemSummary/SummaryForSystem```|[HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)|

### ArrayControllers (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```ArrayControllers``` is an array containing elements of:

**ArrayControllers[{item}].CacheMemorySizeMiB**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Cache Memory size of the Array Controller.|
|Type|integer|
|Read Only|True|

**ArrayControllers[{item}].FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Firmware Version of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Health Status of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].Location**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Location of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].LocationFormat**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Location format of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].LogicalDrives (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```LogicalDrives``` is an array containing elements of:

**LogicalDrives[{item}].CapacityMiB**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Capacity of the Logical Drive in MiB.|
|Type|integer or null|
|Read Only|True|

**LogicalDrives[{item}].HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Health Status of the Logical Drive.|
|Type|string or null|
|Read Only|True|

**LogicalDrives[{item}].LogicalDriveEncryption**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Logical Drive Encryption is Enabled on the Drive if True, Disabled if False.|
|Type|boolean or null|
|Read Only|True|

**LogicalDrives[{item}].LogicalDriveNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Number of the Logical Drive.|
|Type|integer or null|
|Read Only|True|

**LogicalDrives[{item}].LogicalDriveType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Type of the Logical Drive.|
|Type|string or null|
|Read Only|True|

**LogicalDrives[{item}].Raid**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Raid level of the Logical Drive.|
|Type|string or null|
|Read Only|True|

**LogicalDrives[{item}].State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|State of the Logical Drive.|
|Type|string or null|
|Read Only|True|

**LogicalDrives[{item}].VolumeUniqueIdentifier**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Volume Unique Identifier of the Logical Drive.|
|Type|string or null|
|Read Only|True|

**ArrayControllers[{item}].Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Model of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].PhysicalDrives (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```PhysicalDrives``` is an array containing elements of:

**PhysicalDrives[{item}].CapacityGB**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Capacity of the Physical Drive in GB.|
|Type|integer or null|
|Read Only|True|

**PhysicalDrives[{item}].CapacityMiB**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Capacity of the Physical Drive in MiB.|
|Type|integer or null|
|Read Only|True|

**PhysicalDrives[{item}].FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Firmware Version of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Health Status of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].InterfaceSpeedMbps**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Interface Speed of the Physical Drive.|
|Type|integer or null|
|Read Only|True|

**PhysicalDrives[{item}].InterfaceType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Interface Type of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].Location**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Location of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].LocationFormat**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Location Format of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].MediaType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Media Type of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Model of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].RotationalSpeedRpm**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Rotational Speed of the Physical Drive.|
|Type|integer or null|
|Read Only|True|

**PhysicalDrives[{item}].SerialNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Serial Number of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**PhysicalDrives[{item}].State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|State of the Physical Drive.|
|Type|string or null|
|Read Only|True|

**ArrayControllers[{item}].SerialNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Serial Number of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the State of the Array Controller.|
|Type|string|
|Read Only|True|

**ArrayControllers[{item}].StorageEnclosures (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```StorageEnclosures``` is an array containing elements of:

**StorageEnclosures[{item}].DriveBayCount**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Drive Bay Count of the Storage Enclosure.|
|Type|integer or null|
|Read Only|True|

**StorageEnclosures[{item}].FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Firmware Version of the Storage Enclosure.|
|Type|string or null|
|Read Only|True|

**StorageEnclosures[{item}].HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Health Status of the Storage Enclosure.|
|Type|string or null|
|Read Only|True|

**StorageEnclosures[{item}].Location**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Location of the Storage Enclosure.|
|Type|string or null|
|Read Only|True|

**StorageEnclosures[{item}].LocationFormat**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Location Format of the Storage Enclosure.|
|Type|string or null|
|Read Only|True|

**StorageEnclosures[{item}].SerialNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Serial Number of the Storage Enclosure.|
|Type|string or null|
|Read Only|True|

**StorageEnclosures[{item}].State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|State of the Storage Enclosure.|
|Type|string or null|
|Read Only|True|

### DeviceInventory (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```DeviceInventory``` is an array containing elements of:

**DeviceInventory[{item}].DeviceClass**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The device class of the item.|
|Type|string or null|
|Read Only|True|

**DeviceInventory[{item}].FirmwareId**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The ID of the item.|
|Type|integer|
|Read Only|True|

**DeviceInventory[{item}].Key**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The family-specific key of the firmware item used for correlation to a component database.|
|Type|string or null|
|Read Only|True|

**DeviceInventory[{item}].Location**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The location of the item.|
|Type|string or null|
|Read Only|True|

**DeviceInventory[{item}].Targets (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```Targets``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**DeviceInventory[{item}].VersionString**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The user-displayable version of the firmware item in string format|
|Type|string or null|
|Read Only|True|

### FansSummary (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```FansSummary``` is an array containing elements of:

**FansSummary[{item}].CurrentReading**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The current speed of the fan.|
|Type|integer or null|
|Read Only|True|

**FansSummary[{item}].FanName**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The name of the fan sensor.|
|Type|string or null|
|Read Only|True|

**FansSummary[{item}].ReadingRPM**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The current speed of the fan.|
|Type|integer or null|
|Read Only|True|

**FansSummary[{item}].Status**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
See the Redfish standard schema and specification for information on common Status object.

**FansSummary[{item}].Units**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Units for the CurrentReading.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Null```|
|```RPM```|
|```Percent```|

### FirmwareInventory (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```FirmwareInventory``` is an array containing elements of:

**FirmwareInventory[{item}].DeviceClass**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The device class of the item.|
|Type|string or null|
|Read Only|True|

**FirmwareInventory[{item}].FirmwareId**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The ID of the item.|
|Type|integer|
|Read Only|True|

**FirmwareInventory[{item}].Key**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The family-specific key of the firmware item used for correlation to a component database.|
|Type|string or null|
|Read Only|True|

**FirmwareInventory[{item}].Location**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The location of the item.|
|Type|string or null|
|Read Only|True|

**FirmwareInventory[{item}].Targets (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```Targets``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**FirmwareInventory[{item}].VersionString**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The user-displayable version of the firmware item in string format|
|Type|string or null|
|Read Only|True|

### HealthSummary
**HealthSummary.AgentlessManagementService**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The status of Agentless Management Service.|
|Type|string or null|
|Read Only|True|

**HealthSummary.BiosOrHardwareHealth**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of Bios or Hardware.|
|Type|string or null|
|Read Only|True|

**HealthSummary.Fans**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of Fans.|
|Type|string or null|
|Read Only|True|

**HealthSummary.Memory**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of Memory.|
|Type|string or null|
|Read Only|True|

**HealthSummary.Network**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of Network.|
|Type|string or null|
|Read Only|True|

**HealthSummary.PowerSupplies**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of PowerSupplies.|
|Type|string or null|
|Read Only|True|

**HealthSummary.Processors**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of Processors.|
|Type|string or null|
|Read Only|True|

**HealthSummary.Storage**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of Storage.|
|Type|string or null|
|Read Only|True|

**HealthSummary.Temperatures**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Health status of Temperatures.|
|Type|string or null|
|Read Only|True|

### HostBusAdapters (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```HostBusAdapters``` is an array containing elements of:

**HostBusAdapters[{item}].Drives (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```Drives``` is an array containing elements of:

**Drives[{item}].CapacityMiB**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Capacity of the drive in MiB.|
|Type|integer or null|
|Read Only|True|

**Drives[{item}].FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Firmware Version of the Disk Drive.|
|Type|string or null|
|Read Only|True|

**Drives[{item}].HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Health Status of the Disk.|
|Type|string or null|
|Read Only|True|

**Drives[{item}].Location**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Location of the Disk Drive.|
|Type|string or null|
|Read Only|True|

**Drives[{item}].Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Model of the Disk.|
|Type|string or null|
|Read Only|True|

**Drives[{item}].SerialNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Serial Number of the Disk.|
|Type|string or null|
|Read Only|True|

**Drives[{item}].State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|State of the Disk.|
|Type|string or null|
|Read Only|True|

**HostBusAdapters[{item}].FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Firmware Version of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

**HostBusAdapters[{item}].HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Health Status of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

**HostBusAdapters[{item}].Location**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Location of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

**HostBusAdapters[{item}].Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Model of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

**HostBusAdapters[{item}].SerialNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Serial Number of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

**HostBusAdapters[{item}].State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the State of the Host Bus Adapter.|
|Type|string|
|Read Only|True|

### Manager
**Manager.Credentials**
**Manager.Credentials.Password**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Password to use to log in to the management processor.|
|Type|string|
|Read Only|False|

**Manager.Credentials.UserName**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Name to use to log in to the management processor.|
|Type|string|
|Read Only|False|

**Manager.FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The firmware version of this Manager|
|Type|string or null|
|Read Only|True|

**Manager.License**
**Manager.License.LicenseKey**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The license key installed on this management processor. License keys are 25 characters in length and contain both letters and numbers.Use POST method to collection of membertype HpiLOLicense to install / update the license|
|Type|string|
|Read Only|True|

**Manager.License.LicenseType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**Manager.ManagerEthernetAddresses (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```ManagerEthernetAddresses``` is an array containing elements of:

**ManagerEthernetAddresses[{item}].IPv4Address**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the IPv4 Address of the Manager Ethernet Interface.|
|Type|string|
|Read Only|True|

**ManagerEthernetAddresses[{item}].ManagerFQDN**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the FQDN of the Manager Ethernet Interface.|
|Type|string|
|Read Only|True|

**ManagerEthernetAddresses[{item}].NICEnabled**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates whether the NIC is enabled or not.|
|Type|boolean|
|Read Only|True|

**Manager.ManagerType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|This property is the manager type for this resource.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```ManagementController```|A controller used primarily to monitor or manage the operation of a device or system|
|```EnclosureManager```|A controller which provides management functions for a chassis or group of devices or systems|
|```BMC```|A controller which provides management functions for a single computer system|

**Manager.Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Model name of the manager.|
|Type|string or null|
|Read Only|True|

**Manager.RemoteSyslog**
**Manager.RemoteSyslog.Enabled**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates whether Remote Syslog is enabled. When enabled, management processor sends notification messages to the specified Syslog server. This can be enabled only when the property RemoteSyslogServer is set or not empty.|
|Type|boolean|
|Read Only|False|

**Manager.RemoteSyslog.Port**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The port number through which the Syslog server is listening.|
|Type|integer|
|Read Only|False|

**Manager.RemoteSyslog.Server**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The IP address, FQDN, IPv6 name, or short name of the server running the Syslog service.|
|Type|string|
|Read Only|False|

**Manager.UUID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The universal unique identifier for this Manager|
|Type|string or null|
|Read Only|True|

**Manager.UpdateService**
**Manager.UpdateService.Details**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Details about the current firmware flash status.|
|Type|string|
|Read Only|True|

**Manager.UpdateService.Flags**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Other flags.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```NONE```|
|```RESET_ILO```|
|```REQUEST_SYSTEM_COLD_BOOT```|
|```REQUEST_SYSTEM_WARM_BOOT```|
|```DEFERRED_AUX_PWR_CYCLE```|

**Manager.UpdateService.ImageType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Firmware flash image type.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```NO_DEVICE```|
|```ILO_DEVICE```|
|```ILO_DEVICE_FIRMWARE```|
|```ILO_DEVICE_LANGPK```|
|```ILO_DEVICE_DEBUGGER```|
|```BIOS_DEVICE```|
|```SCD_DEVICE```|
|```CPLD_DEVICE```|
|```CARB_DEVICE```|
|```PM_DEVICE```|
|```UNKNOWN```|

**Manager.UpdateService.ProgressPercent**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Firmware flash progress.|
|Type|integer|
|Read Only|True|

**Manager.UpdateService.State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Current state of the firmware flash.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```IDLE```|
|```UPLOADING```|
|```PROGRESSING```|
|```COMPLETED```|
|```ERROR```|

**Manager.VirtualMedia**
**Manager.VirtualMedia.ConnectedVia**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Specifies how the virtual media is connected to the server.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```NotConnected```|No current connection.|
|```URI```|Connected to a URI location.|
|```Applet```|Connected to a client application.|

### MemorySummary
**MemorySummary.Details (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```Details``` is an array containing elements of:

**Details[{item}].DIMMStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Specifies memory module status and whether the module in use.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```Unknown```|The status of the DIMM is unknown.|
|```Other```|DIMM status that does not fit any of these definitions.|
|```NotPresent```|DIMM is not present.|
|```PresentUnused```|DIMM is present but unused.|
|```GoodInUse```|DIMM is functioning properly and currently in use.|
|```AddedButUnused```|DIMM is added but currently unused.|
|```UpgradedButUnused```|DIMM is upgraded but currently unused.|
|```ExpectedButMissing```|DIMM is expected but missing.|
|```DoesNotMatch```|DIMM type does not match.|
|```NotSupported```|DIMM is not supported.|
|```ConfigurationError```|Configuration error in DIMM.|
|```Degraded```|DIMM state is degraded.|
|```PresentSpare```|DIMM is present but used as spare.|
|```GoodPartiallyInUse```|DIMM is functioning properly but partially in use.|

**Details[{item}].DIMMTechnology**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The memory module technology type.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Null```|
|```BurstEDO```|
|```FastPage```|
|```Synchronous```|
|```EDO```|
|```LRDIMM```|
|```RDRAM```|
|```RDIMM```|
|```UDIMM```|
|```NVDIMM```|
|```RNVDIMM```|
|```LRNVDIMM```|
|```Unknown```|

**Details[{item}].DIMMType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The type of memory DIMM used in this system.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Null```|
|```DDR```|
|```DDR2```|
|```DDR3```|
|```DDR4```|
|```FBD2```|
|```LPDD3```|
|```LPDDR```|
|```LPDDR2```|
|```LPDDR4```|

**Details[{item}].MaximumFrequencyMHz**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Identifies the maximum, capable speed of the device in megahertz (MHz). If the value is null, the speed is unknown.|
|Type|integer or null|
|Read Only|True|

**Details[{item}].SizeMB**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The size of the memory device in megabytes.|
|Type|integer or null|
|Read Only|True|

**Details[{item}].SocketLocator**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The socket of this device|
|Type|string or null|
|Read Only|True|

**MemorySummary.Status**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
See the Redfish standard schema and specification for information on common Status object.

**MemorySummary.TotalSystemMemoryGiB**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|This is the total amount of memory in the system measured in GiB.|
|Type|integer or null|
|Read Only|True|

### NetworkAdapters (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```NetworkAdapters``` is an array containing elements of:

**NetworkAdapters[{item}].FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Network Adapter firmware version|
|Type|string or null|
|Read Only|True|

**NetworkAdapters[{item}].PhysicalPorts (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```PhysicalPorts``` is an array containing elements of:

**PhysicalPorts[{item}].FullDuplex**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Full-duplex data transmission means that data can be transmitted in both directions on a signal carrier at the same time.|
|Type|boolean or null|
|Read Only|True|

**PhysicalPorts[{item}].IPv4Addresses (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```IPv4Addresses``` is an array containing elements of:

**IPv4Addresses[{item}].Address**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|This is the IPv4 Address.|
|Type|string or null|
|Read Only|True|

**PhysicalPorts[{item}].IPv6Addresses (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```IPv6Addresses``` is an array containing elements of:

**IPv6Addresses[{item}].Address**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|This is the IPv6 Address.|
|Type|string or null|
|Read Only|True|

**PhysicalPorts[{item}].MacAddress**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The port MAC address.|
|Type|string or null|
|Read Only|True|

**PhysicalPorts[{item}].SpeedMbps**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|An estimate of the interface's current bandwidth in Megabits per second.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.|
|Type|integer or null|
|Read Only|True|

**PhysicalPorts[{item}].Status**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
See the Redfish standard schema and specification for information on common Status object.

### PCIDeviceSummary (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```PCIDeviceSummary``` is an array containing elements of:

**PCIDeviceSummary[{item}].DeviceID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Device ID of the PCI Device.|
|Type|integer|
|Read Only|False|

**PCIDeviceSummary[{item}].DeviceLocation**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the location of the PCI Device.|
|Type|string|
|Read Only|False|

**PCIDeviceSummary[{item}].DeviceType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the device type of the PCI Device.|
|Type|string|
|Read Only|False|

**PCIDeviceSummary[{item}].SubsystemDeviceID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Subsystem Device ID of the PCI Device.|
|Type|integer|
|Read Only|True|

**PCIDeviceSummary[{item}].SubsystemVendorID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Subsystem Vendor ID of the PCI Device.|
|Type|integer|
|Read Only|False|

**PCIDeviceSummary[{item}].VendorID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Vendor ID of the PCI Device.|
|Type|integer|
|Read Only|True|

### Persona
**Persona.AppliedDetails**
**Persona.AppliedDetails.LastApplied**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The date and time when the persona was applied on this system.|
|Type|string|
|Read Only|True|

**Persona.AppliedDetails.PersonaId**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The name of the presona that was applied on this system.|
|Type|integer|
|Read Only|True|

**Persona.AppliedDetails.Status**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
See the Redfish standard schema and specification for information on common Status object.

**Persona.ValidationDetails**
**Persona.ValidationDetails.LastValidated**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The date and time when the persona was validated on this system.|
|Type|string|
|Read Only|True|

**Persona.ValidationDetails.PersonaId**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The name of the presona that was validated on this system.|
|Type|integer|
|Read Only|True|

**Persona.ValidationDetails.Status**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
See the Redfish standard schema and specification for information on common Status object.

### PowerSummary
**PowerSummary.PowerConsumedWatts**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The amount of power consumed in Watts.|
|Type|integer or null|
|Read Only|True|

**PowerSummary.PowerSupplies (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```PowerSupplies``` is an array containing elements of:

**PowerSupplies[{item}].BayNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The bay number of this processor|
|Type|integer or null|
|Read Only|True|

**PowerSupplies[{item}].FirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Firmware version of the power supply|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The health status of the power supply|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].HotplugCapable**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Firmware version of the power supply|
|Type|boolean|
|Read Only|True|

**PowerSupplies[{item}].Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The product model of this device|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].PowerCapacityWatts**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The total Power Capacity in Watts|
|Type|integer or null|
|Read Only|True|

**PowerSupplies[{item}].PowerSupplyStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Status of the power supply|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].SerialNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The power supply Serial Number|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].SparePartNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The power supply Spare Part Number|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The state of the power supply|
|Type|string or null|
|Read Only|True|

### ProcessorSummary
**ProcessorSummary.Count**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The number of processors in the system.|
|Type|integer or null|
|Read Only|True|

**ProcessorSummary.Details (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```Details``` is an array containing elements of:

**Details[{item}].CoresEnabled**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The total number of cores enabled in this processor|
|Type|integer or null|
|Read Only|True|

**Details[{item}].Manufacturer**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The processor manufacturer|
|Type|string or null|
|Read Only|True|

**Details[{item}].Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The product model number of this device|
|Type|string or null|
|Read Only|True|

**Details[{item}].Socket**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The socket of this device|
|Type|string or null|
|Read Only|True|

**Details[{item}].SpeedMHz**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The maximum clock speed of the processor|
|Type|integer or null|
|Read Only|True|

**Details[{item}].Status**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
See the Redfish standard schema and specification for information on common Status object.

**Details[{item}].TotalCores**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The total number of cores contained in this processor|
|Type|integer or null|
|Read Only|True|

**Details[{item}].TotalThreads**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The total number of execution threads supported by this processor|
|Type|integer or null|
|Read Only|True|

**ProcessorSummary.Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The processor model for the primary or majority of processors in this system.|
|Type|string or null|
|Read Only|True|

**ProcessorSummary.Status**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
See the Redfish standard schema and specification for information on common Status object.

### SoftwareInventory (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```SoftwareInventory``` is an array containing elements of:

**SoftwareInventory[{item}].SoftwareId**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the ID of the Software.|
|Type|integer|
|Read Only|True|

**SoftwareInventory[{item}].Version**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Version of the Software.|
|Type|string|
|Read Only|True|

### SystemSummary
**SystemSummary.AMSStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the status of AMS.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionCapabilities**
**SystemSummary.ActionCapabilities.AHSDownload**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for AHS Download.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.AbsarokaOfflineUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Absaroka Offline Update.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.AbsarokaOnlineUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Absaroka Online Update.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.AssignRecovery**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Assign Recovery.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.BaselineAutomaticUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Baseline Automatic Update.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.Delete**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Delete.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.FirmwareUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Firmware Update.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.GroupManage**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Group Manage.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.ImportConfigBaseline**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Import config baseline.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.ManualRecovery**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Manual Recovery.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.OfflineFirmwareUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Offline Firmware Update.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.OnlineFirmwareUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Online Firmware Update.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.Power**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Power.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.Refresh**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Refresh.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.RemoteSyslog**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Remote Syslog.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.UID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for UID.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.UnAssignRecovery**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Unassign Recovery.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionCapabilities.VirtualMedia**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Action capability for Virtual Media.|
|Type|boolean|
|Read Only|True|

**SystemSummary.ActionErrorMessage**
**SystemSummary.ActionErrorMessage.AbsarokaOfflineUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Absaroka Offline Update.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionErrorMessage.AbsarokaOnlineUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Absaroka Online Update.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionErrorMessage.AssignRecovery**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Assign Recovery.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionErrorMessage.BaselineAutomaticUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Baseline Automatic Update.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionErrorMessage.GroupManage**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Manage Group.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionErrorMessage.ImportConfigBaseline**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Import Config Baseline.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionErrorMessage.OfflineFirmwareUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Offline Firmware Update.|
|Type|string|
|Read Only|True|

**SystemSummary.ActionErrorMessage.OnlineFirmwareUpdate**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The error message for Online Firmware Update.|
|Type|string|
|Read Only|True|

**SystemSummary.ChassisType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The chassis type.|
|Type|string|
|Read Only|True|

**SystemSummary.Discovery**
**SystemSummary.Discovery.LastRefreshed**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Last refreshed timestamp|
|Type|string|
|Read Only|True|

**SystemSummary.Discovery.ProgressPercent**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The progress percent of the discovery|
|Type|integer|
|Read Only|True|

**SystemSummary.Discovery.State**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.Discovery.StateDescription**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The description of the state|
|Type|string|
|Read Only|True|

**SystemSummary.EncryptionSecurityState**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.FederationActionGroupName**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the name of the Group server belongs to.|
|Type|string|
|Read Only|True|

**SystemSummary.FederationEnabled**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates whether management processor federation management is enabled or disabled.|
|Type|boolean|
|Read Only|True|

**SystemSummary.FederationSupported**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates whether management processor federation is supported.|
|Type|boolean|
|Read Only|True|

**SystemSummary.GatewayManaged**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates if the Server is Gateway Managed(Federation Group)|
|Type|boolean|
|Read Only|True|

**SystemSummary.HealthStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.HostName**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The DNS Host Name, without any domain information|
|Type|string|
|Read Only|True|

**SystemSummary.HostOSDescription**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives description about OS on the Host.|
|Type|string|
|Read Only|True|

**SystemSummary.HostOSName**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the OS Name of the Host.|
|Type|string|
|Read Only|True|

**SystemSummary.HostOSType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the OS Type of the Host.|
|Type|integer|
|Read Only|True|

**SystemSummary.HostOSVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the OS Version of the Host.|
|Type|string|
|Read Only|True|

**SystemSummary.IndicatorLED**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.LastTaskStatus**
**SystemSummary.LastTaskStatus.EndTime**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The date-time stamp that the task was last completed.|
|Type|string|
|Read Only|True|

**SystemSummary.LastTaskStatus.Messages (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```Messages``` is an array containing elements of:

**Messages[{item}].Message**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|This is the human readable message, if provided.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].MessageArgs (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```MessageArgs``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].MessageId**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|This is the key for this message which can be used to look up the message in a message registry.|
|Type|string|
|Read Only|True|

**Messages[{item}].RelatedProperties (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```RelatedProperties``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].Resolution**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Used to provide suggestions on how to resolve the situation that caused the error.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].Severity**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|This is the severity of the errors.|
|Type|string or null|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.CreatedBy**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The name of the user that created this task.|
|Type|string|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.DetailedTaskLink**
Detailed status of the task.
**SystemSummary.LastTaskStatus.Oem.Hpe.History**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The history of the task.|
|Type|string|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.ProgressMessages (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```ProgressMessages``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.ProgressPercent**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The progress percent of this task.|
|Type|integer|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.SelectedAddress (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.SelectedGroups (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```SelectedGroups``` is an array containing elements of:

**SelectedGroups[{item}].GroupName**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Group name of the selected group.|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].SelectedAddress (array)**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].allSystemsInGroup**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The flag suggests whether all the servers in the group are selected.|
|Type|boolean|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.SubTaskCount**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Number of subtasks for this task.|
|Type|integer|
|Read Only|True|

**SystemSummary.LastTaskStatus.Oem.Hpe.TaskIdentifier**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|A unique task identifier number for this task.|
|Type|integer|
|Read Only|True|

**SystemSummary.LastTaskStatus.StartTime**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The date-time stamp that the task was last started.|
|Type|string|
|Read Only|True|

**SystemSummary.LastTaskStatus.TaskState**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.LastTaskStatus.TaskStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.ManagerAddress**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The IP address or DNS of the manager which was added by user.|
|Type|string|
|Read Only|True|

**SystemSummary.ManagerFQDN**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The fully qualified domain name of the manager.|
|Type|string|
|Read Only|True|

**SystemSummary.ManagerFirmwareVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the Firmware Version of the manager.|
|Type|string|
|Read Only|True|

**SystemSummary.ManagerIPAddress**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The IPv4 address of the manager.|
|Type|string|
|Read Only|True|

**SystemSummary.ManagerLicense**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the License of the manager.|
|Type|string|
|Read Only|True|

**SystemSummary.ManagerSSLPort**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The Web Server SSL Port of the manager.|
|Type|integer|
|Read Only|True|

**SystemSummary.ManagerVirtualMediaImage**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The valid URI indicating the image that is mounted on this server. A null value indicates that no image exists.|
|Type|string|
|Read Only|False|

**SystemSummary.ManualRecoveryFlag**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates if the Server is set for Manual or Automatic Recovery|
|Type|boolean|
|Read Only|True|

**SystemSummary.Manufacturer**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The manaufacturer of the system.|
|Type|string|
|Read Only|True|

**SystemSummary.MasterManagerType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The type of the manager.|
|Type|string|
|Read Only|True|

**SystemSummary.Model**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The model information that the manufacturer uses to refer to this system.|
|Type|string|
|Read Only|True|

**SystemSummary.NumOfGrpsNodeBelongs**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the number of Federation Groups this iLO is part of.|
|Type|integer|
|Read Only|True|

**SystemSummary.PowerState**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.ProductID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The system product ID.|
|Type|string|
|Read Only|True|

**SystemSummary.RecoveryAction**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Action that is set for recovery|
|Type|string|
|Read Only|True|

**SystemSummary.RecoveryPolicyId**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the Recovery Policy Id.|
|Type|integer|
|Read Only|True|

**SystemSummary.RecoveryPolicyName**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Recovery Persona Applied on the System.|
|Type|string|
|Read Only|True|

**SystemSummary.RecoveryStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Status of the System.If the recovery install set is applied or not and once recovery starts , its status|
|Type|string|
|Read Only|True|

**SystemSummary.SUTMode**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the Mode of HPSUT.|
|Type|string|
|Read Only|True|

**SystemSummary.SUTServiceState**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the Service state of HPSUT.|
|Type|string|
|Read Only|True|

**SystemSummary.SUTServiceVersion**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the Service Version of HPSUT.|
|Type|string|
|Read Only|True|

**SystemSummary.SecurityState**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the Security State of the System.|
|Type|string|
|Read Only|True|

**SystemSummary.SerialNumber**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The system serial number.|
|Type|string|
|Read Only|True|

**SystemSummary.StandAloneManaged**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates if the Server is Standalone Managed with Credentials|
|Type|boolean|
|Read Only|True|

**SystemSummary.StatusState**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Indicates the State of the System.|
|Type|string|
|Read Only|True|

**SystemSummary.SummaryForSystem**
Link to the Managed System with detailed information.
**SystemSummary.SystemCategory**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

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

**SystemSummary.SystemType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The system type.|
|Type|string|
|Read Only|True|

**SystemSummary.TPMModuleType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the Module Type of TPM on the Server.|
|Type|string|
|Read Only|True|

**SystemSummary.TPMStatus**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|Gives the Status of TPM on the Server.|
|Type|string|
|Read Only|True|

**SystemSummary.UUID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The universal unique identifier for this system.|
|Type|string|
|Read Only|True|

**SystemSummary.iLOType**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The iLO type of this Manager|
|Type|string|
|Read Only|True|

**SystemSummary.iLOUUID**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

| | |
|---|---|
|Description|The universal unique identifier for the iLO.|
|Type|string|
|Read Only|True|

### TaskHistory (array)
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)
```TaskHistory``` is an array containing elements of:

### Actions

**Reset**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

**Parameters:**

**ResetType (string)**

|Value|Description|
|---|---|
|On|
|ForceOff|
|ForceRestart|
|PushPowerButton|

**VirtualMedia**
Member of [HpeWfmManagedSystem.v1_0_0.HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)

**Parameters:**
## HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary
```@odata.type: "#HpeWfmReportsSummary.v1_0_0.HpeWfmReportsSummary"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/aggregatorservice/managedsystems/{item}/reportssummary```|GET |

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
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/taskservice/resetsystemtasks/{item}0000```|GET POST DELETE |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```TaskSummary/Oem/Hpe/DetailedTaskLink```|[HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)|

### SelectedGroups (array)
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```SelectedGroups``` is an array containing elements of:

**SelectedGroups[{item}].AllSystemsInGroup**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|If true then the task is run on all systems in the group otherwise will be run only on systems selected.|
|Type|boolean|
|Read Only|False|

**SelectedGroups[{item}].FederationGroupName**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The name of the federation group.|
|Type|string|
|Read Only|False|

**SelectedGroups[{item}].SelectedSystemsManagerAddress (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```SelectedSystemsManagerAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

### SelectedSystemsManagerAddress (array)
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```SelectedSystemsManagerAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

### TaskParameters
**TaskParameters.ResetType**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The reset type to be performed for the system.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|
|---|
|```On```|
|```ForceOff```|
|```ForceRestart```|
|```PushPowerButton```|

### TaskProgress (array)
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```TaskProgress``` is an array containing elements of:

**TaskProgress[{item}].IpAddress**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The system/group on which the task is applied.|
|Type|string|
|Read Only|True|

**TaskProgress[{item}].Message**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|Progress message associated with the task.|
|Type|string|
|Read Only|True|

**TaskProgress[{item}].ProgressPercent**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The progress percent of this task.|
|Type|integer|
|Read Only|True|

**TaskProgress[{item}].SubTaskState**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The state of the sub task.|
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

**TaskProgress[{item}].TaskName**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The name of the sub task.|
|Type|string|
|Read Only|True|

### TaskSummary
**TaskSummary.EndTime**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The date-time stamp that the task was last completed.|
|Type|string|
|Read Only|True|

**TaskSummary.Messages (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```Messages``` is an array containing elements of:

**Messages[{item}].Message**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|This is the human readable message, if provided.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].MessageArgs (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```MessageArgs``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].MessageId**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|This is the key for this message which can be used to look up the message in a message registry.|
|Type|string|
|Read Only|True|

**Messages[{item}].RelatedProperties (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```RelatedProperties``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].Resolution**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|Used to provide suggestions on how to resolve the situation that caused the error.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].Severity**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|This is the severity of the errors.|
|Type|string or null|
|Read Only|True|

**TaskSummary.Oem.Hpe.CreatedBy**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The name of the user that created this task.|
|Type|string|
|Read Only|True|

**TaskSummary.Oem.Hpe.DetailedTaskLink**
Detailed status of the task.
**TaskSummary.Oem.Hpe.History**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The history of the task.|
|Type|string|
|Read Only|True|

**TaskSummary.Oem.Hpe.ProgressMessages (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```ProgressMessages``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**TaskSummary.Oem.Hpe.ProgressPercent**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The progress percent of this task.|
|Type|integer|
|Read Only|True|

**TaskSummary.Oem.Hpe.SelectedAddress (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**TaskSummary.Oem.Hpe.SelectedGroups (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```SelectedGroups``` is an array containing elements of:

**SelectedGroups[{item}].GroupName**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The Group name of the selected group.|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].SelectedAddress (array)**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].allSystemsInGroup**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The flag suggests whether all the servers in the group are selected.|
|Type|boolean|
|Read Only|True|

**TaskSummary.Oem.Hpe.SubTaskCount**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|Number of subtasks for this task.|
|Type|integer|
|Read Only|True|

**TaskSummary.Oem.Hpe.TaskIdentifier**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|A unique task identifier number for this task.|
|Type|integer|
|Read Only|True|

**TaskSummary.StartTime**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

| | |
|---|---|
|Description|The date-time stamp that the task was last started.|
|Type|string|
|Read Only|True|

**TaskSummary.TaskState**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

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

**TaskSummary.TaskStatus**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)

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

### Actions

**Abort**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
There are no parameters for this action.

**ReRun**
Member of [HpeWfmResetSystemTask.v1_0_0.HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)
There are no parameters for this action.
## HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary
```@odata.type: "#HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/aggregatorservice/managedsystems/{item}/summary```|GET |

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

### ChassisType
Member of [HpeWfmSystemSummary.v1_0_0.HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)

| | |
|---|---|
|Description|The chassis type.|
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

## LogEntry.v1_1_1.LogEntry
```@odata.type: "#LogEntry.v1_1_1.LogEntry"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/aggregatorservice/logservices/alertlog/entries/{item}```|GET |
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
|```/redfish/v1/aggregatorservice/logservices/alertlog```|GET POST |
|```/redfish/v1/managers/iloamplifier/logservices/devicealertlog```|GET POST |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Entries```|Collection of [LogEntry](#logentry-v1_1_1-logentry)|

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
## Manager.v1_3_0.Manager
```@odata.type: "#Manager.v1_3_0.Manager"```

This is the schema definition for a manager.  Examples of managers are BMCs, Enclosure Managers, Management Controllers and other subsystems assigned manageability functions.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier```|GET POST PATCH |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Oem/Hpe/Links/UpdateService```|[UpdateService](#updateservice-v1_2_0-updateservice)|
|```Oem/Hpe/Links/BaselineService```|[HpeWfmBaselineService](#hpewfmbaselineservice-v1_0_0-hpewfmbaselineservice)|
|```LogServices```|Collection of [LogService](#logservice-v1_0_3-logservice)|
|```EthernetInterfaces```|Collection of [EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)|
|```Oem/Hpe/Links/LoggerPolicy```|[HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)|
|```Oem/Hpe/Links/SecurityService```|[HpeSecurityService](#hpesecurityservice-v1_0_0-hpesecurityservice)|
|```Oem/Hpe/Links/LicenseService```|Collection of [HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)|
|```NetworkProtocol```|[ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)|
|```Oem/Hpe/Links/Telemetry```|[HpeWfmTelemetryInfo](#hpewfmtelemetryinfo-v1_0_0-hpewfmtelemetryinfo)|
|```Oem/Hpe/Links/DateTimeService```|[HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)|

### CommandShell
**CommandShell.ConnectTypesSupported (array)**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
```ConnectTypesSupported``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```SSH```|The controller supports a Command Shell connection using the SSH protocol|
|```Telnet```|The controller supports a Command Shell connection using the Telnet protocol|
|```IPMI```|The controller supports a Command Shell connection using the IPMI Serial-over-LAN (SOL) protocol|
|```Oem```|The controller supports a Command Shell connectino using an OEM-specific protocol|

**CommandShell.MaxConcurrentSessions**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|This is the maximum number of Command Shell sessions, regardless of protocol, that this manager supports.|
|Type|integer|
|Read Only|True|

**CommandShell.ServiceEnabled**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Indicates if the Command Shell service is enabled for this manager.|
|Type|boolean|
|Read Only|True|

### DateTime
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The current DateTime (with offset) for the manager, used to set or read time.|
|Type|string or null|
|Read Only|False|

### DateTimeLocalOffset
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The time offset from UTC that the DateTime property is set to in format: +06:00 .|
|Type|string or null|
|Read Only|False|

### EthernetInterfaces
This is a reference to a collection of NICs that this manager uses for network communication.  It is here that clients will find NIC configuration options and settings.
### FirmwareVersion
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The firmware version of this Manager|
|Type|string or null|
|Read Only|True|

### GraphicalConsole
**GraphicalConsole.ConnectTypesSupported (array)**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
```ConnectTypesSupported``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```KVMIP```|The controller supports a Graphical Console connection using a KVM-IP (redirection of Keyboard, Video, Mouse over IP) protocol|
|```Oem```|The controller supports a Graphical Console connection using an OEM-specific protocol|

**GraphicalConsole.MaxConcurrentSessions**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Indicates the maximum number of Graphical Console sessions, regardless of protocol, this manager supports.|
|Type|integer|
|Read Only|True|

**GraphicalConsole.ServiceEnabled**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Indicates if the Command Shell service is enabled for this manager.|
|Type|boolean|
|Read Only|True|

### HostInterfaces
This is a reference to a collection of Host Interfaces that this manager uses for local host communication.  It is here that clients will find Host Interface configuration options and settings.
### LogServices
Reference to a resource of type Collection with a MemberType of Logs.
### ManagerType
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|This property is the manager type for this resource.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```ManagementController```|A controller used primarily to monitor or manage the operation of a device or system.|
|```EnclosureManager```|A controller which provides management functions for a chassis or group of devices or systems.|
|```BMC```|A controller which provides management functions for a single computer system.|
|```RackManager```|A controller which provides management functions for a whole or part of a rack.|
|```AuxiliaryController```|A controller which provides management functions for a particular subsystem or group of devices.|

### Model
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The model information of this Manager as defined by the manufacturer.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```iLO Amplifier Pack```|Manager Mode iLO Amplifier Pack|

### NetworkProtocol
 This is a reference to the network services and their settings that the manager controls.  It is here that clients will find network configuration options as well as network services.
### Oem.Hpe.Firmware
**Oem.Hpe.Firmware.Backup**
**Oem.Hpe.Firmware.Backup.BuildNumber**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build number of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.BuildNumberString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The string version of the build number of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.Date**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build date of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.DebugBuild**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|True if the firmware is a debug build; False if it is not.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.Family**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The family of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.MajorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The major version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.MinorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The minor version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.Time**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build time of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Backup.VersionString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The version string of the firmware. This value might be null if VersionString is unavailable.|
|Type|string or null|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock**
**Oem.Hpe.Firmware.Bootblock.BuildNumber**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build number of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.BuildNumberString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The string version of the build number of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.Date**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build date of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.DebugBuild**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|True if the firmware is a debug build; False if it is not.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.Family**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The family of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.MajorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The major version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.MinorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The minor version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.Time**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build time of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Bootblock.VersionString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The version string of the firmware. This value might be null if VersionString is unavailable.|
|Type|string or null|
|Read Only|True|

**Oem.Hpe.Firmware.Current**
**Oem.Hpe.Firmware.Current.BuildNumber**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build number of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Current.BuildNumberString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The string version of the build number of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Current.Date**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build date of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Current.DebugBuild**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|True if the firmware is a debug build; False if it is not.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Firmware.Current.Family**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The family of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Current.MajorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The major version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Current.MinorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The minor version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Current.Time**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build time of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Current.VersionString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The version string of the firmware. This value might be null if VersionString is unavailable.|
|Type|string or null|
|Read Only|True|

**Oem.Hpe.Firmware.Pending**
**Oem.Hpe.Firmware.Pending.BuildNumber**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build number of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.BuildNumberString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The string version of the build number of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.Date**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build date of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.DebugBuild**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|True if the firmware is a debug build; False if it is not.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.Family**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The family of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.MajorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The major version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.MinorVersion**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The minor version of the firmware.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.Time**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The build time of the firmware.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Firmware.Pending.VersionString**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The version string of the firmware. This value might be null if VersionString is unavailable.|
|Type|string or null|
|Read Only|True|

### Oem.Hpe.License
**Oem.Hpe.License.License**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Describes the name of the license installed on management processor.|
|Type|string|
|Read Only|True|

**Oem.Hpe.License.LicenseFirstName**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|First name.|
|Type|string|
|Read Only|True|

**Oem.Hpe.License.LicenseKey**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The installed license key.Will be set to NULL on read.|
|Type|string or null|
|Read Only|False|

**Oem.Hpe.License.LicenseLastName**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Last name.|
|Type|string|
|Read Only|True|

**Oem.Hpe.License.LicenseMailID**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Users email ID .|
|Type|string|
|Read Only|True|

**Oem.Hpe.License.LicenseOrganization**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Organization name.|
|Type|string|
|Read Only|True|

**Oem.Hpe.License.LicenseType**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Indicates whether the license is Perpetual or Evaluation.|
|Type|string|
|Read Only|True|

**Oem.Hpe.License.LicensedNoOfServers**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Indicates the number of servers that can be managed.|
|Type|integer|
|Read Only|True|

### Oem.Hpe.SerialCLISpeed
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Serial command line interface speed in bits/second.|
|Type|integer|
|Read Only|False|

The following are the supported values:

|Value|
|---|
|```9600```|
|```19200```|
|```38400```|
|```57600```|
|```115200```|

### Oem.Hpe.SerialCLIStatus
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Status of serial command line interface.|
|Type|string or null|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```Disabled```|Serial command line interface is disabled.|
|```EnabledNoAuth```|Serial command line interface is enabled with no authentication required.|
|```EnabledAuthReq```|Serial command line interface is enabled with authentication required.|

### Oem.Hpe.Type
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

### Oem.Hpe.WatchdogTimerActive
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Specifies whether Watchdog is enabled ro not.|
|Type|boolean|
|Read Only|False|

### PowerState
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|This is the current power state of the Manager.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```On```|The state is powered On.|
|```Off```|The state is powered Off.|
|```PoweringOn```|A temporary state between Off and On.|
|```PoweringOff```|A temporary state between On and Off.|

### Redundancy
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
See the Redfish standard schema and specification for information on common Redundancy object.

### SerialConsole
**SerialConsole.ConnectTypesSupported (array)**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
```ConnectTypesSupported``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```SSH```|The controller supports a Serial Console connection using the SSH protocol|
|```Telnet```|The controller supports a Serial Console connection using the Telnet protocol|
|```IPMI```|The controller supports a Serial Console connection using the IPMI Serial-over-LAN (SOL) protocol|
|```Oem```||

**SerialConsole.MaxConcurrentSessions**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|This is the maximum number of Serial Console sessions, regardless of protocol, that this manager supports.|
|Type|integer|
|Read Only|True|

**SerialConsole.ServiceEnabled**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|Indicates if the Command Shell service is enabled for this manager.|
|Type|boolean|
|Read Only|True|

### SerialInterfaces
This is a reference to a collection of serial interfaces that this manager uses for serial and console communication.  It is here that clients will find serial configuration options and settings.
### ServiceEntryPointUUID
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The UUID of the Redfish Service provided by this manager.|
|Type|string|
|Read Only|True|

### UUID
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)

| | |
|---|---|
|Description|The Universal Unique Identifier (UUID) for this Manager.|
|Type|string|
|Read Only|True|

### VirtualMedia
This is a reference to the Virtual Media services for this particular manager.
### Actions

**Reset**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
There are no parameters for this action.

**ResetToFactoryDefaults**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
Resets Central Management Device to Factory Defaults.


**Parameters:**

**ResetType (string)**

|Value|Description|
|---|---|
|AllConfiguration|Resets all configuration and reboot's the Centeral Management Device.|
|ManagedSystemsConfiguration|Reset the stored configuration files of managed systems and reboot's the Central Management Device.|

**Target (string)**

The Target defines an OEM action.

|Value|Description|
|---|---|
|/Oem/Hpe|

**Backup**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
Performs Backup of Central Management Device Configuration.


**Parameters:**

**MountPath (string)**

The mount path of the network share server where the Backup data will be stored.

**Target (string)**

The Target defines an OEM action.

|Value|Description|
|---|---|
|/Oem/Hpe|

**StorageType (string)**

The type of storage on which the Backup data is downloaded.

|Value|Description|
|---|---|
|USB|
|SHARE|

**DestinationPath (string)**

The folder path in which the Backup data will be stored.

**RemovableStorageDeviceName (string)**

The device name of the removable storage.

**NetworkShareAddress (string)**

The network share IP address or DNS name where the Backup data will be stored.

**Password (string)**

The key that will be used to encrypt the backup data.

**Shutdown**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
Shuts down Management Device.


**Parameters:**

**Target (string)**

The Target defines an OEM action.

|Value|Description|
|---|---|
|/Oem/Hpe|

**Restore**
Member of [Manager.v1_3_0.Manager](#manager-v1_3_0-manager)
Restores the Central Management Device Configuration from the specified file.


**Parameters:**

**MountPath (string)**

The mount path of the network share server from where the Backup data will be restored.

**Target (string)**

The Target defines an OEM action.

|Value|Description|
|---|---|
|/Oem/Hpe|

**StorageType (string)**

The type of storage from which the Backup data is restored.

|Value|Description|
|---|---|
|USB|
|SHARE|

**DestinationPath (string)**

The folder path from which the Backup data will be stored.

**RemovableStorageDeviceName (string)**

The device name of the removable storage.

**NetworkShareAddress (string)**

The network share IP address or DNS name from where the Backup data will be restored.

**Password (string)**

The key that will be used to decrypt the backup data.
## ManagerAccount.v1_0_3.ManagerAccount
```@odata.type: "#ManagerAccount.v1_0_3.ManagerAccount"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/accountservice/accounts/{item}```|GET PATCH DELETE |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Links/Role```|[Role](#role-v1_0_0-role)|

### Enabled
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|This property is used by a User Administrator to disable an account w/o having to delet the user information.  When set to true, the user can login.  When set to false, the account is administratively disabled and the user cannot login.|
|Type|boolean|
|Read Only|False|

### Locked
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|This property indicates that the account has been auto-locked by the account service because the lockout threshold has been exceeded.  When set to true, the account is locked. A user admin can write the property to false to manually unlock, or the account service will unlock it once the lockout duration period has passed.|
|Type|boolean|
|Read Only|False|

### Oem.Hpe.DisplayName
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|Descriptive display name that helps to easily identify the owner of each user name. The display name does not have to be the same as the user name and must use printable characters. The maximum length for a display name is 127 characters.|
|Type|string|
|Read Only|False|

### Oem.Hpe.Enabled
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|Indicates whether the user accound is enabled or not.|
|Type|boolean|
|Read Only|False|

### Oem.Hpe.Privilege
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|This privilege enables a user to log in to management processor. All local accounts have the login privilege. This privilege is added automatically if it is not specified.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Login```|Read operations allowed like viewing discovered nodes and groups and generate reports|
|```Device```|Allows configuring and performing actions on devices includes login privilege|
|```User```|Allows configuring users with device privilege|
|```Manager```|All operations allowed|
|```Security```||

### Password
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|The password used to log in to the management processor. The maximum length for a password is 39 characters. The minimum length for a password is specified in the MinPasswordLength property of the AccountService schema.|
|Type|string or null|
|Read Only|False|

### RoleId
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|This property contains the Role for this account.|
|Type|string|
|Read Only|False|

### UserName
Member of [ManagerAccount.v1_0_3.ManagerAccount](#manageraccount-v1_0_3-manageraccount)

| | |
|---|---|
|Description|The name used to log in to the management processor. The user name does not have to be the same as the login name. The maximum length for the user name is 32 characters. The user name must use printable characters.|
|Type|string|
|Read Only|False|

## ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol
```@odata.type: "#ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol"```

This resource is used to obtain or modify the network services managed by this manager.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/managers/iloamplifier/networkprotocol```|GET POST PATCH |

### DHCP
**DHCP.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**DHCP.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### FQDN
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|This is the fully qualified domain name for the manager obtained by DNS including the host name and top-level domain name.|
|Type|string or null|
|Read Only|True|

### HTTP
**HTTP.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**HTTP.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### HTTPS
**HTTPS.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**HTTPS.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### HostName
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The DNS Host Name of this manager, without any domain information.|
|Type|string or null|
|Read Only|True|

### IPMI
**IPMI.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**IPMI.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### KVMIP
**KVMIP.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**KVMIP.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### Oem.Hpe.ProxyServer
**Oem.Hpe.ProxyServer.Enabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates whether to use proxy server or not. When enabled, management processor sends alerts via proxy server otherwise it will not use the proxy server.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.ProxyServer.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The port number through which the Proxy server is listening.|
|Type|integer|
|Read Only|False|

**Oem.Hpe.ProxyServer.SecureProxyEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates whether to connect to proxy server securely. When enabled, proxy server is connected via https otherwise uses http|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.ProxyServer.Server**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The IP address, FQDN, IPv6 name, or short name of the Proxy server.|
|Type|string|
|Read Only|False|

### Oem.Hpe.RemoteSyslog
**Oem.Hpe.RemoteSyslog.Enabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates whether Remote Syslog is enabled. When enabled, management processor sends notification messages to the specified Syslog server. This can be enabled only when the property RemoteSyslogServer is set or not empty.|
|Type|boolean|
|Read Only|False|

**Oem.Hpe.RemoteSyslog.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The port number through which the Syslog server is listening.|
|Type|integer|
|Read Only|False|

**Oem.Hpe.RemoteSyslog.PrimaryServer**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The IP address, FQDN, IPv6 name, or short name of the server running the Syslog service.|
|Type|string|
|Read Only|False|

**Oem.Hpe.RemoteSyslog.SecondaryServer**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The IP address, FQDN, IPv6 name, or short name of the server running the Syslog service.|
|Type|string|
|Read Only|False|

### SNMP
**SNMP.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**SNMP.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### SSDP
**SSDP.Enabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates whether SSDP is enabled for the manager.|
|Type|boolean or null|
|Read Only|False|

**SSDP.NotifyIPv6Scope**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The scope for IPv6 Notify messages for SSDP.|
|Type|string or null|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```Link```|SSDP Notify messages are sent to addresses in the IPv6 Local Link scope|
|```Site```|SSDP Notify messages are sent to addresses in the IPv6 Local Site scope.|
|```Organization```|SSDP Notify messages are sent to addresses in the IPv6 Local Organization scope.|

**SSDP.NotifyMulticastIntervalSeconds**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates how often multicast is performed for SSDP.|
|Type|integer or null|
|Read Only|False|

**SSDP.NotifyTTL**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The Time to Live (TTL) hop count for SSDP Notify messages.|
|Type|integer or null|
|Read Only|False|

**SSDP.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|The SSDP port number.|
|Type|integer or null|
|Read Only|True|

**SSDP.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates whether SSDP is enabled for the manager.|
|Type|boolean or null|
|Read Only|False|

### SSH
**SSH.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**SSH.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### Status
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)
See the Redfish standard schema and specification for information on common Status object.

### Telnet
**Telnet.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**Telnet.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### VirtualMedia
**VirtualMedia.Port**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates the protocol port.|
|Type|number or null|
|Read Only|True|

**VirtualMedia.ProtocolEnabled**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

| | |
|---|---|
|Description|Indicates if the protocol is enabled or disabled.|
|Type|boolean or null|
|Read Only|True|

### Actions

**SendTestSyslog**
Member of [ManagerNetworkProtocol.v1_1_0.ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)

**Parameters:**

**Target (string)**

The Target defines an OEM action.

|Value|Description|
|---|---|
|/Oem/Hpe|
## Memory.v1_2_0.Memory
```@odata.type: "#Memory.v1_2_0.Memory"```

This is the schema definition for the Memory resource. It represents memory and its configuration attached to a system.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/systems/{item}/memory/{item}```|GET POST PATCH |

### AllocationAlignmentMiB
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The boundary which memory regions are allocated on, measured in MiB.|
|Type|number or null|
|Read Only|True|

### AllocationIncrementMiB
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The size of the smallest unit of allocation for a memory region, thus it is the multiple in which regions are actually reserved.|
|Type|number or null|
|Read Only|True|

### AllowedSpeedsMHz (array)
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
```AllowedSpeedsMHz``` is an array containing elements of:


| | |
|---|---|
|Type|number|
|Read Only|True|

### BaseModuleType
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The base module type of Memory.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```RDIMM```|Registered DIMM.|
|```UDIMM```|UDIMM.|
|```SO_DIMM```|SO_DIMM.|
|```LRDIMM```|Load Reduced.|
|```Mini_RDIMM```|Mini_RDIMM.|
|```Mini_UDIMM```|Mini_UDIMM.|
|```SO_RDIMM_72b```|SO_RDIMM_72b.|
|```SO_UDIMM_72b```|SO_UDIMM_72b.|
|```SO_DIMM_16b```|SO_DIMM_16b.|
|```SO_DIMM_32b```|SO_DIMM_32b.|

### BusWidthBits
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Bus Width in bits.|
|Type|number or null|
|Read Only|True|

### CapacityMiB
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Memory Capacity in MiB.|
|Type|number or null|
|Read Only|True|

### DataWidthBits
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Data Width in bits.|
|Type|number or null|
|Read Only|True|

### DeviceID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Device ID.|
|Type|string or null|
|Read Only|True|

### DeviceLocator
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Location of the Memory in the platform.|
|Type|string or null|
|Read Only|True|

### ErrorCorrection
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Error correction scheme supported for this memory.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```NoECC```|No ECC available.|
|```SingleBitECC```|Single bit Data error can be corrected by ECC.|
|```MultiBitECC```|Multi-bit Data errors can be corrected by ECC.|
|```AddressParity```|Address Parity errors can be corrected.|

### FirmwareApiVersion
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Version of API supported by the firmware.|
|Type|string or null|
|Read Only|True|

### FirmwareRevision
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Revision of firmware on the Memory controller.|
|Type|string or null|
|Read Only|True|

### FunctionClasses (array)
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
```FunctionClasses``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

### IsRankSpareEnabled
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Rank spare enabled status.|
|Type|boolean or null|
|Read Only|True|

### IsSpareDeviceEnabled
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Spare device enabled status.|
|Type|boolean or null|
|Read Only|True|

### Manufacturer
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The Memory manufacturer.|
|Type|string or null|
|Read Only|True|

### MaxTDPMilliWatts (array)
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
```MaxTDPMilliWatts``` is an array containing elements of:


| | |
|---|---|
|Type|number|
|Read Only|True|

### MemoryDeviceType
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Type details of the Memory.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```DDR```|DDR.|
|```DDR2```|DDR2.|
|```DDR3```|DDR3.|
|```DDR4```|DDR4.|
|```DDR4_SDRAM```|DDR4 SDRAM.|
|```DDR4E_SDRAM```|DDR4E SDRAM.|
|```LPDDR4_SDRAM```|LPDDR4 SDRAM.|
|```DDR3_SDRAM```|DDR3 SDRAM.|
|```LPDDR3_SDRAM```|LPDDR3 SDRAM.|
|```DDR2_SDRAM```|DDR2 SDRAM.|
|```DDR2_SDRAM_FB_DIMM```|DDR2 SDRAM FB_DIMM.|
|```DDR2_SDRAM_FB_DIMM_PROBE```|DDR2 SDRAM FB_DIMM PROBE.|
|```DDR_SGRAM```|DDR SGRAM.|
|```DDR_SDRAM```|DDR SDRAM.|
|```ROM```|ROM.|
|```SDRAM```|SDRAM.|
|```EDO```|EDO.|
|```FastPageMode```|Fast Page Mode.|
|```PipelinedNibble```|Pipelined Nibble.|

### MemoryLocation
**MemoryLocation.Channel**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Channel number in which Memory is connected.|
|Type|number or null|
|Read Only|True|

**MemoryLocation.MemoryController**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Memory controller number in which Memory is connected.|
|Type|number or null|
|Read Only|True|

**MemoryLocation.Slot**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Slot number in which Memory is connected.|
|Type|number or null|
|Read Only|True|

**MemoryLocation.Socket**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Socket number in which Memory is connected.|
|Type|number or null|
|Read Only|True|

### MemoryMedia (array)
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
```MemoryMedia``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```DRAM```|DRAM media.|
|```NAND```|NAND media.|
|```Proprietary```|Proprietary media.|

### MemorySubsystemControllerManufacturerID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The manufacturer ID of the memory subsystem controller of this memory module.|
|Type|string or null|
|Read Only|True|

### MemorySubsystemControllerProductID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The product ID of the memory subsystem controller of this memory module.|
|Type|string or null|
|Read Only|True|

### MemoryType
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The type of Memory.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```DRAM```|The memory module is composed of volatile memory.|
|```NVDIMM_N```|The memory module is composed of volatile memory backed by non-volatile memory.|
|```NVDIMM_F```|The memory module is composed of non-volatile memory.|
|```NVDIMM_P```|The memory module is composed of a combination of non-volatile and volatile memory.|

### Metrics
**Metrics.BlockSizeBytes**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Block size in bytes.|
|Type|number or null|
|Read Only|True|

**Metrics.CurrentPeriod**
**Metrics.CurrentPeriod.BlocksRead**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Number of blocks read since reset.|
|Type|number or null|
|Read Only|True|

**Metrics.CurrentPeriod.BlocksWritten**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Number of blocks written since reset.|
|Type|number or null|
|Read Only|True|

**Metrics.HealthData**
**Metrics.HealthData.AlarmTrips**
**Metrics.HealthData.AlarmTrips.AddressParityError**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Address parity error detected status.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.AlarmTrips.CorrectableECCError**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Correctable data error threshold crossing alarm trip detected status.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.AlarmTrips.SpareBlock**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Spare block capacity crossing alarm trip detected status.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.AlarmTrips.Temperature**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Temperature threshold crossing alarm trip detected status.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.AlarmTrips.UncorrectableECCError**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Uncorrectable data error threshold crossing alarm trip detected status.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.DataLossDetected**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Data loss detection status.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.LastShutdownSuccess**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Status of last shutdown.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.PerformanceDegraded**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Performance degraded mode status.|
|Type|boolean or null|
|Read Only|True|

**Metrics.HealthData.PredictedMediaLifeLeftPercent**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The percentage of reads and writes that are predicted to still be available for the media.|
|Type|number or null|
|Read Only|True|

**Metrics.HealthData.RemainingSpareBlockPercentage**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Remaining spare blocks in percentage.|
|Type|number or null|
|Read Only|True|

**Metrics.LifeTime**
**Metrics.LifeTime.BlocksRead**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Number of blocks read for the lifetime of the Memory.|
|Type|number or null|
|Read Only|True|

**Metrics.LifeTime.BlocksWritten**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Number of blocks written for the lifetime of the Memory.|
|Type|number or null|
|Read Only|True|

### ModuleManufacturerID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The manufacturer ID of this memory module.|
|Type|string or null|
|Read Only|True|

### ModuleProductID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The product ID of this memory module.|
|Type|string or null|
|Read Only|True|

### Oem.Hpe.DIMMStatus
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Specifies memory module status and whether the module in use.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Null```|A value is temporarily unavailable|
|```Unknown```|The status of the DIMM is unknown.|
|```Other```|DIMM status that does not fit any of these definitions.|
|```NotPresent```|DIMM is not present.|
|```PresentUnused```|DIMM is present but unused.|
|```GoodInUse```|DIMM is functioning properly and currently in use.|
|```AddedButUnused```|DIMM is added but currently unused.|
|```UpgradedButUnused```|DIMM is upgraded but currently unused.|
|```ExpectedButMissing```|DIMM is expected but missing.|
|```DoesNotMatch```|DIMM type does not match.|
|```NotSupported```|DIMM is not supported.|
|```ConfigurationError```|Configuration error in DIMM.|
|```Degraded```|DIMM state is degraded.|
|```PresentSpare```|DIMM is present but used as spare.|
|```GoodPartiallyInUse```|DIMM is functioning properly but partially in use.|

### Oem.Hpe.Type
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

### OperatingMemoryModes (array)
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
```OperatingMemoryModes``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Volatile```|Volatile memory.|
|```PMEM```|Persistent memory, byte accesible through system address space.|
|```Block```|Block accessible system memory.|

### OperatingSpeedMhz
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Operating speed of Memory in MHz.|
|Type|number or null|
|Read Only|True|

### PartNumber
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The product part number of this device.|
|Type|string or null|
|Read Only|True|

### PersistentRegionNumberLimit
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Total number of persistent regions this Memory can support.|
|Type|number or null|
|Read Only|True|

### PersistentRegionSizeLimitMiB
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Total size of persistent regions in MiB.|
|Type|number or null|
|Read Only|True|

### PersistentRegionSizeMaxMiB
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Maximum size of a single persistent region in MiB.|
|Type|number or null|
|Read Only|True|

### PowerManagementPolicy
**PowerManagementPolicy.AveragePowerBudgetMilliWatts**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Average power budget in milli watts.|
|Type|number or null|
|Read Only|True|

**PowerManagementPolicy.MaxTDPMilliWatts**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Maximum TDP in milli watts.|
|Type|number or null|
|Read Only|True|

**PowerManagementPolicy.PeakPowerBudgetMilliWatts**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Peak power budget in milli watts.|
|Type|number or null|
|Read Only|True|

**PowerManagementPolicy.PolicyEnabled**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Power management policy enabled status.|
|Type|boolean or null|
|Read Only|True|

### RankCount
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Number of ranks available in the Memory.|
|Type|number or null|
|Read Only|True|

### Regions (array)
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
```Regions``` is an array containing elements of:

**Regions[{item}].MemoryClassification**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Classification of memory occupied by the given memory region.|
|Type|string or null|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Volatile```|Volatile memory.|
|```ByteAccessiblePersistent```|Byte accessible persistent memory.|
|```Block```|Block accesible memory.|

**Regions[{item}].OffsetMiB**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Offset with in the Memory that corresponds to the starting of this memory region in MiB.|
|Type|number or null|
|Read Only|True|

**Regions[{item}].PassphraseState**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|State of the passphrase for this region.|
|Type|boolean or null|
|Read Only|True|

**Regions[{item}].RegionId**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Unique region ID representing a specific region within the Memory.|
|Type|string or null|
|Read Only|True|

**Regions[{item}].SizeMiB**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Size of this memory region in MiB.|
|Type|number or null|
|Read Only|True|

### SecurityCapabilities
**SecurityCapabilities.MaxPassphraseCount**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Maximum number of passphrases supported for this Memory.|
|Type|number or null|
|Read Only|True|

**SecurityCapabilities.PassphraseCapable**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Memory passphrase set capability.|
|Type|boolean or null|
|Read Only|True|

**SecurityCapabilities.SecurityStates (array)**
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
```SecurityStates``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Enabled```|Secure mode is enabled.|
|```Disabled```|Secure mode is disabled.|
|```Unlocked```|Secure mode is enabled and access to the data is unlocked.|
|```Locked```|Secure mode is enabled and access to the data is locked.|
|```Frozen```|Secure state is frozen and can not be modified until reset.|
|```Passphraselimit```|Number of attempts to unlock the Memory exceeded limit.|

### SerialNumber
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|The product serial number of this device.|
|Type|string or null|
|Read Only|True|

### SpareDeviceCount
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Number of unused spare devices available in the Memory.|
|Type|number or null|
|Read Only|True|

### Status
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)
See the Redfish standard schema and specification for information on common Status object.

### SubsystemDeviceID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Subsystem Device ID.|
|Type|string or null|
|Read Only|True|

### SubsystemVendorID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|SubSystem Vendor ID.|
|Type|string or null|
|Read Only|True|

### VendorID
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Vendor ID.|
|Type|string or null|
|Read Only|True|

### VolatileRegionNumberLimit
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Total number of volatile regions this Memory can support.|
|Type|number or null|
|Read Only|True|

### VolatileRegionSizeLimitMiB
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Total size of volatile regions in MiB.|
|Type|number or null|
|Read Only|True|

### VolatileRegionSizeMaxMiB
Member of [Memory.v1_2_0.Memory](#memory-v1_2_0-memory)

| | |
|---|---|
|Description|Maximum size of a single volatile region in MiB.|
|Type|number or null|
|Read Only|True|

## PCIeDevice.v1_1_0.PCIeDevice
```@odata.type: "#PCIeDevice.v1_1_0.PCIeDevice"```

This is the schema definition for the PCIeDevice resource.  It represents the properties of a PCIeDevice attached to a System.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/systems/{item}/pciedevices/{item}```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Links/PCIeFunctions[]```|[PCIeFunction](#pciefunction-v1_1_0-pciefunction)|

### AssetTag
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|The user assigned asset tag for this PCIe device.|
|Type|string or null|
|Read Only|False|

### DeviceType
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|The device type for this PCIe device.|
|Type|string or null|
|Read Only|True|

### FirmwareVersion
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|The version of firmware for this PCIe device.|
|Type|string or null|
|Read Only|True|

### Manufacturer
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|This is the manufacturer of this PCIe device.|
|Type|string or null|
|Read Only|True|

### Model
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|This is the model number for the PCIe device.|
|Type|string or null|
|Read Only|True|

### PartNumber
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|The part number for this PCIe device.|
|Type|string or null|
|Read Only|True|

### SKU
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|This is the SKU for this PCIe device.|
|Type|string or null|
|Read Only|True|

### SerialNumber
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)

| | |
|---|---|
|Description|The serial number for this PCIe device.|
|Type|string or null|
|Read Only|True|

### Status
Member of [PCIeDevice.v1_1_0.PCIeDevice](#pciedevice-v1_1_0-pciedevice)
See the Redfish standard schema and specification for information on common Status object.

## PCIeFunction.v1_1_0.PCIeFunction
```@odata.type: "#PCIeFunction.v1_1_0.PCIeFunction"```

This is the schema definition for the PCIeFunction resource.  It represents the properties of a PCIeFunction attached to a System.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/systems/{item}/pciedevices/{item}/pciefunction```|GET |

### ClassCode
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The Class Code of this PCIe function.|
|Type|string or null|
|Read Only|True|

### DeviceClass
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The class for this PCIe Function.|
|Type|string or null|
|Read Only|True|

### DeviceId
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The Device ID of this PCIe function.|
|Type|string or null|
|Read Only|True|

### FunctionId
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The the PCIe Function identifier.|
|Type|number or null|
|Read Only|True|

### FunctionType
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The type of the PCIe Function.|
|Type|string or null|
|Read Only|True|

### RevisionId
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The Revision ID of this PCIe function.|
|Type|string or null|
|Read Only|True|

### Status
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)
See the Redfish standard schema and specification for information on common Status object.

### SubsystemId
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The Subsystem ID of this PCIe function.|
|Type|string or null|
|Read Only|True|

### SubsystemVendorId
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The Subsystem Vendor ID of this PCIe function.|
|Type|string or null|
|Read Only|True|

### VendorId
Member of [PCIeFunction.v1_1_0.PCIeFunction](#pciefunction-v1_1_0-pciefunction)

| | |
|---|---|
|Description|The Vendor ID of this PCIe function.|
|Type|string or null|
|Read Only|True|

## Power.v1_3_0.Power
```@odata.type: "#Power.v1_3_0.Power"```

This is the schema definition for the Power Metrics. It represents the properties for Power Consumption and Power Limiting.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/chassis/8f55097c/power```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```PowerSupplies[]/RelatedItem[]```|[ComputerSystem](#computersystem-v1_3_0-computersystem)|

### PowerControl (array)
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
```PowerControl``` is an array containing elements of:

**PowerControl[{item}].MemberId**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|This is the identifier for the member within the collection.|
|Type|string|
|Read Only|True|

**PowerControl[{item}].PhysicalContext**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Room```|The room.|
|```Intake```|The intake point of the chassis.|
|```Exhaust```|The exhaust point of the chassis.|
|```Front```|The front of the chassis.|
|```Back```|The back of the chassis.|
|```Upper```|The upper portion of the chassis.|
|```Lower```|The lower portion of the chassis.|
|```CPU```|A Processor (CPU).|
|```GPU```|A Graphics Processor (GPU).|
|```Backplane```|A backplane within the chassis.|
|```SystemBoard```|The system board (PCB).|
|```PowerSupply```|A power supply.|
|```VoltageRegulator```|A voltage regulator device.|
|```StorageDevice```|A storage device.|
|```NetworkingDevice```|A networking device.|
|```ComputeBay```|Within a compute bay.|
|```StorageBay```|Within a storage bay.|
|```NetworkBay```|Within a networking bay.|
|```ExpansionBay```|Within an expansion bay.|
|```PowerSupplyBay```|Within a power supply bay.|
|```Memory```|A memory device.|

**PowerControl[{item}].PowerAllocatedWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The total amount of power that has been allocated (or budegeted)to  chassis resources.|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerAvailableWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The amount of power not already budgeted and therefore available for additional allocation. (powerCapacity - powerAllocated).  This indicates how much reserve power capacity is left.|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerCapacityWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The total amount of power available to the chassis for allocation. This may the power supply capacity, or power budget assigned to the chassis from an up-stream chassis.|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerConsumedWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The actual power being consumed by the chassis.|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerLimit**
**PowerControl[{item}].PowerLimit.CorrectionInMs**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The time required for the limiting process to reduce power consumption to below the limit.|
|Type|number or null|
|Read Only|False|

**PowerControl[{item}].PowerLimit.LimitException**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The action that is taken if the power cannot be maintained below the LimitInWatts.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```NoAction```|Take no action when the limit is exceeded.|
|```HardPowerOff```|Turn the power off immediately when the limit is exceeded.|
|```LogEventOnly```|Log an event when the limit is exceeded, but take no further action.|
|```Oem```|Take an OEM-defined action.|

**PowerControl[{item}].PowerLimit.LimitInWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The Power limit in watts. Set to null to disable power capping.|
|Type|number or null|
|Read Only|False|

**PowerControl[{item}].PowerMetrics**
**PowerControl[{item}].PowerMetrics.AverageConsumedWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The average power level over the measurement window (the last IntervalInMin minutes).|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerMetrics.IntervalInMin**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The time interval (or window) in which the PowerMetrics are measured over.|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerMetrics.MaxConsumedWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The highest power consumption level that has occured over the measurement window (the last IntervalInMin minutes).|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerMetrics.MinConsumedWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The lowest power consumption level over the measurement window (the last IntervalInMin minutes).|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].PowerRequestedWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The potential power that the chassis resources are requesting which may be higher than the current level being consumed since requested power includes budget that the chassis resource wants for future use.|
|Type|number or null|
|Read Only|True|

**PowerControl[{item}].RelatedItem (array)**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
```RelatedItem``` is an array containing elements of:

**PowerControl[{item}].Status**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
See the Redfish standard schema and specification for information on common Status object.

### PowerSupplies (array)
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
```PowerSupplies``` is an array containing elements of:

**PowerSupplies[{item}].FirmwareVersion**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The firmware version for this Power Supply.|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].IndicatorLED**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The state of the indicator LED, used to identify the power supply.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Lit```|The Indicator LED is lit.|
|```Blinking```|The Indicator LED is blinking.|
|```Off```|The Indicator LED is off.|

**PowerSupplies[{item}].InputRanges (array)**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
```InputRanges``` is an array containing elements of:

**InputRanges[{item}].InputType**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The Input type (AC or DC).|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```AC```|Alternating Current (AC) input range.|
|```DC```|Direct Current (DC) input range.|

**InputRanges[{item}].MaximumFrequencyHz**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The maximum line input frequency at which this power supply input range is effective.|
|Type|number or null|
|Read Only|True|

**InputRanges[{item}].MaximumVoltage**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The maximum line input voltage at which this power supply input range is effective.|
|Type|number or null|
|Read Only|True|

**InputRanges[{item}].MinimumFrequencyHz**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The minimum line input frequency at which this power supply input range is effective.|
|Type|number or null|
|Read Only|True|

**InputRanges[{item}].MinimumVoltage**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The minimum line input voltage at which this power supply input range is effective.|
|Type|number or null|
|Read Only|True|

**InputRanges[{item}].OutputWattage**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The maximum capacity of this Power Supply when operating in this input range.|
|Type|number or null|
|Read Only|True|

**PowerSupplies[{item}].LastPowerOutputWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The average power output of this Power Supply.|
|Type|number or null|
|Read Only|True|

**PowerSupplies[{item}].LineInputVoltage**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The line input voltage at which the Power Supply is operating.|
|Type|number or null|
|Read Only|True|

**PowerSupplies[{item}].LineInputVoltageType**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The line voltage type supported as an input to this Power Supply.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Unknown```|The power supply line input voltage type cannot be determined.|
|```ACLowLine```|100-127V AC input.|
|```ACMidLine```|200-240V AC input.|
|```ACHighLine```|277V AC input.|
|```DCNeg48V```|-48V DC input.|
|```DC380V```|High Voltage DC input (380V).|
|```AC120V```|AC 120V nominal input.|
|```AC240V```|AC 240V nominal input.|
|```AC277V```|AC 277V nominal input.|
|```ACandDCWideRange```|Wide range AC or DC input.|
|```ACWideRange```|Wide range AC input.|
|```DC240V```|DC 240V nominal input.|

**PowerSupplies[{item}].Manufacturer**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|This is the manufacturer of this power supply.|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].MemberId**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|This is the identifier for the member within the collection.|
|Type|string|
|Read Only|True|

**PowerSupplies[{item}].Model**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The model number for this Power Supply.|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].PartNumber**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The part number for this Power Supply.|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].PowerCapacityWatts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The maximum capacity of this Power Supply.|
|Type|number or null|
|Read Only|True|

**PowerSupplies[{item}].PowerSupplyType**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The Power Supply type (AC or DC).|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Unknown```|The power supply type cannot be determined.|
|```AC```|Alternating Current (AC) power supply.|
|```DC```|Direct Current (DC) power supply.|
|```ACorDC```|Power Supply supports both DC or AC.|

**PowerSupplies[{item}].RelatedItem (array)**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
```RelatedItem``` is an array containing elements of:

**PowerSupplies[{item}].SerialNumber**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The serial number for this Power Supply.|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].SparePartNumber**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The spare part number for this Power Supply.|
|Type|string or null|
|Read Only|True|

**PowerSupplies[{item}].Status**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
See the Redfish standard schema and specification for information on common Status object.

### Status
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
See the Redfish standard schema and specification for information on common Status object.

### Voltages (array)
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
```Voltages``` is an array containing elements of:

**Voltages[{item}].LowerThresholdCritical**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Below normal range but not yet fatal.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].LowerThresholdFatal**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Below normal range and is fatal.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].LowerThresholdNonCritical**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Below normal range.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].MaxReadingRange**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Maximum value for this Voltage sensor.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].MemberId**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|This is the identifier for the member within the collection.|
|Type|string|
|Read Only|True|

**Voltages[{item}].MinReadingRange**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Minimum value for this Voltage sensor.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].PhysicalContext**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Room```|The room.|
|```Intake```|The intake point of the chassis.|
|```Exhaust```|The exhaust point of the chassis.|
|```Front```|The front of the chassis.|
|```Back```|The back of the chassis.|
|```Upper```|The upper portion of the chassis.|
|```Lower```|The lower portion of the chassis.|
|```CPU```|A Processor (CPU).|
|```GPU```|A Graphics Processor (GPU).|
|```Backplane```|A backplane within the chassis.|
|```SystemBoard```|The system board (PCB).|
|```PowerSupply```|A power supply.|
|```VoltageRegulator```|A voltage regulator device.|
|```StorageDevice```|A storage device.|
|```NetworkingDevice```|A networking device.|
|```ComputeBay```|Within a compute bay.|
|```StorageBay```|Within a storage bay.|
|```NetworkBay```|Within a networking bay.|
|```ExpansionBay```|Within an expansion bay.|
|```PowerSupplyBay```|Within a power supply bay.|
|```Memory```|A memory device.|

**Voltages[{item}].ReadingVolts**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|The present reading of the voltage sensor.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].RelatedItem (array)**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
```RelatedItem``` is an array containing elements of:

**Voltages[{item}].SensorNumber**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|A numerical identifier to represent the voltage sensor.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].Status**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)
See the Redfish standard schema and specification for information on common Status object.

**Voltages[{item}].UpperThresholdCritical**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Above normal range but not yet fatal.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].UpperThresholdFatal**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Above normal range and is fatal.|
|Type|number or null|
|Read Only|True|

**Voltages[{item}].UpperThresholdNonCritical**
Member of [Power.v1_3_0.Power](#power-v1_3_0-power)

| | |
|---|---|
|Description|Above normal range.|
|Type|number or null|
|Read Only|True|

## PrivilegeRegistry.v1_0_0.PrivilegeRegistry
```@odata.type: "#PrivilegeRegistry.v1_0_0.PrivilegeRegistry"```

This is the schema definition for Operation to Privilege mapping.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/accountservice/privilegeregistry```|GET |

### Mappings (array)
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Mappings``` is an array containing elements of:

**Mappings[{item}].Entity**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)

| | |
|---|---|
|Description|Indicates entity name. e.g., Manager.|
|Type|string|
|Read Only|True|

**Mappings[{item}].OperationMap**
**Mappings[{item}].OperationMap.DELETE (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```DELETE``` is an array containing elements of:

**DELETE[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Mappings[{item}].OperationMap.GET (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```GET``` is an array containing elements of:

**GET[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Mappings[{item}].OperationMap.HEAD (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```HEAD``` is an array containing elements of:

**HEAD[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Mappings[{item}].OperationMap.PATCH (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PATCH``` is an array containing elements of:

**PATCH[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Mappings[{item}].OperationMap.POST (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```POST``` is an array containing elements of:

**POST[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Mappings[{item}].OperationMap.PUT (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PUT``` is an array containing elements of:

**PUT[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Mappings[{item}].PropertyOverrides (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PropertyOverrides``` is an array containing elements of:

**PropertyOverrides[{item}].OperationMap**
**PropertyOverrides[{item}].OperationMap.DELETE (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```DELETE``` is an array containing elements of:

**DELETE[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**PropertyOverrides[{item}].OperationMap.GET (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```GET``` is an array containing elements of:

**GET[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**PropertyOverrides[{item}].OperationMap.HEAD (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```HEAD``` is an array containing elements of:

**HEAD[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**PropertyOverrides[{item}].OperationMap.PATCH (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PATCH``` is an array containing elements of:

**PATCH[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**PropertyOverrides[{item}].OperationMap.POST (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```POST``` is an array containing elements of:

**POST[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**PropertyOverrides[{item}].OperationMap.PUT (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PUT``` is an array containing elements of:

**PUT[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**PropertyOverrides[{item}].Targets (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Targets``` is an array containing elements of:


| | |
|---|---|
|Type|string or null|
|Read Only|True|

**Mappings[{item}].ResourceURIOverrides (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```ResourceURIOverrides``` is an array containing elements of:

**ResourceURIOverrides[{item}].OperationMap**
**ResourceURIOverrides[{item}].OperationMap.DELETE (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```DELETE``` is an array containing elements of:

**DELETE[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**ResourceURIOverrides[{item}].OperationMap.GET (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```GET``` is an array containing elements of:

**GET[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**ResourceURIOverrides[{item}].OperationMap.HEAD (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```HEAD``` is an array containing elements of:

**HEAD[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**ResourceURIOverrides[{item}].OperationMap.PATCH (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PATCH``` is an array containing elements of:

**PATCH[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**ResourceURIOverrides[{item}].OperationMap.POST (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```POST``` is an array containing elements of:

**POST[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**ResourceURIOverrides[{item}].OperationMap.PUT (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PUT``` is an array containing elements of:

**PUT[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**ResourceURIOverrides[{item}].Targets (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Targets``` is an array containing elements of:


| | |
|---|---|
|Type|string or null|
|Read Only|True|

**Mappings[{item}].SubordinateOverrides (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```SubordinateOverrides``` is an array containing elements of:

**SubordinateOverrides[{item}].OperationMap**
**SubordinateOverrides[{item}].OperationMap.DELETE (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```DELETE``` is an array containing elements of:

**DELETE[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SubordinateOverrides[{item}].OperationMap.GET (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```GET``` is an array containing elements of:

**GET[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SubordinateOverrides[{item}].OperationMap.HEAD (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```HEAD``` is an array containing elements of:

**HEAD[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SubordinateOverrides[{item}].OperationMap.PATCH (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PATCH``` is an array containing elements of:

**PATCH[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SubordinateOverrides[{item}].OperationMap.POST (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```POST``` is an array containing elements of:

**POST[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SubordinateOverrides[{item}].OperationMap.PUT (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PUT``` is an array containing elements of:

**PUT[{item}].Privilege (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Privilege``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SubordinateOverrides[{item}].Targets (array)**
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```Targets``` is an array containing elements of:


| | |
|---|---|
|Type|string or null|
|Read Only|True|

### OEMPrivilegesUsed (array)
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```OEMPrivilegesUsed``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```OemConfigureManagerWithSecurity```|Allows a user to perform all iLO Amplifier Tasks, including Recovery Management|

### PrivilegesUsed (array)
Member of [PrivilegeRegistry.v1_0_0.PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)
```PrivilegesUsed``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Login```|Able to log into the service and read resources.|
|```ConfigureManager```|Able to configure Manager resources.|
|```ConfigureUsers```|Able to configure Users and their Accounts.|
|```ConfigureSelf```|Able to change the password for the current user Account.|
|```ConfigureComponents```|Able to configure components managed by this service.|

## Processor.v1_1_0.Processor
```@odata.type: "#Processor.v1_1_0.Processor"```

This is the schema definition for the Processor resource. It represents the properties of a processor attached to a system.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/systems/{item}/processor/{item}```|GET POST PATCH |

### InstructionSet
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The instruction set of the processor|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```x86```|x86 32-bit|
|```x86-64```|x86 64-bit|
|```IA-64```|Intel IA-64|
|```ARM-A32```|ARM 32-bit|
|```ARM-A64```|ARM 64-bit|
|```MIPS32```|MIPS 32-bit|
|```MIPS64```|MIPS 64-bit|
|```OEM```|OEM-defined|

### Manufacturer
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The processor manufacturer|
|Type|string or null|
|Read Only|True|

### MaxSpeedMHz
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The maximum clock speed of the processor|
|Type|number or null|
|Read Only|True|

### Model
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The product model number of this device|
|Type|string or null|
|Read Only|True|

### Oem.Hpe.CoresEnabled
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The number of enabled cores in the processor.|
|Type|integer or null|
|Read Only|True|

### ProcessorArchitecture
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The architecture of the processor|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```x86```|x86 or x86-64|
|```IA-64```|Intel Itanium|
|```ARM```|ARM|
|```MIPS```|MIPS|
|```OEM```|OEM-defined|

### ProcessorId
**ProcessorId.EffectiveFamily**
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The effective Family for this processor|
|Type|string or null|
|Read Only|True|

**ProcessorId.EffectiveModel**
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The effective Model for this processor|
|Type|string or null|
|Read Only|True|

**ProcessorId.IdentificationRegisters**
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The contents of the Identification Registers (CPUID) for this processor|
|Type|string or null|
|Read Only|True|

**ProcessorId.MicrocodeInfo**
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The Microcode Information for this processor|
|Type|string or null|
|Read Only|True|

**ProcessorId.Step**
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The Step value for this processor|
|Type|string or null|
|Read Only|True|

**ProcessorId.VendorId**
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The Vendor Identification for this processor|
|Type|string or null|
|Read Only|True|

### ProcessorType
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The type of processor|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```CPU```|A Central Processing Unit|
|```GPU```|A Graphics Processing Unit|
|```FPGA```|A Field Programmable Gate Array|
|```DSP```|A Digital Signal Processor|
|```Accelerator```|An Accelerator|
|```OEM```|An OEM-defined Processing Unit|

### Socket
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The socket or location of the processor|
|Type|string or null|
|Read Only|True|

### Status
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)
See the Redfish standard schema and specification for information on common Status object.

### TotalCores
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The total number of cores contained in this processor|
|Type|number or null|
|Read Only|True|

### TotalThreads
Member of [Processor.v1_1_0.Processor](#processor-v1_1_0-processor)

| | |
|---|---|
|Description|The total number of execution threads supported by this processor|
|Type|number or null|
|Read Only|True|

## Role.v1_0_0.Role
```@odata.type: "#Role.v1_0_0.Role"```

This resource defines a user role to be used in conjunction with a Manager Account.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/accountservice/roles/administrator```|GET |
|```/redfish/v1/accountservice/roles/configmanagerrole```|GET |

### AssignedPrivileges (array)
Member of [Role.v1_0_0.Role](#role-v1_0_0-role)
```AssignedPrivileges``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Login```|Able to log into the service and read resources.|
|```ConfigureManager```|Able to configure Manager resources.|
|```ConfigureUsers```|Able to configure Users and their Accounts.|
|```ConfigureSelf```|Able to change the password for the current user Account.|
|```ConfigureComponents```|Able to configure components managed by this service.|

### IsPredefined
Member of [Role.v1_0_0.Role](#role-v1_0_0-role)

| | |
|---|---|
|Description|This property is used to indicate if the Role is one of the Redfish Predefined Roles vs a Custom role.|
|Type|boolean|
|Read Only|True|

### OemPrivileges (array)
Member of [Role.v1_0_0.Role](#role-v1_0_0-role)
```OemPrivileges``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```OemConfigureManagerWithSecurity```|Allows a user to perform all iLO Amplifier Tasks, including Recovery Management|

### RoleId
Member of [Role.v1_0_0.Role](#role-v1_0_0-role)

| | |
|---|---|
|Description|This property contains the name of the Role.|
|Type|string|
|Read Only|True|

## ServiceRoot.v1_1_1.ServiceRoot
```@odata.type: "#ServiceRoot.v1_1_1.ServiceRoot"```

This object represents the HPE RESTful API root service.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Tasks```|[TaskService](#taskservice-v1_0_3-taskservice)|
|```Registries```|Collection of [MessageRegistryFile](#messageregistryfile-v1_1_0-messageregistryfile)|
|```Managers```|Collection of [Manager](#manager-v1_3_0-manager)|
|```JsonSchemas```|Collection of [JsonSchemaFile](#jsonschemafile-v1_0_3-jsonschemafile)|
|```AccountService```|[AccountService](#accountservice-v1_0_4-accountservice)|
|```SessionService```|[SessionService](#sessionservice-v1_1_1-sessionservice)|
|```Oem/Hpe/Links/AggregatorService```|[HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)|
|```Chassis```|Collection of [Chassis](#chassis-v1_4_0-chassis)|
|```Systems```|Collection of [ComputerSystem](#computersystem-v1_3_0-computersystem)|
|```Links/Sessions```|Collection of [Session](#session-v1_0_3-session)|

### AccountService
The URI to this account service resource.
### Chassis
The URI to this chassis resource.
### EventService
The URI to the event service resource.
### Fabrics
A link to a collection of all fabric entities.
### JsonSchemas
The URI to this registries resource.
### Managers
The URI to this managers resource.
### Oem.Hpe.Language
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Specifies the Language to be used.|
|Type|string|
|Read Only|False|

### Oem.Hpe.Manager (array)
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)
```Manager``` is an array containing elements of:

**Manager[{item}].FQDN**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Fully qualified domain name of the management processor.|
|Type|string|
|Read Only|True|

**Manager[{item}].HostName**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The name of management processor.|
|Type|string|
|Read Only|True|

**Manager[{item}].ManagerFirmwareVersion**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The major and minor management processor version numbers.|
|Type|string|
|Read Only|True|

**Manager[{item}].ManagerFirmwareVersionPass**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The build or pass number of the management processor version.|
|Type|string|
|Read Only|True|

**Manager[{item}].Model**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The type of the service manager.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Mercury```|Manager Mode Mercury|
|```Wolfram```|Manager Mode Wolfram|

### Oem.Hpe.Sessions
**Oem.Hpe.Sessions.CertCommonName**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The name of the management processor as it appears in the digital certificate when a secure web GUI session is established to the management processor.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Sessions.KerberosEnabled**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Specifies whether Kerberos login is enabled.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Sessions.LDAPAuthLicenced**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Specifies whether a valid license is installed for LDAP use.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Sessions.LDAPEnabled**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Specifies whether LDAP login is enabled.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Sessions.LocalLoginEnabled**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Specifies whether local users can log in.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Sessions.LoginFailureDelay**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The delay (seconds) when a management processor login attempt has failed.|
|Type|integer|
|Read Only|True|

**Oem.Hpe.Sessions.LoginHint**
**Oem.Hpe.Sessions.LoginHint.Hint**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The information on how to log in to the management processor.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Sessions.LoginHint.HintPOSTData**
**Oem.Hpe.Sessions.LoginHint.HintPOSTData.Password**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The password for logging in to the management processor.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Sessions.LoginHint.HintPOSTData.UserName**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The user name for logging in to the management processor.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Sessions.SecurityMessage**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The login security banner message that is displayed on the management processor Login page.|
|Type|string|
|Read Only|True|

**Oem.Hpe.Sessions.SecurityOverride**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Specifies whether the security override switch is enabled.|
|Type|boolean|
|Read Only|True|

**Oem.Hpe.Sessions.ServerName**
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The name of the server that this management processor is managing.|
|Type|string|
|Read Only|True|

### RedfishVersion
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|The version of the Redfish service|
|Type|string|
|Read Only|True|

### Registries
The URI to this registries resource.
### SessionService
The URI to this sessions service resource.
### StorageServices
A link to a collection of all storage service entities.
### StorageSystems
This is a link to a collection of storage systems.
### Systems
The URI to this systems resource.
### Tasks
This is a link to the Task Service.
### UUID
Member of [ServiceRoot.v1_1_1.ServiceRoot](#serviceroot-v1_1_1-serviceroot)

| | |
|---|---|
|Description|Unique identifier for a service instance.  This value should be an exact match of the UUID value returned in a 200OK from an SSDP M-SEARCH request during discovery.|
|Type|string or null|
|Read Only|True|

### UpdateService
This is a link to the UpdateService.
## Session.v1_0_3.Session
```@odata.type: "#Session.v1_0_3.Session"```
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/sessionservice/sessions/{item}```|GET DELETE |

### Oem.Hpe.AccessTime
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|User session last-access time|
|Type|string|
|Read Only|True|

### Oem.Hpe.LoginTime
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|User session login time|
|Type|string|
|Read Only|True|

### Oem.Hpe.MySession
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|Indicates whether this is a session I own.|
|Type|boolean|
|Read Only|True|

### Oem.Hpe.Privilege
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|Account privileges available for the user|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Login```|Read operations allowed like viewing discovered nodes and groups and generate reports|
|```Device```|Allows configuring and performing actions on devices includes login privilege|
|```User```|Allows configuring users with device privilege|
|```Manager```|All operations allowed|

### Oem.Hpe.Type
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|This object represents the type property. It represents the schema used for the resource and indicates the version of the schema in the format <schema>.<majorversion>.<minorversion>.<errataversion>.|
|Type|string|
|Read Only|True|

### Oem.Hpe.UserAccount
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|Login details of the user|
|Type|string|
|Read Only|True|

### Oem.Hpe.UserExpires
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|User session expire time|
|Type|string|
|Read Only|True|

### Oem.Hpe.UserIP
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|IP address of the user|
|Type|string|
|Read Only|True|

### Oem.Hpe.UserTag
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|Session source|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Web UI```|
|```SSH```|
|```Console```|
|```Unknown```|

### Oem.Hpe.UserType
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|User type|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Local```|
|```Directory```|
|```Single Sign On```|
|```Kerberos```|
|```Trusted Key```|
|```Security Override```|
|```System```|
|```Federation```|

### Password
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|This property is used in a POST to specify a password when creating a new session.  This property is null on a GET.|
|Type|string or null|
|Read Only|True|

### UserName
Member of [Session.v1_0_3.Session](#session-v1_0_3-session)

| | |
|---|---|
|Description|Name to use to log in to the management processor.|
|Type|string|
|Read Only|True|

## SessionService.v1_1_1.SessionService
```@odata.type: "#SessionService.v1_1_1.SessionService"```

This is the schema definition for the Session Service.  It represents the properties for the service itself and has links to the actual list of sessions.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/sessionservice```|GET PATCH |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Sessions```|Collection of [Session](#session-v1_0_3-session)|

### ServiceEnabled
Member of [SessionService.v1_1_1.SessionService](#sessionservice-v1_1_1-sessionservice)

| | |
|---|---|
|Description|This indicates whether this service is enabled.|
|Type|boolean or null|
|Read Only|True|

### SessionTimeout
Member of [SessionService.v1_1_1.SessionService](#sessionservice-v1_1_1-sessionservice)

| | |
|---|---|
|Description|This is the number of seconds of inactivity that a session may have before the session service closes the session due to inactivity. Zero indicates that the session will not be closed due to inactivity.|
|Type|integer|
|Read Only|False|

The following are the supported values:

|Value|
|---|
|```Null```|
|```900```|
|```1800```|
|```3600```|
|```7200```|

### Sessions
This property references a Collection resource of Sessions.
### Status
Member of [SessionService.v1_1_1.SessionService](#sessionservice-v1_1_1-sessionservice)
See the Redfish standard schema and specification for information on common Status object.

## SoftwareInventory.v1_1_1.SoftwareInventory
```@odata.type: "#SoftwareInventory.v1_1_1.SoftwareInventory"```

This schema defines an inventory of software components.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/updateservice/firmwareinventory/{item}```|GET |
|```/redfish/v1/updateservice/softwareinventory/{item}```|GET |

### LowestSupportedVersion
Member of [SoftwareInventory.v1_1_1.SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)

| | |
|---|---|
|Description|A string representing the lowest supported version of this software.|
|Type|string or null|
|Read Only|True|

### Oem.Hpe.DeviceClass
Member of [SoftwareInventory.v1_1_1.SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)

| | |
|---|---|
|Description|The Device Class of the firmware.|
|Type|string|
|Read Only|True|

### Oem.Hpe.DeviceContext
Member of [SoftwareInventory.v1_1_1.SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)

| | |
|---|---|
|Description|The Device Context of the firmware.|
|Type|string|
|Read Only|True|

### SoftwareId
Member of [SoftwareInventory.v1_1_1.SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)

| | |
|---|---|
|Description|A string representing the implementation-specific ID for identifying this software.|
|Type|string|
|Read Only|True|

### UefiDevicePaths (array)
Member of [SoftwareInventory.v1_1_1.SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)
```UefiDevicePaths``` is an array containing elements of:


| | |
|---|---|
|Type|string or null|
|Read Only|True|

### Updateable
Member of [SoftwareInventory.v1_1_1.SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)

| | |
|---|---|
|Description|Indicates whether this software can be updated by the update service.|
|Type|boolean or null|
|Read Only|True|

### Version
Member of [SoftwareInventory.v1_1_1.SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)

| | |
|---|---|
|Description|A string representing the version of this software.|
|Type|string or null|
|Read Only|True|

## Storage.v1_2_0.Storage
```@odata.type: "#Storage.v1_2_0.Storage"```

This schema defines a storage subsystem and its respective properties.  A storage subsystem represents a set of storage controllers (physical or virtual) and the resources such as volumes that can be accessed from that subsystem.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/systems/{item}/storage/{item}```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Volumes```|VolumeCollection|
|```Drives[]```|[Drive](#drive-v1_2_0-drive)|

### Drives (array)
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)
```Drives``` is an array containing elements of:

### Status
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)
See the Redfish standard schema and specification for information on common Status object.

### StorageControllers (array)
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)
```StorageControllers``` is an array containing elements of:

**StorageControllers[{item}].AssetTag**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|The user assigned asset tag for this storage controller.|
|Type|string or null|
|Read Only|False|

**StorageControllers[{item}].FirmwareVersion**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|The firmware version of this storage Controller.|
|Type|string or null|
|Read Only|True|

**StorageControllers[{item}].Identifiers (array)**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)
```Identifiers``` is an array containing elements of:

**Identifiers[{item}].DurableName**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|This indicates the world wide, persistent name of the resource.|
|Type|string or null|
|Read Only|True|

**Identifiers[{item}].DurableNameFormat**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

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

**StorageControllers[{item}].Manufacturer**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|This is the manufacturer of this storage controller.|
|Type|string or null|
|Read Only|True|

**StorageControllers[{item}].MemberId**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|This is the identifier for the member within the collection.|
|Type|string|
|Read Only|True|

**StorageControllers[{item}].Model**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|This is the model number for the storage controller.|
|Type|string or null|
|Read Only|True|

**StorageControllers[{item}].PartNumber**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|The part number for this storage controller.|
|Type|string or null|
|Read Only|True|

**StorageControllers[{item}].SKU**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|This is the SKU for this storage controller.|
|Type|string or null|
|Read Only|True|

**StorageControllers[{item}].SerialNumber**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|The serial number for this storage controller.|
|Type|string or null|
|Read Only|True|

**StorageControllers[{item}].SpeedGbps**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)

| | |
|---|---|
|Description|The speed of the storage controller interface.|
|Type|number or null|
|Read Only|True|

**StorageControllers[{item}].Status**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)
See the Redfish standard schema and specification for information on common Status object.

**StorageControllers[{item}].SupportedControllerProtocols (array)**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)
```SupportedControllerProtocols``` is an array containing elements of:


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

**StorageControllers[{item}].SupportedDeviceProtocols (array)**
Member of [Storage.v1_2_0.Storage](#storage-v1_2_0-storage)
```SupportedDeviceProtocols``` is an array containing elements of:


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

### Volumes
The set of volumes produced by the storage controllers represented by this resource.
## Task.v1_0_3.Task
```@odata.type: "#Task.v1_0_3.Task"```

This is the schema definition for a Task resource.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/taskservice/tasks/{item}0000```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Oem/Hpe/DetailedTaskLink```|[HpeWfmDeleteTask](#hpewfmdeletetask-v1_0_0-hpewfmdeletetask)|

### EndTime
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|The date-time stamp that the task was last completed.|
|Type|string|
|Read Only|True|

### Messages (array)
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)
```Messages``` is an array containing elements of:

**Messages[{item}].Message**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|This is the human readable message, if provided.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].MessageArgs (array)**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)
```MessageArgs``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].MessageId**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|This is the key for this message which can be used to look up the message in a message registry.|
|Type|string|
|Read Only|True|

**Messages[{item}].RelatedProperties (array)**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)
```RelatedProperties``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**Messages[{item}].Resolution**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|Used to provide suggestions on how to resolve the situation that caused the error.|
|Type|string or null|
|Read Only|True|

**Messages[{item}].Severity**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|This is the severity of the errors.|
|Type|string or null|
|Read Only|True|

### Oem.Hpe.CreatedBy
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|The name of the user that created this task.|
|Type|string|
|Read Only|True|

### Oem.Hpe.DetailedTaskLink
Detailed status of the task.
### Oem.Hpe.History
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|The history of the task.|
|Type|string|
|Read Only|True|

### Oem.Hpe.ProgressMessages (array)
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)
```ProgressMessages``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

### Oem.Hpe.ProgressPercent
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|The progress percent of this task.|
|Type|integer|
|Read Only|True|

### Oem.Hpe.SelectedAddress (array)
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

### Oem.Hpe.SelectedGroups (array)
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)
```SelectedGroups``` is an array containing elements of:

**SelectedGroups[{item}].GroupName**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|The Group name of the selected group.|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].SelectedAddress (array)**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)
```SelectedAddress``` is an array containing elements of:


| | |
|---|---|
|Type|string|
|Read Only|True|

**SelectedGroups[{item}].allSystemsInGroup**
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|The flag suggests whether all the servers in the group are selected.|
|Type|boolean|
|Read Only|True|

### Oem.Hpe.SubTaskCount
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|Number of subtasks for this task.|
|Type|integer|
|Read Only|True|

### Oem.Hpe.TaskIdentifier
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|A unique task identifier number for this task.|
|Type|integer|
|Read Only|True|

### StartTime
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

| | |
|---|---|
|Description|The date-time stamp that the task was last started.|
|Type|string|
|Read Only|True|

### TaskState
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

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

### TaskStatus
Member of [Task.v1_0_3.Task](#task-v1_0_3-task)

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

## TaskService.v1_0_3.TaskService
```@odata.type: "#TaskService.v1_0_3.TaskService"```

This is the schema definition for the Task Service.  It represents the properties for the service itself and has links to the various tasks that can be peformed by the system.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/taskservice```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Tasks```|Collection of [Task](#task-v1_0_3-task)|
|```Oem/Hpe/ResetSystemTasks```|Collection of [HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)|

### CompletedTaskOverWritePolicy
Member of [TaskService.v1_0_3.TaskService](#taskservice-v1_0_3-taskservice)

| | |
|---|---|
|Description|Overwrite policy of completed tasks|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Manual```|Completed tasks are not automatically overwritten|
|```Oldest```|Oldest completed tasks are overwritten|

### DateTime
Member of [TaskService.v1_0_3.TaskService](#taskservice-v1_0_3-taskservice)

| | |
|---|---|
|Description|The current DateTime (with offset) setting that the task service is using.|
|Type|string or null|
|Read Only|True|

### LifeCycleEventOnTaskStateChange
Member of [TaskService.v1_0_3.TaskService](#taskservice-v1_0_3-taskservice)

| | |
|---|---|
|Description|Send an Event upon Task State Change.|
|Type|boolean|
|Read Only|True|

### Oem.Hpe.AhsDownloadTasks
This property references a collection resource of AHS download tasks.
### Oem.Hpe.ApplyPersonaTasks
This property references a collection resource of apply persona tasks.
### Oem.Hpe.ConfigureRemoteSyslogTasks
This property references a collection resource of configure remote syslog tasks.
### Oem.Hpe.CreateGroupTasks
This property references a collection resource of Create Group tasks.
### Oem.Hpe.DeleteTasks
This property references a collection resource of delete tasks.
### Oem.Hpe.ImportBaselineTasks
This property references a collection resource of Import SPP tasks.
### Oem.Hpe.ImportPersonaTasks
This property references a collection resource of import persona tasks.
### Oem.Hpe.InstallLicenseTasks
This property references a collection resource of License Install tasks.
### Oem.Hpe.NonInteractiveOnlineUpdateTasks
This property references a collection resource of Non Interactive Update tasks.
### Oem.Hpe.OfflineUpdateTasks
This property references a collection resource of offline firmware update tasks.
### Oem.Hpe.OnlineSppUpdateTasks
This property references a collection resource of online SPP update tasks.
### Oem.Hpe.OnlineUpdateTasks
This property references a collection resource of offline firmware update tasks.
### Oem.Hpe.OsProvisioningTasks
This property references a collection resource of OS Provisioning tasks.
### Oem.Hpe.RefreshTasks
This property references a collection resource of refresh tasks.
### Oem.Hpe.ResetSystemTasks
This property references a collection resource of System Reset tasks.
### Oem.Hpe.SetIndicatorLedTasks
This property references a collection resource of Setting Indicator LED tasks.
### Oem.Hpe.SppComplianceTasks
This property references a collection resource of Spp compliance tasks.
### Oem.Hpe.UpdateFirmwareTasks
This property references a collection resource of firmware update tasks.
### Oem.Hpe.ValidatePersonaTasks
This property references a collection resource of validate persona tasks.
### Oem.Hpe.VirtualMediaTasks
This property references a collection resource of virtual media tasks.
### ServiceEnabled
Member of [TaskService.v1_0_3.TaskService](#taskservice-v1_0_3-taskservice)

| | |
|---|---|
|Description|This indicates whether this service is enabled.|
|Type|boolean or null|
|Read Only|True|

### Status
Member of [TaskService.v1_0_3.TaskService](#taskservice-v1_0_3-taskservice)
See the Redfish standard schema and specification for information on common Status object.

### Tasks
This property references a collection resource of summary of tasks.
## Thermal.v1_3_0.Thermal
```@odata.type: "#Thermal.v1_3_0.Thermal"```

This is the schema definition for the Thermal properties. It represents the properties for Temperature and Cooling.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/chassis/8f55097c/thermal```|GET |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```Fans[]/RelatedItem[]```|[ComputerSystem](#computersystem-v1_3_0-computersystem)|

### Fans (array)
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)
```Fans``` is an array containing elements of:

**Fans[{item}].FanName**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Name of the fan.|
|Type|string or null|
|Read Only|True|

**Fans[{item}].IndicatorLED**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|The state of the indicator LED, used to identify this Fan.|
|Type|string|
|Read Only|False|

The following are the supported values:

|Value|Description|
|---|---|
|```Lit```|The Indicator LED is lit.|
|```Blinking```|The Indicator LED is blinking.|
|```Off```|The Indicator LED is off.|

**Fans[{item}].LowerThresholdCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Below normal range but not yet fatal.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].LowerThresholdFatal**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Below normal range and is fatal.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].LowerThresholdNonCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Below normal range.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].Manufacturer**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|This is the manufacturer of this Fan.|
|Type|string or null|
|Read Only|True|

**Fans[{item}].MaxReadingRange**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Maximum value for Reading.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].MemberId**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|This is the identifier for the member within the collection.|
|Type|string|
|Read Only|True|

**Fans[{item}].MinReadingRange**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Minimum value for Reading.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].Model**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|The model number for this Fan.|
|Type|string or null|
|Read Only|True|

**Fans[{item}].PartNumber**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|The part number for this Fan.|
|Type|string or null|
|Read Only|True|

**Fans[{item}].PhysicalContext**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Room```|The room.|
|```Intake```|The intake point of the chassis.|
|```Exhaust```|The exhaust point of the chassis.|
|```Front```|The front of the chassis.|
|```Back```|The back of the chassis.|
|```Upper```|The upper portion of the chassis.|
|```Lower```|The lower portion of the chassis.|
|```CPU```|A Processor (CPU).|
|```GPU```|A Graphics Processor (GPU).|
|```Backplane```|A backplane within the chassis.|
|```SystemBoard```|The system board (PCB).|
|```PowerSupply```|A power supply.|
|```VoltageRegulator```|A voltage regulator device.|
|```StorageDevice```|A storage device.|
|```NetworkingDevice```|A networking device.|
|```ComputeBay```|Within a compute bay.|
|```StorageBay```|Within a storage bay.|
|```NetworkBay```|Within a networking bay.|
|```ExpansionBay```|Within an expansion bay.|
|```PowerSupplyBay```|Within a power supply bay.|
|```Memory```|A memory device.|

**Fans[{item}].Reading**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Current fan speed.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].ReadingUnits**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Units in which the reading and thresholds are measured.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```RPM```|Indicates that the fan reading and thresholds are measured in rotations per minute.|
|```Percent```|Indicates that the fan reading and thresholds are measured in percentage.|

**Fans[{item}].RelatedItem (array)**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)
```RelatedItem``` is an array containing elements of:

**Fans[{item}].SerialNumber**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|The serial number for this Fan.|
|Type|string or null|
|Read Only|True|

**Fans[{item}].SparePartNumber**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|The spare part number for this Fan.|
|Type|string or null|
|Read Only|True|

**Fans[{item}].Status**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)
See the Redfish standard schema and specification for information on common Status object.

**Fans[{item}].UpperThresholdCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Above normal range but not yet fatal.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].UpperThresholdFatal**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Above normal range and is fatal.|
|Type|number or null|
|Read Only|True|

**Fans[{item}].UpperThresholdNonCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Above normal range.|
|Type|number or null|
|Read Only|True|

### Status
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)
See the Redfish standard schema and specification for information on common Status object.

### Temperatures
**Temperatures.LowerThresholdCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Below normal range but not yet fatal.|
|Type|number or null|
|Read Only|True|

**Temperatures.LowerThresholdFatal**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Below normal range and is fatal.|
|Type|number or null|
|Read Only|True|

**Temperatures.LowerThresholdNonCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Below normal range.|
|Type|number or null|
|Read Only|True|

**Temperatures.MaxReadingRangeTemp**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Maximum value for ReadingCelsius.|
|Type|number or null|
|Read Only|True|

**Temperatures.MemberId**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|This is the identifier for the member within the collection.|
|Type|string|
|Read Only|True|

**Temperatures.MinReadingRangeTemp**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Minimum value for ReadingCelsius.|
|Type|number or null|
|Read Only|True|

**Temperatures.PhysicalContext**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|Description|
|---|---|
|```Room```|The room.|
|```Intake```|The intake point of the chassis.|
|```Exhaust```|The exhaust point of the chassis.|
|```Front```|The front of the chassis.|
|```Back```|The back of the chassis.|
|```Upper```|The upper portion of the chassis.|
|```Lower```|The lower portion of the chassis.|
|```CPU```|A Processor (CPU).|
|```GPU```|A Graphics Processor (GPU).|
|```Backplane```|A backplane within the chassis.|
|```SystemBoard```|The system board (PCB).|
|```PowerSupply```|A power supply.|
|```VoltageRegulator```|A voltage regulator device.|
|```StorageDevice```|A storage device.|
|```NetworkingDevice```|A networking device.|
|```ComputeBay```|Within a compute bay.|
|```StorageBay```|Within a storage bay.|
|```NetworkBay```|Within a networking bay.|
|```ExpansionBay```|Within an expansion bay.|
|```PowerSupplyBay```|Within a power supply bay.|
|```Memory```|A memory device.|

**Temperatures.ReadingCelsius**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Temperature.|
|Type|number or null|
|Read Only|True|

**Temperatures.RelatedItem (array)**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)
```RelatedItem``` is an array containing elements of:

**Temperatures.SensorNumber**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|A numerical identifier to represent the temperature sensor.|
|Type|number or null|
|Read Only|True|

**Temperatures.Status**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)
See the Redfish standard schema and specification for information on common Status object.

**Temperatures.UpperThresholdCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Above normal range but not yet fatal.|
|Type|number or null|
|Read Only|True|

**Temperatures.UpperThresholdFatal**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Above normal range and is fatal.|
|Type|number or null|
|Read Only|True|

**Temperatures.UpperThresholdNonCritical**
Member of [Thermal.v1_3_0.Thermal](#thermal-v1_3_0-thermal)

| | |
|---|---|
|Description|Above normal range.|
|Type|number or null|
|Read Only|True|

## UpdateService.v1_2_0.UpdateService
```@odata.type: "#UpdateService.v1_2_0.UpdateService"```

This is the schema definition for the Update Service. It represents the properties for the service itself and has links to collections of firmware and software inventory.
### Resource Instances
|Uri|HTTP Allow|
|---|---|
|```/redfish/v1/updateservice```|GET POST |

### Links to other Resources
|Link Name|Destination type
|---|---|
|```FirmwareInventory```|SoftwareInventoryCollection|
|```SoftwareInventory```|SoftwareInventoryCollection|

### FirmwareInventory
An inventory of firmware.
### HttpPushUri
Member of [UpdateService.v1_2_0.UpdateService](#updateservice-v1_2_0-updateservice)

| | |
|---|---|
|Description|The URI used to perform an HTTP or HTTPS push update to the Update Service.|
|Type|string|
|Read Only|True|

### HttpPushUriTargets (array)
Member of [UpdateService.v1_2_0.UpdateService](#updateservice-v1_2_0-updateservice)
```HttpPushUriTargets``` is an array containing elements of:


| | |
|---|---|
|Type|string or null|
|Read Only|True|

### HttpPushUriTargetsBusy
Member of [UpdateService.v1_2_0.UpdateService](#updateservice-v1_2_0-updateservice)

| | |
|---|---|
|Description|This represents if the HttpPushUriTargets property is reserved by any client.|
|Type|boolean or null|
|Read Only|False|

### Oem.Hpe.ProgressPercent
Member of [UpdateService.v1_2_0.UpdateService](#updateservice-v1_2_0-updateservice)

| | |
|---|---|
|Description|The progress percentage of firmware update.|
|Type|integer|
|Read Only|True|

### Oem.Hpe.State
Member of [UpdateService.v1_2_0.UpdateService](#updateservice-v1_2_0-updateservice)

| | |
|---|---|
|Description|The State of firmware update.|
|Type|string|
|Read Only|True|

The following are the supported values:

|Value|
|---|
|```Idle```|
|```In Progress```|
|```Completed```|
|```Error```|

### ServiceEnabled
Member of [UpdateService.v1_2_0.UpdateService](#updateservice-v1_2_0-updateservice)

| | |
|---|---|
|Description|This indicates whether this service is enabled.|
|Type|boolean or null|
|Read Only|False|

### SoftwareInventory
An inventory of software.
### Actions

**ManagerUpdate**
Member of [UpdateService.v1_2_0.UpdateService](#updateservice-v1_2_0-updateservice)
Performs Update of Central Management Device.


**Parameters:**

**MountPath (string)**

The mount path of the network share server where the Firmware Binary is present.

**Target (string)**

The Target defines an OEM action.

|Value|Description|
|---|---|
|/Oem/Hpe|

**StorageType (string)**

The type of storage on which the Firmware Binary is present.

|Value|Description|
|---|---|
|RemovableStorage|
|NetworkShare|
|ClientUpload|
|HTTPShare|

**FirmwarePath (string)**

The file path where the Firmware Binary is present.

**RemovableStorageDeviceName (string)**

The device name of the removable storage.

**NetworkShareAddress (string)**

The network share IP address or DNS name where the Firmware Binary is present.

