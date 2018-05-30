# Resource Map
|URI|Type|
|:---|:---|
|`/redfish/v1/`|[ServiceRoot](#serviceroot-v1_1_1-serviceroot)|
|`/redfish/v1/accountservice`|[AccountService](#accountservice-v1_0_4-accountservice)|
|`/redfish/v1/accountservice/accounts`|Collection of [ManagerAccount](#manageraccount-v1_0_3-manageraccount)|
|`/redfish/v1/accountservice/accounts/{item}`|[ManagerAccount](#manageraccount-v1_0_3-manageraccount)|
|`/redfish/v1/accountservice/privilegeregistry`|[PrivilegeRegistry](#privilegeregistry-v1_0_0-privilegeregistry)|
|`/redfish/v1/accountservice/roles`|Collection of [Role](#role-v1_0_0-role)|
|`/redfish/v1/accountservice/roles/administrator`|[Role](#role-v1_0_0-role)|
|`/redfish/v1/accountservice/roles/configmanagerrole`|[Role](#role-v1_0_0-role)|
|`/redfish/v1/aggregatorservice`|[HpeWfmAggregatorService](#hpewfmaggregatorservice-v1_1_0-hpewfmaggregatorservice)|
|`/redfish/v1/aggregatorservice/federationgroups`|HpeWfmFederationGroupCollection|
|`/redfish/v1/aggregatorservice/logservices`|Collection of [LogService](#logservice-v1_0_3-logservice)|
|`/redfish/v1/aggregatorservice/logservices/alertlog`|[LogService](#logservice-v1_0_3-logservice)|
|`/redfish/v1/aggregatorservice/logservices/alertlog/entries`|Collection of [LogEntry](#logentry-v1_1_1-logentry)|
|`/redfish/v1/aggregatorservice/logservices/alertlog/entries/{item}`|[LogEntry](#logentry-v1_1_1-logentry)|
|`/redfish/v1/aggregatorservice/managedgroups`|HpeWfmManagedGroupCollection|
|`/redfish/v1/aggregatorservice/managedsystems`|Collection of [HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)|
|`/redfish/v1/aggregatorservice/managedsystems/{item}`|[HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)|
|`/redfish/v1/aggregatorservice/managedsystems/{item}/reportssummary`|[HpeWfmReportsSummary](#hpewfmreportssummary-v1_0_0-hpewfmreportssummary)|
|`/redfish/v1/aggregatorservice/managedsystems/{item}/summary`|[HpeWfmSystemSummary](#hpewfmsystemsummary-v1_0_0-hpewfmsystemsummary)|
|`/redfish/v1/aggregatorservice/systems`|Collection of [ComputerSystem](#computersystem-v1_3_0-computersystem)|
|`/redfish/v1/chassis`|Collection of [Chassis](#chassis-v1_4_0-chassis)|
|`/redfish/v1/chassis/8f55097c`|[Chassis](#chassis-v1_4_0-chassis)|
|`/redfish/v1/chassis/8f55097c/power`|[Power](#power-v1_3_0-power)|
|`/redfish/v1/chassis/8f55097c/thermal`|[Thermal](#thermal-v1_3_0-thermal)|
|`/redfish/v1/managers`|Collection of [Manager](#manager-v1_3_0-manager)|
|`/redfish/v1/managers/iloamplifier`|[Manager](#manager-v1_3_0-manager)|
|`/redfish/v1/managers/iloamplifier/datetime`|[HpeWfmDateTime](#hpewfmdatetime-v1_0_0-hpewfmdatetime)|
|`/redfish/v1/managers/iloamplifier/debuglogpolicy`|[HpeWfmDebugLogs](#hpewfmdebuglogs-v1_0_0-hpewfmdebuglogs)|
|`/redfish/v1/managers/iloamplifier/ethernetinterfaces`|Collection of [EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)|
|`/redfish/v1/managers/iloamplifier/ethernetinterfaces/{item}`|[EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)|
|`/redfish/v1/managers/iloamplifier/licenseservice`|Collection of [HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)|
|`/redfish/v1/managers/iloamplifier/licenseservice/{item}`|[HpeWfmLicense](#hpewfmlicense-v1_0_0-hpewfmlicense)|
|`/redfish/v1/managers/iloamplifier/logservices`|Collection of [LogService](#logservice-v1_0_3-logservice)|
|`/redfish/v1/managers/iloamplifier/logservices/devicealertlog`|[LogService](#logservice-v1_0_3-logservice)|
|`/redfish/v1/managers/iloamplifier/logservices/devicealertlog/entries`|Collection of [LogEntry](#logentry-v1_1_1-logentry)|
|`/redfish/v1/managers/iloamplifier/logservices/devicealertlog/entries/{item}`|[LogEntry](#logentry-v1_1_1-logentry)|
|`/redfish/v1/managers/iloamplifier/networkprotocol`|[ManagerNetworkProtocol](#managernetworkprotocol-v1_1_0-managernetworkprotocol)|
|`/redfish/v1/managers/iloamplifier/securityservice`|[HpeSecurityService](#hpesecurityservice-v1_0_0-hpesecurityservice)|
|`/redfish/v1/managers/iloamplifier/securityservice/httpscacerts`|HpWfmHttpsCertCollection|
|`/redfish/v1/managers/iloamplifier/securityservice/httpscert`|[HpeHttpsCert](#hpehttpscert-v1_0_0-hpehttpscert)|
|`/redfish/v1/managers/iloamplifier/telemetry`|[HpeWfmTelemetryInfo](#hpewfmtelemetryinfo-v1_0_0-hpewfmtelemetryinfo)|
|`/redfish/v1/registries`|Collection of [MessageRegistryFile](#messageregistryfile-v1_1_0-messageregistryfile)|
|`/redfish/v1/registries/{item}`|[MessageRegistryFile](#messageregistryfile-v1_1_0-messageregistryfile)|
|`/redfish/v1/schemas`|Collection of [JsonSchemaFile](#jsonschemafile-v1_0_3-jsonschemafile)|
|`/redfish/v1/schemas/{item}`|[JsonSchemaFile](#jsonschemafile-v1_0_3-jsonschemafile)|
|`/redfish/v1/sessionservice`|[SessionService](#sessionservice-v1_1_1-sessionservice)|
|`/redfish/v1/sessionservice/sessions`|Collection of [Session](#session-v1_0_3-session)|
|`/redfish/v1/sessionservice/sessions/{item}`|[Session](#session-v1_0_3-session)|
|`/redfish/v1/systems`|Collection of [ComputerSystem](#computersystem-v1_3_0-computersystem)|
|`/redfish/v1/systems/{item}`|[ComputerSystem](#computersystem-v1_3_0-computersystem)|
|`/redfish/v1/systems/{item}/ethernetinterfaces`|Collection of [EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)|
|`/redfish/v1/systems/{item}/ethernetinterfaces/{item}`|[EthernetInterface](#ethernetinterface-v1_2_0-ethernetinterface)|
|`/redfish/v1/systems/{item}/firmwareinventory`|SoftwareInventoryCollection|
|`/redfish/v1/systems/{item}/memory`|Collection of [Memory](#memory-v1_2_0-memory)|
|`/redfish/v1/systems/{item}/memory/{item}`|[Memory](#memory-v1_2_0-memory)|
|`/redfish/v1/systems/{item}/pciedevices`|Collection of [PCIeDevice](#pciedevice-v1_1_0-pciedevice)|
|`/redfish/v1/systems/{item}/pciedevices/{item}`|[PCIeDevice](#pciedevice-v1_1_0-pciedevice)|
|`/redfish/v1/systems/{item}/pciedevices/{item}/pciefunction`|[PCIeFunction](#pciefunction-v1_1_0-pciefunction)|
|`/redfish/v1/systems/{item}/processor`|Collection of [Processor](#processor-v1_1_0-processor)|
|`/redfish/v1/systems/{item}/processor/{item}`|[Processor](#processor-v1_1_0-processor)|
|`/redfish/v1/systems/{item}/softwareinventory`|SoftwareInventoryCollection|
|`/redfish/v1/systems/{item}/storage`|Collection of [Storage](#storage-v1_2_0-storage)|
|`/redfish/v1/systems/{item}/storage/{item}`|[Storage](#storage-v1_2_0-storage)|
|`/redfish/v1/systems/{item}/storage/{item}/drives/{item}`|[Drive](#drive-v1_2_0-drive)|
|`/redfish/v1/systems/{item}/storage/{item}/volumes`|VolumeCollection|
|`/redfish/v1/taskservice`|[TaskService](#taskservice-v1_0_3-taskservice)|
|`/redfish/v1/taskservice/resetsystemtasks`|Collection of [HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)|
|`/redfish/v1/taskservice/resetsystemtasks/{item}0000`|[HpeWfmResetSystemTask](#hpewfmresetsystemtask-v1_0_0-hpewfmresetsystemtask)|
|`/redfish/v1/taskservice/tasks`|Collection of [Task](#task-v1_0_3-task)|
|`/redfish/v1/taskservice/tasks/{item}0000`|[Task](#task-v1_0_3-task)|
|`/redfish/v1/updateservice`|[UpdateService](#updateservice-v1_2_0-updateservice)|
|`/redfish/v1/updateservice/firmwareinventory`|SoftwareInventoryCollection|
|`/redfish/v1/updateservice/firmwareinventory/{item}`|[SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)|
|`/redfish/v1/updateservice/softwareinventory`|SoftwareInventoryCollection|
|`/redfish/v1/updateservice/softwareinventory/{item}`|[SoftwareInventory](#softwareinventory-v1_1_1-softwareinventory)|
