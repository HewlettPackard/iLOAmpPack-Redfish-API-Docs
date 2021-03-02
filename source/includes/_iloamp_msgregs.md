
### Base.1.4.AccessDenied
Indicates that while attempting to access, connect to or transfer to/from another resource, the service denied access.

| | |
|:---|:---|
|Message Format|"While attempting to establish a connection to %1, the service denied access."
|Severity|Critical
|Resolution|Attempt to ensure that the URI is correct and that the service has the appropriate credentials.

### Base.1.4.AccountForSessionNoLongerExists
Indicates that the account for the session has been removed, thus the session has been removed as well.

| | |
|:---|:---|
|Message Format|"The account for the current session has been removed, thus the current session has been removed as well."
|Severity|OK
|Resolution|Attempt to connect with a valid account.

### Base.1.4.AccountModified
Indicates that the account was successfully modified.

| | |
|:---|:---|
|Message Format|"The account was successfully modified."
|Severity|OK
|Resolution|No resolution is required.

### Base.1.4.AccountNotModified
Indicates that the modification requested for the account was not successful.

| | |
|:---|:---|
|Message Format|"The account modification request failed."
|Severity|Warning
|Resolution|The modification may have failed due to permission issues or issues with the request body.

### Base.1.4.AccountRemoved
Indicates that the account was successfully removed.

| | |
|:---|:---|
|Message Format|"The account was successfully removed."
|Severity|OK
|Resolution|No resolution is required.

### Base.1.4.ActionNotSupported
Indicates that the action supplied with the POST operation is not supported by the resource.

| | |
|:---|:---|
|Message Format|"The action %1 is not supported by the resource."
|Severity|Critical
|Resolution|The action supplied cannot be resubmitted to the implementation.  Perhaps the action was invalid, the wrong resource was the target or the implementation documentation may be of assistance.

### Base.1.4.ActionParameterDuplicate
Indicates that the action was supplied with a duplicated parameter in the request body.

| | |
|:---|:---|
|Message Format|"The action %1 was submitted with more than one value for the parameter %2."
|Severity|Warning
|Resolution|Resubmit the action with only one instance of the parameter in the request body if the operation failed.

### Base.1.4.ActionParameterMissing
Indicates that the action requested was missing a parameter that is required to process the action.

| | |
|:---|:---|
|Message Format|"The action %1 requires the parameter %2 to be present in the request body."
|Severity|Critical
|Resolution|Supply the action with the required parameter in the request body when the request is resubmitted.

### Base.1.4.ActionParameterNotSupported
Indicates that the parameter supplied for the action is not supported on the resource.

| | |
|:---|:---|
|Message Format|"The parameter %1 for the action %2 is not supported on the target resource."
|Severity|Warning
|Resolution|Remove the parameter supplied and resubmit the request if the operation failed.

### Base.1.4.ActionParameterUnknown
Indicates that an action was submitted but a parameter supplied did not match any of the known parameters.

| | |
|:---|:---|
|Message Format|"The action %1 was submitted with the invalid parameter %2."
|Severity|Warning
|Resolution|Correct the invalid parameter and resubmit the request if the operation failed.

### Base.1.4.ActionParameterValueFormatError
Indicates that a parameter was given the correct value type but the value of that parameter was not supported.  This includes value size/length exceeded.

| | |
|:---|:---|
|Message Format|"The value %1 for the parameter %2 in the action %3 is of a different format than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the parameter in the request body and resubmit the request if the operation failed.

### Base.1.4.ActionParameterValueTypeError
Indicates that a parameter was given the wrong value type, such as when a number is supplied for a parameter that requires a string.

| | |
|:---|:---|
|Message Format|"The value %1 for the parameter %2 in the action %3 is of a different type than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the parameter in the request body and resubmit the request if the operation failed.

### Base.1.4.CouldNotEstablishConnection
Indicates that the attempt to access the resource/file/image at the URI was unsuccessful because a session could not be established.

| | |
|:---|:---|
|Message Format|"The service failed to establish a connection with the URI %1."
|Severity|Critical
|Resolution|Ensure that the URI contains a valid and reachable node name, protocol information and other URI components.

### Base.1.4.CreateFailedMissingReqProperties
Indicates that a create was attempted on a resource but that properties that are required for the create operation were missing from the request.

| | |
|:---|:---|
|Message Format|"The create operation failed because the required property %1 was missing from the request."
|Severity|Critical
|Resolution|Correct the body to include the required property with a valid value and resubmit the request if the operation failed.

### Base.1.4.CreateLimitReachedForResource
Indicates that no more resources can be created on the resource as it has reached its create limit.

| | |
|:---|:---|
|Message Format|"The create operation failed because the resource has reached the limit of possible resources."
|Severity|Critical
|Resolution|Either delete resources and resubmit the request if the operation failed or do not resubmit the request.

### Base.1.4.Created
Indicates that all conditions of a successful creation operation have been met.

| | |
|:---|:---|
|Message Format|"The resource has been created successfully"
|Severity|OK
|Resolution|None

### Base.1.4.EventServiceDisabled
Event subscription requests failed because Event Service is disabled. 

| | |
|:---|:---|
|Message Format|"Subscription request to %1 failed because the event service is not enabled."
|Severity|Warning
|Resolution|In order to perform any operations on subscriptions, please set ServiceEnabled to true at EventService level.

### Base.1.4.EventSubscriptionLimitExceeded
Indicates that a event subscription establishment has been requested but the operation failed due to the number of simultaneous connection exceeding the limit of the implementation.

| | |
|:---|:---|
|Message Format|"The event subscription failed due to the number of simultaneous subscriptions exceeding the limit of the implementation."
|Severity|Critical
|Resolution|Reduce the number of other subscriptions before trying to establish the event subscription or increase the limit of simultaneous subscriptions (if supported).

### Base.1.4.GeneralError
Indicates that a general error has occurred.

| | |
|:---|:---|
|Message Format|"A general error has occurred. See ExtendedInfo for more information."
|Severity|Critical
|Resolution|See ExtendedInfo for more information.

### Base.1.4.InfoSightServiceDisabed
Indicates that the request could not be performed because the infosight service is disabled.

| | |
|:---|:---|
|Message Format|"The request could not be performed because the infosight service is disabled."
|Severity|Critical
|Resolution|Ensure that the infosight service is enabled.

### Base.1.4.InsufficientPrivilege
Indicates that the credentials associated with the established session do not have sufficient privileges for the requested operation

| | |
|:---|:---|
|Message Format|"There are insufficient privileges for the account or credentials associated with the current session to perform the requested operation."
|Severity|Critical
|Resolution|Either abandon the operation or change the associated access rights and resubmit the request if the operation failed.

### Base.1.4.InternalError
Indicates that the request failed for an unknown internal error but that the service is still operational.

| | |
|:---|:---|
|Message Format|"The request failed due to an internal service error.  The service is still operational."
|Severity|Critical
|Resolution|Resubmit the request.  If the problem persists, consider resetting the service.

### Base.1.4.InvalidIndex
The Index is not valid.

| | |
|:---|:---|
|Message Format|"The Index %1 is not a valid offset into the array."
|Severity|Warning
|Resolution|Verify the index value provided is within the bounds of the array.

### Base.1.4.InvalidObject
Indicates that the object in question is invalid according to the implementation.  Examples include a firmware update malformed URI.

| | |
|:---|:---|
|Message Format|"The object at %1 is invalid."
|Severity|Critical
|Resolution|Either the object is malformed or the URI is not correct.  Correct the condition and resubmit the request if it failed.

### Base.1.4.MalformedJSON
Indicates that the request body was malformed JSON.  Could be duplicate, syntax error,etc.

| | |
|:---|:---|
|Message Format|"The request body submitted was malformed JSON and could not be parsed by the receiving service."
|Severity|Critical
|Resolution|Ensure that the request body is valid JSON and resubmit the request.

### Base.1.4.NoValidSession
Indicates that the operation failed because a valid session is required in order to access any resources.

| | |
|:---|:---|
|Message Format|"There is no valid session established with the implementation."
|Severity|Critical
|Resolution|Establish as session before attempting any operations.

### Base.1.4.PropertyDuplicate
Indicates that a duplicate property was included in the request body.

| | |
|:---|:---|
|Message Format|"The property %1 was duplicated in the request."
|Severity|Warning
|Resolution|Remove the duplicate property from the request body and resubmit the request if the operation failed.

### Base.1.4.PropertyMissing
Indicates that a required property was not supplied as part of the request.

| | |
|:---|:---|
|Message Format|"The property %1 is a required property and must be included in the request."
|Severity|Warning
|Resolution|Ensure that the property is in the request body and has a valid value and resubmit the request if the operation failed.

### Base.1.4.PropertyNotWritable
Indicates that a property was given a value in the request body, but the property is a readonly property.

| | |
|:---|:---|
|Message Format|"The property %1 is a read only property and cannot be assigned a value."
|Severity|Warning
|Resolution|Remove the property from the request body and resubmit the request if the operation failed.

### Base.1.4.PropertyUnknown
Indicates that an unknown property was included in the request body.

| | |
|:---|:---|
|Message Format|"The property %1 is not in the list of valid properties for the resource."
|Severity|Warning
|Resolution|Remove the unknown property from the request body and resubmit the request if the operation failed.

### Base.1.4.PropertyValueFormatError
Indicates that a property was given the correct value type but the value of that property was not supported.  This includes value size/length exceeded.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is of a different format than the property can accept."
|Severity|Warning
|Resolution|Correct the value for the property in the request body and resubmit the request if the operation failed.

### Base.1.4.PropertyValueModified
Indicates that a property was given the correct value type but the value of that property was modified.  Examples are truncated or rounded values.

| | |
|:---|:---|
|Message Format|"The property %1 was assigned the value %2 due to modification by the service."
|Severity|Warning
|Resolution|No resolution is required.

### Base.1.4.PropertyValueNotInList
Indicates that a property was given the correct value type but the value of that property was not supported.  This values not in an enumeration

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is not in the list of acceptable values."
|Severity|Warning
|Resolution|Choose a value from the enumeration list that the implementation can support and resubmit the request if the operation failed.

### Base.1.4.PropertyValueTypeError
Indicates that a property was given the wrong value type, such as when a number is supplied for a property that requires a string.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is of a different type than the property can accept."
|Severity|Warning
|Resolution|Correct the value for the property in the request body and resubmit the request if the operation failed.

### Base.1.4.QueryNotSupported
Indicates that query is not supported on the implementation.

| | |
|:---|:---|
|Message Format|"Querying is not supported by the implementation."
|Severity|Warning
|Resolution|Remove the query parameters and resubmit the request if the operation failed.

### Base.1.4.QueryNotSupportedOnResource
Indicates that query is not supported on the given resource, such as when a start/count query is attempted on a resource that is not a collection.

| | |
|:---|:---|
|Message Format|"Querying is not supported on the requested resource."
|Severity|Warning
|Resolution|Remove the query parameters and resubmit the request if the operation failed.

### Base.1.4.QueryParameterOutOfRange
Indicates that a query parameter was supplied that is out of range for the given resource.  This can happen with values that are too low or beyond that possible for the supplied resource, such as when a page is requested that is beyond the last page.

| | |
|:---|:---|
|Message Format|"The value %1 for the query parameter %2 is out of range %3."
|Severity|Warning
|Resolution|Reduce the value for the query parameter to a value that is within range, such as a start or count value that is within bounds of the number of resources in a collection or a page that is within the range of valid pages.

### Base.1.4.QueryParameterValueFormatError
Indicates that a query parameter was given the correct value type but the value of that parameter was not supported.  This includes value size/length exceeded.

| | |
|:---|:---|
|Message Format|"The value %1 for the parameter %2 is of a different format than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the query parameter in the request and resubmit the request if the operation failed.

### Base.1.4.QueryParameterValueTypeError
Indicates that a query parameter was given the wrong value type, such as when a number is supplied for a query parameter that requires a string.

| | |
|:---|:---|
|Message Format|"The value %1 for the query parameter %2 is of a different type than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the query parameter in the request and resubmit the request if the operation failed.

### Base.1.4.ResourceAlreadyExists
Indicates that a resource change or creation was attempted but that the operation cannot proceed because the resource already exists.

| | |
|:---|:---|
|Message Format|"The requested resource already exists."
|Severity|Critical
|Resolution|Do not repeat the create operation as the resource has already been created.

### Base.1.4.ResourceAtUriInUnknownFormat
Indicates that the URI was valid but the resource or image at that URI was in a format not supported by the service.

| | |
|:---|:---|
|Message Format|"The resource at %1 is in a format not recognized by the service."
|Severity|Critical
|Resolution|Place an image or resource or file that is recognized by the service at the URI.

### Base.1.4.ResourceAtUriUnauthorized
Indicates that the attempt to access the resource/file/image at the URI was unauthorized.

| | |
|:---|:---|
|Message Format|"While accessing the resource at %1, the service received an authorization error %2."
|Severity|Critical
|Resolution|Ensure that the appropriate access is provided for the service in order for it to access the URI.

### Base.1.4.ResourceCannotBeDeleted
Indicates that a delete operation was attempted on a resource that cannot be deleted.

| | |
|:---|:---|
|Message Format|"The delete request failed because the resource requested cannot be deleted."
|Severity|Critical
|Resolution|Do not attempt to delete a non-deletable resource.

### Base.1.4.ResourceInStandby
Indicates that the request could not be performed because the resource is in standby.

| | |
|:---|:---|
|Message Format|"The request could not be performed because the resource is in standby."
|Severity|Critical
|Resolution|Ensure that the resource is in the correct power state and resubmit the request.

### Base.1.4.ResourceInUse
Indicates that a change was requested to a resource but the change was rejected due to the resource being in use or transition.

| | |
|:---|:---|
|Message Format|"The change to the requested resource failed because the resource is in use or in transition."
|Severity|Warning
|Resolution|Remove the condition and resubmit the request if the operation failed.

### Base.1.4.ResourceMissingAtURI
Indicates that the operation expected an image or other resource at the provided URI but none was found.  Examples of this are in requests that require URIs like Firmware Update.

| | |
|:---|:---|
|Message Format|"The resource at the URI %1 was not found."
|Severity|Critical
|Resolution|Place a valid resource at the URI or correct the URI and resubmit the request.

### Base.1.4.ServiceInUnknownState
Indicates that the operation failed because the service is in an unknown state and cannot accept additional requests.

| | |
|:---|:---|
|Message Format|"The operation failed because the service is in an unknown state and can no longer take incoming requests."
|Severity|Critical
|Resolution|Restart the service and resubmit the request if the operation failed.

### Base.1.4.ServiceShuttingDown
Indicates that the operation failed as the service is shutting down, such as when the service reboots.

| | |
|:---|:---|
|Message Format|"The operation failed because the service is shutting down and can no longer take incoming requests."
|Severity|Critical
|Resolution|When the service becomes available, resubmit the request if the operation failed.

### Base.1.4.ServiceTemporarilyUnavailable
Indicates the service is temporarily unavailable.

| | |
|:---|:---|
|Message Format|"The service is temporarily unavailable.  Retry in %1 seconds."
|Severity|Critical
|Resolution|Wait for the indicated retry duration and retry the operation.

### Base.1.4.SessionLimitExceeded
Indicates that a session establishment has been requested but the operation failed due to the number of simultaneous sessions exceeding the limit of the implementation.

| | |
|:---|:---|
|Message Format|"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation."
|Severity|Critical
|Resolution|Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported).

### Base.1.4.SourceDoesNotSupportProtocol
Indicates that while attempting to access, connect to or transfer a resource/file/image from another location that the other end of the connection did not support the protocol

| | |
|:---|:---|
|Message Format|"The other end of the connection at %1 does not support the specified protocol %2."
|Severity|Critical
|Resolution|Change protocols or URIs. 

### Base.1.4.Success
Indicates that all conditions of a successful operation have been met.

| | |
|:---|:---|
|Message Format|"Successfully Completed Request"
|Severity|OK
|Resolution|None

### Base.1.4.UnrecognizedRequestBody
Indicates that the service encountered an unrecognizable request body that could not even be interpreted as malformed JSON.

| | |
|:---|:---|
|Message Format|"The service detected a malformed request body that it was unable to interpret."
|Severity|Warning
|Resolution|Correct the request body and resubmit the request if it failed.

### HpeBiosMessageRegistry.1.4.MessagesMaxSizeExceeded
Indicates that the last configuration change attempted by the user resulted in a number of error messages that exceeded the maximum storage capacity alloted for messages corresponding to this resource.

| | |
|:---|:---|
|Message Format|"The messages array has been truncated because the last configuration change resulted in too many error messages."
|Severity|Warning
|Resolution|Inspect the last configuration change request for issues that may be generating errors, compare the request against the resource's schema, then retry the configuration change.

### HpeBiosMessageRegistry.1.4.UnsupportedAMPConfiguration
Indicates that the user provided Advanced Memory Protection (AMP) option is not appropriate for this memory configuration, as the underlying hardware does not support it.

| | |
|:---|:---|
|Message Format|"Underlying hardware does not support the requested AMP configuration, the settings are invalid."
|Severity|Warning
|Resolution|Ensure that the current memory configuration meets the requirements of the requested value before applying the settings.

### HpeBiosMessageRegistry.1.4.UnsupportedDramRaplValue
Indicates that the user provided Running Average Power Limit (RAPL) value could not be applied due to inherent DRAM power limitation. The value may be out of bounds or invalid.

| | |
|:---|:---|
|Message Format|"Underlying DRAM does not support the requested value."
|Severity|Warning
|Resolution|Ensure that the requested value is within the supported bounds before applying the settings.

### HpeBiosMessageRegistry.1.4.UnsupportedProcessorRaplValue
Indicates that the user provided Running Average Power Limit (RAPL) value could not be applied due to inherent processor power limitation. The value may be out of bounds or invalid.

| | |
|:---|:---|
|Message Format|"Underlying processor does not support the requested value."
|Severity|Warning
|Resolution|Ensure that the processor supports the requested value and that it is within the supported bounds before applying the settings.

### HpeCommon.1.4.ArrayPropertyOutOfBound
The items in the array exceed the maximum  number supported.

| | |
|:---|:---|
|Message Format|"An array %1 was supplied with %2 items that exceeds the maximum supported count of %3."
|Severity|Warning
|Resolution|Retry the operation using the correct number of items for the array.

### HpeCommon.1.4.ConditionalSuccess
A property value was successfully changed but the change may be reverted upon system reset.

| | |
|:---|:---|
|Message Format|"The property %1 was successfully changed to %2, but the change may be reverted upon system reset."
|Severity|Warning
|Resolution|Check the "SettingsResult" messages after the system has reset for errors referring to the corresponding property.

### HpeCommon.1.4.InternalErrorWithParam
The operation was not successful due to an internal service error (shown), but the service is still operational.

| | |
|:---|:---|
|Message Format|"The operation was not successful due to an internal service error (%1), but the service is still operational."
|Severity|Critical
|Resolution|Retry the operation. If the problem persists, consider resetting the service.

### HpeCommon.1.4.InvalidConfigurationSpecified
The specified configuration is not valid.

| | |
|:---|:---|
|Message Format|"The specified configuration is not valid."
|Severity|Warning
|Resolution|Correct the configuration, and then retry the operation.

### HpeCommon.1.4.JobCreated
A job was created in response to the operation.

| | |
|:---|:---|
|Message Format|"A job was created in response to the operation. The status of the job is accessible at %1."
|Severity|OK
|Resolution|Perform an HTTP GET request on the supplied URI for job status.

### HpeCommon.1.4.PropertyValueExceedsMaxLength
The value for the property exceeds the maximum length.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 exceeds the maximum length of %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeCommon.1.4.PropertyValueIncompatible
The value for the property is the correct type, but this value is incompatible with the current value of another property.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is incompatible with the value for property %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeCommon.1.4.PropertyValueOutOfRange
The value for the property is out of range.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is out of range %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeCommon.1.4.ResetInProgress
A device or service reset is in progress.

| | |
|:---|:---|
|Message Format|"A reset on %1 is in progress."
|Severity|Warning
|Resolution|Wait for device or service reset to complete, and then retry the operation.

### HpeCommon.1.4.ResetRequired
One or more properties were changed, but these changes will not take effect until the device or service is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed, but these changes will not take effect until %1 is reset."
|Severity|Warning
|Resolution|To enable the changed properties, reset the device or service.

### HpeCommon.1.4.ResourceNotReadyRetry
The resource is present but is not ready to perform operations due to an internal condition such as initialization or reset.

| | |
|:---|:---|
|Message Format|"The resource is present but is not ready to perform operations.  The resource will be ready in %1 seconds."
|Severity|Warning
|Resolution|Retry the operation when the resource is ready.

### HpeCommon.1.4.SuccessFeedback
The operation completed successfully

