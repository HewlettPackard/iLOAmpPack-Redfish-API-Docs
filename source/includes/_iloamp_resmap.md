# Resource Map
|URI|Type|
|:---|:---|
|`/redfish/v1`|[ServiceRoot](#serviceroot-1-3-1)|
|`/redfish/v1/AccountService`|[AccountService](#accountservice-1-3-0)|
|`/redfish/v1/AccountService/Accounts`|Collection of [ManagerAccount](#manageraccount-1-1-2)|
|`/redfish/v1/AccountService/Accounts/{item}`|[ManagerAccount](#manageraccount-1-1-2)|
|`/redfish/v1/AccountService/PrivilegeRegistry`|[PrivilegeRegistry](#privilegeregistry-1-1-1)|
|`/redfish/v1/AccountService/Roles`|Collection of [Role](#role-1-2-1)|
|`/redfish/v1/AddOnServices`|Collection of [HpeWfmAddOnServices](#hpewfmaddonservices)|
|`/redfish/v1/AggregatorService`|[HpeWfmAggregatorService](#hpewfmaggregatorservice)|
|`/redfish/v1/AggregatorService/Dashboard/Alerts`|[HpeWfmDashboardAlerts](#hpewfmdashboardalerts)|
|`/redfish/v1/AggregatorService/Dashboard/Assets`|[HpeWfmDashboardAssets](#hpewfmdashboardassets)|
|`/redfish/v1/AggregatorService/Dashboard/Compliance`|[HpeWfmDashboardCompliance](#hpewfmdashboardcompliance)|
|`/redfish/v1/AggregatorService/Dashboard/InfoSightAlerts`|[HpeWfmDashboardInfoSightAlerts](#hpewfmdashboardInfoSightalerts-v1_0_0-hpewfmdashboardInfoSightalerts)|
|`/redfish/v1/AggregatorService/Dashboard/ServerGroups`|[HpeWfmDashboardServerGroups](#hpewfmdashboardservergroups)|
|`/redfish/v1/AggregatorService/FederationGroups`|Collection of [HpeWfmFederationGroup](#hpewfmfederationgroup)|
|`/redfish/v1/AggregatorService/LicenseInfo`|[HpeWfmLicenseInfo](#hpewfmlicenseinfo)|
|`/redfish/v1/AggregatorService/LogServices`|Collection of [LogService](#logservice-1-1-0)|
|`/redfish/v1/AggregatorService/LogServices/AlertLog`|[LogService](#logservice-1-1-0)|
|`/redfish/v1/AggregatorService/LogServices/AlertLog/Entries`|Collection of [LogEntry](#logentry-1-3-0)|
|`/redfish/v1/AggregatorService/ManagedGroups`|Collection of [HpeWfmManagedGroup](#hpewfmmanagedgroup)|
|`/redfish/v1/AggregatorService/ManagedServerGroups`|Collection of [HpeWfmManagedServerGroups](#hpewfmmanagedservergroups)|
|`/redfish/v1/AggregatorService/ManagedServerGroups/{item}`|[HpeWfmManagedServerGroups](#hpewfmmanagedservergroups)|
|`/redfish/v1/AggregatorService/ManagedServerGroups/{item}/ManagedSystems`|Collection of [HpeWfmManagedSystem](#hpewfmmanagedsystem)|
|`/redfish/v1/AggregatorService/ManagedServerGroups/{item}/ManagedSystems/{item}`|[HpeWfmManagedSystem](#hpewfmmanagedsystem)|
|`/redfish/v1/AggregatorService/ManagedServerGroups/{item}/ManagedSystems/{item}`|Collection of [HpeWfmSystemSummary](#hpewfmsystemsummary)|
|`/redfish/v1/AggregatorService/ManagedServerGroups/{item}/ManagedSystems/{item}/Summary`|[HpeWfmSystemSummary](#hpewfmsystemsummary)|
|`/redfish/v1/AggregatorService/ManagedSystems`|Collection of [HpeWfmManagedSystem](#hpewfmmanagedsystem)|
|`/redfish/v1/AggregatorService/ManagedSystems/{item}`|[HpeWfmManagedSystem](#hpewfmmanagedsystem)|
|`/redfish/v1/AggregatorService/ManagedSystems/{item}`|Collection of [HpeWfmSystemSummary](#hpewfmsystemsummary)|
|`/redfish/v1/AggregatorService/ManagedSystems/{item}/Summary`|[HpeWfmSystemSummary](#hpewfmsystemsummary)|
|`/redfish/v1/AggregatorService/Reports`|Collection of [HpeWfmManagedSystem](#hpewfmmanagedsystem-v1_0_0-hpewfmmanagedsystem)|
|`/redfish/v1/AggregatorService/ServerGroups`|Collection of [HpeWfmServerGroups](#hpewfmservergroups)|
|`/redfish/v1/AggregatorService/ServerGroups/{item}`|[HpeWfmServerGroups](#hpewfmservergroups)|
|`/redfish/v1/AggregatorService/ServerGroups/{item}/Systems`|Collection of [ComputerSystem](#computersystem-1-5-0)|
|`/redfish/v1/AggregatorService/Systems`|Collection of [ComputerSystem](#computersystem-1-5-0)|
|`/redfish/v1/Chassis`|Collection of [Chassis](#chassis-1-7-0)|
|`/redfish/v1/Chassis/{item}`|[Chassis](#chassis-1-7-0)|
|`/redfish/v1/Chassis/{item}/Power`|[Power](#power-1-5-0)|
|`/redfish/v1/Chassis/{item}/Thermal`|[Thermal](#thermal-1-4-0)|
|`/redfish/v1/EventService`|[EventService](#eventservice-1-0-6)|
|`/redfish/v1/EventService/Subscriptions`|Collection of [EventDestination](#eventdestination-1-3-0)|
|`/redfish/v1/JobService`|[JobService](#jobservice-1-0-0)|
|`/redfish/v1/JobService/Jobs`|Collection of [Job](#job-1-0-1)|
|`/redfish/v1/JobService/Jobs/{item}`|[Job](#job-1-0-1)|
|`/redfish/v1/JobService/Jobs/{item}/Steps`|Collection of [Job](#job-1-0-1)|
|`/redfish/v1/JobService/Jobs/{item}/Steps/{item}`|[Job](#job-v1_0_1-job)|
|`/redfish/v1/JobService/Results/BaselineComplianceJobs/{item}`|[HpeWfmSppComplianceJobResults](#hpewfmsppcompliancejobresults)|
|`/redfish/v1/JobService/Results/ServerUpdateJobs/{item}`|Collection of [HpeWfmUpdateJobResults](#hpewfmupdatejobresults)|
|`/redfish/v1/JobService/Results/ServerUpdateJobs/{item}/{item}`|[HpeWfmUpdateJobResults](#hpewfmupdatejobresults)|
|`/redfish/v1/Managers`|Collection of [Manager](#manager-1-4-0)|
|`/redfish/v1/Managers/iLOAmplifier`|[Manager](#manager-1-4-0)|
|`/redfish/v1/Managers/iLOAmplifier/AddOnServicesManager`|Collection of [HpeWfmAddOnServicesManager](#hpewfmaddonservicesmanager-v1_0_0-hpewfmaddonservicesmanager)|
|`/redfish/v1/Managers/iLOAmplifier/AddOnServicesManager/hpehsm`|[HpeWfmAddOnServicesManager](#hpewfmaddonservicesmanager-v1_0_0-hpewfmaddonservicesmanager)|
|`/redfish/v1/Managers/iLOAmplifier/BaselineService`|[HpeWfmBaselineService](#hpewfmbaselineservice)|
|`/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines`|Collection of [HpeWfmBaseline](#hpewfmbaseline)|
|`/redfish/v1/Managers/iLOAmplifier/BaselineService/Baselines/{item}`|[HpeWfmBaseline](#hpewfmbaseline)|
|`/redfish/v1/Managers/iLOAmplifier/DateTime`|[HpeWfmDateTime](#hpewfmdatetime)|
|`/redfish/v1/Managers/iLOAmplifier/EthernetInterfaces`|Collection of [EthernetInterface](#ethernetinterface-1-4-0)|
|`/redfish/v1/Managers/iLOAmplifier/EthernetInterfaces/{item}`|[EthernetInterface](#ethernetinterface-1-4-0)|
|`/redfish/v1/Managers/iLOAmplifier/InfoSightPolicy`|[HpeWfmInfoSightAggregation](#hpewfmInfoSightaggregation)|
|`/redfish/v1/Managers/iLOAmplifier/LicenseService`|Collection of [HpeWfmLicense](#hpewfmlicense)|
|`/redfish/v1/Managers/iLOAmplifier/LicenseService/{item}`|[HpeWfmLicense](#hpewfmlicense)|
|`/redfish/v1/Managers/iLOAmplifier/LogServices`|Collection of [LogService](#logservice-1-1-0)|
|`/redfish/v1/Managers/iLOAmplifier/LogServices/DeviceAlertLog`|[LogService](#logservice-1-1-0)|
|`/redfish/v1/Managers/iLOAmplifier/LogServices/DeviceAlertLog/Entries`|Collection of [LogEntry](#logentry-1-3-0)|
|`/redfish/v1/Managers/iLOAmplifier/NetworkProtocol`|[ManagerNetworkProtocol](#managernetworkprotocol-1-2-0)|
|`/redfish/v1/Managers/iLOAmplifier/SecurityService`|[HpeSecurityService](#hpesecurityservice)|
|`/redfish/v1/Managers/iLOAmplifier/SecurityService/HttpsCACerts`|Collection of [HpeWfmHttpsCert](#hpewfmhttpscert)|
|`/redfish/v1/Managers/iLOAmplifier/SecurityService/HttpsCert`|[HpeHttpsCert](#hpehttpscert)|
|`/redfish/v1/Registries`|Collection of [MessageRegistryFile](#messageregistryfile-1-1-0)|
|`/redfish/v1/Registries/{item}`|[MessageRegistryFile](#messageregistryfile-1-1-0)|
|`/redfish/v1/Schemas`|Collection of [JsonSchemaFile](#jsonschemafile-1-1-0)|
|`/redfish/v1/Schemas/{item}`|[JsonSchemaFile](#jsonschemafile-1-1-0)|
|`/redfish/v1/SessionService`|[SessionService](#sessionservice-1-1-3)|
|`/redfish/v1/SessionService/Sessions`|Collection of [Session](#session-1-1-0)|
|`/redfish/v1/SessionService/Sessions/{item}`|[Session](#session-1-1-0)|
|`/redfish/v1/Systems`|Collection of [ComputerSystem](#computersystem-1-5-0)|
|`/redfish/v1/Systems/{item}`|[ComputerSystem](#computersystem-1-5-0)|
|`/redfish/v1/Systems/{item}/EthernetInterfaces`|Collection of [EthernetInterface](#ethernetinterface-1-4-0)|
|`/redfish/v1/Systems/{item}/EthernetInterfaces/{item}`|[EthernetInterface](#ethernetinterface-1-4-0)|
|`/redfish/v1/Systems/{item}/FirmwareInventory`|Collection of [SoftwareInventory](#softwareinventory-1-2-0)|
|`/redfish/v1/Systems/{item}/Memory`|Collection of [Memory](#memory-1-5-0)|
|`/redfish/v1/Systems/{item}/Memory/{item}`|[Memory](#memory-1-5-0)|
|`/redfish/v1/Systems/{item}/Processor`|Collection of [Processor](#processor-1-3-0)|
|`/redfish/v1/Systems/{item}/Processor/{item}`|[Processor](#processor-1-3-0)|
|`/redfish/v1/Systems/{item}/SoftwareInventory`|Collection of [SoftwareInventory](#softwareinventory-1-2-0)|
|`/redfish/v1/Systems/{item}/Storage`|Collection of [Storage](#storage-1-4-0)|
|`/redfish/v1/Systems/{item}/Storage/{item}`|[Storage](#storage-1-4-0)|
|`/redfish/v1/Systems/{item}/Storage/{item}/Drives/{item}`|[Drive](#drive-1-4-0)|
|`/redfish/v1/Systems/{item}/Storage/{item}/Volumes`|Collection of [Volume](#volume-1-0-3)|
|`/redfish/v1/Systems/{item}/Storage/{item}/Volumes/{item}`|[Volume](#volume-1-0-3)|
|`/redfish/v1/TaskService`|[TaskService](#taskservice-1-1-1)|
|`/redfish/v1/TaskService/Tasks`|Collection of [Task](#task-1-2-0)|
|`/redfish/v1/TaskService/Tasks/{item}`|[Task](#task-1-2-0)|
|`/redfish/v1/UpdateService`|[UpdateService](#updateservice-1-2-1)|
|`/redfish/v1/UpdateService/FirmwareInventory`|Collection of [SoftwareInventory](#softwareinventory-1-2-0)|
|`/redfish/v1/UpdateService/FirmwareInventory/{item}`|[SoftwareInventory](#softwareinventory-1-2-0)|
|`/redfish/v1/UpdateService/SoftwareInventory`|Collection of [SoftwareInventory](#softwareinventory-1-2-0)|
|`/redfish/v1/UpdateService/SoftwareInventory/{item}`|[SoftwareInventory](#softwareinventory-1-2-0)|