| | |
|:---|:---|
|Message Format|"The operation completed successfully"
|Severity|OK
|Resolution|None

### HpeCommon.1.4.TaskCreated
A task was created in response to the operation.

| | |
|:---|:---|
|Message Format|"A task was created in response to the operation and is accessible at %1."
|Severity|OK
|Resolution|Perform an HTTP GET request on the supplied URI for task status.

### HpeCommon.1.4.UnsupportedHwConfiguration
A previously requested property value change was reverted because the current hardware configuration does not support it.

| | |
|:---|:---|
|Message Format|"The value %1 for property %2 was reverted because the current hardware configuration does not support it."
|Severity|Warning
|Resolution|Ensure that the system's hardware configuration supports the property value.

### HpeRedfishMessage.1.4.AHSDownloadJobException
The AHS Downlaod Job Failed.

| | |
|:---|:---|
|Message Format|"%1 job failed. %2."
|Severity|Warning
|Resolution|Retry the operation.

### HpeRedfishMessage.1.4.ApplyServerConfigurationFailed
Apply server configuration job Failed.

| | |
|:---|:---|
|Message Format|" Apply server configuration job failed. %1."
|Severity|Warning
|Resolution|Retry the operation.

### HpeRedfishMessage.1.4.ConfigBaseLineValidationFailed
Configuration Baseline Validation Failed

| | |
|:---|:---|
|Message Format|"Server configuration baseline validation job failed. %1"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.ETagVerificationFailed
Unable to verify ETag

| | |
|:---|:---|
|Message Format|"%1 job failed. %2."
|Severity|Warning
|Resolution|Retry the operation.

### HpeRedfishMessage.1.4.ETagVerificationPartiallyCompleted
Apply configuration baseline completed partially

| | |
|:---|:---|
|Message Format|"%1 job partially completed. %2"
|Severity|OK
|Resolution|Verify the configuration settings manually.

### HpeRedfishMessage.1.4.EmptySerialNumberorProductID
Serial Number or Product ID is blank.

| | |
|:---|:---|
|Message Format|"%1 job failed as Serial number/Product ID is empty for server: %2."
|Severity|Warning
|Resolution|Contact HPE support to get serial number.

### HpeRedfishMessage.1.4.FWImageNotAccessible
Firmware Image not accessible

| | |
|:---|:---|
|Message Format|"%1 job failed because the firmware image is not accessible."
|Severity|Warning
|Resolution|Retry the operation with correct credentials. 

### HpeRedfishMessage.1.4.FWUpdateNotStarted
Firmware update not started

| | |
|:---|:---|
|Message Format|"%1 job failed beacause the firmware update job is not started for group %2."
|Severity|Warning
|Resolution|Retry the operation. 

### HpeRedfishMessage.1.4.GroupAlreadyExists
Group Name already Exists

| | |
|:---|:---|
|Message Format|"%1 job Failed because the group is already present."
|Severity|Warning
|Resolution|Create the group with a different name.

### HpeRedfishMessage.1.4.GroupDoesNotExist
Group Name Does Not Exist

| | |
|:---|:---|
|Message Format|"%1 job failed because the Group Name does not exist."
|Severity|Warning
|Resolution|Specify a Group Name that exists and retry the operation.

### HpeRedfishMessage.1.4.GroupEmpty
No Servers present in Group

| | |
|:---|:---|
|Message Format|"%1 job failed because no servers are present in the Group."
|Severity|Warning
|Resolution|Add servers in the group and retry the operation.

### HpeRedfishMessage.1.4.HpeOneViewManagedServer
One View Managed Server

| | |
|:---|:---|
|Message Format|"%1 failed.Server is HPE OneView managed."
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.InsufficientPrivilege
Job failure message

| | |
|:---|:---|
|Message Format|"%1 job failed due to insufficient privilege."
|Severity|Warning
|Resolution|Retry the operation with sufficent privileges.

### HpeRedfishMessage.1.4.InvalidCredentials
Server Credentials are not valid

| | |
|:---|:---|
|Message Format|"%1 job failed because credentials used for server are invalid."
|Severity|Warning
|Resolution|Retry the operation with correct credentials.

### HpeRedfishMessage.1.4.InvalidSUTMode
Invalid SUT Mode

| | |
|:---|:---|
|Message Format|"%1 job failed because existing SUT mode must be in AutoStage for Deploy Operation"
|Severity|Warning
|Resolution|Start the SUT service.

### HpeRedfishMessage.1.4.JobAborted
The job was aborted

| | |
|:---|:---|
|Message Format|"%1 Job aborted."
|Severity|Warning
|Resolution|None.

### HpeRedfishMessage.1.4.JobCompleted
Job completion message

| | |
|:---|:---|
|Message Format|"%1 job completed"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.JobCompletedStatus
Job completed on some servers

| | |
|:---|:---|
|Message Format|"%1 job completed for %2 servers"
|Severity|Warning
|Resolution|None.

### HpeRedfishMessage.1.4.JobCompletedWithException
Job completed with exception on some servers

| | |
|:---|:---|
|Message Format|"%1 job completed. Failed for %2 servers."
|Severity|Warning
|Resolution|Retry the operation on failed servers

### HpeRedfishMessage.1.4.JobCompletedWithExceptionStatus
Job completed with exception on some servers and failed for some servers

| | |
|:---|:---|
|Message Format|"%1 job completed for %2 servers, Succeeded for %3 servers, Failed for %4 servers"
|Severity|Warning
|Resolution|Retry the operation on failed servers

### HpeRedfishMessage.1.4.JobCompletedWithFailure
Job completed with failure

| | |
|:---|:---|
|Message Format|"%1 job completed. %2"
|Severity|Warning
|Resolution|Clear the iLO Repository manually

### HpeRedfishMessage.1.4.JobCompletedWithStatus
Job completed with status

| | |
|:---|:---|
|Message Format|"%1 job completed. %2"
|Severity|Ok
|Resolution|None.

### HpeRedfishMessage.1.4.JobException
Job failure message

| | |
|:---|:---|
|Message Format|"%1 job failed because %2."
|Severity|Warning
|Resolution|Retry the operation.

### HpeRedfishMessage.1.4.JobExceptionInternalError
Job failure message

| | |
|:---|:---|
|Message Format|"%1 job failed because of an internal error."
|Severity|Warning
|Resolution|Retry the operation.

### HpeRedfishMessage.1.4.JobExceptionWithStatus
Job failure message

| | |
|:---|:---|
|Message Format|"%1 job failed. %2."
|Severity|Warning
|Resolution|Retry the operation.

### HpeRedfishMessage.1.4.JobFailed
Job failed message

| | |
|:---|:---|
|Message Format|"%1 job failed"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.JobPartiallyCompleted
Job completion message

| | |
|:---|:---|
|Message Format|"%1 job partially completed. %2"
|Severity|OK
|Resolution|Manually reboot the server.

### HpeRedfishMessage.1.4.JobRunning
The job is currently running

| | |
|:---|:---|
|Message Format|"%1 job is in progress."
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.JobRunningStatus
The job is running and finished on some of the servers

| | |
|:---|:---|
|Message Format|"%1 started on %2 Servers. Succeeded for %3 servers, Failed for %4 servers."
|Severity|Warning
|Resolution|None.

### HpeRedfishMessage.1.4.JobRunningStep
The job is currently running

| | |
|:---|:---|
|Message Format|"%1 job is in progress. %2"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.MaxGroupCreated
The maximum number of allowed Server Groups have been created.

| | |
|:---|:---|
|Message Format|"%1 job failed because the maximum number of allowed groups have been created."
|Severity|Warning
|Resolution|Delete an existing Group and then create the new Group.

### HpeRedfishMessage.1.4.ModifyServerToInfosight
Modify the InfoSight connectivity of server

| | |
|:---|:---|
|Message Format|"%1 completed"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.NoManagedServers
Servers does not exist in iLO Amplifier Pack.

| | |
|:---|:---|
|Message Format|"%1 failed as there are no servers managed by this iLO Amplifier Pack."
|Severity|Warning
|Resolution|Add server in iLO Amplifier Pack and retry the operation.

### HpeRedfishMessage.1.4.NodeAddressException
Exception for Node Address.

| | |
|:---|:---|
|Message Format|"%1 job failed with exception for server address: %2"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.RecoveryEventNotReceived
Recovery Job failed because the recovery event was not received from iLO

| | |
|:---|:---|
|Message Format|"%1 failed because the recovery event was not received from iLO"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.SUTModeNotSupported
SUT Mode is not supported

| | |
|:---|:---|
|Message Format|"%1 job failed because SUT mode is not supported. iLO Error Response: %2"
|Severity|Warning
|Resolution|Set the supported SUT mode.

### HpeRedfishMessage.1.4.SUTNotInstalled
SUT is not installed/responding

| | |
|:---|:---|
|Message Format|"%1 job failed because SUT is not installed/responding. iLO Error Response: %2"
|Severity|Warning
|Resolution|Start the SUT service.

### HpeRedfishMessage.1.4.SUTOperatorRequestorFailed
SUT Operator Requestor failed

| | |
|:---|:---|
|Message Format|"%1 job failed because setting the Operator Requestor in SUT to iLO Amplifier Pack is failed."
|Severity|Warning
|Resolution|Retry the SUT operator request to set to iLO Amplifier Pack.

### HpeRedfishMessage.1.4.SUTOperatorRequestorFailedForOSAdministrator
SUT Operator Requestor failed

| | |
|:---|:---|
|Message Format|"%1 job failed because setting the Operator Requestor in SUT to OS Administrator was not successful."
|Severity|Warning
|Resolution|Retry the SUT operator request to set to OS Administrator.

### HpeRedfishMessage.1.4.SUTServiceNotRunning
SUT Service is not running

| | |
|:---|:---|
|Message Format|"%1 job failed because SUT service is not running. iLO Error Response: %2"
|Severity|Warning
|Resolution|Start the SUT service.

### HpeRedfishMessage.1.4.SUTUpdateRequestFailed
SUT Update Request failed

| | |
|:---|:---|
|Message Format|"%1 job failed because SUT Update Request is failed. iLO Error Response: %2"
|Severity|Warning
|Resolution|Retry the SUT update request.

### HpeRedfishMessage.1.4.ServerGroupNotResponding
Credentials of servers in group are either incorrect or servers are not responding

| | |
|:---|:---|
|Message Format|"%1 job failed because either credentials of servers in the group are incorrect or servers are not responding."
|Severity|Warning
|Resolution|Retry the operation with correct credentials.

### HpeRedfishMessage.1.4.ServerInventoryNotFound
Server Inventory details Not Exist

| | |
|:---|:---|
|Message Format|"%1 job failed because the Server inventory details not found in the iLO Amplifier."
|Severity|Warning
|Resolution|Specify the server that is managed by iLO Amplifier and retry the operation.

### HpeRedfishMessage.1.4.ServerNotResponding
Server Credentials is incorrect or not responding

| | |
|:---|:---|
|Message Format|"%1 job failed because Server credentials is incorrect or Server is not responding."
|Severity|Warning
|Resolution|Retry the operation with correct credentials.

### HpeRedfishMessage.1.4.SystemUpToDate
System is up to date

| | |
|:---|:---|
|Message Format|"System is up to date. %1"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.TelemetryJobCompleted
Telemetry Job completion message

| | |
|:---|:---|
|Message Format|"%1 completed"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.TelemetryJobException
Telemetry Job exception message

| | |
|:---|:---|
|Message Format|"%1 failed. %2"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.ValidatingServerConfigUpdateProgress
Validating server configuration update progress status

| | |
|:---|:---|
|Message Format|"%1"
|Severity|OK
|Resolution|None.

### HpeRedfishMessage.1.4.iLOErrorId
 iLO message ID

| | |
|:---|:---|
|Message Format|" %1 job failed. iLoMessage Id: %2"
|Severity|Warning
|Resolution|None

### HpeRedfishMessage.1.4.iLOErrorMessage
iLo Message args

| | |
|:---|:---|
|Message Format|" %1 job failed. iLoMessage Args: %2"
|Severity|Warning
|Resolution|None

### HpeRedfishMessage.1.4.iLOMessageID
iLo Message args

| | |
|:---|:---|
|Message Format|" %1 job failed. iLoMessage ID:%2"
|Severity|Warning
|Resolution|None

### HpeSmartStorage.2.0.AddEditableDataDriveFailed
Indicates that the data drive was not added due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: data drive %1 not added to logical drive with ID "%2" due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.AddEditableSpareDriveFailed
Indicates that the spare drive was not added due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: spare drive %1 not added to logical drive with ID "%2" due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveArrayHasFailedSpareDrive
Indicates that the spare drive cannot be added to the array because the array has failed spare drive(s).

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has at least one failed spare drive"
|Severity|Critical
|Resolution|Remove all failed spare drives from the array.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveArrayHasNoDataDrives
Indicates that the spare drive cannot be added to the array because the array has no data drives assigned.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has no data drives assign"
|Severity|Critical
|Resolution|Assign data drives to the array.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveArrayStatusNotOK
Indicates that the spare drive cannot be added to the array because the array status is not OK.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array status is not OK"
|Severity|Critical
|Resolution|Check status messages on the array for more information.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveCannotChangeSpareType
Indicates that the spare drive cannot be added to the array because the spare type does not match.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the spare type does not match"
|Severity|Critical
|Resolution|Correct the spare type to match the array.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveCannotMixDriveTypes
Indicates that the spare drive cannot be added to the array because its drive type does not match that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because its drive type does not match that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveDriveAlreadyUsedAsSpare
Indicates that the spare drive cannot be added because the requested spare drive is already configured as a spare.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the requested spare drive is already configured as a spare"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveDriveIsNotConfigurable
Indicates that the spare drive cannot be added to the array because the selected drive is not configurable.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because it is not configurable"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveDriveIsNotUnassigned
Indicates that the spare drive cannot be added to the array because the selected drive is not unassigned.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because it is not unassigned"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveDriveIsNotUnassignedOrShareableStandby
Indicates that the spare drive cannot be added to the array because the requested drive is not available.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the requested drive is not available"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveIncompatibleBlockSize
Indicates that the spare drive cannot be added to the array because its block size is not compatible with that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because its block size is not compatible with that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveInvalidSAM
Indicates that the spare drive cannot be added to the array because spare activation mode must be set to predictive to assign spare drives to RAID 0 volumes.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the logical drive is RAID 0 and the spare activation mode is set to failure"
|Severity|Critical
|Resolution|Change the spare activation mode.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveInvalidSpareType
Indicates that the spare drive cannot be added to the array because the desired spare type is invalid.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has an invalid spare type"
|Severity|Critical
|Resolution|Correct the spare type of the array.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveMaxSpareDriveCountReached
Indicates that the spare drive cannot be added to the array because the maximum number of spare drives has been reached.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the maximum number of spare drives has been reached"
|Severity|Critical
|Resolution|Remove one or more spare drive(s).

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveNoSpareTypeSet
Indicates that the spare drive cannot be added to the array because the array has no spare type set.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has no spare type set"
|Severity|Critical
|Resolution|Specify the spare type.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveNotAllowed
Indicates that adding a spare drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot add spare drive %1 to logical drive with ID "%2" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveTooSmall
Indicates that the spare drive cannot be added to the array because the selected drive is too small.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because it is too small"
|Severity|Critical
|Resolution|Select a larger physical drive.

### HpeSmartStorage.2.0.CanAddEditableArraySpareDriveUnknownError
Indicates that the spare drive cannot be added to the array for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2""
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanAddEditableDataDriveArrayContainsUnsavedLogicalDrives
Indicates that the data drive cannot be added to the array because the array has unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Internal error: cannot add data drive %1 to logical drive with ID "%2" because the array has unlocked logical drives"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanAddEditableDataDriveCannotMixDriveTypes
Indicates that the data drive cannot be added to the array because its drive type does not match that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because its drive type does not match that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableDataDriveDriveIsNotConfigurable
Indicates that the data drive cannot be added to the array because the selected drive is not configurable.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because it is not configurable"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableDataDriveDriveIsNotUnassigned
Indicates that the data drive cannot be added to the array because the selected drive is not unassigned.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because it is not unassigned"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableDataDriveIncompatibleBlockSize
Indicates that the data drive cannot be added to the array because its block size is not compatible with that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because its block size is not compatible with that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanAddEditableDataDriveMaxDataDriveCountReached
Indicates that the data drive cannot be added to the array because the maximum number of physical drives on the array has been reached.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because the maximum number of physical drives on the array has been reached"
|Severity|Critical
|Resolution|Remove one or more physical drive(s) from the array.

### HpeSmartStorage.2.0.CanAddEditableDataDriveNotAllowed
Indicates that adding a data drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot add data drive %1 to logical drive with ID "%2" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanAddEditableDataDriveUnknownError
Indicates that the data drive cannot be added to the array for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2""
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeAlreadySet
Indicates that desired boot volume is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target is already set as a boot volume"
|Severity|Critical
|Resolution|No actions required.

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeInvalidBootVolumeNumber
Indicates that the controller boot volume cannot be set because target device is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target device is invalid"
|Severity|Critical
|Resolution|Target a valid device for the boot volume.

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeInvalidBootVolumeType
Indicates that the controller boot volume cannot be set because the boot volume type is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the boot volume type is invalid"
|Severity|Critical
|Resolution|Correct the boot volume type.

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeInvalidLogicalBootVolume
Indicates that the controller boot volume cannot be set because the target logical drive is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target logical drive is invalid"
|Severity|Critical
|Resolution|Resolution

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeInvalidPhysicalBootVolume
Indicates that the controller boot volume cannot be set because the target physical drive is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target physical drive is invalid"
|Severity|Critical
|Resolution|Resolution

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeInvalidPrecedence
Indicates that the desired boot volume priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the boot volume priority is invalid"
|Severity|Critical
|Resolution|Correct the boot volume priority.

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeNotAllowed
Indicates that setting the boot volume is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeOperationUnsupported
Indicates that the controller does not support setting boot volumes.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the controller does not support setting boot volumes"
|Severity|Critical
|Resolution|Do not modify the controller boot volume.

### HpeSmartStorage.2.0.CanChangeEditableControllerBootVolumeUnknownError
Indicates that the controller boot volume cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerDPOInvalidValue
Indicates that the controller degraded performance optimization cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller degraded performance optimization.

### HpeSmartStorage.2.0.CanChangeEditableControllerDPONoChange
Indicates that the desired controller degraded performance optimization is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerDPONoLogicalDrives
Indicates that the controller degraded performance optimization cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerDPONotSupported
Indicates that the controller degraded performance optimization cannot be set because the feature is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because the controller does not support the feature"
|Severity|Critical
|Resolution|Do not modify the degraded performance optimization.

### HpeSmartStorage.2.0.CanChangeEditableControllerDPOUnknownError
Indicates that the controller degraded performance optimization cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerDriveWriteCacheModeInvalidMode
Indicates that the controller drive write cache mode cannot be set because the desired drive write cache mode is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the drive write cache mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerDriveWriteCacheModeNoChange
Indicates that the desired controller drive write cache mode is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerDriveWriteCacheModeNoLogicalDrives
Indicates that the controller drive write cache mode cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerDriveWriteCacheModeNotSupported
Indicates that the controller drive write cache mode cannot be changed because the operation is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because it is not supported"
|Severity|Critical
|Resolution|Do not modify the controller drive write cache mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerDriveWriteCacheModeUnknownError
Indicates that the controller drive write cache mode cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerElevatorSortInvalidValue
Indicates that the controller elevator sort cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller elevator sort.

### HpeSmartStorage.2.0.CanChangeEditableControllerElevatorSortNoChange
Indicates that the desired controller elevator sort is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerElevatorSortNoLogicalDrives
Indicates that the controller elevator sort cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerElevatorSortUnknownError
Indicates that the controller elevator sort cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerEncryptionHasEncryptedVolumes
Indicates that the encryption configuration cannot be set because encrypted logical drives exist.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because encrypted logical drives exist"
|Severity|Critical
|Resolution|Delete all encrypted logical drives.

### HpeSmartStorage.2.0.CanChangeEditableControllerEncryptionInHBAMode
Indicates that the encryption configuration cannot be set because the controller is currently in or pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because the controller is currently in or pending HBA mode"
|Severity|Critical
|Resolution|Set the controller or connector mode to mixed or RAID mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerEncryptionInvalidValue
Indicates that the desired encryption configuration is invalid.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the encryption configuration.

### HpeSmartStorage.2.0.CanChangeEditableControllerEncryptionNoChange
Indicates that the desired encryption configuration is already set.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because it is already set"
|Severity|Critical
|Resolution|Resolution

### HpeSmartStorage.2.0.CanChangeEditableControllerEncryptionNotAllowed
Indicates that setting the encryption configuration is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because it is invalid"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanChangeEditableControllerEncryptionOperationUnsupported
Indicates that encryption is not supported on the controller.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because encryption is not supported on the controller"
|Severity|Critical
|Resolution|Do not modify the encryption configuration.

### HpeSmartStorage.2.0.CanChangeEditableControllerEncryptionUnknownError
Indicates that the encryption configuration cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerExpandPriorityInvalidValue
Indicates that the controller expand priority cannot be set because the desired expand priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the expand priority.

### HpeSmartStorage.2.0.CanChangeEditableControllerExpandPriorityNoChange
Indicates that the desired controller expand priority is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerExpandPriorityNoLogicalDrives
Indicates that the controller expand priority cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerExpandPriorityUnknownError
Indicates that the controller expand priority cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerFLSInvalidValue
Indicates that the controller flexible latency scheduler cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the flexible latency scheduler.

### HpeSmartStorage.2.0.CanChangeEditableControllerFLSNoChange
Indicates that the desired controller flexible latency scheduler is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerFLSNoLogicalDrives
Indicates that the controller flexible latency scheduler cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerFLSUnknownError
Indicates that the controller flexible latency scheduler cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerIRPInvalidValue
Indicates that the controller inconsistency repair policy cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller inconsistency repair policy.

### HpeSmartStorage.2.0.CanChangeEditableControllerIRPNoChange
Indicates that the desired controller inconsistency repair policy is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerIRPNoLogicalDrives
Indicates that the controller inconsistency repair policy cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerIRPUnknownError
Indicates that the controller inconsistency repair policy cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerIRPUnsupported
Indicates that the controller does not support changing the inconsistency repair policy.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because it is unsupported"
|Severity|Critical
|Resolution|Do not modify the inconsistency repair policy.

### HpeSmartStorage.2.0.CanChangeEditableControllerMNPDelayInvalidValue
Indicates that the controller monitor and performance delay cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the monitor and performance delay.

### HpeSmartStorage.2.0.CanChangeEditableControllerMNPDelayNoChange
Indicates that the desired controller monitor and performance delay is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerMNPDelayNoLogicalDrives
Indicates that the controller monitor and performance delay cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerMNPDelayUnknownError
Indicates that the controller monitor and performance delay cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCControllerCacheInactive
Indicates that the controller no battery write cache cannot be set because the controller cache is inactive.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because the controller cache is inactive"
|Severity|Critical
|Resolution|Activate the controller cache.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCInHBAMode
Indicates that the controller no battery write cache cannot be set because the controller is currently in or pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because the controller is currently in or pending HBA mode"
|Severity|Critical
|Resolution|Set the controller or connector mode to mixed or RAID mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCInvalidValue
Indicates that the controller no battery write cache cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the no battery write cache.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCNoCachePresent
Indicates that the controller no battery write cache cannot be set because there is no cache board present.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because there is no cache board present"
|Severity|Critical
|Resolution|Attach a cache board.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCNoChange
Indicates that the desired controller no battery write cache is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCNoLogicalDrives
Indicates that the controller no battery write cache cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCOperationUnsupported
Indicates that the controller does not support changing the no battery write cache.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because it is unsupported"
|Severity|Critical
|Resolution|Do not modify the no battery write cache.

### HpeSmartStorage.2.0.CanChangeEditableControllerNBWCUnknownError
Indicates that the controller no battery write cache cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerPSSCountNoChange
Indicates that desired controller parallel surface scan count is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerPSSCountNoLogicalDrives
Indicates that the controller parallel surface scan count cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerPSSCountOperationUnsupported
Indicates that the controller does not support parallel surface scan.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because parallel surface scan is not supported"
|Severity|Critical
|Resolution|Do not modify the parallel surface scan count.

### HpeSmartStorage.2.0.CanChangeEditableControllerPSSCountOutOfRange
Indicates that the controller parallel surface scan count cannot be set because the desired value is out of range.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because it is out of range"
|Severity|Critical
|Resolution|Correct the parallel surface scan count.

### HpeSmartStorage.2.0.CanChangeEditableControllerPSSCountUnknownError
Indicates that the controller parallel surface scan count cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerQueueDepthInvalidValue
Indicates that the controller queue depth cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller queue depth.

### HpeSmartStorage.2.0.CanChangeEditableControllerQueueDepthNoChange
Indicates that the desired controller queue depth is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerQueueDepthNoLogicalDrives
Indicates that the controller queue depth cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerQueueDepthUnknownError
Indicates that the controller queue depth cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentBadPowerSource
Indicates that the controller read cache percent cannot be set because the backup power source is not charged or not present.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because the backup power source is not charged or not present"
|Severity|Critical
|Resolution|Attach a backup power source or allow it to charge fully.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentControllerCacheInactive
Indicates that the controller read cache percent cannot be set because the controller cache is inactive.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because the controller cache is inactive"
|Severity|Critical
|Resolution|Activate the controller cache.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentInHBAMode
Indicates that the controller read cache percent cannot be set because the controller is currently in or pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because the controller is currently in or pending HBA mode"
|Severity|Critical
|Resolution|Set the controller or connector mode to mixed or RAID mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentInvalidValue
Indicates that the controller read cache percent cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the read cache percent.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentNoCachePresent
Indicates that the controller read cache percent cannot be set because there is no cache board present.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because there is no cache board present"
|Severity|Critical
|Resolution|Attach a cache board.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentNoChange
Indicates that the desired controller read cache percent is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentNoLogicalDrives
Indicates that the controller read cache percent cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerReadCachePercentUnknownError
Indicates that the controller read cache percent cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerRebuildPriorityInvalidValue
Indicates that the controller rebuild priority cannot be set because the desired rebuild priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the rebuild priority.

### HpeSmartStorage.2.0.CanChangeEditableControllerRebuildPriorityNoChange
Indicates that the desired controller rebuild priority is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerRebuildPriorityNoLogicalDrives
Indicates that the controller rebuild priority cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerRebuildPriorityRapidUnsupported
Indicates that the controller does not support rapid rebuild.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because it is not supported on this controller"
|Severity|Critical
|Resolution|Select a non-rapid rebuild priority.

### HpeSmartStorage.2.0.CanChangeEditableControllerRebuildPriorityUnknownError
Indicates that the controller rebuild priority cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerSAMArrayHasActiveSpare
Indicates that the controller spare activation mode cannot be set to predictive because a RAID 0 logical drive with an active spare exists.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because a RAID 0 logical drive with an active spare exists"
|Severity|Critical
|Resolution|Delete the RAID 0 logical drive, remove the active spare, or select a different controller spare activation mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerSAMArrayHasAutoReplaceSpare
Indicates that the controller spare activation mode cannot be set to failure because a RAID 0 logical drive with an auto-replace spare exists.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because a RAID 0 logical drive with an auto-replace spare exists"
|Severity|Critical
|Resolution|Delete the RAID 0 logical drive, remove the auto-replace spare, or select a different controller spare activation mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerSAMArrayIsTransforming
Indicates that the controller spare activation mode cannot be set because the array is transforming.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because the array is transforming"
|Severity|Critical
|Resolution|Resubmit the request when the array finishes transforming.

### HpeSmartStorage.2.0.CanChangeEditableControllerSAMNoLogicalDrives
Indicates that the controller spare activation mode cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerSAMSelectedModeActive
Indicates that the desired controller spare activation mode is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerSAMUnknownError
Indicates that the controller spare activation mode cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerSAMUnsupportedMode
Indicates that the controller spare activation mode is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because it is not supported"
|Severity|Critical
|Resolution|Select a different spare activation mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerSSAPriorityInvalidValue
Indicates that the controller surface scan analysis priority cannot be set because the desired surface scan analysis priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the surface scan analysis priority.

### HpeSmartStorage.2.0.CanChangeEditableControllerSSAPriorityNoChange
Indicates that the desired controller surface scan analysis priority is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerSSAPriorityNoLogicalDrives
Indicates that the controller surface scan analysis priority cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerSSAPriorityUnknownError
Indicates that the controller surface scan analysis priority cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerSurvivalPowerModeInvalidValue
Indicates that the desired controller survival mode is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller survival mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerSurvivalPowerModeNoChange
Indicates that the desired survival mode is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerSurvivalPowerModeNotConfigurable
Indicates that the controller survival mode cannot be set because the controller does not support survival mode configuration.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because survival mode configuration is not supported on the controller"
|Severity|Critical
|Resolution|Do not modify the survival mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerSurvivalPowerModeOperationUnsupported
Indicates that the controller survival mode cannot be set because the controller does not support survival mode.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because survival mode is not supported on the controller"
|Severity|Critical
|Resolution|Do not modify the survival mode.

### HpeSmartStorage.2.0.CanChangeEditableControllerSurvivalPowerModeUnknownError
Indicates that the controller survival mode cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanChangeEditableControllerWCBTInvalidValue
Indicates that the desired controller write cache bypass threshold is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the write cache bypass threshold.

### HpeSmartStorage.2.0.CanChangeEditableControllerWCBTNoChange
Indicates that desired write cache bypass threshold is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanChangeEditableControllerWCBTNoLogicalDrives
Indicates that the controller write cache bypass threshold cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### HpeSmartStorage.2.0.CanChangeEditableControllerWCBTOperationUnsupported
Indicates that the controller write cache bypass threshold is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because it is not supported"
|Severity|Critical
|Resolution|Do not modify the write cache bypass threshold.

### HpeSmartStorage.2.0.CanChangeEditableControllerWCBTUnknownError
Indicates that the controller write cache bypass threshold cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanClearEditableControllerBootVolumeInvalidPrecedence
Indicates that the the boot volume cannot be cleared because the boot volume priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because the boot volume priority is invalid"
|Severity|Critical
|Resolution|Correct the boot volume priority.

### HpeSmartStorage.2.0.CanClearEditableControllerBootVolumeNotAllowed
Indicates that clearing the controller boot volume is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanClearEditableControllerBootVolumeNotSet
Indicates that the boot volume cannot be cleared because no boot volume is set.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because no boot volume is set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanClearEditableControllerBootVolumeOperationUnsupported
Indicates that clearing the boot volume is not suppported on the controller.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because it is not supported on the controller"
|Severity|Critical
|Resolution|Do not clear the controller boot volume.

### HpeSmartStorage.2.0.CanClearEditableControllerBootVolumeUnknownError
Indicates that the controller boot volume cannot be cleared for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanCommitEditableConfigurationNoChangesToCommit
Indicates that the editable configuration was not committed because there are no editable changes to commit.

| | |
|:---|:---|
|Message Format|"Internal error: cannot commit the editable configuration because no changes were made"
|Severity|Warning
|Resolution|Modify the editable configuration.

### HpeSmartStorage.2.0.CanCommitEditableConfigurationOutOfSync
Indicates that an external change occured which invalidates the editable configuration.

| | |
|:---|:---|
|Message Format|"Cannot commit the editable configuration"
|Severity|Critical
|Resolution|Recreate and re-submit the configuration request.

### HpeSmartStorage.2.0.CanCommitEditableConfigurationUnknownError
Indicates that an editable configuration cannot be committed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot commit the editable configuration"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanCommitEditableConfigurationUnlockedLogicalDrivesExist
Indicates that the editable configuration was not committed because there are unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Internal error: cannot commit the editable configuration because unlocked logical drives exist"
|Severity|Critical
|Resolution|Lock all logical drives.

### HpeSmartStorage.2.0.CanCreateEditableArrayCreatesNotAllowed
Indicates that creating arrays is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot create logical drive with ID "%1" because array creation is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanCreateEditableArrayMaxLDCountReached
Indicates that the array cannot be created because the maximum number of logical drives on the controller has been reached.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the maximum number of logical drives on the controller has been reached"
|Severity|Critical
|Resolution|Delete one or more logical drive(s).

### HpeSmartStorage.2.0.CanCreateEditableArrayNoUnassignedDrivesAvailable
Indicates that the array cannot be created because no unassigned drives are available.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the controller has no unassigned drives available"
|Severity|Critical
|Resolution|Delete an existing array or add more physical drives.

### HpeSmartStorage.2.0.CanCreateEditableArrayUnknownError
Indicates that the array cannot be created for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanCreateEditableConfigControllerStatusNotOK
Indicates that an editable configuration was not created because the status of the controller is not in an OK state.

| | |
|:---|:---|
|Message Format|"Cannot create an editable configuration because the controller status is not OK"
|Severity|Critical
|Resolution|Check status messages on the controller for more information.

### HpeSmartStorage.2.0.CanCreateEditableConfigEditableConfigExists
Indicates that an editable configuration was not created because an editable configuration already being edited.

| | |
|:---|:---|
|Message Format|"Internal error: cannot create an editable configuration because an editable configuration already exists"
|Severity|Critical
|Resolution|Delete the existing editable configuration.

### HpeSmartStorage.2.0.CanCreateEditableConfigInconsistentPortSettings
Indicates that an editable configuration was not created because the controller's port settings do not match.

| | |
|:---|:---|
|Message Format|"Cannot create an editable configuration because the port modes on the controller are in a conflicting state"
|Severity|Critical
|Resolution|Make the port settings consistent in the request and resubmit.

### HpeSmartStorage.2.0.CanCreateEditableConfigUnknownError
Indicates that an editable configuration cannot be created for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot create an editable configuration"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanCreateEditableLogicalDriveControllerNotOK
Indicates that the logical drive cannot be created because the controller status is not OK.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the controller status is not OK"
|Severity|Critical
|Resolution|Check status messages on the controller for more information.

### HpeSmartStorage.2.0.CanCreateEditableLogicalDriveMaxLDReached
Indicates that the logical drive cannot be created because the maximum number of logical drives on the controller has been reached.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the maximum number of logical drives on the controller has been reached"
|Severity|Critical
|Resolution|Delete on or more logical drive(s).

### HpeSmartStorage.2.0.CanCreateEditableLogicalDriveNoFreeSpaceAvailable
Indicates that the logical drive cannot be created because the array has no free space available.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the array has no free space available"
|Severity|Critical
|Resolution|Delete one or more logical drive(s) from the array.

### HpeSmartStorage.2.0.CanCreateEditableLogicalDriveNotAllowed
Indicates that creating logical drives is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot create logical drive with ID "%1" because logical drive creation is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanCreateEditableLogicalDriveUnknownError
Indicates that the logical drive cannot be created for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanDeleteEditableArrayContainsUnsavedLogicalDrives
Indicates that the array cannot be deleted because the array contains unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1" because unlocked logical drives exist"
|Severity|Critical
|Resolution|Lock all logical drives on the array.

### HpeSmartStorage.2.0.CanDeleteEditableArrayNotAllowed
Indicates that deleting an array is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot delete logical drive with ID "%1" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanDeleteEditableArrayUnknownError
Indicates that the array size cannot be deleted for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanDeleteEditableLogicalDriveIsLocked
Indicates that the logical drive cannot be deleted because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1" because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### HpeSmartStorage.2.0.CanDeleteEditableLogicalDriveNotAllowed
Indicates that deleting the logical drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot delete logical drive with ID "%1" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanDeleteEditableLogicalDriveNotLastLDInArray
Indicates that the logical drive cannot be deleted because the logical drive is not the last logical drive on the array.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1" because the logical drive is not the last logical drive on the array"
|Severity|Critical
|Resolution|Delete the last logical drive on the array first.

### HpeSmartStorage.2.0.CanDeleteEditableLogicalDriveUnknownError
Indicates that the logical drive size cannot be deleted for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanEnableErasedPhysicalDriveRestrictedSanitize
Indicates that the physical drive cannot be enabled because of a restricted, failed sanitize erase.

| | |
|:---|:---|
|Message Format|"Physical drive %1 was not enabled because it is currently in a restricted, failed sanitize state"
|Severity|Critical
|Resolution|Restart the sanitize erase on the physical drive.

### HpeSmartStorage.2.0.CanErasePhysicalDriveIsErasing
Indicates that the physical drive cannot be erased because the drive is currently erasing.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is currently erasing"
|Severity|Critical
|Resolution|Wait for the physical drive erase to complete.

### HpeSmartStorage.2.0.CanErasePhysicalDriveIsFailed
Indicates that the physical drive cannot be erased because the drive is failed.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is failed"
|Severity|Critical
|Resolution|Check the state of the drive.

### HpeSmartStorage.2.0.CanErasePhysicalDriveIsHBA
Indicates that the physical drive cannot be erased because the drive is exposed to the operating system.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is exposed to the operating system"
|Severity|Critical
|Resolution|Change the controller or connector to RAID mode to mask the drive from the operating system.

### HpeSmartStorage.2.0.CanErasePhysicalDriveNotAllowed
Indicates that the physical drive erase is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drives at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanErasePhysicalDriveNotUnassigned
Indicates that the physical drive cannot be erased because it is not unassigned.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is not unassigned"
|Severity|Critical
|Resolution|Unassign the physical drive.

### HpeSmartStorage.2.0.CanErasePhysicalDrivePatternNotSupported
Indicates that the desired erase pattern is not supported on the target drive.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 using pattern %2 because the drive does not support the erase pattern"
|Severity|Critical
|Resolution|Select a different erase pattern.

### HpeSmartStorage.2.0.CanErasePhysicalDriveUnknownError
Indicates that the physical drive cannot be erased for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanLockEditableLogicalDriveAlreadyLocked
Indicates that the logical drive cannot be locked because it is already locked.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because it is already locked"
|Severity|Critical
|Resolution|No action.

### HpeSmartStorage.2.0.CanLockEditableLogicalDriveNoArraySet
Indicates that the logical drive cannot be locked because it is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because it is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### HpeSmartStorage.2.0.CanLockEditableLogicalDriveNoRAIDLevelSet
Indicates that the logical drive cannot be locked because the RAID level is not set.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because the logical drive RAID level is not set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### HpeSmartStorage.2.0.CanLockEditableLogicalDriveNoSizeSet
Indicates that the logical drive cannot be locked because the size is not set.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because the logical drive size is not set"
|Severity|Critical
|Resolution|Set the logical drive size.

### HpeSmartStorage.2.0.CanLockEditableLogicalDriveNoStripSizeSet
Indicates that the logical drive cannot be locked because the strip size is not set.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because the logical drive strip size is not set"
|Severity|Critical
|Resolution|Set the logical drive strip size.

### HpeSmartStorage.2.0.CanLockEditableLogicalDriveUnknownError
Indicates that the logical drive cannot be locked for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorAlreadySet
Indicates that the desired logical drive accelerator is already set.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorArrayUsesIOBypass
Indicates that IOBypass is already set as the logical drive accelerator.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is already set"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorDriveTypeNotSSD
Indicates that IOBypass is only supported on SSD arrays.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is only supported on SSD arrays"
|Severity|Critical
|Resolution|Select a different logical drive accelerator for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorLogicalDriveNotCreated
Indicates that the logical drive accelerator cannot be set because the target logical drive does not exist.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because the logical drive does not exist"
|Severity|Critical
|Resolution|Create the logical drive first.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorNoArraySet
Indicates that the logical drive accelerator cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorNotAllowed
Indicates that setting the logical drive accelerator is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorNotTheFirstLDInArray
Indicates that the logical drive accelerator cannot be set because the logical drive is not the first logical drive of the array.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because the logical drive is not the first logical drive of the array"
|Severity|Critical
|Resolution|Delete the last logical drive in the array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorUnknownError
Indicates that the logical drive accelerator cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveAcceleratorUnsupported
Indicates that the logical drive accelerator cannot be set because the desired logical drive accelerator is unsupported.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is not supported"
|Severity|Critical
|Resolution|Do not modify the logical drive accelerator.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayArrayHasNoDataDrives
Indicates that the logical drive cannot be assigned to the array because the array has no data drives.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array has no data drives"
|Severity|Critical
|Resolution|Add data drives to the array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayArrayStatusNotOK
Indicates that the logical drive cannot be assigned to the array because the array status is not OK.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array status is not OK"
|Severity|Critical
|Resolution|Check status messages on the array for more information.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayChangeArrayNotAllowed
Indicates that changing the array assignment of the logical drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot change the array assignment of logical drive with ID "%1" because it is not allowed at this time"
|Severity|Critical
|Resolution|Do not assign the logical drive to a different array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayHasUnlockedLD
Indicates that the logical drive cannot be assigned to the array because the array has unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "1" to the array because the array has unlocked logical drives"
|Severity|Critical
|Resolution|Lock all existing logical drives on the array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayLogicalDriveIsLocked
Indicates that the logical drive cannot be assigned to the array because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayNoSpaceAvailableOnArray
Indicates that the logical drive cannot be assigned to the array because the array has no available space.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array has no available space"
|Severity|Critical
|Resolution|Free up space on the array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayNotAllowed
Indicates that assigning the logical drive to the array is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot assign logical drive with ID "%1" to an array because it is not allowed at this time"
|Severity|Critical
|Resolution|Resolution

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayNotDataArray
Indicates that the logical drive cannot be assigned to the array because the array is not a data array.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array is not a data array"
|Severity|Critical
|Resolution|Assign the logical drive to a different array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveArrayUnknownError
Indicates that the logical drive cannot be assigned to the array for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodDriveTypeNotSSD
Indicates that the logical drive initialization method cannot be set for a non-SSD logical drive.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is not on an SSD array"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodLDIsLocked
Indicates that the logical drive initialization method cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodNoArraySet
Indicates that the logical drive initialization method cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodNoRAIDLevelSet
Indicates that the logical drive initialization method cannot be set because the logical drive has no RAID level set.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive has no RAID level set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodNotAllowed
Indicates that setting the logical drive initialization method is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: setting the logical drive initialization method is not allowed for logical drive with ID "%1" at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodNotFirstLDInArray
Indicates that the logical drive initialization method cannot be set for the logical drive because the logical drive is not the first in the array.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is not the first logical drive in the array"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodNotRequiredForRAID
Indicates that rapid parity initialization is not valid for the RAID level of the logical drive.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because it is not valid for the RAID level of the logical drive"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodOPONotSupported
Indicates that the controller does not support over provisioning optimization.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because it is not supported by the controller"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodRPINotSupported
Indicates that the controller does not support rapid parity initialization.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because it is not supported by the controller"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveInitializationMethodUnknownError
Indicates that the logical drive initialization method cannot be set for the logical drive for an unknown reason.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveLabelInvalidCharacter
Indicates that the logical drive label cannot be set because an invalid character was found in the logical drive label.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because an invalid character was found in the logical drive label"
|Severity|Critical
|Resolution|Remove invalid characters from the logical drive label.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveLabelInvalidLabel
Indicates that the logical drive label cannot be set because the logical drive label is invalid.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive label is invalid"
|Severity|Critical
|Resolution|Correct the logical drive label.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveLabelInvalidLogicalDrive
Indicates that the logical drive label cannot be set because the target logical drive is invalid.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the target logical drive is invalid"
|Severity|Critical
|Resolution|Target a different logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveLabelLabelTooLong
Indicates that the logical drive label cannot be set because the logical drive label is too long.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive label is too long"
|Severity|Critical
|Resolution|Decrease the length of the logical drive label.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveLabelLogicalDriveIsLocked
Indicates that the logical drive label cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveLabelNoArraySet
Indicates that the logical drive label cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveLabelUnknownError
Indicates that the logical drive label cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelFullStripeSizeOverflow
Indicates that the logical drive RAID level cannot be set because it will cause the stripe size of the logical drive to exceed the maximum safe value.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because it will cause the stripe size of the logical drive to exceed the maximum safe value"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelInvalidRAIDLevel
Indicates that the logical drive RAID level cannot be set because the desired RAID level is invalid.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the desired RAID level is invalid"
|Severity|Critical
|Resolution|Correct the RAID level of the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelLogicalDriveIsLocked
Indicates that the logical drive RAID level cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelNoArraySet
Indicates that the logical drive RAID level cannot be set because the logical drive has not been assigned to an array.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the logical drive has not been assigned to an arra"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelNotAllowed
Indicates that setting the logical drive RAID level is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot set RAID level for logical drive with ID "%1" to %2 at this time because it is not allowed"
|Severity|Critical
|Resolution|Resubmit the request

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelNotEnoughFreeSpaceForRAID
Indicates that the logical drive RAID level cannot be set because there is not enough available free space on the array.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the array does not have enough available free space"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelUnknownError
Indicates that the logical drive RAID level cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelUnsupportedDriveCount
Indicates that the logical drive RAID level cannot be set because the number of drives assigned to the array is not supported by the desired RAID level.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the number of drives assigned to the array is not supported by the desired RAID level"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveRAIDLevelUnsupportedRAIDLevel
Indicates that the logical drive RAID level cannot be set because the desired RAID level is not supported on the controller.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the desired RAID level is not supported on the controller"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeInvalidSizeType
Indicates that the logical drive size cannot be set because the units given for the size is invalid.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the units give for the size is invalid"
|Severity|Critical
|Resolution|Correct the size of the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeLogicalDriveIsLocked
Indicates that the logical drive size cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeNoArraySet
Indicates that the logical drive size cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeNoRAIDLevelSet
Indicates that the logical drive size cannot be set because the logical drive RAID level is not set.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive RAID level is not set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeNoStripSizeSet
Indicates that the logical drive size cannot be set because the logical drive strip size is not set.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive strip size is not set"
|Severity|Critical
|Resolution|Set the logical drive strip size.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeNotAllowed
Indicates that setting the logical drive size is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: size for logical drive with ID "%1" cannot be set to %2 GiB because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeRequestedSizeTooLarge
Indicates that the logical drive size cannot be set because the logical drive size is too large.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive size is too large"
|Severity|Critical
|Resolution|Decrease the logical drive size.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeRequestedSizeTooSmall
Indicates that the logical drive size cannot be set because the logical drive size is too small.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive size is too small"
|Severity|Critical
|Resolution|Increase the logical drive size.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveSizeUnknownError
Indicates that the logical drive size cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveStripSizeInvalidValue
Indicates that the logical drive strip size cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the value is invalid"
|Severity|Critical
|Resolution|Correct the value of the logical drive strip size.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveStripSizeLogicalDriveIsLocked
Indicates that the logical drive strip size cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveStripSizeNoArraySet
Indicates that the logical drive stirp size cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveStripSizeNoRAIDLevelSet
Indicates that the logical drive strip size cannot be set because the RAID level is not set.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the logical drive RAID level is not set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveStripSizeNotAllowed
Indicates that setting the logical drive strip size is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveStripSizeUnknownError
Indicates that the logical drive strip size cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanSetEditableLogicalDriveStripSizeValueOutOfRange
Indicates that the logical drive strip size cannot be set because the desired value is out of range.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the value is out of range"
|Severity|Critical
|Resolution|Correct the value of the logical drive strip size.

### HpeSmartStorage.2.0.CanStopEnableErasedPhysicalDriveUnknownError
Indicates that the physical drive cannot be enabled for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot enable physical drive %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.CanStopErasePhysicalDriveNotErasing
Indicates that the physical drive was not enabled because it is not erasing.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not enabled because drive is not erasing"
|Severity|Warning
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.CanStopErasePhysicalDriveSanitizing
Indicates that the physical drive cannot be enabled because it is currently sanitizing.

| | |
|:---|:---|
|Message Format|"Physical drive %1 was not enabled because it is currently undergoing a sanitize erase"
|Severity|Critical
|Resolution|Resubmit the request at a later time.

### HpeSmartStorage.2.0.ChangeConnectorModeConnectorNotFound
Indicates that the connector mode was not changed because the connector was not found.

| | |
|:---|:---|
|Message Format|"Internal error: connector mode not changed because connector at index %1 not found"
|Severity|Critical
|Resolution|Select a valid connector.

### HpeSmartStorage.2.0.ChangeConnectorModeFailed
Indicates that the connector was not changed to the desired mode due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: not changed connector %1 to %2 mode due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeConnectorModeLogicalDrivesExist
Indicates that the connector mode cannot be changed because the connector has configured logical drives.

| | |
|:---|:---|
|Message Format|"Connector %1 cannot be changed to %2 because the connector has configured logical drives"
|Severity|Critical
|Resolution|Delete the configured logical drives.

### HpeSmartStorage.2.0.ChangeConnectorModeSelectedModePending
Indicates that the desired connector mode is already pending a reboot.

| | |
|:---|:---|
|Message Format|"Connector %1 is already set to %2 and is pending a reboot"
|Severity|Critical
|Resolution|Reboot the system to apply the pending connector mode.

### HpeSmartStorage.2.0.ChangeConnectorModeUnknownError
Indicates that the connector mode cannot be changed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change connector %1 to %2 mode"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.ChangeConnectorModeUnsupportedMode
Indicates that the desired connector mode is invalid or unsupported.

| | |
|:---|:---|
|Message Format|"Connector %1 could not be set to %1 because it is an invalid/unsupported value"
|Severity|Critical
|Resolution|Correct the value of the connector mode.

### HpeSmartStorage.2.0.ChangeConnectorModeUnsupportedOperation
Indicates that changing the connector mode is not supported on the connector.

| | |
|:---|:---|
|Message Format|"The connector mode for connector %1 cannot be changed because the connector does not support changing connector modes"
|Severity|Critical
|Resolution|Remove the connector mode property from the request.

### HpeSmartStorage.2.0.ChangeControllerModeEncryptionIsEnabled
Indicates that the controller mode cannot be changed because encryption is enabled.

| | |
|:---|:---|
|Message Format|"The controller mode cannot be changed to %1 because the controller has encryption enabled"
|Severity|Critical
|Resolution|Disable encryption on the controller.

### HpeSmartStorage.2.0.ChangeControllerModeFailed
Indicates that the controller was not changed to the desired mode due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: not changed controller mode to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeControllerModeLogicalDrivesExist
Indicates that the controller mode cannot be changed because the controller has configured logical drives.

| | |
|:---|:---|
|Message Format|"The controller mode cannot be changed to %1 because the controller has configured logical drives"
|Severity|Critical
|Resolution|Delete the configured logical drives.

### HpeSmartStorage.2.0.ChangeControllerModeSelectedModePending
Indicates that the desired controller mode is already pending a reboot.

| | |
|:---|:---|
|Message Format|"The controller mode is already set to %1 and is pending a reboot"
|Severity|Critical
|Resolution|Reboot the system to apply the pending controller mode.

### HpeSmartStorage.2.0.ChangeControllerModeUnknownError
Indicates that the controller mode cannot be changed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change controller mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.ChangeControllerModeUnsupportedMode
Indicates that the desired controller mode is invalid or unsupported.

| | |
|:---|:---|
|Message Format|"%1 is an invalid/unsupported value for the controller mode"
|Severity|Critical
|Resolution|Correct the value of the controller mode.

### HpeSmartStorage.2.0.ChangeControllerModeUnsupportedOperation
Indicates that changing the controller mode is not supported on controller.

| | |
|:---|:---|
|Message Format|"Changing the controller mode is not supported on this controller"
|Severity|Critical
|Resolution|Remove the controller mode property from the request.

### HpeSmartStorage.2.0.ChangeEditableControllerBootVolumeConflict
Indicates that multiple drives have been requested as a boot volume.

| | |
|:---|:---|
|Message Format|"Device %1 and device %2 cannot both be set as the %3 boot volume"
|Severity|Critical
|Resolution|Select only one device as a boot volume.

### HpeSmartStorage.2.0.ChangeEditableControllerBootVolumeFailed
Indicates that the controller boot volume was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: cannot set controller %1 boot volume due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerDPOFailed
Indicates that the controller degraded performance optimization was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller degraded performance optimization not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerDriveWriteCacheModeFailed
Indicates that the controller drive write cache mode was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller drive write cache mode not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerElevatorSortFailed
Indicates that the controller elevator sort was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller elevator sort not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerEncryptionFailed
Indicates that the controller encryption configuration was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller encryption configuration not set to %1 due toi an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerExpandPriorityFailed
Indicates that the controller expand priority was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller expand priority not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerFLSFailed
Indicates that the controller flexible latency scheduler was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller flexible latency scheduler not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerIRPFailed
Indicates that the controller inconsistency repair policy was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller inconsistency repair policy not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerMNPDelayFailed
Indicates that the controller monitor and performance delay was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller monitor and performance delay not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerNBWCFailed
Indicates that the controller no battery write cache was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller no battery write cache not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerPSSCountFailed
Indicates that the controller parallel surface scan count was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller parallel surface scan count not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerQueueDepthFailed
Indicates that the controller queue depth was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller queue depth not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerReadCachePercentFailed
Indicates that the controller read cache percent was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller read cache percent not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerRebuildPriorityFailed
Indicates that the controller rebuild priority was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller rebuild priority not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerSAMFailed
Indicates that the controller spare activation mode was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller spare activation mode not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerSSAPriorityFailed
Indicates that the controller surface scan analysis priority was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller surface scan analysis priority not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerSurvivalPowerModeFailed
Indicates that the controller survival mode was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller survival mode not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangeEditableControllerWCBTFailed
Indicates that the controller write cache bypass threshold was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller write cache bypass threshold not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangePowerModeFailed
Indicates that the power mode was not changed to maximum due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: power mode not changed to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ChangePowerModeSelectedModePending
Indicates that the desired power mode is already pending a reboot.

| | |
|:---|:---|
|Message Format|"The power mode is already set to %1 and is pending a reboot"
|Severity|Critical
|Resolution|Reboot the system to apply the pending power mode.

### HpeSmartStorage.2.0.ChangePowerModeUnknownError
Indicates that the power mode cannot be changed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change power mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.ChangePowerModeUnsupportedMode
Indicates that the desired power mode is invalid or unsupported.

| | |
|:---|:---|
|Message Format|"%1 is an invalid/unsupported value for the power mode"
|Severity|Critical
|Resolution|Correct the value of the power mode.

### HpeSmartStorage.2.0.ClearConfigurationClearPhysicalDriveCCMEncryptionLocked
Indicates that the controller configuration metadata on the physical drive cannot be cleared because encryption is enabled.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because the controller has encryption enabled"
|Severity|Critical
|Resolution|Disabled encryption on the controller.

### HpeSmartStorage.2.0.ClearConfigurationClearPhysicalDriveCCMNoCCM
Indicates that the controller configuration metadata on physical drives cannot be cleared because no physical drives drives contain configuration metadata.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because no physical drives contain configuration metadata"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.ClearConfigurationClearPhysicalDriveCCMNoDrivesAttached
Indicates that the controller configuration metadata on physical drives cannot be cleared because the controller has no physical drives attached.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because the controller has no physical drives attached"
|Severity|Critical
|Resolution|No action required.

### HpeSmartStorage.2.0.ClearConfigurationClearPhysicalDriveCCMNotAllowed
Indicates that clearing the controller configuration metadata on physical drives is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot clear the controller configuration metadata on physical drives at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ClearConfigurationClearPhysicalDriveCCMNotSupported
Indicates that clearing the controller configuration metadata on physical drives is not supported on this controller.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because it is not supported by the controller"
|Severity|Critical
|Resolution|Do not attempt to clear the controller configuration metadata from the physical drive.

### HpeSmartStorage.2.0.ClearConfigurationClearPhysicalDriveCCMUnknownError
Indicates that the controller configuration metadata on physical drives cannot be cleared for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives"
|Severity|Critical
|Resolution|No resolution available.

### HpeSmartStorage.2.0.ClearEditableControllerBootVolumeFailed
Indicates that the controller boot volume was not cleared due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: cannot clear controller %1 boot volume due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CommitEditableConfigurationFailed
Indicates that the editable configuration was not committed because of an unknown reason.

| | |
|:---|:---|
|Message Format|"Internal error: editable configuration not committed"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CreateEditableArrayFailed
Indicates that the array was not created due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not created due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CreateEditableConfigFailed
Indicates that the editable configuration was not created due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: editable configuration not created due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.CreateEditableLogicalDriveFailed
Indicates that the logical drive was not created due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not created due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.DataDriveNotFound
Indicates that the requested data drive was not found.

| | |
|:---|:---|
|Message Format|"Data drive %1 for logical drive with ID "%2" was not found"
|Severity|Critical
|Resolution|Modify the requested data drive list.

### HpeSmartStorage.2.0.DataDriveSetNotFound
Indicates that the requested data drive set was not found.

| | |
|:---|:---|
|Message Format|"Data drive set with desired parameters for logical drive with ID "%1" was not found"
|Severity|Critical
|Resolution|Modify the requested data drive set.

### HpeSmartStorage.2.0.DeleteEditableArrayFailed
Indicates that the logical drive was not deleted due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not deleted due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.DeleteEditableLogicalDriveFailed
Indicates that the logical drive was not deleted due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not deleted due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.EnablePhysicalDriveFailed
Indicates that the physical drive was not enabled due to an unknown error.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not enabled due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.EnablePhysicalDriveNotFound
Indicates that the physical drive requested to be enabled was not found.

| | |
|:---|:---|
|Message Format|"Physical drive %1 was not enabled because it is not found"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.ErasePhysicalDriveFailed
Indicates that the physical drive was not erased due to an unknown error.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not erased due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.ErasePhysicalDriveNotFound
Indicates that the physical drive requested for erase was not found.

| | |
|:---|:---|
|Message Format|"Erase not started on physical drive %1 because it is not found"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.InternalError
Indicates that an internal error has occurred.

| | |
|:---|:---|
|Message Format|"Internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.LockEditableLogicalDriveFailed
Indicates that locking the logical drive failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not locked due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.LogicalDriveNotFound
Indicates that the logical drive was not found.

| | |
|:---|:---|
|Message Format|"Logical drive with ID %1 not found"
|Severity|Critical
|Resolution|Select a different logical drive.

### HpeSmartStorage.2.0.LogicalDriveNotFoundWarning
Indicates that the logical drive was not found but is not required to complete the request.

| | |
|:---|:---|
|Message Format|"Logical drive with ID %1 not found"
|Severity|Warning
|Resolution|Select a different logical drive.

### HpeSmartStorage.2.0.LogicalDrivesInPendingHBAMode
Indicates that the logical drives are being requested and the controller is pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot process request due to conflicting logical drives and controller pending HBA mode"
|Severity|Critical
|Resolution|Change the controller mode or delete all logical drives.

### HpeSmartStorage.2.0.MalformedJSON
Indicates that the request body was malformed JSON.  Could be duplicate, syntax error, etc.

| | |
|:---|:---|
|Message Format|"The request body submitted was malformed JSON and could not be parsed by the receiving service"
|Severity|Critical
|Resolution|Ensure that the request body is valid JSON and resubmit the request.

### HpeSmartStorage.2.0.NoEditableConfigCreated
Indicates that a configuration has not been created to edit.

| | |
|:---|:---|
|Message Format|"Internal error: no editable configuration has been created"
|Severity|Critical
|Resolution|Create an editable configuration.

### HpeSmartStorage.2.0.PhysicalDriveNotFound
Indicates that the physical drive was not found.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not found"
|Severity|Critical
|Resolution|Select a different physical drive.

### HpeSmartStorage.2.0.PropertyKeyMissing
Indicates that the request is missing a required property.

| | |
|:---|:---|
|Message Format|"Property %1 is missing from the request"
|Severity|Critical
|Resolution|Add the missing property to the request.

### HpeSmartStorage.2.0.PropertyRequiresLogicalDrives
Indicates that the value given for the property requires at least one configured logical drive.

| | |
|:---|:---|
|Message Format|"Setting property %1 requires at least one configured logical drive"
|Severity|Critical
|Resolution|Configure at least one logical drive.

### HpeSmartStorage.2.0.PropertyRequiresMixedModeSupport
Indicates that the value given for the property requires mixed mode support on the controller.

| | |
|:---|:---|
|Message Format|"Setting property %1 requires mixed mode support on the controller"
|Severity|Critical
|Resolution|Remove the property or attempt on a controller that supports mixed mode.

### HpeSmartStorage.2.0.PropertyValueEnumNotInList
Indicates that the desired value is not in the enum list for the property.

| | |
|:---|:---|
|Message Format|"Property %1 does not have enum value %2"
|Severity|Critical
|Resolution|Select a value for the property that is in the enum list.

### HpeSmartStorage.2.0.PropertyValueOutOfRange
Indicates that the property could not be set because the desired value is out of range.

| | |
|:---|:---|
|Message Format|"Property %1 was given value %2 which is out of range for the property"
|Severity|Critical
|Resolution|Correct the value of the property.

### HpeSmartStorage.2.0.PropertyValueTypeError
Indicates that the property could not be set because the value type is incorrect.

| | |
|:---|:---|
|Message Format|"Property %1 was given value %2 which does not match the correct type of the property"
|Severity|Critical
|Resolution|Correct the value of the property.

### HpeSmartStorage.2.0.RebootAndRetryRequired
Indicates that a reboot is required then reapply the configuration.

| | |
|:---|:---|
|Message Format|"Reboot is required then reapply the configuration"
|Severity|Warning
|Resolution|Reboot the system then reapply the configuration.

### HpeSmartStorage.2.0.RebootRequired
Indicates that a reboot is required to apply the configuration.

| | |
|:---|:---|
|Message Format|"Reboot is required to apply the configuration"
|Severity|Warning
|Resolution|Reboot the system to apply the configuration.

### HpeSmartStorage.2.0.ReturnToFactoryNotAllowed
Indicates that reseting the controller to factory settings is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot reset the controller to factory defaults at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SetEditableLogicalDriveAcceleratorFailed
Indicates that setting the logical drive accelerator failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive accelerator for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SetEditableLogicalDriveArrayFailed
Indicates that the logical drive was not assigned to an array due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not assigned to array due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SetEditableLogicalDriveInitializationMethodFailed
Indicates that setting the logical drive initialization method failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: initialization method for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SetEditableLogicalDriveLabelFailed
Indicates that setting the logical drive label failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: label for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SetEditableLogicalDriveRAIDLevelFailed
Indicates that setting the logical drive RAID level failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: RAID level for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SetEditableLogicalDriveSizeFailed
Indicates that setting the logical drive size failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: size for logical drive with ID "%1" failed to be set to %2 GiB due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SetEditableLogicalDriveStripSizeFailed
Indicates that setting the logical drive strip size failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: strip size for logical drive with ID "%1" failed to be set to %2 bytes due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### HpeSmartStorage.2.0.SpareDriveNotFound
Indicates that the requested spare drive was not found.

| | |
|:---|:---|
|Message Format|"Spare drive %1 for logical drive with ID "%2" was not found"
|Severity|Critical
|Resolution|Modify the requested spare drive list.

### HpeSmartStorage.2.0.SpareDriveSetNotFound
Indicates that the requested spare drive set was not found.

| | |
|:---|:---|
|Message Format|"Spare drive set with desired parameters for logical drive with ID "%1" was not found"
|Severity|Critical
|Resolution|Modify the requested spare drive set.

### HpeSmartStorage.2.0.Success
Indicates that all conditions of a successful operation have been met.

| | |
|:---|:---|
|Message Format|"Request successfully completed"
|Severity|OK
|Resolution|None.

### HpeWolfram.1.4.Accepted
Indicates that the operation was accepted, but may not be in effect yet.

| | |
|:---|:---|
|Message Format|"Indicates that the operation was accepted, but may not be in effect yet."
|Severity|OK
|Resolution|None

### HpeWolfram.1.4.ActionOnSystemFailed
An action on a Server was initiated, but the operation was not successful.

| | |
|:---|:---|
|Message Format|"The Server action was not successful because of the error returned from the Server."
|Severity|Warning
|Resolution|Check extended error info for details.

### HpeWolfram.1.4.ActionParameterValueNotInList
Indicates that the correct value type was supplied for the action parameter, but the value is not supported. (The value is not in the enumeration list.)

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is not in the list of valid values."
|Severity|Warning
|Resolution|Choose a value from the enumeration list and resubmit the request if the operation failed.

### HpeWolfram.1.4.ActivationError
Device not activated or Invalid Activation Key.

| | |
|:---|:---|
|Message Format|"Device not activated or Invalid Activation Key."
|Severity|Warning
|Resolution|Install Activation Key

### HpeWolfram.1.4.AddNodeFailed
Add server failed because the supplied credentials are wrong or the server is not reachable or timeout has occurred for the request or server has unsupported iLO version.

| | |
|:---|:---|
|Message Format|"The login was not successful, credentials are wrong or Timeout has occurred or Server is not reachable or server has unsupported iLO version."
|Severity|Warning
|Resolution|Log in with correct user name and password credentials. Also verify if the server has supported iLO Version installed.

### HpeWolfram.1.4.AddNodeValidationFail
Add server operation failed the validation check for iLO firmware version.

| | |
|:---|:---|
|Message Format|"Adding server failed due to incompatible iLO firmware version"
|Severity|Warning
|Resolution|Check if the iLO firmware version is supported. The supported iLO version is 2.50 and above.

### HpeWolfram.1.4.AddOnServiceInstallationCannotBeInitiated
Add-on Service installation cannot be initiated because some jobs are in running state.

| | |
|:---|:---|
|Message Format|"Add-on Service installation cannot be initiated because some jobs are in running state."
|Severity|Warning
|Resolution|No action required.

### HpeWolfram.1.4.AddOnServiceInstallationFailed
Add-on Service installation Failed

| | |
|:---|:---|
|Message Format|"Add-on Service installation Failed."
|Severity|Warning
|Resolution|No action required.

### HpeWolfram.1.4.AddOnServiceInstallationSuccessful
Add-on Service installation completed successfully.

| | |
|:---|:---|
|Message Format|"Add-on Service installation completed successfully."
|Severity|OK
|Resolution|No action required.

### HpeWolfram.1.4.AddOnServiceResetFailed
Add-on Service reset failed

| | |
|:---|:---|
|Message Format|"Add-on Service reset failed."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.AddOnServiceResetSuccessful
Add-on Service reset successfully

| | |
|:---|:---|
|Message Format|"Add-on Service reset successfully."
|Severity|OK
|Resolution|No action required

### HpeWolfram.1.4.AddOnServiceStartFailed
Add-on Service failed to start

| | |
|:---|:---|
|Message Format|"Add-on Service failed to start."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.AddOnServiceStartSuccessful
Add-on Service started successfully

| | |
|:---|:---|
|Message Format|"Add-on Service started successfully."
|Severity|OK
|Resolution|No action required

### HpeWolfram.1.4.AddOnServiceStopFailed
Add-on Service stop failed

| | |
|:---|:---|
|Message Format|"Add-on Service stop failed."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.AddOnServiceStopSuccessful
Add-on Service stopped successfully

| | |
|:---|:---|
|Message Format|"Add-on Service stopped successfully."
|Severity|OK
|Resolution|No action required

### HpeWolfram.1.4.AddOnServiceUnInstallationFailed
Add-on Service uninstallation failed

| | |
|:---|:---|
|Message Format|"Add-on Service uninstallation failed."
|Severity|Warning
|Resolution|No action required.

### HpeWolfram.1.4.AddOnServiceUnInstallationSuccessful
Add-on Service uninstallation successful

| | |
|:---|:---|
|Message Format|"Add-on Service uninstallation completed successfully."
|Severity|OK
|Resolution|No action required.

### HpeWolfram.1.4.AutoRefreshStarted
Periodic refresh of all the servers and groups has started

| | |
|:---|:---|
|Message Format|"Periodic refresh of all the servers and groups has started."
|Severity|OK
|Resolution|No action required.

### HpeWolfram.1.4.BaselineAlreadyPresent
Cannot create Import Baseline task as the baseline is already imported or another task is importing the same baseline.

| | |
|:---|:---|
|Message Format|"The baseline trying to be imported already exists or is being processed."
|Severity|Warning
|Resolution|Delete the existing baseline and try again.

### HpeWolfram.1.4.BaselineCannotBeDeleted
The baseline cannot be deleted now.

| | |
|:---|:---|
|Message Format|"The baseline cannot be deleted as the state of baseline import is %s."
|Severity|Critical
|Resolution|Wait for the baseline import to be completed or abort the related task and retry the delete.

### HpeWolfram.1.4.CannotDeleteBaselinesPendingTasks
Baseline cannot be deleted as there are running/pending tasks using this baseline or the baseline is part of some active recovery policy.

| | |
|:---|:---|
|Message Format|"Baseline cannot be deleted as there are running/pending tasks using this baseline or this baseline is part of an active recovery policy."
|Severity|Warning
|Resolution|Wait until the running tasks complete or delete the recovery policy this baseline is part of and retry the operation.

### HpeWolfram.1.4.CannotDownloadAuditLogs
Audit logs cannot be downloaded.

| | |
|:---|:---|
|Message Format|"Audit logs cannot be downloaded beacuse there are no servers added at all."
|Severity|Critical
|Resolution|No action required.

### HpeWolfram.1.4.CannotDownloadDebugLogs
Debug logs cannot be downloaded.

| | |
|:---|:---|
|Message Format|"Debug logs cannot be downloaded because there is a download in progress"
|Severity|Critical
|Resolution|No action required.

### HpeWolfram.1.4.CannotModifyDefaultUser
Cannot delete or modify certain properties for user created during first time setup.

| | |
|:---|:---|
|Message Format|"Cannot delete or modify certain properties for user created during first time setup."
|Severity|Warning
|Resolution|Only Username, Password and DisplayName can be modified for user created during first time setup.

### HpeWolfram.1.4.CannotModifyUser
Cannot modify certain properties for a user.

| | |
|:---|:---|
|Message Format|"Cannot modify certain properties for a user"
|Severity|Warning
|Resolution|Not allowed to reset certain properties for user.

### HpeWolfram.1.4.CertCSRKeyMismatch
Certificate Import Failed, Private/Public Key Mismatch.

| | |
|:---|:---|
|Message Format|"Certificate Import Failed due to mismatch of Private/Public key of CSR and Certificate."
|Severity|Warning
|Resolution|Generate a new CSR and Import the certificate.

### HpeWolfram.1.4.CertDateTimeMismatch
Certificate Import Failed, Invalid Start or End Date.

| | |
|:---|:---|
|Message Format|"Certificate Import Failed as the Certificate has expired or is not yet valid."
|Severity|Warning
|Resolution|Retry importing a certificate with a valid date/time.

### HpeWolfram.1.4.CertInvalidCAFormat
Certificate Import Failed, Invalid CA Certificate.

| | |
|:---|:---|
|Message Format|"Certificate Import Failed due to Invalid CA Certificate."
|Severity|Warning
|Resolution|Retry importing a certificate with a valid CA Certificate.

### HpeWolfram.1.4.CertInvalidX509Format
Certificate Import Failed, Invalid X.509 Format.

| | |
|:---|:---|
|Message Format|"Certificate Import Failed due to Invalid X.509 Format."
|Severity|Warning
|Resolution|Retry importing a certificate with a valid X.509 format.

### HpeWolfram.1.4.ClaimTokenValidationInProgress
A claim token validation is already in progress.

| | |
|:---|:---|
|Message Format|"A claim token validation is already in progress."
|Severity|Warning
|Resolution|Wait for the current claim token validation to finish and then try again.

### HpeWolfram.1.4.ConfigurationBaselineAlreadyExists
The configuration baseline of the same name already exists.

| | |
|:---|:---|
|Message Format|"The configuration baseline of the same name already exists."
|Severity|Warning
|Resolution|Specify a different configuration baseline name and retry the operation.

### HpeWolfram.1.4.ConfigurationBaselineInUse
The configuration baseline is in use by a recovery policy and cannot be deleted.

| | |
|:---|:---|
|Message Format|"The configuration baseline is in use by a recovery policy and cannot be deleted."
|Severity|Warning
|Resolution|Remove the configuration baseline from the recovery policy and retry the operation.

### HpeWolfram.1.4.ConfigurationBaselineReadOnly
The configuration baseline specified is read only.

| | |
|:---|:---|
|Message Format|"The configuration baseline specified is read only and cannot be created/modified/deleted."
|Severity|Warning
|Resolution|Specify a configuration baseline that is not read only and retry the operation.

### HpeWolfram.1.4.ConfigurationSettingNotFound
The configuration setting was not found in master configuration.

| | |
|:---|:---|
|Message Format|"The configuration setting with name %1 was not found in master configuration."
|Severity|Warning
|Resolution|Specify a different configuration baseline name and retry the operation.

### HpeWolfram.1.4.DeleteGroupFailed
Delete group failed because the group Discovery is in Progress.

| | |
|:---|:---|
|Message Format|"Group Discovery is in progress. Hence operations like Delete are not allowed"
|Severity|Warning
|Resolution|Wait for the group discovery to be completed and then try again.

### HpeWolfram.1.4.DeviceResetRequired
Indicates that one or more properties were correctly changed, but will not take effect until device is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until the device is reset."
|Severity|Warning
|Resolution|Reset the device for the settings to take effect.

### HpeWolfram.1.4.DiscoverServersFromCSVInProgress
Discovery of servers from CSV is already in progress.Cannot start a new csv discovery.

| | |
|:---|:---|
|Message Format|"Discovery of servers from CSV is already in progress. Cannot start a new csv discovery."
|Severity|Warning
|Resolution|Wait for the current Discovery of servers from CSV to complete.

### HpeWolfram.1.4.ETagTooLong
The supplied ETag is too long. The maximum supported ETag length is 63 bytes.

| | |
|:---|:---|
|Message Format|"The supplied ETag is too long. The maximum supported ETag length is 63 bytes."
|Severity|Warning
|Resolution|Retry the operation using an ETag with a length of 63 bytes or less.

### HpeWolfram.1.4.EULANotAccepted
EULA for Intelligent Provisioning not accepted and hence OS provisioning could not be started.

| | |
|:---|:---|
|Message Format|"User must accept EULA to start OS Provisioning."
|Severity|Warning
|Resolution|Accept the EULA to start the OS Provisioning Tasks.

### HpeWolfram.1.4.EnabledSendingServerAddressInfo
The user has enabled sending the server hostname and IP Address to InfoSight.

| | |
|:---|:---|
|Message Format|"The user has enabled sending the server hostname and IP Address information in the heartbeat to InfoSight."
|Severity|OK
|Resolution|None.

### HpeWolfram.1.4.FileExists
File already exists in folder.

| | |
|:---|:---|
|Message Format|"File already exists in folder."
|Severity|Warning
|Resolution|Try another name.

### HpeWolfram.1.4.FileReadFailed
Unable to read file.

| | |
|:---|:---|
|Message Format|"Restore was not successful."
|Severity|Warning
|Resolution|Verify File path.

### HpeWolfram.1.4.FileWriteFailed
Unable to write file.

| | |
|:---|:---|
|Message Format|"Backup was not successful."
|Severity|Warning
|Resolution|Verify File path.

### HpeWolfram.1.4.FirmwareFlashAlreadyInProgress
A firmware upgrade operation is already in progress.

| | |
|:---|:---|
|Message Format|"A firmware flash operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current firmware flash to complete, and then retry the operation.

### HpeWolfram.1.4.FirmwareUpdateCannotBeInitiated
Firmware Update cannot be initiated because some tasks are in running state.

| | |
|:---|:---|
|Message Format|"Firmware Update cannot be initiated because some tasks are in running state."
|Severity|Warning
|Resolution|No action required.

### HpeWolfram.1.4.FirmwareUpdateFailed
Firmware Update Failed

| | |
|:---|:---|
|Message Format|"Firmware Update Failed because %1"
|Severity|Warning
|Resolution|No action required.

### HpeWolfram.1.4.FirmwareUpdateSuccessful
Firmware Update Successful.

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|No action required.

### HpeWolfram.1.4.GatewayNodeFail
Add iLO federation group operation failed due to gateway server not responding or invalid address was given.

| | |
|:---|:---|
|Message Format|"Adding iLO federation group failed due to gateway server not responding."
|Severity|Warning
|Resolution|Verify if the gateway server is powered up and responding.

### HpeWolfram.1.4.GeneratingCertificate
Generating the X.509 Certificate.

| | |
|:---|:---|
|Message Format|"X.509 Certificate is being generated and the process might take up to 10 minutes."
|Severity|OK
|Resolution|None.

### HpeWolfram.1.4.GetServerGroupsHealthStatusInProgress
Get server groups health status is already in progress. Cannot start a new health status process.

| | |
|:---|:---|
|Message Format|"Get server groups health status is already in progress. Cannot start a new health status process."
|Severity|Warning
|Resolution|Wait for the current server groups health status action to complete.

### HpeWolfram.1.4.GroupDoesNotExist
Group Name Does Not Exist

| | |
|:---|:---|
|Message Format|"Group join failed since the Group Name does not Exist."
|Severity|Warning
|Resolution|Specify a Group Name that exists and retry the operation.

### HpeWolfram.1.4.GroupKeyMisMatch
Invalid Group Key Provided.

| | |
|:---|:---|
|Message Format|"Group creation failed since Invalid Group Key Provided."
|Severity|Warning
|Resolution|Specify a Group key that matches and retry the operation.

### HpeWolfram.1.4.GroupNameAlreadyExists
Group Name already Exists

| | |
|:---|:---|
|Message Format|"Group creation failed since the Group Name %1 already exists."
|Severity|Warning
|Resolution|Specify a Group Name that doesn't exist and retry the operation.

### HpeWolfram.1.4.IPRangeAddInProgress
IP Range Add is already in progress. Cannot start a new range discovery.

| | |
|:---|:---|
|Message Format|"IP Range Add is already in progress. Cannot start a new range discovery until the previous discovery is complete."
|Severity|Warning
|Resolution|Wait for the current IP Range discovery to complete.

### HpeWolfram.1.4.IPv6ConfigurationError
The specified IPv6 configuration caused an error.

| | |
|:---|:---|
|Message Format|"The specified IPv6 configuration was in error due to %1."
|Severity|Warning
|Resolution|Resolve the indicated error in the configuration data.

### HpeWolfram.1.4.IPv6StaticRouteNotSupported
IPv6 Static Route is not supported

| | |
|:---|:---|
|Message Format|"IPv6 Static Route is not supported"
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.IncompatibleBaseline
Recovery policy cannot be created or modified as an incompatible baseline is specified.

| | |
|:---|:---|
|Message Format|"Recovery policy cannot be created or modified as an incompatible baseline is specified. "
|Severity|Warning
|Resolution|Specify a compatible baseline and retry the operation.

### HpeWolfram.1.4.IncompatibleGateway
The specified manager address is incompatible for discovering federation groups.

| | |
|:---|:---|
|Message Format|"The specified manager address is incompatible for discovering federation groups."
|Severity|Warning
|Resolution|Verify if the manager supports federation groups and then retry.

### HpeWolfram.1.4.IncompatibleManagedSystem
The managed system is incompatible for the requested operation.

| | |
|:---|:---|
|Message Format|"The managed system %1 is incompatible for the requested operation."
|Severity|Warning
|Resolution|Specify a system that is compatible for the operation and retry again. Please check the documentation for further details.

### HpeWolfram.1.4.IncorrectFilterQuery
Incorrect filter query format.

| | |
|:---|:---|
|Message Format|"Incorrect filter query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.IncorrectPassphrase
An incorrect passphrase has been specified

| | |
|:---|:---|
|Message Format|"An incorrect passphrase has been specified"
|Severity|Warning
|Resolution|Retry the operation using a correct passphrase

### HpeWolfram.1.4.IncorrectSearchQuery
Incorrect search query parameters given.

| | |
|:---|:---|
|Message Format|"Incorrect search query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.IncorrectSearchQuerySelectMissing
Incorrect search query parameters given. Select query parameter is mandatory for search query.

| | |
|:---|:---|
|Message Format|"Incorrect search query format. Select parameter is mandatory."
|Severity|Warning
|Resolution|Please specify select query parameters to search the given field in.

### HpeWolfram.1.4.IncorrectSelectQuery
Incorrect select query parameters given.

| | |
|:---|:---|
|Message Format|"Incorrect select query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.IncorrectSortQuery
Incorrect sorting order or sorting parameters given.

| | |
|:---|:---|
|Message Format|"Incorrect sorting query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.4.InvalidActivationKey
Invalid Activation Key.

| | |
|:---|:---|
|Message Format|"Invalid Activation Key."
|Severity|Warning
|Resolution|Retry Installation with a valid Activation Key.

### HpeWolfram.1.4.InvalidDateRange
Indicates that the end date specified is earlier than start date.

| | |
|:---|:---|
|Message Format|"Ensure that the end date %2 is later than or same as start date %1."
|Severity|Warning
|Resolution|Retry the operation using valid date range.

### HpeWolfram.1.4.InvalidFederationGroupName
Specified Federation group name is invalid.

| | |
|:---|:---|
|Message Format|"The specified Federation group name is not valid. The 'DEFAULT' name for Federation group is reserved."
|Severity|Warning
|Resolution|Modify the Federation group name and retry.

### HpeWolfram.1.4.InvalidLicenseKey
The license key is not valid.

| | |
|:---|:---|
|Message Format|"The license key is not valid."
|Severity|Warning
|Resolution|Retry the operation using a valid license key.

### HpeWolfram.1.4.InvalidOperationForSystemState
The operation was not successful due to the current power state (for example, attempting to turn the power off when it is already off).

| | |
|:---|:---|
|Message Format|"The operation was not successful due to the current power state."
|Severity|Warning
|Resolution|Verify that the system is in the correct power state, and then retry the operation.

### HpeWolfram.1.4.InvalidPasswordLength
The password length is not valid.

| | |
|:---|:---|
|Message Format|"A valid password must contain between %1 to %2 characters."
|Severity|Critical
|Resolution|Retry the operation using a corrected password.

### HpeWolfram.1.4.InvalidSelectionForTaskCreation
Creation of tasks are mutually exclusive for federated and non federated nodes.

| | |
|:---|:---|
|Message Format|"Creation of tasks are mutually exclusive for federated and non federated nodes."
|Severity|Warning
|Resolution|Specify either federated or non federated nodes for the action and try again.

### HpeWolfram.1.4.JobCannotBeAborted
Job cannot be aborted at this time.

| | |
|:---|:---|
|Message Format|"Job cannot be aborted completely at this time"
|Severity|Warning
|Resolution|Job cannot be aborted at this time, wait for the job to be completed.

### HpeWolfram.1.4.JobCannotBeContinued
Job cannot be Continued at this time.

| | |
|:---|:---|
|Message Format|"Job cannot be Continued at this time"
|Severity|Critical
|Resolution|No Resolution.

### HpeWolfram.1.4.JobNameNotValid
Job Creation Failed due to Bad Job Type.

| | |
|:---|:---|
|Message Format|"Job Creation Failed due to Bad Job Type"
|Severity|Critical
|Resolution|Provide a valid Job Type string.

### HpeWolfram.1.4.JobQueueFull
New Jobs cannot be created at this time.

| | |
|:---|:---|
|Message Format|"New Jobs cannot be created at this time as the task queue is full"
|Severity|Warning
|Resolution|Wait for other jobs to be completed and then try again.

### HpeWolfram.1.4.LDAPGroupAlreadyExist
Specified LDAP group name/DN already exists.

| | |
|:---|:---|
|Message Format|"Specified LDAP group name/DN already exists."
|Severity|Warning
|Resolution|Try a different LDAP group name/DN.

### HpeWolfram.1.4.ManagedSystemNotFound
One or more specified managed systems is not found.

| | |
|:---|:---|
|Message Format|"One or more specified managed systems is not found."
|Severity|Warning
|Resolution|Specify a system managed by the appliance and retry the operation.

### HpeWolfram.1.4.MaxConfigurationBaselineLimit
Limit for maximum number of configuration baselines reached.

| | |
|:---|:---|
|Message Format|"Limit for maximum number of configuration baselines reached."
|Severity|Warning
|Resolution|Delete some configuration baselines and retry the operation.

### HpeWolfram.1.4.MaxEventSubscriptionsReached
The maximum number of event subscriptions has reached.

| | |
|:---|:---|
|Message Format|"The operation can not be completed because the maximum number of event subscriptions has reached."
|Severity|Warning
|Resolution|None.

### HpeWolfram.1.4.MaxRecoveryPolicyLimit
Limit for maximum number of recovery policies reached.

| | |
|:---|:---|
|Message Format|"Limit for maximum number of recovery policies reached."
|Severity|Warning
|Resolution|Delete some recovery policies and retry the operation.

### HpeWolfram.1.4.MaxServerGroupsCreated
Server group creation was not successful, because the maximum number of allowed Server Groups have been created.

| | |
|:---|:---|
|Message Format|"The Server group creation was not successful, because the maximum number of allowed Server Groups have been created."
|Severity|Warning
|Resolution|Delete an existing Server Group and try again.

### HpeWolfram.1.4.MaxSessionsCreated
The login was not successful, because the maximum number of allowed sessions have been created.

| | |
|:---|:---|
|Message Format|"The login was not successful, because the maximum number of allowed sessions have been created."
|Severity|Warning
|Resolution|Delete an existing Session and login.

### HpeWolfram.1.4.MembersOfGrpCannotBeDeleted
Delete operation failed because members of a group cannot be deleted.

| | |
|:---|:---|
|Message Format|"Deleting Members of a group failed."
|Severity|Warning
|Resolution|Members of a group cannot be deleted. Only the whole group can be deleted.

### HpeWolfram.1.4.MethodNotAllowed
The specified method for the operation is not allowed.

| | |
|:---|:---|
|Message Format|"The specified method for the operation is not allowed."
|Severity|Warning
|Resolution|Specify a method that is allowed and retry the operation.

### HpeWolfram.1.4.ModifyDefaultCredentials
Modify Credentials of Default User.

| | |
|:---|:---|
|Message Format|"Modify Credentials of Default User."
|Severity|Warning
|Resolution|Modify Credentials of Default User

### HpeWolfram.1.4.MountFailed
Mount operation failed.

| | |
|:---|:---|
|Message Format|"Mount operation failed."
|Severity|Warning
|Resolution|If NFS is specified, please make sure the NFS server is reachable. If USB is specified, please make sure the USB is connected to the system.

### HpeWolfram.1.4.MountFailedDetectingCause
Mount operation failed, detecting the cause...

| | |
|:---|:---|
|Message Format|"Mount operation failed."
|Severity|Warning
|Resolution|If NFS is specified, please make sure the NFS server is reachable. If USB is specified, please make sure the USB is connected to the system.

### HpeWolfram.1.4.MountOperationFailed
Mount operation failed for the provided IP.

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|Check issues related to firewall & check if the folder has been mounted properly.

### HpeWolfram.1.4.MountSuccess
Mount operation was successful.

| | |
|:---|:---|
|Message Format|"Mount operation was successful."
|Severity|Warning
|Resolution|OK

### HpeWolfram.1.4.NoAlertsFound
Indicates that no InfoSight Hotfix Alerts were found.

| | |
|:---|:---|
|Message Format|"No InfoSight Hotfix Alerts found."
|Severity|Warning
|Resolution|Please ensure InfoSight Hotfix Alerts exist.

### HpeWolfram.1.4.NoRebootRequired
NoRebootRequired.

| | |
|:---|:---|
|Message Format|"NoRebootRequired."
|Severity|Warning
|Resolution|NoRebootRequired.

### HpeWolfram.1.4.NoSamples
No power history samples are available.

| | |
|:---|:---|
|Message Format|"No power history samples are available."
|Severity|OK
|Resolution|To accumulate power history samples, power on the server, and then wait at least 5 minutes.

### HpeWolfram.1.4.NotAcceptable
Indicates that one of the values in the request headers are not accpetable.

| | |
|:---|:---|
|Message Format|"Indicates that one of the values in the request headers are not accpetable."
|Severity|Critical
|Resolution|Provide proper values in the request header and try the operation again.

### HpeWolfram.1.4.NotValidIPAddrOrDNS
The value for the property is not a valid IPv4/v6 address or DNS name.

| | |
|:---|:---|
|Message Format|"The value for property %1 is not a valid IPv4/v6 address or DNS name."
|Severity|Warning
|Resolution|Correct the IPv4/v6 address or DNS name, and then retry the operation.

### HpeWolfram.1.4.NotValidIPAddress
The value for the property is not a valid IP address.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid IP address for %2"
|Severity|Warning
|Resolution|Use a valid IP address.

### HpeWolfram.1.4.NotValidSubnetMask
The value for the property is not a valid subnet mask.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid subnet mask for %2"
|Severity|Warning
|Resolution|Use a valid subnet mask.

### HpeWolfram.1.4.PreConditionFailed
Indicates that one of the precondition for the operation failed.

| | |
|:---|:---|
|Message Format|"Indicates that one of the precondition for the operation failed."
|Severity|Critical
|Resolution|Provide the proper precondition and try the operation again.

### HpeWolfram.1.4.PropertyLengthLessThanMinLength
The length for the property is less than the minimum length.

| | |
|:---|:---|
|Message Format|"The length for the property %1 is less than the specified minimum length of %2."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeWolfram.1.4.PropertyLengthMoreThanMaxLength
The length for the property is more than the maximum length.

| | |
|:---|:---|
|Message Format|"The length for the property %1 is more than the specified maximum length of %2."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeWolfram.1.4.PropertyValueBadParam
The property value is not valid.

| | |
|:---|:---|
|Message Format|"The property value is not valid."
|Severity|Warning
|Resolution|Retry the operation using a corrected value.

### HpeWolfram.1.4.PropertyValueRequired
Indicates that a property was required but not specified.

| | |
|:---|:---|
|Message Format|"%1 requires Property %2 to be specified."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### HpeWolfram.1.4.RecoveryPolicyAlreadyExists
A recovery policy of the same name already exists.

| | |
|:---|:---|
|Message Format|"A recovery policy of the same name already exists."
|Severity|Warning
|Resolution|Specify a different recovery policy name and retry the operation.

### HpeWolfram.1.4.RecoveryPolicyInUse
The recovery policy is currently assigned to managed servers. Hence the policy cannot be deleted.

| | |
|:---|:---|
|Message Format|"The recovery policy is currently assigned to managed servers. Hence the policy cannot be deleted."
|Severity|Warning
|Resolution|Unassign the policy from the managed servers before trying to delete.

### HpeWolfram.1.4.RemoteSyslogServiceDisabled
The user has disabled the remoteSysLog service.

| | |
|:---|:---|
|Message Format|"The user has disabled the remoteSysLog service."
|Severity|Warning
|Resolution|Please enable the remoteSysLog service.

### HpeWolfram.1.4.RequiredPropertyMissing
Indicates that a required property is not specified.

| | |
|:---|:---|
|Message Format|"Required Property %1 needs to be specifed."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### HpeWolfram.1.4.ReservedGroupName
Group Name used is reserved.

| | |
|:---|:---|
|Message Format|"Group creation failed since the Group Name is reserved."
|Severity|Warning
|Resolution|Specify a different Group Name and retry the operation.

### HpeWolfram.1.4.ResourceBeingFlashed
The change to the requested resource failed because the resource is being flashed.

| | |
|:---|:---|
|Message Format|"The change to the requested resource failed because the resource is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### HpeWolfram.1.4.ResourceInUseWithDetail
The change could not be made because the resource was in use or in a transitioning state.

| | |
|:---|:---|
|Message Format|"The change to the resource failed because the resource is in use or in transition."
|Severity|Warning
|Resolution|Retry the request.

### HpeWolfram.1.4.ResourceTemporarilyUnavailable
The resource is temporarily unavailable because the firmware is being flashed.

| | |
|:---|:---|
|Message Format|"The resource is temporarily unavailable because the firmware is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### HpeWolfram.1.4.RestoreFailed
Restore was not successful.

| | |
|:---|:---|
|Message Format|"Restore was not successful."
|Severity|Warning
|Resolution|Verify Password.

### HpeWolfram.1.4.RestoreFileNotFound
Restore Failed, File not found.

| | |
|:---|:---|
|Message Format|"Restore Failed as the specified file is not found"
|Severity|Warning
|Resolution|Specify a valid backup file and retry the operation.

### HpeWolfram.1.4.ServerGenerationsMismatchInPayload
The payload for this action can accept either only Gen8/Gen9 servers or Gen10 servers.

| | |
|:---|:---|
|Message Format|"The payload for this action can accept either only Gen8/Gen9 servers or Gen10 servers."
|Severity|Warning
|Resolution|Seperate out Gen8/Gen9 and Gen10 servers into two requests.

### HpeWolfram.1.4.ServerInformationMissing
Server information required for this action is missing.

| | |
|:---|:---|
|Message Format|"Server information required for this action is missing."
|Severity|Warning
|Resolution|Make sure the servers are valid and of known type

### HpeWolfram.1.4.SpecialCharacterNotAllowedInUsername
No special characters except underscore are allowed in the username.

| | |
|:---|:---|
|Message Format|"No special characters except underscore are allowed in the username."
|Severity|Warning
|Resolution|Try a different user or login user name.

### HpeWolfram.1.4.SystemResetRequired
The system properties were correctly changed, but will not take effect until the system is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until system is reset."
|Severity|Warning
|Resolution|Reset the system for the settings to take effect.

### HpeWolfram.1.4.TaskCannotBeAborted
Task cannot be aborted at this time.

| | |
|:---|:---|
|Message Format|"Task cannot be aborted completely at this time"
|Severity|Warning
|Resolution|Task cannot be aborted at this time, wait for the task to be completed.

### HpeWolfram.1.4.TaskCannotBeContinued
Task cannot be Continued at this time.

| | |
|:---|:---|
|Message Format|"Task cannot be Continued at this time."
|Severity|Critical
|Resolution|No Resolution.

### HpeWolfram.1.4.TaskCannotBeCreated
New Tasks cannot be created at this time

| | |
|:---|:---|
|Message Format|"New Tasks cannot be created at this time as the task queue is full"
|Severity|Warning
|Resolution|Wait for the tasks to be completed and then try again.

### HpeWolfram.1.4.TestNMAPCommandCompleted
Completed execution of nmap command for the provided network share IP.

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|Check issues related to firewall & check if the folder has been mounted properly.

### HpeWolfram.1.4.TestShowMountCompleted
Completed execution of showmount -e command for the provided network share IP.

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|OK

### HpeWolfram.1.4.USBNotMounted
USB not mounted.

| | |
|:---|:---|
|Message Format|"No USB found plugged to the device."
|Severity|Warning
|Resolution|Plug in ext2 type USB and perform operation.

### HpeWolfram.1.4.UnableToModifyDuringSystemPOST
The value for the property cannot be changed while the computer system BIOS is in POST.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed while the computer system BIOS is in POST."
|Severity|Warning
|Resolution|After the computer system is either fully booted or powered off, retry the operation.

### HpeWolfram.1.4.UnauthorizedLoginAttempt
The login was not successful, because the supplied credentials could not be authorized.

| | |
|:---|:---|
|Message Format|"The login was not successful, because the supplied credentials could not be authorized."
|Severity|Warning
|Resolution|Log in with authorized user name and password credentials.

### HpeWolfram.1.4.UnsupportedMediaType
Indicates that the media type used or specified is unsupported.

| | |
|:---|:---|
|Message Format|"Indicates that the media type used or specified is unsupported."
|Severity|Critical
|Resolution|Provide or use the right media type and try the operation again.

### HpeWolfram.1.4.UnsupportedOperationInSystemBIOS
This operation is not supported by the current version of the system BIOS.

| | |
|:---|:---|
|Message Format|"This operation is not supported by the current version of the system BIOS."
|Severity|Warning
|Resolution|None.

### HpeWolfram.1.4.UpgradeRunning
Calls are blocked because upgrade is in progress.

| | |
|:---|:---|
|Message Format|"Calls are blocked because upgrade is in progress."
|Severity|Warning
|Resolution|No action required.

### HpeWolfram.1.4.UserAlreadyExist
A User Account with the specified user name already exists.

| | |
|:---|:---|
|Message Format|"A User Account with the specified user name already exists."
|Severity|Warning
|Resolution|Try a different user or login user name.

### HpeWolfram.1.4.UserInitiatedRefreshAllStarted
The user has initiated a refresh of all the servers and groups.

| | |
|:---|:---|
|Message Format|"User Initiated refresh of all the servers and groups has started"
|Severity|OK
|Resolution|No action required.

### HpeWolfram.1.4.UserLimitExceeded
Unable to create a new User Account as the number of user accounts exceed the maximum number allowed by the implementation.

| | |
|:---|:---|
|Message Format|"Unable to create a new User Account as the number of user accounts exceed the maximum number allowed by the implementation."
|Severity|Warning
|Resolution|Before creating a new user account, reduce the number of existing user accounts.

### iLO.2.5.AHSDisabled
Modifying AHS properties is not possible with AHS disabled.

| | |
|:---|:---|
|Message Format|"Modifying AHS properties is not possible with AHS disabled."
|Severity|Warning
|Resolution|Enable AHS, and then modify the AHS properties.

### iLO.2.5.Accepted
Indicates that one or more properties were correctly changed, but may not be in effect yet.

| | |
|:---|:---|
|Message Format|"Indicates that one or more properties were correctly changed, but may not be in effect yet."
|Severity|OK
|Resolution|None

### iLO.2.5.ActionParameterValueNotInList
Indicates that the correct value type was supplied for the action parameter, but the value is not supported. (The value is not in the enumeration list.)

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is not in the list of valid values."
|Severity|Warning
|Resolution|Choose a value from the enumeration list and resubmit the request if the operation failed.

### iLO.2.5.AlertDestinationAssociationError
AlertDestination cannot be configured with both SNMPv1 and SNMPv3.

| | |
|:---|:---|
|Message Format|"AlertDestination cannot be configured with both SNMPv1 and SNMPv3."
|Severity|Warning
|Resolution|For SNMPv1 alert, configure SNMPAlertProtocol to SNMPv1. For SNMPv3 alert, configure SNMPAlertProtocol to SNMPv3.

### iLO.2.5.AlertMailFeatureDisabled
AlertMail feature is disabled.

| | |
|:---|:---|
|Message Format|"AlertMail feature is disabled."
|Severity|Warning
|Resolution|Enable AlertMail feature to send test alert message.

### iLO.2.5.AlreadyInProgress
An operation is already in progress.

| | |
|:---|:---|
|Message Format|"An operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current operation to complete, and then retry the operation.

### iLO.2.5.AlreadyUpToDate
The update did not occur because the component was already up to date.

| | |
|:---|:---|
|Message Format|"The update did not occur because the component was already up to date."
|Severity|OK
|Resolution|None.

### iLO.2.5.ApmPowerCapModeInUsed
Operation is currently unavailable because the power regulator is set to APM Power Capping Mode.

| | |
|:---|:---|
|Message Format|"Operation is currently unavailable because the power regulator is set to APM Power Capping Mode."
|Severity|Warning
|Resolution|Change the power regulator to other modes rather than APM Power Capping Mode through APM interface.

### iLO.2.5.ArrayPropertyAlreadyExists
Duplicate value.

| | |
|:---|:---|
|Message Format|"The property value %1 is already exists in index %2"
|Severity|Warning
|Resolution|If the operation did not complete, correct the property value in the request body and resubmit the request.

### iLO.2.5.ArrayPropertyOutOfBound
The number of items in the array exceeds the maximum number supported.

| | |
|:---|:---|
|Message Format|"An array %1 was supplied with %2 items that exceeds the maximum supported count of %3."
|Severity|Warning
|Resolution|Retry the operation using the correct number of items for the array.

### iLO.2.5.ArrayPropertyValueBadParam
The property value is not valid.

| | |
|:---|:---|
|Message Format|"The property value %1 in index %2 is not valid."
|Severity|Warning
|Resolution|Retry the operation using a corrected value.

### iLO.2.5.BatteryBackupUnitSettingsDisabled
Battery Backup Unit settings are currently disabled.

| | |
|:---|:---|
|Message Format|"Battery Backup Unit settings are disabled when the system is configured for Scalable Persistent Memory."
|Severity|Warning
|Resolution|To re-enable Battery Backup Unit settings, disable Scalable Persistent Memory functionality in the system ROM RBSU.

### iLO.2.5.BiosActionTBD
The BIOS action supplied in the POST operation is not yet implemented.

| | |
|:---|:---|
|Message Format|"The BIOS action %1 is not implemented yet."
|Severity|Critical
|Resolution|The action was invalid or the wrong resource was the target. See the implementation documentation for assistance.

### iLO.2.5.BiosPasswordInfoInvalid
The stored BIOS password information is invalid. A system reboot is neccessary to retore password defaults.

| | |
|:---|:---|
|Message Format|"The stored BIOS password information is invalid.  Reboot system."
|Severity|Critical
|Resolution|The system will need to be rebooted to restore BIOS password information to defaults.

### iLO.2.5.BiosPasswordMismatch
The provided OldPassword does not match the stored BIOS password.

| | |
|:---|:---|
|Message Format|"The provided OldPassword does not match the stored BIOS password."
|Severity|Critical
|Resolution|Retry the action with the matching password.

### iLO.2.5.CalibrateInProgress
Power calibrate is in progress.

| | |
|:---|:---|
|Message Format|"Power calibrate is in progress."
|Severity|Warning
|Resolution|Wait for previous power calibrate complete or stop previous power calibrate, and then retry the operation.

### iLO.2.5.CannotRemoveDefaultLanguagePack
Cannot remove default language pack.

| | |
|:---|:---|
|Message Format|"Cannot remove default language pack."
|Severity|Warning
|Resolution|None.

### iLO.2.5.CannotRemoveLanguagePack
Cannot remove language pack.

| | |
|:---|:---|
|Message Format|"Cannot remove %1 language pack."
|Severity|Warning
|Resolution|None.

### iLO.2.5.CannotRemoveLicense
Cannot remove the base license.

| | |
|:---|:---|
|Message Format|"The base license cannot be removed."
|Severity|Warning
|Resolution|None.

### iLO.2.5.ChassisPowerDataUnAvailable
Chassis power regulation data is currently unavailable.

| | |
|:---|:---|
|Message Format|"Chassis power regulation data is currently unavailable."
|Severity|Warning
|Resolution|Reset the management processor or chassis manager, and then retry the operation.

### iLO.2.5.ChassisResetRequired
The chassis properties were correctly changed, but will not take effect until the chassis is reset or all nodes in chassis remain powered off for at least 5 seconds.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until chassis is reset or all nodes in chassis remain powered off for at least 5 seconds."
|Severity|Warning
|Resolution|Reset chassis or remain power off for all nodes in chassis for at least 5 seconds for the settings to take effect.

### iLO.2.5.ComponentUploadAlreadyInProgress
A component upload operation is already in progress.

| | |
|:---|:---|
|Message Format|"A component upload operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current component upload to complete, and then retry the operation.

### iLO.2.5.ComponentUploadFailed
A component upload operation failed.

| | |
|:---|:---|
|Message Format|"A component upload operation failed."
|Severity|Warning
|Resolution|Wait for the current component upload to complete, and then retry the operation.

### iLO.2.5.DailyUpdateLimitExceeded
An update operation failed due to exceeding a daily limit.

| | |
|:---|:---|
|Message Format|"An update operation failed due to exceeding a daily limit."
|Severity|Warning
|Resolution|Retry the operation at a later date.

### iLO.2.5.DemoLicenseKeyPreviouslyInstalled
A license was previously activated and now a demo key may not be used.

| | |
|:---|:---|
|Message Format|"A license was previously activated."
|Severity|Warning
|Resolution|The system is no longer eligible for demo licenses.

### iLO.2.5.DeviceIsBusy
Device was not available for communication.

| | |
|:---|:---|
|Message Format|"Device communication response was busy."
|Severity|Warning
|Resolution|Retry the attempted operation after a delay.

### iLO.2.5.DeviceResetRequired
Indicates that one or more properties were correctly changed, but will not take effect until device is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until the device is reset."
|Severity|Warning
|Resolution|Reset the device for the settings to take effect.

### iLO.2.5.DiagsTestAlreadyRunning
A diagnostics self test is already running.

| | |
|:---|:---|
|Message Format|"A diagnostics self test is already running."
|Severity|Warning
|Resolution|Stop the running test and try again.

### iLO.2.5.DowngradeNotAllowed
The task did not execute because a downgrade is not allowed by policy.

| | |
|:---|:---|
|Message Format|"The task did not execute because a downgrade is not allowed by policy."
|Severity|Warning
|Resolution|Obtain the latest available component and retry, and clear the task from the queue so processing can continue.

### iLO.2.5.DowngradePolicyAlreadySet
The downgrade policy has been set and cannot be changed.

| | |
|:---|:---|
|Message Format|"The downgrade policy has been set and cannot be changed."
|Severity|Warning
|Resolution|None.

### iLO.2.5.ESKMServersNotConfigured
Enterprise Secure Key Manager Servers are not configured.

| | |
|:---|:---|
|Message Format|"Enterprise Secure Key Manager Servers are not configured."
|Severity|OK
|Resolution|None.

### iLO.2.5.ETagTooLong
The supplied ETag is too long. The maximum supported ETag length is 63 bytes.

| | |
|:---|:---|
|Message Format|"The supplied ETag is too long. The maximum supported ETag length is 63 bytes."
|Severity|Warning
|Resolution|Retry the operation using an ETag with a length of 63 bytes or less.

### iLO.2.5.EmptyDNSName
DNS name is empty.

| | |
|:---|:---|
|Message Format|"Empty DNS name."
|Severity|Warning
|Resolution|Retry the request with a valid DNS name.

### iLO.2.5.ErrorIntializingESKM
Failed to initialize ESKM.

| | |
|:---|:---|
|Message Format|"Failed to initialize ESKM."
|Severity|Warning
|Resolution|Check if Account Group, Local CA Certificate Name, Login Name and Password are correct and try again.

### iLO.2.5.EventLogCleared
Event log cleared successfully.

| | |
|:---|:---|
|Message Format|"Event log cleared successfully."
|Severity|OK
|Resolution|None.

### iLO.2.5.EventSubscriptionModified
The event subscription was modified successfully.

| | |
|:---|:---|
|Message Format|"The event subscription was modified successfully."
|Severity|OK
|Resolution|None.

### iLO.2.5.EventSubscriptionRemoved
The event subscription was removed successfully.

| | |
|:---|:---|
|Message Format|"The event subscription was removed successfully."
|Severity|OK
|Resolution|None.

### iLO.2.5.ExtendedInfo
Indicates that extended information is available.

| | |
|:---|:---|
|Message Format|"See @Message.ExtendedInfo for more information."
|Severity|OK
|Resolution|See @Message.ExtendedInfo for more information.

### iLO.2.5.FWFlashSuccessTPMOverrideEnabled
A Trusted Module is  detected in this system. If you have not performed the proper OS encryption procedures, you will lose access to your data if recovery key is not available. Recommended procedure is to suspend encryption software prior to System ROM or Option ROM firmware flash. TPMOverrideFlag is enabled and firmware flash initiated.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module is detected in this system. Updating the System ROM or Option Card Firmware may have impact to measurements stored in the TM and may have impact to security functionality on the platform which depends on these measurements."
|Severity|OK
|Resolution|None.

### iLO.2.5.FWFlashSuccessTrustedModuleOverrideEnabled
A Trusted Module (type unspecified) is installed in the system and TPMOverrideFlag is enabled. Firmware flash initiated.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module (type unspecified) has been detected in this system. If you have not performed the proper OS encryption procedures, you will lose access to your data if recovery key is not available. Recommended procedure for Microsoft Windows(R) BitLocker(TM) is to "suspend" BitLocker prior to System ROM or Option ROM firmware flash."
|Severity|OK
|Resolution|None.

### iLO.2.5.FWFlashTPMOverrideFlagRequired
A Trusted Module is  detected in this system. Failure to perform proper OS encryption procedures will result in loss of access to your data if recovery key is not available. Recommended procedure is to suspend encryption software prior to System ROM or Option ROM firmware flash. If you do not have your recovery key or have not suspended encryption software, cancel this firmware upload. Failure to follow these instructions will result in loss of access to your data. To continue with firmware flash TPMOverrideFlag is required.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module is detected in this system. Updating the System ROM or Option Card Firmware may have impact to measurements stored in the TM and may have impact to security functionality on the platform which depends on these measurements."
|Severity|Warning
|Resolution|Please set the TPMOverrideFlag to true and try again.

### iLO.2.5.FWFlashTrustedModuleOverrideFlagRequired
A Trusted Module (type unspecified) is installed in the system, TPMOverrideFlag is required for firmware flash to proceed.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module (type unspecified) has been detected in this system. Failure to perform proper OS encryption procedures will result in loss of access to your data if recovery key is not available. Recommended procedure for Microsoft Windows(R) BitLocker(TM) is to "suspend" BitLocker prior to System ROM or Option ROM firmware flash. If you do not have your recovery key or have not suspended BitLocker, exit this flash: Failure to follow these instructions will result in loss of access to your data."
|Severity|Warning
|Resolution|Please set the TPMOverrideFlag to true and try again.

### iLO.2.5.FirmwareFlashAlreadyInProgress
A firmware upgrade operation is already in progress.

| | |
|:---|:---|
|Message Format|"A firmware flash operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current firmware flash to complete, and then retry the operation.

### iLO.2.5.GeneratingCertificate
Generating the X509 Certificate.

| | |
|:---|:---|
|Message Format|"X509 Certificate is being generated and the process might take up to 10 minutes."
|Severity|OK
|Resolution|None.

### iLO.2.5.HardDriveZoneBackupFailure
Backup hard drive zoning configuration to BMC has encountered an error.

| | |
|:---|:---|
|Message Format|"Backup hard drive zoning configuration to BMC has encountered an error."
|Severity|Warning
|Resolution|Retry the operation. If the problem persists, consider resetting the BMC or the entire chassis.

### iLO.2.5.HardDriveZoneFailure
Hard Drive Zoning was in error state.

| | |
|:---|:---|
|Message Format|"Hard Drive Zoning was in error state due to %1."
|Severity|Critical
|Resolution|Retry the operation. If the problem persists, consider resetting the entire chassis.

### iLO.2.5.ICRUInvalidAddress
ICRU returned invalid address for translation.

| | |
|:---|:---|
|Message Format|"ICRU returned invalid address for translation."
|Severity|Warning
|Resolution|Input valid address for translation.

### iLO.2.5.ICRUNotSupported
ICRU feature or function is not supported on the system.

| | |
|:---|:---|
|Message Format|"ICRU feature or function is not supported on the system."
|Severity|Warning
|Resolution|None.

### iLO.2.5.IPv6ConfigurationError
The specified IPv6 configuration caused an error.

| | |
|:---|:---|
|Message Format|"The specified IPv6 configuration was in error due to %1."
|Severity|Warning
|Resolution|Resolve the indicated error in the configuration data.

### iLO.2.5.ImportCertSuccessful
Import Certificate was successful.

| | |
|:---|:---|
|Message Format|"Import Certificate was successful."
|Severity|OK
|Resolution|None.

### iLO.2.5.ImportCertSuccessfuliLOResetinProgress
Import Certificate was successful and the management processor is being reset.

| | |
|:---|:---|
|Message Format|"Import Certificate was successful. Management Processor reset is in progress to enable the new certificate."
|Severity|Warning
|Resolution|None.

### iLO.2.5.ImportCertificateFailed
Failed importing Certificate.

| | |
|:---|:---|
|Message Format|"Failed importing the X509 Certificate."
|Severity|Warning
|Resolution|Retry the operation with proper Certificate information.

### iLO.2.5.ImportSSOParamError
Not a valid parameter.

| | |
|:---|:---|
|Message Format|"Invalid Parameter."
|Severity|Warning
|Resolution|Retry the request with valid parameters.

### iLO.2.5.ImportSSOUriError
Not a valid Uri to import SSO certificate.

| | |
|:---|:---|
|Message Format|"Invalid Uri."
|Severity|Warning
|Resolution|Retry the request with valid URI.

### iLO.2.5.IndicatorLedInvalidStateChange
The request to change the state of the Indicator LED cannot be granted because the current state is either Blinking or is Unknown.

| | |
|:---|:---|
|Message Format|"The Indicator LED cannot be changed when its state is Blinking or Unknown."
|Severity|Warning
|Resolution|Please wait until the server has completed its reserved state.

### iLO.2.5.InstallSetWriteError
The InstallSet write failed.

| | |
|:---|:---|
|Message Format|"The InstallSet write of %1 failed."
|Severity|Warning
|Resolution|Ensure a valid name for the item and that space exists to hold the item.

### iLO.2.5.InterfaceDisabledResetRequired
Disabling one or more interfaces/features will cause certain functionalities to be not available. Please refer to User Guide for details on the implications. Changes will not take effect until the management processor is reset

| | |
|:---|:---|
|Message Format|"CAUTION: Disabling one or more interfaces/features will cause certain functionalities to be not available. Please refer to User Guide for details on the implications. Changes will not take effect until the management processor is reset"
|Severity|OK
|Resolution|None.

### iLO.2.5.InternalErrorWithParam
The operation was not successful due to an internal service error (shown), but the service is still operational.

| | |
|:---|:---|
|Message Format|"The operation was not successful due to an internal service error (%1), but the service is still operational."
|Severity|Critical
|Resolution|Retry the operation. If the problem persists, consider resetting the service.

### iLO.2.5.InvalidConfigurationSpecified
The specified configuration is not valid.

| | |
|:---|:---|
|Message Format|"The specified configuration is not valid."
|Severity|Warning
|Resolution|Correct the configuration, and then retry the operation.

### iLO.2.5.InvalidConfigurationSpecifiedForFederation
iLO Federation Management cannot be supported in the current configuration.

| | |
|:---|:---|
|Message Format|"iLO Federation Management cannot be supported in the current configuration."
|Severity|Warning
|Resolution|Review the management processor network settings or Onboard Administrator settings and refer to the User Guide.

### iLO.2.5.InvalidDwellTime
The dwell time specified is not valid.

| | |
|:---|:---|
|Message Format|"The dwell time %1 is not valid."
|Severity|Warning
|Resolution|Adhere to the dwell time supported.

### iLO.2.5.InvalidEngineID
EngineID should be a hexadecimal number starting with 0x (for example, 0x0102030405abcdef). The string length should be an even number, greater than or equal to 6 characters (excluding the "0x"), and less than or equal to 32 characters.

| | |
|:---|:---|
|Message Format|"EngineID should be a hexadecimal number starting with 0x (for example, 0x0102030405abcdef). The string length should be an even number, greater than or equal to 6 characters (excluding the "0x"), and less than or equal to 32 characters."
|Severity|Warning
|Resolution|Retry the operation using an EngineID within the specified parameters.

### iLO.2.5.InvalidIndex
The Index is not valid.

| | |
|:---|:---|
|Message Format|"The Index provided is not valid."
|Severity|Warning
|Resolution|Adhere to the indexes supported in the self links.

### iLO.2.5.InvalidLicenseKey
The license key is not valid.

| | |
|:---|:---|
|Message Format|"The license key is not valid."
|Severity|Warning
|Resolution|Retry the operation using a valid license key.

### iLO.2.5.InvalidOperationForAutoPowerOnState
The operation was not successful because the current auto power on mode specifies power is to remain off.

| | |
|:---|:---|
|Message Format|"The auto power on delay cannot be set because power is configured to remain off."
|Severity|Warning
|Resolution|Verify that the system auto power on mode is set to turn power on or follow the previous power setting.

### iLO.2.5.InvalidOperationForSystemState
The operation was not successful due to the current power state (for example, attempting to turn the power off when it is already off).

| | |
|:---|:---|
|Message Format|"The operation was not successful due to the current power state."
|Severity|Warning
|Resolution|Verify that the system is in the correct power state, and then retry the operation.

### iLO.2.5.InvalidPassphraseLength
The passphrase must contain 8 to 49 characters.

| | |
|:---|:---|
|Message Format|"%1 must contain 8 to 49 characters."
|Severity|Warning
|Resolution|Correct the passphrase, and then retry the operation.

### iLO.2.5.InvalidPasswordComplexity
The password failed the complexity enforcement.

| | |
|:---|:---|
|Message Format|"A valid password must contain three of the following: uppercase, lowercase, numerals, and other."
|Severity|Critical
|Resolution|Retry the operation using a corrected password.

### iLO.2.5.InvalidPasswordLength
The password length is not valid.

| | |
|:---|:---|
|Message Format|"A valid password must contain between %1 to %2 characters."
|Severity|Critical
|Resolution|Retry the operation using a corrected password.

### iLO.2.5.InvalidSerialNumberLength
The serial number length is not valid.

| | |
|:---|:---|
|Message Format|"A valid serial number must be %1 characters of length."
|Severity|Critical
|Resolution|Adjust the length of the serial number and retry the operation.

### iLO.2.5.LicenseKeyDenied
The license key activation was refused.  Includes details.

| | |
|:---|:---|
|Message Format|"The license activation key cannot be installed.  %1"
|Severity|Warning
|Resolution|Address the condition or use a valid license activation key.

### iLO.2.5.LicenseKeyNotSupported
The use of a license key is not supported on this system.

| | |
|:---|:---|
|Message Format|"The use of a license key is not supported on this system."
|Severity|Warning
|Resolution|None.

### iLO.2.5.LicenseKeyRequired
A license key is required to use this operation or feature.

| | |
|:---|:---|
|Message Format|"A license key is required to use this operation or feature."
|Severity|Warning
|Resolution|Install a license key to use this feature.

### iLO.2.5.LoginAttemptDelayed
The login was not successful, so the service enforces a delay before another login is allowed.

| | |
|:---|:---|
|Message Format|"The login was not successful, so the service enforces a delay before another login is allowed."
|Severity|Warning
|Resolution|Wait for the delay time to expire, and then retry the login.

### iLO.2.5.LoginAttemptDelayedSeconds
The login was not successful, so the service enforces a delay before another login is allowed.

| | |
|:---|:---|
|Message Format|"The login was not successful, so the service enforces a %1 second delay before another login is allowed."
|Severity|Warning
|Resolution|None.

### iLO.2.5.MaxProviders
The maximum number of providers are already registered.

| | |
|:---|:---|
|Message Format|"The maximum number of providers are already registered."
|Severity|Warning
|Resolution|None.

### iLO.2.5.MaxVirtualMediaConnectionEstablished
No more Virtual Media connections are available, because the maximum number of connections are already established.

| | |
|:---|:---|
|Message Format|"No more Virtual Media connections are available, because the maximum number of connections are already established."
|Severity|Warning
|Resolution|Close an established Virtual Media connection, and then retry creating or opening another connection.

### iLO.2.5.MembistVariablesNotSupported
Membist variables are not supported on the system.

| | |
|:---|:---|
|Message Format|"Membist variables are not supported on the system."
|Severity|Warning
|Resolution|None.

### iLO.2.5.MemoryInterleaveSetError
The memory set specified in InterleaveSets is not supported.

| | |
|:---|:---|
|Message Format|"The memory set specified in InterleaveSets is not supported."
|Severity|Warning
|Resolution|Ensure the memory set specified in InterleaveSets matches one of the memory domain's InterleavableMemrorySets.

### iLO.2.5.NewerVersionRequired
Update does not meet minimum version requirements.

| | |
|:---|:---|
|Message Format|"Update does not meet minimum version requirements."
|Severity|Warning
|Resolution|Use newer version.

### iLO.2.5.NoContent
The requested resource exists but has no content.

| | |
|:---|:---|
|Message Format|"The resource exists but has no content."
|Severity|OK
|Resolution|None

### iLO.2.5.NoEventSubscriptions
There are no event subscriptions registerd.

| | |
|:---|:---|
|Message Format|"The opeartion can not be completed because there are no event subscribers."
|Severity|Warning
|Resolution|None

### iLO.2.5.NoPowerMetering
No support for power metering available on platform.

| | |
|:---|:---|
|Message Format|"No support for power metering available on platform."
|Severity|OK
|Resolution|Enable Power Metering on platform if supported.

### iLO.2.5.NoSNMPAlertDestinationsConfigured
No SNMP alert destinations are configured.

| | |
|:---|:---|
|Message Format|"No SNMP alert destinations are configured."
|Severity|Warning
|Resolution|Disable SNMP pass-thru, modify the property, and then re-enable SNMP pass-thru.

### iLO.2.5.NoSamples
No power history samples are available.

| | |
|:---|:---|
|Message Format|"No power history samples are available."
|Severity|OK
|Resolution|To accumulate power history samples, power on the server, and then wait at least 5 minutes.

### iLO.2.5.NoScriptedVirtualMediaConnectionAvailable
No scripted virtual media connections exist to perform the operation.

| | |
|:---|:---|
|Message Format|"No scripted virtual media connections exist to perform the operation."
|Severity|Warning
|Resolution|Create or open a scripted virtual media connection, and then retry the operation.

### iLO.2.5.NoSpaceforDNSName
No space to store DNS name.

| | |
|:---|:---|
|Message Format|"No space to store DNS name."
|Severity|Warning
|Resolution|Make sure SSO database has enough space to store DNS name.

### iLO.2.5.NoVirtualMediaConnectionAvailable
No Virtual Media connections exist to perform the operation.

| | |
|:---|:---|
|Message Format|"No Virtual Media connections exist to perform the operation."
|Severity|Warning
|Resolution|Create or open a Virtual Media connection, and then retry the operation.

### iLO.2.5.NodeAssignedCrossRegion
Each zone can only manage the node in the same region, cannot manage overlap region.

| | |
|:---|:---|
|Message Format|"Each zone can only manage the node for range %1 or range %2, cannot manage overlap region."
|Severity|Warning
|Resolution|Correct the out of range value, and then retry the operation.

### iLO.2.5.NodeNotPresentInZone
Operation is currently unavailable because there is no node installed in the zone.

| | |
|:---|:---|
|Message Format|"Operation is currently unavailable because there is no node installed in the zone."
|Severity|Warning
|Resolution|Install at least one node in the zone and retry the operation.

### iLO.2.5.NotSupportedOnNIC
This property is not supported by the indicated network port.

| | |
|:---|:---|
|Message Format|"%1 is not supported on the %2 Network Port."
|Severity|Warning
|Resolution|Do not specify this property on the indicated network port.

### iLO.2.5.NotValidIPAddrOrDNS
The value for the property is not a valid IPv4/v6 address or DNS name.

| | |
|:---|:---|
|Message Format|"The value for property %1 is not a valid IPv4/v6 address or DNS name."
|Severity|Warning
|Resolution|Correct the IPv4/v6 address or DNS name, and then retry the operation.

### iLO.2.5.NotValidIPAddress
The value for the property is not a valid IP address.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid IP address for %2"
|Severity|Warning
|Resolution|Use a valid IP address.

### iLO.2.5.NotValidSubnetMask
The value for the property is not a valid subnet mask.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid subnet mask for %2"
|Severity|Warning
|Resolution|Use a valid subnet mask.

### iLO.2.5.OperationAvailableAfterSystemPOST
The value for the property can not be set until System BIOS POST completes.

| | |
|:---|:---|
|Message Format|"Property %1 will be settable after the System BIOS completes POST."
|Severity|Warning
|Resolution|Wait to see the change in value until after the System BIOS completes POST.

### iLO.2.5.OperationWillCompleteAfterSystemPOST
The value for the property will be applied after System BIOS POST completes.

| | |
|:---|:---|
|Message Format|"The value for property %1 will be changed after the System BIOS completes POST."
|Severity|Information
|Resolution|Wait to see the change in value until after the System BIOS completes POST.

### iLO.2.5.PowerCapOACntrld
The enclosure Onboard Administrator is currently managing the power cap.

| | |
|:---|:---|
|Message Format|"The enclosure Onboard Administrator is currently managing the power cap."
|Severity|Warning
|Resolution|Use Onboard Administrator to Manage the PowerCap

### iLO.2.5.PowerCapROMCntrld
The System ROM is currently managing the power cap.

| | |
|:---|:---|
|Message Format|"The System ROM is currently managing the power cap."
|Severity|Warning
|Resolution|Enable RESTful API management of the power cap in System ROM

### iLO.2.5.PowerLimitMayNotTakeEffect
One of power limit setpoint may become unreachable due to power limit range is unknown. It's not recommended configure power limit setpoint when power limit range is unknown.

| | |
|:---|:---|
|Message Format|"One of power limit setpoint may become unreachable due to power limit range is unknown. It's not recommended configure power limit setpoint when power limit range is unknown."
|Severity|Warning
|Resolution|Please execute calibrate action to get power limit range then reconfigure power limit setpoint.

### iLO.2.5.PowerRegulationNotDisable
Operation is currently unavailable because chassis power regulation is enabled.

| | |
|:---|:---|
|Message Format|"Operation is currently unavailable because chassis power regulation is enabled."
|Severity|Warning
|Resolution|Disable chassis power regulation, and then retry the operation.

### iLO.2.5.PowerSettingAdjustRequired
Indicates that one or more power limit setting were correctly changed, but will not take effect until power regulation enable and power regulator mode switch to user configurable mode.

| | |
|:---|:---|
|Message Format|"Indicates that one or more power limit setting were correctly changed, but will not take effect until power regulation enable and power regulator mode switch to user configurable mode."
|Severity|Warning
|Resolution|Enable power regulation and switch power regulator mode to user configurable mode for the settings to take effect.

### iLO.2.5.PowerValueBadParam
The power cap value is not valid.

| | |
|:---|:---|
|Message Format|"The power cap value is not valid."
|Severity|Warning
|Resolution|Retry the operation using a corrected value.

### iLO.2.5.PowerValueInvalidCalibrationData
The request to set the power cap failed. Invalid power cap calibration data. The Power Cap feature is currently unavailable.

| | |
|:---|:---|
|Message Format|"The request to set the power cap failed. Invalid power cap calibration data. The Power Cap feature is currently unavailable"
|Severity|Warning
|Resolution|Restart the server to retrieve calibration data from initial POST.

### iLO.2.5.PowerValueNotOptimal
Power caps set below the specified percentage threshold may become unreachable due to changes in the server. It is not recommended to set a cap for less than this threshold.

| | |
|:---|:---|
|Message Format|"Power caps set below the specified percentage threshold may become unreachable due to changes in the server. It is not recommended to set a cap for less than %1%."
|Severity|Warning
|Resolution|Please provide an optimal value in integer considering the power cap range.

### iLO.2.5.PowerValueUnAvailable
Advanced power capping is not currently available due to the system configuration or state.

| | |
|:---|:---|
|Message Format|"Advanced power capping is not currently available due to the system configuration or state."
|Severity|Warning
|Resolution|Change the system configuration or wait for the system to become fully initialized, and then retry the operation.

### iLO.2.5.PowerValueUnSupported
Advanced power capping is not supported on this system.

| | |
|:---|:---|
|Message Format|"Advanced power capping is not supported on this system."
|Severity|Warning
|Resolution|None.

### iLO.2.5.PrimaryESKMServerAccessible
Only the primary ESKM server is accessible.

| | |
|:---|:---|
|Message Format|"No redundancy. Only the primary ESKM server is accessible."
|Severity|OK
|Resolution|None.

### iLO.2.5.PrimarySecondaryAddressesResolveToSameServer
Primary and secondary ESKM server addresses resolve to the same server.

| | |
|:---|:---|
|Message Format|"No redundancy. Primary and secondary ESKM server addresses resolve to the same server."
|Severity|OK
|Resolution|None.

### iLO.2.5.PrimarySecondaryESKMServersAccessible
Both primary and secondary ESKM servers are accessible.

| | |
|:---|:---|
|Message Format|"Redundant solution: Both primary and secondary ESKM servers are accessible."
|Severity|OK
|Resolution|None.

### iLO.2.5.PropertyNotSupported
The property is not supported.

| | |
|:---|:---|
|Message Format|"The property %1 is not supported."
|Severity|Warning
|Resolution|Do not attempt to modify this property.

### iLO.2.5.PropertyNotWritableOrUnknown
The request included a value for a  read-only or unknown property.

| | |
|:---|:---|
|Message Format|"The property %1 is a read-only property and cannot be assigned a value, or not valid for this resource."
|Severity|Warning
|Resolution|If the operation did not complete, remove the property from the request body and resubmit the request.

### iLO.2.5.PropertyValueAlreadySet
The value being set for the property is same as existing value.

| | |
|:---|:---|
|Message Format|"The new value %1 is same as exisiting value for the property %2."
|Severity|OK
|Resolution|None

### iLO.2.5.PropertyValueBadParam
The property value is not valid.

| | |
|:---|:---|
|Message Format|"The property value is not valid."
|Severity|Warning
|Resolution|Retry the operation using a corrected value.

### iLO.2.5.PropertyValueExceedsMaxLength
The value for the property exceeds the maximum length.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 exceeds the maximum length of %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### iLO.2.5.PropertyValueIncompatible
The value for the property is the correct type, but this value is incompatible with the current value of another property.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is incompatible with the value for property %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### iLO.2.5.PropertyValueOutOfRange
The value for the property is out of range.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is out of range %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### iLO.2.5.PropertyValueRequired
Indicates that a property was required but not specified.

| | |
|:---|:---|
|Message Format|"%1 requires Property %2 to be specified."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### iLO.2.5.RecoveryInstallSetRequired
A recovery install set is required for this action.

| | |
|:---|:---|
|Message Format|"No recovery install set present."
|Severity|Critical
|Resolution|Create a recovery install set (install set with IsRecovery property set true).

### iLO.2.5.RepairNotSupported
IML event with this severity is not supported to be repaired. IML events with Critical or Warning severities can marked as repaired.

| | |
|:---|:---|
|Message Format|"IML event with %1 severity is not supported to be repaired. IML events with Critical or Warning severities can marked as repaired."
|Severity|Warning
|Resolution|Please do not try to repair IML events with severity other than Critical or Warning.

### iLO.2.5.RequiredPropertyMissing
Indicates that a required property is not specified.

| | |
|:---|:---|
|Message Format|"Required Property %1 needs to be specifed."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### iLO.2.5.ResetInProgress
A management processor reset is in progress.

| | |
|:---|:---|
|Message Format|"A management processor reset is in progress."
|Severity|Warning
|Resolution|Wait for management processor reset to complete, and then retry the operation.

### iLO.2.5.ResetRequired
One or more properties were changed, but these changes will not take effect until the management processor is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed, but these changes will not take effect until the management processor is reset."
|Severity|Warning
|Resolution|To enable the changed properties, reset the management processor.

### iLO.2.5.ResourceBeingFlashed
The change to the requested resource failed because the resource is being flashed.

| | |
|:---|:---|
|Message Format|"The change to the requested resource failed because the resource is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### iLO.2.5.ResourceInUseWithDetail
The change could not be made because the resource was in use or in a transitioning state.

| | |
|:---|:---|
|Message Format|"The change to the resource failed because the resource is in use or in transition."
|Severity|Warning
|Resolution|Retry the request.

### iLO.2.5.ResourceNotReadyRetry
The resource is present but is not ready to perform operations due to an internal condition such as initialization or reset.

| | |
|:---|:---|
|Message Format|"The resource is present but is not ready to perform operations.  The resource will be ready in %1 seconds."
|Severity|Warning
|Resolution|Retry the operation when the resource is ready.

### iLO.2.5.ResourceTemporarilyUnavailable
The resource is temporarily unavailable because the firmware is being flashed.

| | |
|:---|:---|
|Message Format|"The resource is temporarily unavailable because the firmware is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### iLO.2.5.SMBIOSRecordNotFound
The SMBIOS record type is not found or is not supported on the system.

| | |
|:---|:---|
|Message Format|"The SMBIOS record type %1 is not found or is not supported on the system."
|Severity|Warning
|Resolution|Reset the system to update the SMBIOS records. If the problem persists then the SMBIOS record type is not supported.

### iLO.2.5.SNMPAlertDisabled
The operation could not be completed because SNMP alerts are disabled.

| | |
|:---|:---|
|Message Format|"The operation could not be completed because SNMP alerts are disabled."
|Severity|Warning
|Resolution|Enable SNMP alerts and retry the operation.

### iLO.2.5.SNMPDisabled
Modifying SNMP properties is not possible with SNMP disabled.

| | |
|:---|:---|
|Message Format|"Modifying SNMP properties is not possible with SNMP disabled."
|Severity|Warning
|Resolution|Enable SNMP, and then modify the SNMP properties.

### iLO.2.5.SNMPTestAlertFailed
The SNMP Test Alert did not send successfully.

| | |
|:---|:---|
|Message Format|"The SNMP Test Alert did not send successfully."
|Severity|Warning
|Resolution|Verify the test alert content and retry.

### iLO.2.5.SNMPv1Disabled
Modifying SNMP v1 properties is not possible with SNMP v1 protocol disabled.

| | |
|:---|:---|
|Message Format|"Modifying SNMP v1 properties is not possible with SNMP v1 protocol disabled."
|Severity|Warning
|Resolution|Enable SNMP v1, and then modify the SNMP v1 properties.

### iLO.2.5.SNTPConfigurationManagedByDHCPAndIsReadOnly
SNTP configuration is currently managed by DHCP and is therefore read-only.

| | |
|:---|:---|
|Message Format|"%1 cannot be changed while DHCP is configured to provide SNTP settings."
|Severity|Warning
|Resolution|Disable SNTP configuration options in both DHCPv4 and DHCPv6 (see /Managers/n/NICs), and then reconfigure SNTP as desired with static settings.

### iLO.2.5.SSOCertficateEmpty
SSO Certificate is Empty.

| | |
|:---|:---|
|Message Format|"Empty SSO Certificate."
|Severity|Warning
|Resolution|None.

### iLO.2.5.SSOCertificateReadError
SSO Certificate Read Error.

| | |
|:---|:---|
|Message Format|"Error reading SSO certificate."
|Severity|Warning
|Resolution|Retry the request with valid SSO certificate.

### iLO.2.5.SSONoSpaceError
No space to store SSO certificate.

| | |
|:---|:---|
|Message Format|"No space to store SSO certificate."
|Severity|Warning
|Resolution|Make sure SSO database has enough space to store SSO certificate.

### iLO.2.5.SSORecordNotFound
SSO Record Not Found.

| | |
|:---|:---|
|Message Format|"SSO Record Not Found."
|Severity|Warning
|Resolution|None.

### iLO.2.5.SamplesNotCaptured
Samples are not captured for %1 duration.

| | |
|:---|:---|
|Message Format|"Samples for metrics are not captured for %1 duration."
|Severity|OK
|Resolution|Wait for the current duration to complete, and then retry.

### iLO.2.5.SecondaryESKMServerAccessible
Only the secondary ESKM server is accessible.

| | |
|:---|:---|
|Message Format|"No redundancy. Only the secondary ESKM server is accessible."
|Severity|OK
|Resolution|None.

### iLO.2.5.ServerConfigLockStatusUnknown
The current status of Server Configuration Lock is unknown.

| | |
|:---|:---|
|Message Format|"The current status of Server Configuration Lock is unknown."
|Severity|Warning
|Resolution|Ensure if the BIOS firmware supports Server Configuration Lock. If supported, reboot the server and retry the operation

### iLO.2.5.ServerConfigurationLockEnabled
Server Configuration Lock is enabled.

| | |
|:---|:---|
|Message Format|"Server Configuration Lock is enabled."
|Severity|Warning
|Resolution|Disable Server Configuration Lock to initiate secure erase of the system

### iLO.2.5.SuccessFeedback
The operation completed successfully.

| | |
|:---|:---|
|Message Format|"The operation completed successfully."
|Severity|OK
|Resolution|None

### iLO.2.5.SyslogFeatureDisabled
Remote Syslog feature is disabled.

| | |
|:---|:---|
|Message Format|"Remote syslog feature is disabled."
|Severity|Warning
|Resolution|Enable remote syslog feature to send test syslog message.

### iLO.2.5.SystemPowerOffRequired
The system has to be powered off to perform this operation. AutoPowerOn must be set to achieve a power restore.

| | |
|:---|:---|
|Message Format|"The system has to be powered off to perform this operation."
|Severity|OK
|Resolution|Power off the system to perform this operation.

### iLO.2.5.SystemResetRequired
The system properties were correctly changed, but will not take effect until the system is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until system is reset."
|Severity|Warning
|Resolution|Reset system for the settings to take effect.

### iLO.2.5.TokenRequired
Proper 'X-HPRESTFULAPI-AuthToken' authorization token not provided.

| | |
|:---|:---|
|Message Format|"Proper 'X-HPRESTFULAPI-AuthToken' authorization token not provided."
|Severity|Critical
|Resolution|Create proper 'X-HPRESTFULAPI-AuthToken' authorization token. Send token in using the proper HTTP header.

### iLO.2.5.UnableModifyRights
Unable to modify user rights.

| | |
|:---|:---|
|Message Format|"Unable to modify user rights."
|Severity|Warning
|Resolution|None.

### iLO.2.5.UnableToModifyAfterVirtualMediaInsert
The value for the property cannot be changed after virual media image is inserted.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed after virual media image is inserted."
|Severity|Warning
|Resolution|Retry the operation during virtual media image inseration.

### iLO.2.5.UnableToModifyDueToMissingComponent
The value for the property cannot be changed because a related hardware component is not installed.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed because a related hardware component is not installed."
|Severity|Warning
|Resolution|Install the hardware component and retry the operation.

### iLO.2.5.UnableToModifyDuringSystemPOST
The value for the property cannot be changed while the computer system BIOS is in POST.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed while the computer system BIOS is in POST."
|Severity|Warning
|Resolution|After the computer system is either fully booted or powered off, retry the operation.

### iLO.2.5.UnableToModifyWhileKVMIPConnected
The value for the property cannot be changed while a KVMIP connection is in progress.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed while a KVMIP connection is in progress."
|Severity|Warning
|Resolution|Retry the operation after disconnecting all KVMIP connections.

### iLO.2.5.UnauthorizedLoginAttempt
The login was not successful, because the supplied credentials could not be authorized.

| | |
|:---|:---|
|Message Format|"The login was not successful, because the supplied credentials could not be authorized."
|Severity|Warning
|Resolution|Log in with authorized user name and password credentials.

### iLO.2.5.UnsupportedCipherAlgo
Incompatible Cipher Algorithm in FIPS or CNSA Mode.

| | |
|:---|:---|
|Message Format|"Incompatible Cipher Algorithm %1 in %2 Mode."
|Severity|Warning
|Resolution|Select compatible Cipher Algorithm.

### iLO.2.5.UnsupportedOperation
This operation is not supported by RIS for the current system.

| | |
|:---|:---|
|Message Format|"This operation is not supported by RIS for the current system."
|Severity|Warning
|Resolution|None.

### iLO.2.5.UnsupportedOperationInChassisVersion
This operation is not supported by the current version of the XL Chassis firmware.

| | |
|:---|:---|
|Message Format|"This operation is not supported by the current version of the XL Chassis firmware."
|Severity|Warning
|Resolution|Please update the XL Chassis firmware to latest version.

### iLO.2.5.UnsupportedOperationInLegacyBootMode
This operation is not supported when the system Boot Mode is set to Legacy BIOS.

| | |
|:---|:---|
|Message Format|" This operation is not supported when the system Boot Mode is set to Legacy BIOS."
|Severity|Warning
|Resolution|Change the Boot Mode to UEFI and retry the operation.

### iLO.2.5.UnsupportedOperationInSystemBIOS
This operation is not supported by the current version of the system BIOS.

| | |
|:---|:---|
|Message Format|"This operation is not supported by the current version of the system BIOS."
|Severity|Warning
|Resolution|None.

### iLO.2.5.UpdateBadParameter


| | |
|:---|:---|
|Message Format|"The update failed because a bad parameter was supplied."
|Severity|Warning
|Resolution|Supply correct parameters to the component and retry the update.

### iLO.2.5.UpdateCancelled


| | |
|:---|:---|
|Message Format|"The update was canceled by the update process."
|Severity|Warning
|Resolution|Retry the update.

### iLO.2.5.UpdateDependencyFailure


| | |
|:---|:---|
|Message Format|"The update did not complete because the component failed a dependency check."
|Severity|Warning
|Resolution|Install any dependent components first and then retry this update.

### iLO.2.5.UpdateFailed


| | |
|:---|:---|
|Message Format|"The update failed with a component specific error (%1)."
|Severity|Warning
|Resolution|Retry the update after remedying the component error.

### iLO.2.5.UpdateInPOST


| | |
|:---|:---|
|Message Format|"System must not be booted past POST in order to perform this update"
|Severity|Warning
|Resolution|Boot to UEFI and retry the update.

### iLO.2.5.UpdateInterrupted


| | |
|:---|:---|
|Message Format|"The update was interrupted."
|Severity|Warning
|Resolution|Retry the update.

### iLO.2.5.UpdateInvalidFile


| | |
|:---|:---|
|Message Format|"The update operation failed because the file is not valid."
|Severity|Warning
|Resolution|Remove and re-add the component to the repository and try the operation again.

### iLO.2.5.UpdateInvalidOS


| | |
|:---|:---|
|Message Format|"The update did not occur because the running OS is not valid."
|Severity|Warning
|Resolution|Retry the update while running the correct OS.

### iLO.2.5.UpdateNotApplicable


| | |
|:---|:---|
|Message Format|"The task was not completed because the component was not applicable to this system."
|Severity|Warning
|Resolution|None.

### iLO.2.5.UpdateRepositoryUnavailable


| | |
|:---|:---|
|Message Format|"The update operation failed because the component repository is unavailable."
|Severity|Warning
|Resolution|None.

### iLO.2.5.UpdateTaskQueueFull
The Invoke action was not successful because the update task queue is full.

| | |
|:---|:---|
|Message Format|"The Invoke action was not successful because the update task queue is full."
|Severity|Critical
|Resolution|Remove completed tasks from the update task queue to retry the operation.

### iLO.2.5.UpdateTaskQueueWriteError
The UpdateTaskQueue write failed.

| | |
|:---|:---|
|Message Format|"The UpdateTaskQueue write of %1 failed."
|Severity|Warning
|Resolution|Ensure a valid name for the item and that space exists to hold the item.

### iLO.2.5.UpdateTemporarilyUnavailable


| | |
|:---|:---|
|Message Format|"The system is temporarily unable to perform this update"
|Severity|Warning
|Resolution|Retry the update, ensuring that power state is stable.

### iLO.2.5.UpdateWithPowerOff


| | |
|:---|:---|
|Message Format|"System power must be off to perform this update"
|Severity|Warning
|Resolution|Power system on and retry the update.

### iLO.2.5.UpdateWithPowerOn


| | |
|:---|:---|
|Message Format|"System power must be on to perform this update"
|Severity|Warning
|Resolution|Power system on and retry the update.

### iLO.2.5.UserAlreadyExist
The user or login user name already exists.

| | |
|:---|:---|
|Message Format|"The user or login user name already exists."
|Severity|Warning
|Resolution|Try a different user or login user name.

### iLO.2.5.UserNameAlreadyExists
Duplicate SNMPv3 User.

| | |
|:---|:---|
|Message Format|"The username %1 already exists in the list"
|Severity|Warning
|Resolution|Enter a different name and try again.

### iLO.2.5.VirtualMediaIsDisabled
Virtual Media has been disabled.

| | |
|:---|:---|
|Message Format|"Virtual Media has been disabled."
|Severity|Warning
|Resolution|Enable Virtual Media to perform this operation.

### iLO.2.5.ZonePowerLimitExceeded
The sum of zone power limit cannot be more than chassis power limit.

| | |
|:---|:---|
|Message Format|"The value %1 for the sum of %2 cannot be more than chassis power limit %3."
|Severity|Warning
|Resolution|Correct the value avoid the sum of power limit exceeds chassis power limit, and then retry the operation.

### iLO.2.5.iLOResetAndSystemRebootRequired
Indicates that one or more properties were correctly changed, but will not take effect until device is reset and system is rebooted.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until the device is reset and system is rebooted"
|Severity|Warning
|Resolution|Reset the management processor and reboot the server.

### iLO.2.5.iLOServicePortIsDisabled
The Service Port is disabled. Other Service Port properties cannot be changed.

| | |
|:---|:---|
|Message Format|"The Service Port is disabled. Other Service Port properties cannot be changed."
|Severity|Warning
|Resolution|Enable Service Port to modify other Service Port properties.

### iLO.2.5.iLOVirtualNICDisabled
The Virtual NIC is disabled.

| | |
|:---|:---|
|Message Format|"The Virtual NIC is disabled."
|Severity|Warning
|Resolution|Enable iLO Virtual NIC to perform this operation.
