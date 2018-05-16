
### Base.1.1.AccessDenied
Indicates that while attempting to access, connect to or transfer to/from another resource, the service denied access.

| | |
|:---|:---|
|Message Format|"While attempting to establish a connection to %1, the service denied access."
|Severity|Critical
|Resolution|Attempt to ensure that the URI is correct and that the service has the appropriate credentials.

### Base.1.1.AccountForSessionNoLongerExists
Indicates that the account for the session has been removed, thus the session has been removed as well.

| | |
|:---|:---|
|Message Format|"The account for the current session has been removed, thus the current session has been removed as well."
|Severity|OK
|Resolution|Attempt to connect with a valid account.

### Base.1.1.AccountModified
Indicates that the account was successfully modified.

| | |
|:---|:---|
|Message Format|"The account was successfully modified."
|Severity|OK
|Resolution|No resolution is required.

### Base.1.1.AccountNotModified
Indicates that the modification requested for the account was not successful.

| | |
|:---|:---|
|Message Format|"The account modification request failed."
|Severity|Warning
|Resolution|The modification may have failed due to permission issues or issues with the request body.

### Base.1.1.AccountRemoved
Indicates that the account was successfully removed.

| | |
|:---|:---|
|Message Format|"The account was successfully removed."
|Severity|OK
|Resolution|No resolution is required.

### Base.1.1.ActionNotSupported
Indicates that the action supplied with the POST operation is not supported by the resource.

| | |
|:---|:---|
|Message Format|"The action %1 is not supported by the resource."
|Severity|Critical
|Resolution|The action supplied cannot be resubmitted to the implementation.  Perhaps the action was invalid, the wrong resource was the target or the implementation documentation may be of assistance.

### Base.1.1.ActionParameterDuplicate
Indicates that the action was supplied with a duplicated parameter in the request body.

| | |
|:---|:---|
|Message Format|"The action %1 was submitted with more than one value for the parameter %2."
|Severity|Warning
|Resolution|Resubmit the action with only one instance of the parameter in the request body if the operation failed.

### Base.1.1.ActionParameterMissing
Indicates that the action requested was missing a parameter that is required to process the action.

| | |
|:---|:---|
|Message Format|"The action %1 requires the parameter %2 to be present in the request body."
|Severity|Critical
|Resolution|Supply the action with the required parameter in the request body when the request is resubmitted.

### Base.1.1.ActionParameterNotSupported
Indicates that the parameter supplied for the action is not supported on the resource.

| | |
|:---|:---|
|Message Format|"The parameter %1 for the action %2 is not supported on the target resource."
|Severity|Warning
|Resolution|Remove the parameter supplied and resubmit the request if the operation failed.

### Base.1.1.ActionParameterUnknown
Indicates that an action was submitted but a parameter supplied did not match any of the known parameters.

| | |
|:---|:---|
|Message Format|"The action %1 was submitted with the invalid parameter %2."
|Severity|Warning
|Resolution|Correct the invalid parameter and resubmit the request if the operation failed.

### Base.1.1.ActionParameterValueFormatError
Indicates that a parameter was given the correct value type but the value of that parameter was not supported.  This includes value size/length exceeded.

| | |
|:---|:---|
|Message Format|"The value %1 for the parameter %2 in the action %3 is of a different format than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the parameter in the request body and resubmit the request if the operation failed.

### Base.1.1.ActionParameterValueTypeError
Indicates that a parameter was given the wrong value type, such as when a number is supplied for a parameter that requires a string.

| | |
|:---|:---|
|Message Format|"The value %1 for the parameter %2 in the action %3 is of a different type than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the parameter in the request body and resubmit the request if the operation failed.

### Base.1.1.CouldNotEstablishConnection
Indicates that the attempt to access the resource/file/image at the URI was unsuccessful because a session could not be established.

| | |
|:---|:---|
|Message Format|"The service failed to establish a connection with the URI %1."
|Severity|Critical
|Resolution|Ensure that the URI contains a valid and reachable node name, protocol information and other URI components.

### Base.1.1.CreateFailedMissingReqProperties
Indicates that a create was attempted on a resource but that properties that are required for the create operation were missing from the request.

| | |
|:---|:---|
|Message Format|"The create operation failed because the required property %1 was missing from the request."
|Severity|Critical
|Resolution|Correct the body to include the required property with a valid value and resubmit the request if the operation failed.

### Base.1.1.CreateLimitReachedForResource
Indicates that no more resources can be created on the resource as it has reached its create limit.

| | |
|:---|:---|
|Message Format|"The create operation failed because the resource has reached the limit of possible resources."
|Severity|Critical
|Resolution|Either delete resources and resubmit the request if the operation failed or do not resubmit the request.

### Base.1.1.Created
Indicates that all conditions of a successful creation operation have been met.

| | |
|:---|:---|
|Message Format|"The resource has been created successfully"
|Severity|OK
|Resolution|None

### Base.1.1.EventSubscriptionLimitExceeded
Indicates that a event subscription establishment has been requested but the operation failed due to the number of simultaneous connection exceeding the limit of the implementation.

| | |
|:---|:---|
|Message Format|"The event subscription failed due to the number of simultaneous subscriptions exceeding the limit of the implementation."
|Severity|Critical
|Resolution|Reduce the number of other subscriptions before trying to establish the event subscription or increase the limit of simultaneous subscriptions (if supported).

### Base.1.1.GeneralError
Indicates that a general error has occurred.

| | |
|:---|:---|
|Message Format|"A general error has occurred. See ExtendedInfo for more information."
|Severity|Critical
|Resolution|See ExtendedInfo for more information.

### Base.1.1.InsufficientPrivilege
Indicates that the credentials associated with the established session do not have sufficient privileges for the requested operation

| | |
|:---|:---|
|Message Format|"There are insufficient privileges for the account or credentials associated with the current session to perform the requested operation."
|Severity|Critical
|Resolution|Either abandon the operation or change the associated access rights and resubmit the request if the operation failed.

### Base.1.1.InternalError
Indicates that the request failed for an unknown internal error but that the service is still operational.

| | |
|:---|:---|
|Message Format|"The request failed due to an internal service error.  The service is still operational."
|Severity|Critical
|Resolution|Resubmit the request.  If the problem persists, consider resetting the service.

### Base.1.1.InvalidIndex
The Index is not valid.

| | |
|:---|:---|
|Message Format|"The Index %1 is not a valid offset into the array."
|Severity|Warning
|Resolution|Verify the index value provided is within the bounds of the array.

### Base.1.1.InvalidObject
Indicates that the object in question is invalid according to the implementation.  Examples include a firmware update malformed URI.

| | |
|:---|:---|
|Message Format|"The object at %1 is invalid."
|Severity|Critical
|Resolution|Either the object is malformed or the URI is not correct.  Correct the condition and resubmit the request if it failed.

### Base.1.1.MalformedJSON
Indicates that the request body was malformed JSON.  Could be duplicate, syntax error,etc.

| | |
|:---|:---|
|Message Format|"The request body submitted was malformed JSON and could not be parsed by the receiving service."
|Severity|Critical
|Resolution|Ensure that the request body is valid JSON and resubmit the request.

### Base.1.1.NoValidSession
Indicates that the operation failed because a valid session is required in order to access any resources.

| | |
|:---|:---|
|Message Format|"There is no valid session established with the implementation."
|Severity|Critical
|Resolution|Establish as session before attempting any operations.

### Base.1.1.PropertyDuplicate
Indicates that a duplicate property was included in the request body.

| | |
|:---|:---|
|Message Format|"The property %1 was duplicated in the request."
|Severity|Warning
|Resolution|Remove the duplicate property from the request body and resubmit the request if the operation failed.

### Base.1.1.PropertyMissing
Indicates that a required property was not supplied as part of the request.

| | |
|:---|:---|
|Message Format|"The property %1 is a required property and must be included in the request."
|Severity|Warning
|Resolution|Ensure that the property is in the request body and has a valid value and resubmit the request if the operation failed.

### Base.1.1.PropertyNotWritable
Indicates that a property was given a value in the request body, but the property is a readonly property.

| | |
|:---|:---|
|Message Format|"The property %1 is a read only property and cannot be assigned a value."
|Severity|Warning
|Resolution|Remove the property from the request body and resubmit the request if the operation failed.

### Base.1.1.PropertyUnknown
Indicates that an unknown property was included in the request body.

| | |
|:---|:---|
|Message Format|"The property %1 is not in the list of valid properties for the resource."
|Severity|Warning
|Resolution|Remove the unknown property from the request body and resubmit the request if the operation failed.

### Base.1.1.PropertyValueFormatError
Indicates that a property was given the correct value type but the value of that property was not supported.  This includes value size/length exceeded.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is of a different format than the property can accept."
|Severity|Warning
|Resolution|Correct the value for the property in the request body and resubmit the request if the operation failed.

### Base.1.1.PropertyValueModified
Indicates that a property was given the correct value type but the value of that property was modified.  Examples are truncated or rounded values.

| | |
|:---|:---|
|Message Format|"The property %1 was assigned the value %2 due to modification by the service."
|Severity|Warning
|Resolution|No resolution is required.

### Base.1.1.PropertyValueNotInList
Indicates that a property was given the correct value type but the value of that property was not supported.  This values not in an enumeration

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is not in the list of acceptable values."
|Severity|Warning
|Resolution|Choose a value from the enumeration list that the implementation can support and resubmit the request if the operation failed.

### Base.1.1.PropertyValueTypeError
Indicates that a property was given the wrong value type, such as when a number is supplied for a property that requires a string.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is of a different type than the property can accept."
|Severity|Warning
|Resolution|Correct the value for the property in the request body and resubmit the request if the operation failed.

### Base.1.1.QueryNotSupported
Indicates that query is not supported on the implementation.

| | |
|:---|:---|
|Message Format|"Querying is not supported by the implementation."
|Severity|Warning
|Resolution|Remove the query parameters and resubmit the request if the operation failed.

### Base.1.1.QueryNotSupportedOnResource
Indicates that query is not supported on the given resource, such as when a start/count query is attempted on a resource that is not a collection.

| | |
|:---|:---|
|Message Format|"Querying is not supported on the requested resource."
|Severity|Warning
|Resolution|Remove the query parameters and resubmit the request if the operation failed.

### Base.1.1.QueryParameterOutOfRange
Indicates that a query parameter was supplied that is out of range for the given resource.  This can happen with values that are too low or beyond that possible for the supplied resource, such as when a page is requested that is beyond the last page.

| | |
|:---|:---|
|Message Format|"The value %1 for the query parameter %2 is out of range %3."
|Severity|Warning
|Resolution|Reduce the value for the query parameter to a value that is within range, such as a start or count value that is within bounds of the number of resources in a collection or a page that is within the range of valid pages.

### Base.1.1.QueryParameterValueFormatError
Indicates that a query parameter was given the correct value type but the value of that parameter was not supported.  This includes value size/length exceeded.

| | |
|:---|:---|
|Message Format|"The value %1 for the parameter %2 is of a different format than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the query parameter in the request and resubmit the request if the operation failed.

### Base.1.1.QueryParameterValueTypeError
Indicates that a query parameter was given the wrong value type, such as when a number is supplied for a query parameter that requires a string.

| | |
|:---|:---|
|Message Format|"The value %1 for the query parameter %2 is of a different type than the parameter can accept."
|Severity|Warning
|Resolution|Correct the value for the query parameter in the request and resubmit the request if the operation failed.

### Base.1.1.ResourceAlreadyExists
Indicates that a resource change or creation was attempted but that the operation cannot proceed because the resource already exists.

| | |
|:---|:---|
|Message Format|"The requested resource already exists."
|Severity|Critical
|Resolution|Do not repeat the create operation as the resource has already been created.

### Base.1.1.ResourceAtUriInUnknownFormat
Indicates that the URI was valid but the resource or image at that URI was in a format not supported by the service.

| | |
|:---|:---|
|Message Format|"The resource at %1 is in a format not recognized by the service."
|Severity|Critical
|Resolution|Place an image or resource or file that is recognized by the service at the URI.

### Base.1.1.ResourceAtUriUnauthorized
Indicates that the attempt to access the resource/file/image at the URI was unauthorized.

| | |
|:---|:---|
|Message Format|"While accessing the resource at %1, the service received an authorization error %2."
|Severity|Critical
|Resolution|Ensure that the appropriate access is provided for the service in order for it to access the URI.

### Base.1.1.ResourceCannotBeDeleted
Indicates that a delete operation was attempted on a resource that cannot be deleted.

| | |
|:---|:---|
|Message Format|"The delete request failed because the resource requested cannot be deleted."
|Severity|Critical
|Resolution|Do not attempt to delete a non-deletable resource.

### Base.1.1.ResourceInStandby
Indicates that the request could not be performed because the resource is in standby.

| | |
|:---|:---|
|Message Format|"The request could not be performed because the resource is in standby."
|Severity|Critical
|Resolution|Ensure that the resource is in the correct power state and resubmit the request.

### Base.1.1.ResourceInUse
Indicates that a change was requested to a resource but the change was rejected due to the resource being in use or transition.

| | |
|:---|:---|
|Message Format|"The change to the requested resource failed because the resource is in use or in transition."
|Severity|Warning
|Resolution|Remove the condition and resubmit the request if the operation failed.

### Base.1.1.ResourceMissingAtURI
Indicates that the operation expected an image or other resource at the provided URI but none was found.  Examples of this are in requests that require URIs like Firmware Update.

| | |
|:---|:---|
|Message Format|"The resource at the URI %1 was not found."
|Severity|Critical
|Resolution|Place a valid resource at the URI or correct the URI and resubmit the request.

### Base.1.1.ServiceInUnknownState
Indicates that the operation failed because the service is in an unknown state and cannot accept additional requests.

| | |
|:---|:---|
|Message Format|"The operation failed because the service is in an unknown state and can no longer take incoming requests."
|Severity|Critical
|Resolution|Restart the service and resubmit the request if the operation failed.

### Base.1.1.ServiceShuttingDown
Indicates that the operation failed as the service is shutting down, such as when the service reboots.

| | |
|:---|:---|
|Message Format|"The operation failed because the service is shutting down and can no longer take incoming requests."
|Severity|Critical
|Resolution|When the service becomes available, resubmit the request if the operation failed.

### Base.1.1.ServiceTemporarilyUnavailable
Indicates the service is temporarily unavailable.

| | |
|:---|:---|
|Message Format|"The service is temporarily unavailable.  Retry in %1 seconds."
|Severity|Critical
|Resolution|Wait for the indicated retry duration and retry the operation.

### Base.1.1.SessionLimitExceeded
Indicates that a session establishment has been requested but the operation failed due to the number of simultaneous sessions exceeding the limit of the implementation.

| | |
|:---|:---|
|Message Format|"The session establishment failed due to the number of simultaneous sessions exceeding the limit of the implementation."
|Severity|Critical
|Resolution|Reduce the number of other sessions before trying to establish the session or increase the limit of simultaneous sessions (if supported).

### Base.1.1.SourceDoesNotSupportProtocol
Indicates that while attempting to access, connect to or transfer a resource/file/image from another location that the other end of the connection did not support the protocol

| | |
|:---|:---|
|Message Format|"The other end of the connection at %1 does not support the specified protocol %2."
|Severity|Critical
|Resolution|Change protocols or URIs. 

### Base.1.1.Success
Indicates that all conditions of a successful operation have been met.

| | |
|:---|:---|
|Message Format|"Successfully Completed Request"
|Severity|OK
|Resolution|None

### Base.1.1.UnrecognizedRequestBody
Indicates that the service encountered an unrecognizable request body that could not even be interpreted as malformed JSON.

| | |
|:---|:---|
|Message Format|"The service detected a malformed request body that it was unable to interpret."
|Severity|Warning
|Resolution|Correct the request body and resubmit the request if it failed.

### HpeBiosMessageRegistry.1.0.MessagesMaxSizeExceeded
Indicates that the last configuration change attempted by the user resulted in a number of error messages that exceeded the maximum storage capacity alloted for messages corresponding to this resource.

| | |
|:---|:---|
|Message Format|"The messages array has been truncated because the last configuration change resulted in too many error messages."
|Severity|Warning
|Resolution|Inspect the last configuration change request for issues that may be generating errors, compare the request against the resource's schema, then retry the configuration change.

### HpeBiosMessageRegistry.1.0.UnsupportedAMPConfiguration
Indicates that the user provided Advanced Memory Protection (AMP) option is not appropriate for this memory configuration, as the underlying hardware does not support it.

| | |
|:---|:---|
|Message Format|"Underlying hardware does not support the requested AMP configuration, the settings are invalid."
|Severity|Warning
|Resolution|Ensure that the current memory configuration meets the requirements of the requested value before applying the settings.

### HpeBiosMessageRegistry.1.0.UnsupportedDramRaplValue
Indicates that the user provided Running Average Power Limit (RAPL) value could not be applied due to inherent DRAM power limitation. The value may be out of bounds or invalid.

| | |
|:---|:---|
|Message Format|"Underlying DRAM does not support the requested value."
|Severity|Warning
|Resolution|Ensure that the requested value is within the supported bounds before applying the settings.

### HpeBiosMessageRegistry.1.0.UnsupportedProcessorRaplValue
Indicates that the user provided Running Average Power Limit (RAPL) value could not be applied due to inherent processor power limitation. The value may be out of bounds or invalid.

| | |
|:---|:---|
|Message Format|"Underlying processor does not support the requested value."
|Severity|Warning
|Resolution|Ensure that the processor supports the requested value and that it is within the supported bounds before applying the settings.

### HpeCommon.1.0.ArrayPropertyOutOfBound
The items in the array exceed the maximum  number supported.

| | |
|:---|:---|
|Message Format|"An array %1 was supplied with %2 items that exceeds the maximum supported count of %3."
|Severity|Warning
|Resolution|Retry the operation using the correct number of items for the array.

### HpeCommon.1.0.ConditionalSuccess
A property value was successfully changed but the change may be reverted upon system reset.

| | |
|:---|:---|
|Message Format|"The property %1 was successfully changed to %2, but the change may be reverted upon system reset."
|Severity|Warning
|Resolution|Check the "SettingsResult" messages after the system has reset for errors referring to the corresponding property.

### HpeCommon.1.0.InternalErrorWithParam
The operation was not successful due to an internal service error (shown), but the service is still operational.

| | |
|:---|:---|
|Message Format|"The operation was not successful due to an internal service error (%1), but the service is still operational."
|Severity|Critical
|Resolution|Retry the operation. If the problem persists, consider resetting the service.

### HpeCommon.1.0.InvalidConfigurationSpecified
The specified configuration is not valid.

| | |
|:---|:---|
|Message Format|"The specified configuration is not valid."
|Severity|Warning
|Resolution|Correct the configuration, and then retry the operation.

### HpeCommon.1.0.PropertyValueExceedsMaxLength
The value for the property exceeds the maximum length.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 exceeds the maximum length of %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeCommon.1.0.PropertyValueIncompatible
The value for the property is the correct type, but this value is incompatible with the current value of another property.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is incompatible with the value for property %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeCommon.1.0.PropertyValueOutOfRange
The value for the property is out of range.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is out of range %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeCommon.1.0.ResetInProgress
A device or service reset is in progress.

| | |
|:---|:---|
|Message Format|"A reset on %1 is in progress."
|Severity|Warning
|Resolution|Wait for device or service reset to complete, and then retry the operation.

### HpeCommon.1.0.ResetRequired
One or more properties were changed, but these changes will not take effect until the device or service is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed, but these changes will not take effect until %1 is reset."
|Severity|Warning
|Resolution|To enable the changed properties, reset the device or service.

### HpeCommon.1.0.ResourceNotReadyRetry
The resource is present but is not ready to perform operations due to an internal condition such as initialization or reset.

| | |
|:---|:---|
|Message Format|"The resource is present but is not ready to perform operations.  The resource will be ready in %1 seconds."
|Severity|Warning
|Resolution|Retry the operation when the resource is ready.

### HpeCommon.1.0.SuccessFeedback
The operation completed successfully

| | |
|:---|:---|
|Message Format|"The operation completed successfully"
|Severity|OK
|Resolution|None

### HpeCommon.1.0.TaskCreated
A task was created in response to the operation.

| | |
|:---|:---|
|Message Format|"A task was created in response to the operation and is accessible at %1."
|Severity|OK
|Resolution|Perform an HTTP GET request on the supplied URI for task status.

### HpeCommon.1.0.UnsupportedHwConfiguration
A previously requested property value change was reverted because the current hardware configuration does not support it.

| | |
|:---|:---|
|Message Format|"The value %1 for property %2 was reverted because the current hardware configuration does not support it."
|Severity|Warning
|Resolution|Ensure that the system's hardware configuration supports the property value.

### SmartStorageMessages.2.0.AddEditableDataDriveFailed
Indicates that the data drive was not added due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: data drive %1 not added to logical drive with ID "%2" due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.AddEditableSpareDriveFailed
Indicates that the spare drive was not added due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: spare drive %1 not added to logical drive with ID "%2" due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveArrayHasFailedSpareDrive
Indicates that the spare drive cannot be added to the array because the array has failed spare drive(s).

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has at least one failed spare drive"
|Severity|Critical
|Resolution|Remove all failed spare drives from the array.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveArrayHasNoDataDrives
Indicates that the spare drive cannot be added to the array because the array has no data drives assigned.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has no data drives assign"
|Severity|Critical
|Resolution|Assign data drives to the array.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveArrayStatusNotOK
Indicates that the spare drive cannot be added to the array because the array status is not OK.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array status is not OK"
|Severity|Critical
|Resolution|Check status messages on the array for more information.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveCannotChangeSpareType
Indicates that the spare drive cannot be added to the array because the spare type does not match.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the spare type does not match"
|Severity|Critical
|Resolution|Correct the spare type to match the array.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveCannotMixDriveTypes
Indicates that the spare drive cannot be added to the array because its drive type does not match that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because its drive type does not match that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveDriveAlreadyUsedAsSpare
Indicates that the spare drive cannot be added because the requested spare drive is already configured as a spare.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the requested spare drive is already configured as a spare"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveDriveIsNotConfigurable
Indicates that the spare drive cannot be added to the array because the selected drive is not configurable.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because it is not configurable"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveDriveIsNotUnassigned
Indicates that the spare drive cannot be added to the array because the selected drive is not unassigned.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because it is not unassigned"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveDriveIsNotUnassignedOrShareableStandby
Indicates that the spare drive cannot be added to the array because the requested drive is not available.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the requested drive is not available"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveIncompatibleBlockSize
Indicates that the spare drive cannot be added to the array because its block size is not compatible with that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because its block size is not compatible with that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveInvalidSAM
Indicates that the spare drive cannot be added to the array because spare activation mode must be set to predictive to assign spare drives to RAID 0 volumes.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the logical drive is RAID 0 and the spare activation mode is set to failure"
|Severity|Critical
|Resolution|Change the spare activation mode.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveInvalidSpareType
Indicates that the spare drive cannot be added to the array because the desired spare type is invalid.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has an invalid spare type"
|Severity|Critical
|Resolution|Correct the spare type of the array.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveMaxSpareDriveCountReached
Indicates that the spare drive cannot be added to the array because the maximum number of spare drives has been reached.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the maximum number of spare drives has been reached"
|Severity|Critical
|Resolution|Remove one or more spare drive(s).

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveNoSpareTypeSet
Indicates that the spare drive cannot be added to the array because the array has no spare type set.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because the array has no spare type set"
|Severity|Critical
|Resolution|Specify the spare type.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveNotAllowed
Indicates that adding a spare drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot add spare drive %1 to logical drive with ID "%2" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveTooSmall
Indicates that the spare drive cannot be added to the array because the selected drive is too small.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2" because it is too small"
|Severity|Critical
|Resolution|Select a larger physical drive.

### SmartStorageMessages.2.0.CanAddEditableArraySpareDriveUnknownError
Indicates that the spare drive cannot be added to the array for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot add spare drive %1 to logical drive with ID "%2""
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanAddEditableDataDriveArrayContainsUnsavedLogicalDrives
Indicates that the data drive cannot be added to the array because the array has unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Internal error: cannot add data drive %1 to logical drive with ID "%2" because the array has unlocked logical drives"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanAddEditableDataDriveCannotMixDriveTypes
Indicates that the data drive cannot be added to the array because its drive type does not match that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because its drive type does not match that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableDataDriveDriveIsNotConfigurable
Indicates that the data drive cannot be added to the array because the selected drive is not configurable.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because it is not configurable"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableDataDriveDriveIsNotUnassigned
Indicates that the data drive cannot be added to the array because the selected drive is not unassigned.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because it is not unassigned"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableDataDriveIncompatibleBlockSize
Indicates that the data drive cannot be added to the array because its block size is not compatible with that of the array.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because its block size is not compatible with that of the array"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanAddEditableDataDriveMaxDataDriveCountReached
Indicates that the data drive cannot be added to the array because the maximum number of physical drives on the array has been reached.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2" because the maximum number of physical drives on the array has been reached"
|Severity|Critical
|Resolution|Remove one or more physical drive(s) from the array.

### SmartStorageMessages.2.0.CanAddEditableDataDriveNotAllowed
Indicates that adding a data drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot add data drive %1 to logical drive with ID "%2" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanAddEditableDataDriveUnknownError
Indicates that the data drive cannot be added to the array for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot add data drive %1 to logical drive with ID "%2""
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeAlreadySet
Indicates that desired boot volume is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target is already set as a boot volume"
|Severity|Critical
|Resolution|No actions required.

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeInvalidBootVolumeNumber
Indicates that the controller boot volume cannot be set because target device is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target device is invalid"
|Severity|Critical
|Resolution|Target a valid device for the boot volume.

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeInvalidBootVolumeType
Indicates that the controller boot volume cannot be set because the boot volume type is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the boot volume type is invalid"
|Severity|Critical
|Resolution|Correct the boot volume type.

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeInvalidLogicalBootVolume
Indicates that the controller boot volume cannot be set because the target logical drive is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target logical drive is invalid"
|Severity|Critical
|Resolution|Resolution

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeInvalidPhysicalBootVolume
Indicates that the controller boot volume cannot be set because the target physical drive is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the target physical drive is invalid"
|Severity|Critical
|Resolution|Resolution

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeInvalidPrecedence
Indicates that the desired boot volume priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the boot volume priority is invalid"
|Severity|Critical
|Resolution|Correct the boot volume priority.

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeNotAllowed
Indicates that setting the boot volume is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeOperationUnsupported
Indicates that the controller does not support setting boot volumes.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1 because the controller does not support setting boot volumes"
|Severity|Critical
|Resolution|Do not modify the controller boot volume.

### SmartStorageMessages.2.0.CanChangeEditableControllerBootVolumeUnknownError
Indicates that the controller boot volume cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller boot volume to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerDPOInvalidValue
Indicates that the controller degraded performance optimization cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller degraded performance optimization.

### SmartStorageMessages.2.0.CanChangeEditableControllerDPONoChange
Indicates that the desired controller degraded performance optimization is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerDPONoLogicalDrives
Indicates that the controller degraded performance optimization cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerDPONotSupported
Indicates that the controller degraded performance optimization cannot be set because the feature is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1 because the controller does not support the feature"
|Severity|Critical
|Resolution|Do not modify the degraded performance optimization.

### SmartStorageMessages.2.0.CanChangeEditableControllerDPOUnknownError
Indicates that the controller degraded performance optimization cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller degraded performance optimization to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerDriveWriteCacheModeInvalidMode
Indicates that the controller drive write cache mode cannot be set because the desired drive write cache mode is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the drive write cache mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerDriveWriteCacheModeNoChange
Indicates that the desired controller drive write cache mode is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerDriveWriteCacheModeNoLogicalDrives
Indicates that the controller drive write cache mode cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerDriveWriteCacheModeNotSupported
Indicates that the controller drive write cache mode cannot be changed because the operation is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1 because it is not supported"
|Severity|Critical
|Resolution|Do not modify the controller drive write cache mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerDriveWriteCacheModeUnknownError
Indicates that the controller drive write cache mode cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller drive write cache mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerElevatorSortInvalidValue
Indicates that the controller elevator sort cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller elevator sort.

### SmartStorageMessages.2.0.CanChangeEditableControllerElevatorSortNoChange
Indicates that the desired controller elevator sort is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerElevatorSortNoLogicalDrives
Indicates that the controller elevator sort cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerElevatorSortUnknownError
Indicates that the controller elevator sort cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller elevator sort to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerEncryptionHasEncryptedVolumes
Indicates that the encryption configuration cannot be set because encrypted logical drives exist.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because encrypted logical drives exist"
|Severity|Critical
|Resolution|Delete all encrypted logical drives.

### SmartStorageMessages.2.0.CanChangeEditableControllerEncryptionInHBAMode
Indicates that the encryption configuration cannot be set because the controller is currently in or pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because the controller is currently in or pending HBA mode"
|Severity|Critical
|Resolution|Set the controller or connector mode to mixed or RAID mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerEncryptionInvalidValue
Indicates that the desired encryption configuration is invalid.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the encryption configuration.

### SmartStorageMessages.2.0.CanChangeEditableControllerEncryptionNoChange
Indicates that the desired encryption configuration is already set.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because it is already set"
|Severity|Critical
|Resolution|Resolution

### SmartStorageMessages.2.0.CanChangeEditableControllerEncryptionNotAllowed
Indicates that setting the encryption configuration is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because it is invalid"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanChangeEditableControllerEncryptionOperationUnsupported
Indicates that encryption is not supported on the controller.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1 because encryption is not supported on the controller"
|Severity|Critical
|Resolution|Do not modify the encryption configuration.

### SmartStorageMessages.2.0.CanChangeEditableControllerEncryptionUnknownError
Indicates that the encryption configuration cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change encryption configuration to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerExpandPriorityInvalidValue
Indicates that the controller expand priority cannot be set because the desired expand priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the expand priority.

### SmartStorageMessages.2.0.CanChangeEditableControllerExpandPriorityNoChange
Indicates that the desired controller expand priority is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerExpandPriorityNoLogicalDrives
Indicates that the controller expand priority cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerExpandPriorityUnknownError
Indicates that the controller expand priority cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller expand priority to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerFLSInvalidValue
Indicates that the controller flexible latency scheduler cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the flexible latency scheduler.

### SmartStorageMessages.2.0.CanChangeEditableControllerFLSNoChange
Indicates that the desired controller flexible latency scheduler is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerFLSNoLogicalDrives
Indicates that the controller flexible latency scheduler cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerFLSUnknownError
Indicates that the controller flexible latency scheduler cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller flexible latency scheduler to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerIRPInvalidValue
Indicates that the controller inconsistency repair policy cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller inconsistency repair policy.

### SmartStorageMessages.2.0.CanChangeEditableControllerIRPNoChange
Indicates that the desired controller inconsistency repair policy is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerIRPNoLogicalDrives
Indicates that the controller inconsistency repair policy cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerIRPUnknownError
Indicates that the controller inconsistency repair policy cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerIRPUnsupported
Indicates that the controller does not support changing the inconsistency repair policy.

| | |
|:---|:---|
|Message Format|"Cannot set controller inconsistency repair policy to %1 because it is unsupported"
|Severity|Critical
|Resolution|Do not modify the inconsistency repair policy.

### SmartStorageMessages.2.0.CanChangeEditableControllerMNPDelayInvalidValue
Indicates that the controller monitor and performance delay cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the monitor and performance delay.

### SmartStorageMessages.2.0.CanChangeEditableControllerMNPDelayNoChange
Indicates that the desired controller monitor and performance delay is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerMNPDelayNoLogicalDrives
Indicates that the controller monitor and performance delay cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerMNPDelayUnknownError
Indicates that the controller monitor and performance delay cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller monitor and performance delay to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCControllerCacheInactive
Indicates that the controller no battery write cache cannot be set because the controller cache is inactive.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because the controller cache is inactive"
|Severity|Critical
|Resolution|Activate the controller cache.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCInHBAMode
Indicates that the controller no battery write cache cannot be set because the controller is currently in or pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because the controller is currently in or pending HBA mode"
|Severity|Critical
|Resolution|Set the controller or connector mode to mixed or RAID mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCInvalidValue
Indicates that the controller no battery write cache cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the no battery write cache.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCNoCachePresent
Indicates that the controller no battery write cache cannot be set because there is no cache board present.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because there is no cache board present"
|Severity|Critical
|Resolution|Attach a cache board.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCNoChange
Indicates that the desired controller no battery write cache is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCNoLogicalDrives
Indicates that the controller no battery write cache cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCOperationUnsupported
Indicates that the controller does not support changing the no battery write cache.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1 because it is unsupported"
|Severity|Critical
|Resolution|Do not modify the no battery write cache.

### SmartStorageMessages.2.0.CanChangeEditableControllerNBWCUnknownError
Indicates that the controller no battery write cache cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller no battery write cache to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerPSSCountNoChange
Indicates that desired controller parallel surface scan count is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerPSSCountNoLogicalDrives
Indicates that the controller parallel surface scan count cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerPSSCountOperationUnsupported
Indicates that the controller does not support parallel surface scan.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because parallel surface scan is not supported"
|Severity|Critical
|Resolution|Do not modify the parallel surface scan count.

### SmartStorageMessages.2.0.CanChangeEditableControllerPSSCountOutOfRange
Indicates that the controller parallel surface scan count cannot be set because the desired value is out of range.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1 because it is out of range"
|Severity|Critical
|Resolution|Correct the parallel surface scan count.

### SmartStorageMessages.2.0.CanChangeEditableControllerPSSCountUnknownError
Indicates that the controller parallel surface scan count cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller parallel surface scan count to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerQueueDepthInvalidValue
Indicates that the controller queue depth cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller queue depth.

### SmartStorageMessages.2.0.CanChangeEditableControllerQueueDepthNoChange
Indicates that the desired controller queue depth is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerQueueDepthNoLogicalDrives
Indicates that the controller queue depth cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerQueueDepthUnknownError
Indicates that the controller queue depth cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller queue depth to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentBadPowerSource
Indicates that the controller read cache percent cannot be set because the backup power source is not charged or not present.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because the backup power source is not charged or not present"
|Severity|Critical
|Resolution|Attach a backup power source or allow it to charge fully.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentControllerCacheInactive
Indicates that the controller read cache percent cannot be set because the controller cache is inactive.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because the controller cache is inactive"
|Severity|Critical
|Resolution|Activate the controller cache.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentInHBAMode
Indicates that the controller read cache percent cannot be set because the controller is currently in or pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because the controller is currently in or pending HBA mode"
|Severity|Critical
|Resolution|Set the controller or connector mode to mixed or RAID mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentInvalidValue
Indicates that the controller read cache percent cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the read cache percent.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentNoCachePresent
Indicates that the controller read cache percent cannot be set because there is no cache board present.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because there is no cache board present"
|Severity|Critical
|Resolution|Attach a cache board.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentNoChange
Indicates that the desired controller read cache percent is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentNoLogicalDrives
Indicates that the controller read cache percent cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerReadCachePercentUnknownError
Indicates that the controller read cache percent cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller read cache percent to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerRebuildPriorityInvalidValue
Indicates that the controller rebuild priority cannot be set because the desired rebuild priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the rebuild priority.

### SmartStorageMessages.2.0.CanChangeEditableControllerRebuildPriorityNoChange
Indicates that the desired controller rebuild priority is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerRebuildPriorityNoLogicalDrives
Indicates that the controller rebuild priority cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerRebuildPriorityRapidUnsupported
Indicates that the controller does not support rapid rebuild.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1 because it is not supported on this controller"
|Severity|Critical
|Resolution|Select a non-rapid rebuild priority.

### SmartStorageMessages.2.0.CanChangeEditableControllerRebuildPriorityUnknownError
Indicates that the controller rebuild priority cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller rebuild priority to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerSAMArrayHasActiveSpare
Indicates that the controller spare activation mode cannot be set to predictive because a RAID 0 logical drive with an active spare exists.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because a RAID 0 logical drive with an active spare exists"
|Severity|Critical
|Resolution|Delete the RAID 0 logical drive, remove the active spare, or select a different controller spare activation mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerSAMArrayHasAutoReplaceSpare
Indicates that the controller spare activation mode cannot be set to failure because a RAID 0 logical drive with an auto-replace spare exists.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because a RAID 0 logical drive with an auto-replace spare exists"
|Severity|Critical
|Resolution|Delete the RAID 0 logical drive, remove the auto-replace spare, or select a different controller spare activation mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerSAMArrayIsTransforming
Indicates that the controller spare activation mode cannot be set because the array is transforming.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because the array is transforming"
|Severity|Critical
|Resolution|Resubmit the request when the array finishes transforming.

### SmartStorageMessages.2.0.CanChangeEditableControllerSAMNoLogicalDrives
Indicates that the controller spare activation mode cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerSAMSelectedModeActive
Indicates that the desired controller spare activation mode is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerSAMUnknownError
Indicates that the controller spare activation mode cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerSAMUnsupportedMode
Indicates that the controller spare activation mode is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller spare activation mode to %1 because it is not supported"
|Severity|Critical
|Resolution|Select a different spare activation mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerSSAPriorityInvalidValue
Indicates that the controller surface scan analysis priority cannot be set because the desired surface scan analysis priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the surface scan analysis priority.

### SmartStorageMessages.2.0.CanChangeEditableControllerSSAPriorityNoChange
Indicates that the desired controller surface scan analysis priority is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerSSAPriorityNoLogicalDrives
Indicates that the controller surface scan analysis priority cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerSSAPriorityUnknownError
Indicates that the controller surface scan analysis priority cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller surface scan analysis priority to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerSurvivalPowerModeInvalidValue
Indicates that the desired controller survival mode is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the controller survival mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerSurvivalPowerModeNoChange
Indicates that the desired survival mode is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerSurvivalPowerModeNotConfigurable
Indicates that the controller survival mode cannot be set because the controller does not support survival mode configuration.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because survival mode configuration is not supported on the controller"
|Severity|Critical
|Resolution|Do not modify the survival mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerSurvivalPowerModeOperationUnsupported
Indicates that the controller survival mode cannot be set because the controller does not support survival mode.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1 because survival mode is not supported on the controller"
|Severity|Critical
|Resolution|Do not modify the survival mode.

### SmartStorageMessages.2.0.CanChangeEditableControllerSurvivalPowerModeUnknownError
Indicates that the controller survival mode cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller survival mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanChangeEditableControllerWCBTInvalidValue
Indicates that the desired controller write cache bypass threshold is invalid.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because it is invalid"
|Severity|Critical
|Resolution|Correct the write cache bypass threshold.

### SmartStorageMessages.2.0.CanChangeEditableControllerWCBTNoChange
Indicates that desired write cache bypass threshold is already set.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanChangeEditableControllerWCBTNoLogicalDrives
Indicates that the controller write cache bypass threshold cannot be set because no logical drives are configured.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because no logical drives are configured"
|Severity|Critical
|Resolution|Configure a logical drive.

### SmartStorageMessages.2.0.CanChangeEditableControllerWCBTOperationUnsupported
Indicates that the controller write cache bypass threshold is not supported.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1 because it is not supported"
|Severity|Critical
|Resolution|Do not modify the write cache bypass threshold.

### SmartStorageMessages.2.0.CanChangeEditableControllerWCBTUnknownError
Indicates that the controller write cache bypass threshold cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot set controller write cache bypass threshold to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanClearEditableControllerBootVolumeInvalidPrecedence
Indicates that the the boot volume cannot be cleared because the boot volume priority is invalid.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because the boot volume priority is invalid"
|Severity|Critical
|Resolution|Correct the boot volume priority.

### SmartStorageMessages.2.0.CanClearEditableControllerBootVolumeNotAllowed
Indicates that clearing the controller boot volume is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanClearEditableControllerBootVolumeNotSet
Indicates that the boot volume cannot be cleared because no boot volume is set.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because no boot volume is set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanClearEditableControllerBootVolumeOperationUnsupported
Indicates that clearing the boot volume is not suppported on the controller.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume because it is not supported on the controller"
|Severity|Critical
|Resolution|Do not clear the controller boot volume.

### SmartStorageMessages.2.0.CanClearEditableControllerBootVolumeUnknownError
Indicates that the controller boot volume cannot be cleared for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot clear controller %1 boot volume"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanCommitEditableConfigurationNoChangesToCommit
Indicates that the editable configuration was not committed because there are no editable changes to commit.

| | |
|:---|:---|
|Message Format|"Internal error: cannot commit the editable configuration because no changes were made"
|Severity|Warning
|Resolution|Modify the editable configuration.

### SmartStorageMessages.2.0.CanCommitEditableConfigurationOutOfSync
Indicates that an external change occured which invalidates the editable configuration.

| | |
|:---|:---|
|Message Format|"Cannot commit the editable configuration"
|Severity|Critical
|Resolution|Recreate and re-submit the configuration request.

### SmartStorageMessages.2.0.CanCommitEditableConfigurationUnknownError
Indicates that an editable configuration cannot be committed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot commit the editable configuration"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanCommitEditableConfigurationUnlockedLogicalDrivesExist
Indicates that the editable configuration was not committed because there are unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Internal error: cannot commit the editable configuration because unlocked logical drives exist"
|Severity|Critical
|Resolution|Lock all logical drives.

### SmartStorageMessages.2.0.CanCreateEditableArrayCreatesNotAllowed
Indicates that creating arrays is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot create logical drive with ID "%1" because array creation is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanCreateEditableArrayMaxLDCountReached
Indicates that the array cannot be created because the maximum number of logical drives on the controller has been reached.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the maximum number of logical drives on the controller has been reached"
|Severity|Critical
|Resolution|Delete one or more logical drive(s).

### SmartStorageMessages.2.0.CanCreateEditableArrayNoUnassignedDrivesAvailable
Indicates that the array cannot be created because no unassigned drives are available.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the controller has no unassigned drives available"
|Severity|Critical
|Resolution|Delete an existing array or add more physical drives.

### SmartStorageMessages.2.0.CanCreateEditableArrayUnknownError
Indicates that the array cannot be created for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanCreateEditableConfigControllerStatusNotOK
Indicates that an editable configuration was not created because the status of the controller is not in an OK state.

| | |
|:---|:---|
|Message Format|"Cannot create an editable configuration because the controller status is not OK"
|Severity|Critical
|Resolution|Check status messages on the controller for more information.

### SmartStorageMessages.2.0.CanCreateEditableConfigEditableConfigExists
Indicates that an editable configuration was not created because an editable configuration already being edited.

| | |
|:---|:---|
|Message Format|"Internal error: cannot create an editable configuration because an editable configuration already exists"
|Severity|Critical
|Resolution|Delete the existing editable configuration.

### SmartStorageMessages.2.0.CanCreateEditableConfigInconsistentPortSettings
Indicates that an editable configuration was not created because the controller's port settings do not match.

| | |
|:---|:---|
|Message Format|"Cannot create an editable configuration because the port modes on the controller are in a conflicting state"
|Severity|Critical
|Resolution|Make the port settings consistent in the request and resubmit.

### SmartStorageMessages.2.0.CanCreateEditableConfigUnknownError
Indicates that an editable configuration cannot be created for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot create an editable configuration"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanCreateEditableLogicalDriveControllerNotOK
Indicates that the logical drive cannot be created because the controller status is not OK.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the controller status is not OK"
|Severity|Critical
|Resolution|Check status messages on the controller for more information.

### SmartStorageMessages.2.0.CanCreateEditableLogicalDriveMaxLDReached
Indicates that the logical drive cannot be created because the maximum number of logical drives on the controller has been reached.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the maximum number of logical drives on the controller has been reached"
|Severity|Critical
|Resolution|Delete on or more logical drive(s).

### SmartStorageMessages.2.0.CanCreateEditableLogicalDriveNoFreeSpaceAvailable
Indicates that the logical drive cannot be created because the array has no free space available.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1" because the array has no free space available"
|Severity|Critical
|Resolution|Delete one or more logical drive(s) from the array.

### SmartStorageMessages.2.0.CanCreateEditableLogicalDriveNotAllowed
Indicates that creating logical drives is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot create logical drive with ID "%1" because logical drive creation is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanCreateEditableLogicalDriveUnknownError
Indicates that the logical drive cannot be created for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot create logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanDeleteEditableArrayContainsUnsavedLogicalDrives
Indicates that the array cannot be deleted because the array contains unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1" because unlocked logical drives exist"
|Severity|Critical
|Resolution|Lock all logical drives on the array.

### SmartStorageMessages.2.0.CanDeleteEditableArrayNotAllowed
Indicates that deleting an array is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot delete logical drive with ID "%1" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanDeleteEditableArrayUnknownError
Indicates that the array size cannot be deleted for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanDeleteEditableLogicalDriveIsLocked
Indicates that the logical drive cannot be deleted because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1" because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### SmartStorageMessages.2.0.CanDeleteEditableLogicalDriveNotAllowed
Indicates that deleting the logical drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot delete logical drive with ID "%1" because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanDeleteEditableLogicalDriveNotLastLDInArray
Indicates that the logical drive cannot be deleted because the logical drive is not the last logical drive on the array.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1" because the logical drive is not the last logical drive on the array"
|Severity|Critical
|Resolution|Delete the last logical drive on the array first.

### SmartStorageMessages.2.0.CanDeleteEditableLogicalDriveUnknownError
Indicates that the logical drive size cannot be deleted for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot delete logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanEnableErasedPhysicalDriveRestrictedSanitize
Indicates that the physical drive cannot be enabled because of a restricted, failed sanitize erase.

| | |
|:---|:---|
|Message Format|"Physical drive %1 was not enabled because it is currently in a restricted, failed sanitize state"
|Severity|Critical
|Resolution|Restart the sanitize erase on the physical drive.

### SmartStorageMessages.2.0.CanErasePhysicalDriveIsErasing
Indicates that the physical drive cannot be erased because the drive is currently erasing.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is currently erasing"
|Severity|Critical
|Resolution|Wait for the physical drive erase to complete.

### SmartStorageMessages.2.0.CanErasePhysicalDriveIsFailed
Indicates that the physical drive cannot be erased because the drive is failed.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is failed"
|Severity|Critical
|Resolution|Check the state of the drive.

### SmartStorageMessages.2.0.CanErasePhysicalDriveIsHBA
Indicates that the physical drive cannot be erased because the drive is exposed to the operating system.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is exposed to the operating system"
|Severity|Critical
|Resolution|Change the controller or connector to RAID mode to mask the drive from the operating system.

### SmartStorageMessages.2.0.CanErasePhysicalDriveNotAllowed
Indicates that the physical drive erase is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drives at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanErasePhysicalDriveNotUnassigned
Indicates that the physical drive cannot be erased because it is not unassigned.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 because the drive is not unassigned"
|Severity|Critical
|Resolution|Unassign the physical drive.

### SmartStorageMessages.2.0.CanErasePhysicalDrivePatternNotSupported
Indicates that the desired erase pattern is not supported on the target drive.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1 using pattern %2 because the drive does not support the erase pattern"
|Severity|Critical
|Resolution|Select a different erase pattern.

### SmartStorageMessages.2.0.CanErasePhysicalDriveUnknownError
Indicates that the physical drive cannot be erased for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot erase physical drive %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanLockEditableLogicalDriveAlreadyLocked
Indicates that the logical drive cannot be locked because it is already locked.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because it is already locked"
|Severity|Critical
|Resolution|No action.

### SmartStorageMessages.2.0.CanLockEditableLogicalDriveNoArraySet
Indicates that the logical drive cannot be locked because it is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because it is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### SmartStorageMessages.2.0.CanLockEditableLogicalDriveNoRAIDLevelSet
Indicates that the logical drive cannot be locked because the RAID level is not set.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because the logical drive RAID level is not set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### SmartStorageMessages.2.0.CanLockEditableLogicalDriveNoSizeSet
Indicates that the logical drive cannot be locked because the size is not set.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because the logical drive size is not set"
|Severity|Critical
|Resolution|Set the logical drive size.

### SmartStorageMessages.2.0.CanLockEditableLogicalDriveNoStripSizeSet
Indicates that the logical drive cannot be locked because the strip size is not set.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1" because the logical drive strip size is not set"
|Severity|Critical
|Resolution|Set the logical drive strip size.

### SmartStorageMessages.2.0.CanLockEditableLogicalDriveUnknownError
Indicates that the logical drive cannot be locked for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot lock logical drive with ID "%1""
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorAlreadySet
Indicates that the desired logical drive accelerator is already set.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorArrayUsesIOBypass
Indicates that IOBypass is already set as the logical drive accelerator.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is already set"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorDriveTypeNotSSD
Indicates that IOBypass is only supported on SSD arrays.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is only supported on SSD arrays"
|Severity|Critical
|Resolution|Select a different logical drive accelerator for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorLogicalDriveNotCreated
Indicates that the logical drive accelerator cannot be set because the target logical drive does not exist.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because the logical drive does not exist"
|Severity|Critical
|Resolution|Create the logical drive first.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorNoArraySet
Indicates that the logical drive accelerator cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorNotAllowed
Indicates that setting the logical drive accelerator is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorNotTheFirstLDInArray
Indicates that the logical drive accelerator cannot be set because the logical drive is not the first logical drive of the array.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because the logical drive is not the first logical drive of the array"
|Severity|Critical
|Resolution|Delete the last logical drive in the array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorUnknownError
Indicates that the logical drive accelerator cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveAcceleratorUnsupported
Indicates that the logical drive accelerator cannot be set because the desired logical drive accelerator is unsupported.

| | |
|:---|:---|
|Message Format|"Logical drive accelerator for logical drive with ID "%1" cannot be set to %2 because it is not supported"
|Severity|Critical
|Resolution|Do not modify the logical drive accelerator.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayArrayHasNoDataDrives
Indicates that the logical drive cannot be assigned to the array because the array has no data drives.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array has no data drives"
|Severity|Critical
|Resolution|Add data drives to the array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayArrayStatusNotOK
Indicates that the logical drive cannot be assigned to the array because the array status is not OK.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array status is not OK"
|Severity|Critical
|Resolution|Check status messages on the array for more information.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayChangeArrayNotAllowed
Indicates that changing the array assignment of the logical drive is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot change the array assignment of logical drive with ID "%1" because it is not allowed at this time"
|Severity|Critical
|Resolution|Do not assign the logical drive to a different array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayHasUnlockedLD
Indicates that the logical drive cannot be assigned to the array because the array has unlocked logical drives.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "1" to the array because the array has unlocked logical drives"
|Severity|Critical
|Resolution|Lock all existing logical drives on the array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayLogicalDriveIsLocked
Indicates that the logical drive cannot be assigned to the array because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayNoSpaceAvailableOnArray
Indicates that the logical drive cannot be assigned to the array because the array has no available space.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array has no available space"
|Severity|Critical
|Resolution|Free up space on the array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayNotAllowed
Indicates that assigning the logical drive to the array is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot assign logical drive with ID "%1" to an array because it is not allowed at this time"
|Severity|Critical
|Resolution|Resolution

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayNotDataArray
Indicates that the logical drive cannot be assigned to the array because the array is not a data array.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array because the array is not a data array"
|Severity|Critical
|Resolution|Assign the logical drive to a different array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveArrayUnknownError
Indicates that the logical drive cannot be assigned to the array for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot assign logical drive with ID "%1" to the array"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodDriveTypeNotSSD
Indicates that the logical drive initialization method cannot be set for a non-SSD logical drive.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is not on an SSD array"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodLDIsLocked
Indicates that the logical drive initialization method cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodNoArraySet
Indicates that the logical drive initialization method cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodNoRAIDLevelSet
Indicates that the logical drive initialization method cannot be set because the logical drive has no RAID level set.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive has no RAID level set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodNotAllowed
Indicates that setting the logical drive initialization method is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: setting the logical drive initialization method is not allowed for logical drive with ID "%1" at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodNotFirstLDInArray
Indicates that the logical drive initialization method cannot be set for the logical drive because the logical drive is not the first in the array.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because the logical drive is not the first logical drive in the array"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodNotRequiredForRAID
Indicates that rapid parity initialization is not valid for the RAID level of the logical drive.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because it is not valid for the RAID level of the logical drive"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodOPONotSupported
Indicates that the controller does not support over provisioning optimization.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because it is not supported by the controller"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodRPINotSupported
Indicates that the controller does not support rapid parity initialization.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2 because it is not supported by the controller"
|Severity|Critical
|Resolution|Set a different logical drive initialization method for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveInitializationMethodUnknownError
Indicates that the logical drive initialization method cannot be set for the logical drive for an unknown reason.

| | |
|:---|:---|
|Message Format|"Initialization method for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveLabelInvalidCharacter
Indicates that the logical drive label cannot be set because an invalid character was found in the logical drive label.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because an invalid character was found in the logical drive label"
|Severity|Critical
|Resolution|Remove invalid characters from the logical drive label.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveLabelInvalidLabel
Indicates that the logical drive label cannot be set because the logical drive label is invalid.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive label is invalid"
|Severity|Critical
|Resolution|Correct the logical drive label.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveLabelInvalidLogicalDrive
Indicates that the logical drive label cannot be set because the target logical drive is invalid.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the target logical drive is invalid"
|Severity|Critical
|Resolution|Target a different logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveLabelLabelTooLong
Indicates that the logical drive label cannot be set because the logical drive label is too long.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive label is too long"
|Severity|Critical
|Resolution|Decrease the length of the logical drive label.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveLabelLogicalDriveIsLocked
Indicates that the logical drive label cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveLabelNoArraySet
Indicates that the logical drive label cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveLabelUnknownError
Indicates that the logical drive label cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Label for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelFullStripeSizeOverflow
Indicates that the logical drive RAID level cannot be set because it will cause the stripe size of the logical drive to exceed the maximum safe value.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because it will cause the stripe size of the logical drive to exceed the maximum safe value"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelInvalidRAIDLevel
Indicates that the logical drive RAID level cannot be set because the desired RAID level is invalid.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the desired RAID level is invalid"
|Severity|Critical
|Resolution|Correct the RAID level of the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelLogicalDriveIsLocked
Indicates that the logical drive RAID level cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelNoArraySet
Indicates that the logical drive RAID level cannot be set because the logical drive has not been assigned to an array.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the logical drive has not been assigned to an arra"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelNotAllowed
Indicates that setting the logical drive RAID level is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: cannot set RAID level for logical drive with ID "%1" to %2 at this time because it is not allowed"
|Severity|Critical
|Resolution|Resubmit the request

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelNotEnoughFreeSpaceForRAID
Indicates that the logical drive RAID level cannot be set because there is not enough available free space on the array.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the array does not have enough available free space"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelUnknownError
Indicates that the logical drive RAID level cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelUnsupportedDriveCount
Indicates that the logical drive RAID level cannot be set because the number of drives assigned to the array is not supported by the desired RAID level.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the number of drives assigned to the array is not supported by the desired RAID level"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveRAIDLevelUnsupportedRAIDLevel
Indicates that the logical drive RAID level cannot be set because the desired RAID level is not supported on the controller.

| | |
|:---|:---|
|Message Format|"RAID level for logical drive with ID "%1" cannot be set to %2 because the desired RAID level is not supported on the controller"
|Severity|Critical
|Resolution|Select a different RAID level for the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeInvalidSizeType
Indicates that the logical drive size cannot be set because the units given for the size is invalid.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the units give for the size is invalid"
|Severity|Critical
|Resolution|Correct the size of the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeLogicalDriveIsLocked
Indicates that the logical drive size cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeNoArraySet
Indicates that the logical drive size cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeNoRAIDLevelSet
Indicates that the logical drive size cannot be set because the logical drive RAID level is not set.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive RAID level is not set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeNoStripSizeSet
Indicates that the logical drive size cannot be set because the logical drive strip size is not set.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive strip size is not set"
|Severity|Critical
|Resolution|Set the logical drive strip size.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeNotAllowed
Indicates that setting the logical drive size is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Internal error: size for logical drive with ID "%1" cannot be set to %2 GiB because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeRequestedSizeTooLarge
Indicates that the logical drive size cannot be set because the logical drive size is too large.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive size is too large"
|Severity|Critical
|Resolution|Decrease the logical drive size.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeRequestedSizeTooSmall
Indicates that the logical drive size cannot be set because the logical drive size is too small.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB because the logical drive size is too small"
|Severity|Critical
|Resolution|Increase the logical drive size.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveSizeUnknownError
Indicates that the logical drive size cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Size for logical drive with ID "%1" cannot be set to %2 GiB"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveStripSizeInvalidValue
Indicates that the logical drive strip size cannot be set because the desired value is invalid.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the value is invalid"
|Severity|Critical
|Resolution|Correct the value of the logical drive strip size.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveStripSizeLogicalDriveIsLocked
Indicates that the logical drive strip size cannot be set because the logical drive is locked.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the logical drive is locked"
|Severity|Critical
|Resolution|Unlock the logical drive.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveStripSizeNoArraySet
Indicates that the logical drive stirp size cannot be set because the logical drive is not assigned to an array.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the logical drive is not assigned to an array"
|Severity|Critical
|Resolution|Assign the logical drive to an array.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveStripSizeNoRAIDLevelSet
Indicates that the logical drive strip size cannot be set because the RAID level is not set.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the logical drive RAID level is not set"
|Severity|Critical
|Resolution|Set the logical drive RAID level.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveStripSizeNotAllowed
Indicates that setting the logical drive strip size is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because it is not allowed at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveStripSizeUnknownError
Indicates that the logical drive strip size cannot be set for an unknown reason.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanSetEditableLogicalDriveStripSizeValueOutOfRange
Indicates that the logical drive strip size cannot be set because the desired value is out of range.

| | |
|:---|:---|
|Message Format|"Strip size for logical drive with ID "%1" cannot be set to %2 bytes because the value is out of range"
|Severity|Critical
|Resolution|Correct the value of the logical drive strip size.

### SmartStorageMessages.2.0.CanStopEnableErasedPhysicalDriveUnknownError
Indicates that the physical drive cannot be enabled for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot enable physical drive %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.CanStopErasePhysicalDriveNotErasing
Indicates that the physical drive was not enabled because it is not erasing.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not enabled because drive is not erasing"
|Severity|Warning
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.CanStopErasePhysicalDriveSanitizing
Indicates that the physical drive cannot be enabled because it is currently sanitizing.

| | |
|:---|:---|
|Message Format|"Physical drive %1 was not enabled because it is currently undergoing a sanitize erase"
|Severity|Critical
|Resolution|Resubmit the request at a later time.

### SmartStorageMessages.2.0.ChangeConnectorModeConnectorNotFound
Indicates that the connector mode was not changed because the connector was not found.

| | |
|:---|:---|
|Message Format|"Internal error: connector mode not changed because connector at index %1 not found"
|Severity|Critical
|Resolution|Select a valid connector.

### SmartStorageMessages.2.0.ChangeConnectorModeFailed
Indicates that the connector was not changed to the desired mode due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: not changed connector %1 to %2 mode due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeConnectorModeLogicalDrivesExist
Indicates that the connector mode cannot be changed because the connector has configured logical drives.

| | |
|:---|:---|
|Message Format|"Connector %1 cannot be changed to %2 because the connector has configured logical drives"
|Severity|Critical
|Resolution|Delete the configured logical drives.

### SmartStorageMessages.2.0.ChangeConnectorModeSelectedModePending
Indicates that the desired connector mode is already pending a reboot.

| | |
|:---|:---|
|Message Format|"Connector %1 is already set to %2 and is pending a reboot"
|Severity|Critical
|Resolution|Reboot the system to apply the pending connector mode.

### SmartStorageMessages.2.0.ChangeConnectorModeUnknownError
Indicates that the connector mode cannot be changed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change connector %1 to %2 mode"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.ChangeConnectorModeUnsupportedMode
Indicates that the desired connector mode is invalid or unsupported.

| | |
|:---|:---|
|Message Format|"Connector %1 could not be set to %1 because it is an invalid/unsupported value"
|Severity|Critical
|Resolution|Correct the value of the connector mode.

### SmartStorageMessages.2.0.ChangeConnectorModeUnsupportedOperation
Indicates that changing the connector mode is not supported on the connector.

| | |
|:---|:---|
|Message Format|"The connector mode for connector %1 cannot be changed because the connector does not support changing connector modes"
|Severity|Critical
|Resolution|Remove the connector mode property from the request.

### SmartStorageMessages.2.0.ChangeControllerModeEncryptionIsEnabled
Indicates that the controller mode cannot be changed because encryption is enabled.

| | |
|:---|:---|
|Message Format|"The controller mode cannot be changed to %1 because the controller has encryption enabled"
|Severity|Critical
|Resolution|Disable encryption on the controller.

### SmartStorageMessages.2.0.ChangeControllerModeFailed
Indicates that the controller was not changed to the desired mode due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: not changed controller mode to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeControllerModeLogicalDrivesExist
Indicates that the controller mode cannot be changed because the controller has configured logical drives.

| | |
|:---|:---|
|Message Format|"The controller mode cannot be changed to %1 because the controller has configured logical drives"
|Severity|Critical
|Resolution|Delete the configured logical drives.

### SmartStorageMessages.2.0.ChangeControllerModeSelectedModePending
Indicates that the desired controller mode is already pending a reboot.

| | |
|:---|:---|
|Message Format|"The controller mode is already set to %1 and is pending a reboot"
|Severity|Critical
|Resolution|Reboot the system to apply the pending controller mode.

### SmartStorageMessages.2.0.ChangeControllerModeUnknownError
Indicates that the controller mode cannot be changed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change controller mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.ChangeControllerModeUnsupportedMode
Indicates that the desired controller mode is invalid or unsupported.

| | |
|:---|:---|
|Message Format|"%1 is an invalid/unsupported value for the controller mode"
|Severity|Critical
|Resolution|Correct the value of the controller mode.

### SmartStorageMessages.2.0.ChangeControllerModeUnsupportedOperation
Indicates that changing the controller mode is not supported on controller.

| | |
|:---|:---|
|Message Format|"Changing the controller mode is not supported on this controller"
|Severity|Critical
|Resolution|Remove the controller mode property from the request.

### SmartStorageMessages.2.0.ChangeEditableControllerBootVolumeConflict
Indicates that multiple drives have been requested as a boot volume.

| | |
|:---|:---|
|Message Format|"Device %1 and device %2 cannot both be set as the %3 boot volume"
|Severity|Critical
|Resolution|Select only one device as a boot volume.

### SmartStorageMessages.2.0.ChangeEditableControllerBootVolumeFailed
Indicates that the controller boot volume was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: cannot set controller %1 boot volume due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerDPOFailed
Indicates that the controller degraded performance optimization was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller degraded performance optimization not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerDriveWriteCacheModeFailed
Indicates that the controller drive write cache mode was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller drive write cache mode not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerElevatorSortFailed
Indicates that the controller elevator sort was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller elevator sort not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerEncryptionFailed
Indicates that the controller encryption configuration was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller encryption configuration not set to %1 due toi an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerExpandPriorityFailed
Indicates that the controller expand priority was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller expand priority not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerFLSFailed
Indicates that the controller flexible latency scheduler was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller flexible latency scheduler not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerIRPFailed
Indicates that the controller inconsistency repair policy was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller inconsistency repair policy not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerMNPDelayFailed
Indicates that the controller monitor and performance delay was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller monitor and performance delay not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerNBWCFailed
Indicates that the controller no battery write cache was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller no battery write cache not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerPSSCountFailed
Indicates that the controller parallel surface scan count was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller parallel surface scan count not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerQueueDepthFailed
Indicates that the controller queue depth was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller queue depth not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerReadCachePercentFailed
Indicates that the controller read cache percent was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller read cache percent not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerRebuildPriorityFailed
Indicates that the controller rebuild priority was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller rebuild priority not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerSAMFailed
Indicates that the controller spare activation mode was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller spare activation mode not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerSSAPriorityFailed
Indicates that the controller surface scan analysis priority was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller surface scan analysis priority not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerSurvivalPowerModeFailed
Indicates that the controller survival mode was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller survival mode not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangeEditableControllerWCBTFailed
Indicates that the controller write cache bypass threshold was not set due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: controller write cache bypass threshold not set to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangePowerModeFailed
Indicates that the power mode was not changed to maximum due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: power mode not changed to %1 due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ChangePowerModeSelectedModePending
Indicates that the desired power mode is already pending a reboot.

| | |
|:---|:---|
|Message Format|"The power mode is already set to %1 and is pending a reboot"
|Severity|Critical
|Resolution|Reboot the system to apply the pending power mode.

### SmartStorageMessages.2.0.ChangePowerModeUnknownError
Indicates that the power mode cannot be changed for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot change power mode to %1"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.ChangePowerModeUnsupportedMode
Indicates that the desired power mode is invalid or unsupported.

| | |
|:---|:---|
|Message Format|"%1 is an invalid/unsupported value for the power mode"
|Severity|Critical
|Resolution|Correct the value of the power mode.

### SmartStorageMessages.2.0.ClearConfigurationClearPhysicalDriveCCMEncryptionLocked
Indicates that the controller configuration metadata on the physical drive cannot be cleared because encryption is enabled.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because the controller has encryption enabled"
|Severity|Critical
|Resolution|Disabled encryption on the controller.

### SmartStorageMessages.2.0.ClearConfigurationClearPhysicalDriveCCMNoCCM
Indicates that the controller configuration metadata on physical drives cannot be cleared because no physical drives drives contain configuration metadata.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because no physical drives contain configuration metadata"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.ClearConfigurationClearPhysicalDriveCCMNoDrivesAttached
Indicates that the controller configuration metadata on physical drives cannot be cleared because the controller has no physical drives attached.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because the controller has no physical drives attached"
|Severity|Critical
|Resolution|No action required.

### SmartStorageMessages.2.0.ClearConfigurationClearPhysicalDriveCCMNotAllowed
Indicates that clearing the controller configuration metadata on physical drives is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot clear the controller configuration metadata on physical drives at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ClearConfigurationClearPhysicalDriveCCMNotSupported
Indicates that clearing the controller configuration metadata on physical drives is not supported on this controller.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives because it is not supported by the controller"
|Severity|Critical
|Resolution|Do not attempt to clear the controller configuration metadata from the physical drive.

### SmartStorageMessages.2.0.ClearConfigurationClearPhysicalDriveCCMUnknownError
Indicates that the controller configuration metadata on physical drives cannot be cleared for an unknown reason.

| | |
|:---|:---|
|Message Format|"Cannot clear controller configuration metadata from physical drives"
|Severity|Critical
|Resolution|No resolution available.

### SmartStorageMessages.2.0.ClearEditableControllerBootVolumeFailed
Indicates that the controller boot volume was not cleared due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: cannot clear controller %1 boot volume due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CommitEditableConfigurationFailed
Indicates that the editable configuration was not committed because of an unknown reason.

| | |
|:---|:---|
|Message Format|"Internal error: editable configuration not committed"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CreateEditableArrayFailed
Indicates that the array was not created due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not created due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CreateEditableConfigFailed
Indicates that the editable configuration was not created due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: editable configuration not created due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.CreateEditableLogicalDriveFailed
Indicates that the logical drive was not created due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not created due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.DataDriveNotFound
Indicates that the requested data drive was not found.

| | |
|:---|:---|
|Message Format|"Data drive %1 for logical drive with ID "%2" was not found"
|Severity|Critical
|Resolution|Modify the requested data drive list.

### SmartStorageMessages.2.0.DataDriveSetNotFound
Indicates that the requested data drive set was not found.

| | |
|:---|:---|
|Message Format|"Data drive set with desired parameters for logical drive with ID "%1" was not found"
|Severity|Critical
|Resolution|Modify the requested data drive set.

### SmartStorageMessages.2.0.DeleteEditableArrayFailed
Indicates that the logical drive was not deleted due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not deleted due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.DeleteEditableLogicalDriveFailed
Indicates that the logical drive was not deleted due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not deleted due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.EnablePhysicalDriveFailed
Indicates that the physical drive was not enabled due to an unknown error.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not enabled due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.EnablePhysicalDriveNotFound
Indicates that the physical drive requested to be enabled was not found.

| | |
|:---|:---|
|Message Format|"Physical drive %1 was not enabled because it is not found"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.ErasePhysicalDriveFailed
Indicates that the physical drive was not erased due to an unknown error.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not erased due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.ErasePhysicalDriveNotFound
Indicates that the physical drive requested for erase was not found.

| | |
|:---|:---|
|Message Format|"Erase not started on physical drive %1 because it is not found"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.InternalError
Indicates that an internal error has occurred.

| | |
|:---|:---|
|Message Format|"Internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.LockEditableLogicalDriveFailed
Indicates that locking the logical drive failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not locked due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.LogicalDriveNotFound
Indicates that the logical drive was not found.

| | |
|:---|:---|
|Message Format|"Logical drive with ID %1 not found"
|Severity|Critical
|Resolution|Select a different logical drive.

### SmartStorageMessages.2.0.LogicalDriveNotFoundWarning
Indicates that the logical drive was not found but is not required to complete the request.

| | |
|:---|:---|
|Message Format|"Logical drive with ID %1 not found"
|Severity|Warning
|Resolution|Select a different logical drive.

### SmartStorageMessages.2.0.LogicalDrivesInPendingHBAMode
Indicates that the logical drives are being requested and the controller is pending HBA mode.

| | |
|:---|:---|
|Message Format|"Cannot process request due to conflicting logical drives and controller pending HBA mode"
|Severity|Critical
|Resolution|Change the controller mode or delete all logical drives.

### SmartStorageMessages.2.0.MalformedJSON
Indicates that the request body was malformed JSON.  Could be duplicate, syntax error, etc.

| | |
|:---|:---|
|Message Format|"The request body submitted was malformed JSON and could not be parsed by the receiving service"
|Severity|Critical
|Resolution|Ensure that the request body is valid JSON and resubmit the request.

### SmartStorageMessages.2.0.NoEditableConfigCreated
Indicates that a configuration has not been created to edit.

| | |
|:---|:---|
|Message Format|"Internal error: no editable configuration has been created"
|Severity|Critical
|Resolution|Create an editable configuration.

### SmartStorageMessages.2.0.PhysicalDriveNotFound
Indicates that the physical drive was not found.

| | |
|:---|:---|
|Message Format|"Physical drive %1 not found"
|Severity|Critical
|Resolution|Select a different physical drive.

### SmartStorageMessages.2.0.PropertyKeyMissing
Indicates that the request is missing a required property.

| | |
|:---|:---|
|Message Format|"Property %1 is missing from the request"
|Severity|Critical
|Resolution|Add the missing property to the request.

### SmartStorageMessages.2.0.PropertyRequiresLogicalDrives
Indicates that the value given for the property requires at least one configured logical drive.

| | |
|:---|:---|
|Message Format|"Setting property %1 requires at least one configured logical drive"
|Severity|Critical
|Resolution|Configure at least one logical drive.

### SmartStorageMessages.2.0.PropertyRequiresMixedModeSupport
Indicates that the value given for the property requires mixed mode support on the controller.

| | |
|:---|:---|
|Message Format|"Setting property %1 requires mixed mode support on the controller"
|Severity|Critical
|Resolution|Remove the property or attempt on a controller that supports mixed mode.

### SmartStorageMessages.2.0.PropertyValueEnumNotInList
Indicates that the desired value is not in the enum list for the property.

| | |
|:---|:---|
|Message Format|"Property %1 does not have enum value %2"
|Severity|Critical
|Resolution|Select a value for the property that is in the enum list.

### SmartStorageMessages.2.0.PropertyValueOutOfRange
Indicates that the property could not be set because the desired value is out of range.

| | |
|:---|:---|
|Message Format|"Property %1 was given value %2 which is out of range for the property"
|Severity|Critical
|Resolution|Correct the value of the property.

### SmartStorageMessages.2.0.PropertyValueTypeError
Indicates that the property could not be set because the value type is incorrect.

| | |
|:---|:---|
|Message Format|"Property %1 was given value %2 which does not match the correct type of the property"
|Severity|Critical
|Resolution|Correct the value of the property.

### SmartStorageMessages.2.0.RebootAndRetryRequired
Indicates that a reboot is required then reapply the configuration.

| | |
|:---|:---|
|Message Format|"Reboot is required then reapply the configuration"
|Severity|Warning
|Resolution|Reboot the system then reapply the configuration.

### SmartStorageMessages.2.0.RebootRequired
Indicates that a reboot is required to apply the configuration.

| | |
|:---|:---|
|Message Format|"Reboot is required to apply the configuration"
|Severity|Warning
|Resolution|Reboot the system to apply the configuration.

### SmartStorageMessages.2.0.ReturnToFactoryNotAllowed
Indicates that reseting the controller to factory settings is not allowed at this time.

| | |
|:---|:---|
|Message Format|"Cannot reset the controller to factory defaults at this time"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SetEditableLogicalDriveAcceleratorFailed
Indicates that setting the logical drive accelerator failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive accelerator for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SetEditableLogicalDriveArrayFailed
Indicates that the logical drive was not assigned to an array due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: logical drive with ID "%1" not assigned to array due to an unknown error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SetEditableLogicalDriveInitializationMethodFailed
Indicates that setting the logical drive initialization method failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: initialization method for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SetEditableLogicalDriveLabelFailed
Indicates that setting the logical drive label failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: label for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SetEditableLogicalDriveRAIDLevelFailed
Indicates that setting the logical drive RAID level failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: RAID level for logical drive with ID "%1" failed to be set to %2 due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SetEditableLogicalDriveSizeFailed
Indicates that setting the logical drive size failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: size for logical drive with ID "%1" failed to be set to %2 GiB due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SetEditableLogicalDriveStripSizeFailed
Indicates that setting the logical drive strip size failed due to an unknown error.

| | |
|:---|:---|
|Message Format|"Internal error: strip size for logical drive with ID "%1" failed to be set to %2 bytes due to an internal error"
|Severity|Critical
|Resolution|Resubmit the request.

### SmartStorageMessages.2.0.SpareDriveNotFound
Indicates that the requested spare drive was not found.

| | |
|:---|:---|
|Message Format|"Spare drive %1 for logical drive with ID "%2" was not found"
|Severity|Critical
|Resolution|Modify the requested spare drive list.

### SmartStorageMessages.2.0.SpareDriveSetNotFound
Indicates that the requested spare drive set was not found.

| | |
|:---|:---|
|Message Format|"Spare drive set with desired parameters for logical drive with ID "%1" was not found"
|Severity|Critical
|Resolution|Modify the requested spare drive set.

### SmartStorageMessages.2.0.Success
Indicates that all conditions of a successful operation have been met.

| | |
|:---|:---|
|Message Format|"Request successfully completed"
|Severity|OK
|Resolution|None.

### HpeWolfram.1.0.Accepted
Indicates that the operation was accepted, but may not be in effect yet.

| | |
|:---|:---|
|Message Format|"Indicates that the operation was accepted, but may not be in effect yet."
|Severity|OK
|Resolution|None

### HpeWolfram.1.0.ActionOnSystemFailed
An action on a Server was initiated, but the operation was not successful.

| | |
|:---|:---|
|Message Format|"The Server action was not successful because of the error returned from the Server."
|Severity|Warning
|Resolution|Check extended error info for details.

### HpeWolfram.1.0.ActionParameterValueNotInList
Indicates that the correct value type was supplied for the action parameter, but the value is not supported. (The value is not in the enumeration list.)

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is not in the list of valid values."
|Severity|Warning
|Resolution|Choose a value from the enumeration list and resubmit the request if the operation failed.

### HpeWolfram.1.0.ActivationError
Device not activated or Invalid Activation Key

| | |
|:---|:---|
|Message Format|"Device not activated or Invalid Activation Key"
|Severity|Warning
|Resolution|Install Activation Key

### HpeWolfram.1.0.AddNodeFailed
Add server failed because the supplied credentials are wrong or the server is not reachable or timeout has occurred for the request or server has unsupported iLO version.

| | |
|:---|:---|
|Message Format|"The login was not successful, credentials are wrong or Timeout has occurred or Server is not reachable or server has unsupported iLO version."
|Severity|Warning
|Resolution|Log in with correct user name and password credentials.Also verify the server has supported iLO Version.

### HpeWolfram.1.0.AddNodeValidationFail
Add server operation failed the validation check for iLO firmware version.

| | |
|:---|:---|
|Message Format|"Adding server failed due to incompatible iLO firmware version"
|Severity|Warning
|Resolution|Check if the iLO firmware version is supported.The supported iLO version is 2.50 and above.

### HpeWolfram.1.0.AutoRefreshStarted
Periodic refresh of all the servers and groups has started

| | |
|:---|:---|
|Message Format|"Periodic refresh of all the servers and groups has started"
|Severity|OK
|Resolution|No action required

### HpeWolfram.1.0.BaselineAlreadyPresent
Cannot create Import Baseline task as the baseline is already imported or another task is importing the same baseline

| | |
|:---|:---|
|Message Format|"The baseline trying to be imported already exists or is being processed."
|Severity|Warning
|Resolution|Delete the existing baseline and try again

### HpeWolfram.1.0.BaselineCannotBeDeleted
The baseline cannot be deleted now.

| | |
|:---|:---|
|Message Format|"The baseline cannot be deleted as the state of baseline import is %s."
|Severity|Critical
|Resolution|Wait for the baseline import to be completed or abort the related task and retry the delete.

### HpeWolfram.1.0.CannotDeleteBaselinesPendingTasks
Baseline cannot be deleted as there are running/pending tasks using this baseline or the baseline is part of some active recovery policy.

| | |
|:---|:---|
|Message Format|"Baseline cannot be deleted as there are running/pending tasks using this baseline or this baseline is part of an active recovery policy."
|Severity|Warning
|Resolution|Wait until the running tasks complete or delete the recovery policy this baseline is part of and retry the operation.

### HpeWolfram.1.0.CannotDownloadAuditLogs
Audit logs cannot be downloaded.

| | |
|:---|:---|
|Message Format|"Audit logs cannot be downloaded beacuse there are no servers added at all."
|Severity|Critical
|Resolution|No action required

### HpeWolfram.1.0.CannotDownloadDebugLogs
Debug logs cannot be downloaded.

| | |
|:---|:---|
|Message Format|"Debug logs cannot be downloaded beacuse there is a download in progress"
|Severity|Critical
|Resolution|No action required

### HpeWolfram.1.0.CertCSRKeyMismatch
Certificate Import Failed, Private/Public Key Mismatch

| | |
|:---|:---|
|Message Format|"Certificate Import Failed due to mismatch of Private/Public key of CSR and Certificate"
|Severity|Warning
|Resolution|Generate a new CSR and Import the certificate

### HpeWolfram.1.0.CertDateTimeMismatch
Certificate Import Failed, Invalid Start or End Date

| | |
|:---|:---|
|Message Format|"Certificate Import Failed as the Certificate has expired or is not yet valid"
|Severity|Warning
|Resolution|Retry importing a certificate with a valid date/time

### HpeWolfram.1.0.CertInvalidCAFormat
Certificate Import Failed, Invalid CA Certificate

| | |
|:---|:---|
|Message Format|"Certificate Import Failed due to Invalid CA Certificate"
|Severity|Warning
|Resolution|Retry importing a certificate with a valid CA Certificate

### HpeWolfram.1.0.CertInvalidX509Format
Certificate Import Failed, Invalid X.509 Format

| | |
|:---|:---|
|Message Format|"Certificate Import Failed due to Invalid X.509 Format"
|Severity|Warning
|Resolution|Retry importing a certificate with a valid X.509 format

### HpeWolfram.1.0.ConfigurationBaselineAlreadyExists
The configuration baseline of the same name already exists.

| | |
|:---|:---|
|Message Format|"The configuration baseline of the same name already exists."
|Severity|Warning
|Resolution|Specify a different configuration baseline name and retry the operation.

### HpeWolfram.1.0.ConfigurationBaselineInUse
The configuration baseline is in use by a recovery policy and cannot be deleted.

| | |
|:---|:---|
|Message Format|"The configuration baseline is in use by a recovery policy and cannot be deleted."
|Severity|Warning
|Resolution|Remove the configuration baseline from the recovery policy and retry the operation.

### HpeWolfram.1.0.ConfigurationBaselineReadOnly
The configuration baseline specified is read only.

| | |
|:---|:---|
|Message Format|"The configuration baseline specified is read only and cannot be created/modified/deleted."
|Severity|Warning
|Resolution|Specify a configuration baseline that is not read only and retry the operation.

### HpeWolfram.1.0.ConfigurationSettingNotFound
The configuration setting was not found in master configuration.

| | |
|:---|:---|
|Message Format|"The configuration setting with name %1 was not found in master configuration."
|Severity|Warning
|Resolution|Specify a different configuration baseline name and retry the operation.

### HpeWolfram.1.0.DeleteGroupFailed
Delete group failed because the group Discovery is in Progress

| | |
|:---|:---|
|Message Format|"Group Discovery is in progress.Hence operations like Delete is not allowed"
|Severity|Warning
|Resolution|Wait for the group discovery to be completed and then try again.

### HpeWolfram.1.0.DeviceResetRequired
Indicates that one or more properties were correctly changed, but will not take effect until device is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until the device is reset."
|Severity|Warning
|Resolution|Reset the device for the settings to take effect.

### HpeWolfram.1.0.DiscoverServersFromCSVInProgress
Discovery of servers from CSV is already in progress.Cannot start a new csv discovery.

| | |
|:---|:---|
|Message Format|"Discovery of servers from CSV is already in progress.Cannot start a new csv discovery."
|Severity|Warning
|Resolution|Wait for the current Discovery of servers from CSV to complete.

### HpeWolfram.1.0.ETagTooLong
The supplied ETag is too long. The maximum supported ETag length is 63 bytes.

| | |
|:---|:---|
|Message Format|"The supplied ETag is too long. The maximum supported ETag length is 63 bytes."
|Severity|Warning
|Resolution|Retry the operation using an ETag with a length of 63 bytes or less.

### HpeWolfram.1.0.EULANotAccepted
EULA for Intelligent Provisioning not accepted and hence OS provisioning could not be started.

| | |
|:---|:---|
|Message Format|"User must accept EULA to start OS Provisioning."
|Severity|Warning
|Resolution|Accept the EULA to start the OS Provisioning Tasks.

### HpeWolfram.1.0.FileExists
File already exists in folder.

| | |
|:---|:---|
|Message Format|"File already exists in folder."
|Severity|Warning
|Resolution|Try another name.

### HpeWolfram.1.0.FileReadFailed
Unable to read file.

| | |
|:---|:---|
|Message Format|"Restore was not successful."
|Severity|Warning
|Resolution|Verify File path

### HpeWolfram.1.0.FileWriteFailed
Unable to write file.

| | |
|:---|:---|
|Message Format|"Backup was not successful."
|Severity|Warning
|Resolution|Verify File path

### HpeWolfram.1.0.FirmwareFlashAlreadyInProgress
A firmware upgrade operation is already in progress.

| | |
|:---|:---|
|Message Format|"A firmware flash operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current firmware flash to complete, and then retry the operation.

### HpeWolfram.1.0.FirmwareUpdateCannotBeInitiated
Firmware Update cannot be initiated because some tasks are in running state.

| | |
|:---|:---|
|Message Format|"Firmware Update cannot be initiated because some tasks are in running state."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.FirmwareUpdateFailed
Firmware Update Failed

| | |
|:---|:---|
|Message Format|"Firmware Update Failed because %1"
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.FirmwareUpdateSuccessful
Firmware Update Successful

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.GatewayNodeFail
Add iLO federation group operation failed due to gateway server not responding or invalid address was given.

| | |
|:---|:---|
|Message Format|"Adding iLO federation group failed due to gateway server not responding."
|Severity|Warning
|Resolution|Verify if the gateway server is powered up and responding.

### HpeWolfram.1.0.GeneratingCertificate
Generating the X.509 Certificate.

| | |
|:---|:---|
|Message Format|"X.509 Certificate is being generated and the process might take up to 10 minutes."
|Severity|OK
|Resolution|None.

### HpeWolfram.1.0.GroupKeyMisMatch
Invalid Group Key Provided.

| | |
|:---|:---|
|Message Format|"Group creation failed since Invalid Group Key Provided."
|Severity|Warning
|Resolution|Specify a Group key that matches and retry the operation.

### HpeWolfram.1.0.GroupNameAlreadyExist
Group Name already Exists

| | |
|:---|:---|
|Message Format|"Group creation failed since the Group Name already Exists."
|Severity|Warning
|Resolution|Specify a Group Name that doesnt exist and retry the operation.

### HpeWolfram.1.0.IPRangeAddInProgress
IP Range Add is already in progress.Cannot start a new range discovery.

| | |
|:---|:---|
|Message Format|"IP Range Add is already in progress.Cannot start a new range discovery until the previous discovery is complete."
|Severity|Warning
|Resolution|Wait for the current IP Range discovery to complete.

### HpeWolfram.1.0.IPv6ConfigurationError
The specified IPv6 configuration caused an error.

| | |
|:---|:---|
|Message Format|"The specified IPv6 configuration was in error due to %1."
|Severity|Warning
|Resolution|Resolve the indicated error in the configuration data.

### HpeWolfram.1.0.IncompatibleBaseline
Recovery policy cannot be created or modified as an incompatible baseline is specified.

| | |
|:---|:---|
|Message Format|"Recovery policy cannot be created or modified as an incompatible baseline is specified. "
|Severity|Warning
|Resolution|Specify a compatible baseline and retry the operation.

### HpeWolfram.1.0.IncompatibleGateway
The specified manager address is incompatible for discovering federation groups.

| | |
|:---|:---|
|Message Format|"The specified manager address is incompatible for discovering federation groups."
|Severity|Warning
|Resolution|Verify if the manager supports federation groups and then retry.

### HpeWolfram.1.0.IncompatibleManagedSystem
The managed system is incompatible for the requested operation.

| | |
|:---|:---|
|Message Format|"The managed system %1 is incompatible for the requested operation."
|Severity|Warning
|Resolution|Specify a system that is compatible for the operation and retry again. Please check the documentation for further details.

### HpeWolfram.1.0.IncorrectFilterQuery
Incorrect filter query format.

| | |
|:---|:---|
|Message Format|"Incorrect filter query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.IncorrectSearchQuery
Incorrect search query parameters given.

| | |
|:---|:---|
|Message Format|"Incorrect search query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.IncorrectSearchQuerySelectMissing
Incorrect search query parameters given.Select query parameter is mandatory for search query.

| | |
|:---|:---|
|Message Format|"Incorrect search query format.Select parameter is mandatory."
|Severity|Warning
|Resolution|Please specify select query parameters to search the given field in.

### HpeWolfram.1.0.IncorrectSelectQuery
Incorrect select query parameters given.

| | |
|:---|:---|
|Message Format|"Incorrect select query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.IncorrectSortQuery
Incorrect sorting order or sorting parameters given.

| | |
|:---|:---|
|Message Format|"Incorrect sorting query format."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.InvalidActivationKey
Invalid Activation Key

| | |
|:---|:---|
|Message Format|"Invalid Activation Key"
|Severity|Warning
|Resolution|Retry Installation with a valid Activation Key

### HpeWolfram.1.0.InvalidFederationGroupName
Specified Federation group name is invalid.

| | |
|:---|:---|
|Message Format|"The specified Federation group name is not valid. The 'DEFAULT' name for Federation group is reserved."
|Severity|Warning
|Resolution|Modify the Federation group name and retry.

### HpeWolfram.1.0.InvalidLicenseKey
The license key is not valid.

| | |
|:---|:---|
|Message Format|"The license key is not valid."
|Severity|Warning
|Resolution|Retry the operation using a valid license key.

### HpeWolfram.1.0.InvalidOperationForSystemState
The operation was not successful due to the current power state (for example, attempting to turn the power off when it is already off).

| | |
|:---|:---|
|Message Format|"The operation was not successful due to the current power state."
|Severity|Warning
|Resolution|Verify that the system is in the correct power state, and then retry the operation.

### HpeWolfram.1.0.InvalidPasswordLength
The password length is not valid.

| | |
|:---|:---|
|Message Format|"A valid password must contain between %1 to %2 characters."
|Severity|Critical
|Resolution|Retry the operation using a corrected password.

### HpeWolfram.1.0.InvalidSelectionForTaskCreation
Creation of tasks are mutually exclusive for federated and non federated nodes.

| | |
|:---|:---|
|Message Format|"Creation of tasks are mutually exclusive for federated and non federated nodes."
|Severity|Warning
|Resolution|Specify either federated or non federated nodes for the action and try again.

### HpeWolfram.1.0.JobNameNotValid
Job Creation Failed due to Bad Job Type 

| | |
|:---|:---|
|Message Format|"Job Creation Failed due to Bad Job Type"
|Severity|Critical
|Resolution|Provide a valid Job Type string

### HpeWolfram.1.0.LDAPGroupAlreadyExist
Specified LDAP group name/DN already exists.

| | |
|:---|:---|
|Message Format|"Specified LDAP group name/DN already exists."
|Severity|Warning
|Resolution|Try a different LDAP group name/DN.

### HpeWolfram.1.0.ManagedSystemNotFound
One or more specified managed systems is not found.

| | |
|:---|:---|
|Message Format|"One or more specified managed systems is not found."
|Severity|Warning
|Resolution|Specify a system managed by the appliance and retry the operation.

### HpeWolfram.1.0.MaxConfigurationBaselineLimit
Limit for maximum number of configuration baselines reached.

| | |
|:---|:---|
|Message Format|"Limit for maximum number of configuration baselines reached."
|Severity|Warning
|Resolution|Delete few configuration baseline and retry the operation.

### HpeWolfram.1.0.MaxRecoveryPolicyLimit
Limit for maximum number of recovery policies reached.

| | |
|:---|:---|
|Message Format|"Limit for maximum number of recovery policies reached."
|Severity|Warning
|Resolution|Delete few recovery policies and retry the operation.

### HpeWolfram.1.0.MaxSessionsCreated
The login was not successful, because the maximum number of allowed sessions have been created.

| | |
|:---|:---|
|Message Format|"The login was not successful, because the maximum number of allowed sessions have been created."
|Severity|Warning
|Resolution|Delete an existing Session and login.

### HpeWolfram.1.0.MembersOfGrpCannotBeDeleted
Delete operation failed because members of a group cannot be deleted.

| | |
|:---|:---|
|Message Format|"Deleting Members of a group failed."
|Severity|Warning
|Resolution|Members of a group cannot be deleted.Only the whole group can be deleted.

### HpeWolfram.1.0.MethodNotAllowed
The specified method for the operation is not allowed.

| | |
|:---|:---|
|Message Format|"The specified method for the operation is not allowed."
|Severity|Warning
|Resolution|Specify a method that is allowed and retry the operation.

### HpeWolfram.1.0.ModifyDefaultCredentials
Modify Credentials of Default User

| | |
|:---|:---|
|Message Format|"Modify Credentials of Default User"
|Severity|Warning
|Resolution|Modify Credentials of Default User

### HpeWolfram.1.0.MountFailed
Mount operation failed.

| | |
|:---|:---|
|Message Format|"Mount operation failed."
|Severity|Warning
|Resolution|If NFS is specified, please make sure the NFS server is reachable. If USB is specified, please make sure the USB is connected to the system.

### HpeWolfram.1.0.MountFailedDetectingCause
Mount operation failed, detecting the cause...

| | |
|:---|:---|
|Message Format|"Mount operation failed."
|Severity|Warning
|Resolution|If NFS is specified, please make sure the NFS server is reachable. If USB is specified, please make sure the USB is connected to the system.

### HpeWolfram.1.0.MountOperationFailed
Mount operation failed for the provided IP.

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|Check issues related to firewall & check if the folder has been mounted properly

### HpeWolfram.1.0.MountSuccess
Mount operation was successful.

| | |
|:---|:---|
|Message Format|"Mount operation was successful."
|Severity|Warning
|Resolution|

### HpeWolfram.1.0.NoRebootRequired
NoRebootRequired.

| | |
|:---|:---|
|Message Format|"NoRebootRequired."
|Severity|Warning
|Resolution|NoRebootRequired.

### HpeWolfram.1.0.NoSamples
No power history samples are available.

| | |
|:---|:---|
|Message Format|"No power history samples are available."
|Severity|OK
|Resolution|To accumulate power history samples, power on the server, and then wait at least 5 minutes.

### HpeWolfram.1.0.NotAcceptable
Indicates that one of the values in the request headears are not accpetable.

| | |
|:---|:---|
|Message Format|"Indicates that one of the values in the request headears are not accpetable."
|Severity|Critical
|Resolution|Provide proper values in the request header and try the operation again.

### HpeWolfram.1.0.NotValidIPAddrOrDNS
The value for the property is not a valid IPv4/v6 address or DNS name.

| | |
|:---|:---|
|Message Format|"The value for property %1 is not a valid IPv4/v6 address or DNS name."
|Severity|Warning
|Resolution|Correct the IPv4/v6 address or DNS name, and then retry the operation.

### HpeWolfram.1.0.NotValidIPAddress
The value for the property is not a valid IP address.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid IP address for %2"
|Severity|Warning
|Resolution|Use a valid IP address.

### HpeWolfram.1.0.NotValidSubnetMask
The value for the property is not a valid subnet mask.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid subnet mask for %2"
|Severity|Warning
|Resolution|Use a valid subnet mask.

### HpeWolfram.1.0.PreConditionFailed
Indicates that one of the precondition for the operation failed.

| | |
|:---|:---|
|Message Format|"Indicates that one of the precondition for the operation failed."
|Severity|Critical
|Resolution|Provide the proper precondition and try the operation again.

### HpeWolfram.1.0.PropertyLengthLessThanMinLength
The length for the property is less than the minimum length.

| | |
|:---|:---|
|Message Format|"The length of %1 for the property %2 is less than the minimum length of %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### HpeWolfram.1.0.PropertyValueBadParam
The property value is not valid.

| | |
|:---|:---|
|Message Format|"The property value is not valid."
|Severity|Warning
|Resolution|Retry the operation using a corrected value.

### HpeWolfram.1.0.PropertyValueRequired
Indicates that a property was required but not specified.

| | |
|:---|:---|
|Message Format|"%1 requires Property %2 to be specified."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### HpeWolfram.1.0.RecoveryPolicyAlreadyExists
A recovery policy of the same name already exists.

| | |
|:---|:---|
|Message Format|"A recovery policy of the same name already exists."
|Severity|Warning
|Resolution|Specify a different recovery policy name and retry the operation.

### HpeWolfram.1.0.RecoveryPolicyInUse
The recovery policy is currently assigned to managed servers. Hence the policy cannot be deleted.

| | |
|:---|:---|
|Message Format|"The recovery policy is currently assigned to managed servers. Hence the policy cannot be deleted."
|Severity|Warning
|Resolution|Unassign the policy from the managed servers before trying to delete.

### HpeWolfram.1.0.RequiredPropertyMissing
Indicates that a required property is not specified.

| | |
|:---|:---|
|Message Format|"Required Property %1 needs to be specifed."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### HpeWolfram.1.0.ResourceBeingFlashed
The change to the requested resource failed because the resource is being flashed.

| | |
|:---|:---|
|Message Format|"The change to the requested resource failed because the resource is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### HpeWolfram.1.0.ResourceInUseWithDetail
The change could not be made because the resource was in use or in a transitioning state.

| | |
|:---|:---|
|Message Format|"The change to the resource failed because the resource is in use or in transition."
|Severity|Warning
|Resolution|Retry the request.

### HpeWolfram.1.0.ResourceTemporarilyUnavailable
The resource is temporarily unavailable because the firmware is being flashed.

| | |
|:---|:---|
|Message Format|"The resource is temporarily unavailable because the firmware is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### HpeWolfram.1.0.RestoreFailed
Restore was not successful.

| | |
|:---|:---|
|Message Format|"Restore was not successful."
|Severity|Warning
|Resolution|Verify Password

### HpeWolfram.1.0.RestoreFileNotFound
Restore Failed, File not found

| | |
|:---|:---|
|Message Format|"Restore Failed as the specified file is not found"
|Severity|Warning
|Resolution|Specify a valid backup file and retry the operation.

### HpeWolfram.1.0.SystemResetRequired
The system properties were correctly changed, but will not take effect until the system is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until system is reset."
|Severity|Warning
|Resolution|Reset system for the settings to take effect.

### HpeWolfram.1.0.TaskCannotBeAborted
Task cannot be aborted at this time

| | |
|:---|:---|
|Message Format|"Task cannot be aborted completely at this time"
|Severity|Warning
|Resolution|Task cannot be aborted at this time, wait for the task to be completed.

### HpeWolfram.1.0.TaskCannotBeContinued
Task cannot be Continued at this time

| | |
|:---|:---|
|Message Format|"Task cannot be Continued at this time"
|Severity|Critical
|Resolution|No Resolution.

### HpeWolfram.1.0.TaskCannotBeCreated
New Tasks cannot be created at this time

| | |
|:---|:---|
|Message Format|"New Tasks cannot be created at this time as the task queue is full"
|Severity|Warning
|Resolution|Wait for the tasks to be completed and then try again.

### HpeWolfram.1.0.TestNMAPCommandCompleted
Completed execution of nmap command for the provided network share IP.

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|Check issues related to firewall & check if the folder has been mounted properly

### HpeWolfram.1.0.TestShowMountCompleted
Completed execution of showmount -e command for the provided network share IP.

| | |
|:---|:---|
|Message Format|"%1"
|Severity|Warning
|Resolution|

### HpeWolfram.1.0.USBNotMounted
USB not mounted.

| | |
|:---|:---|
|Message Format|"No USB found plugged to the device."
|Severity|Warning
|Resolution|Plug in ext2 type USB and perform operation

### HpeWolfram.1.0.UnableToModifyDuringSystemPOST
The value for the property cannot be changed while the computer system BIOS is in POST.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed while the computer system BIOS is in POST."
|Severity|Warning
|Resolution|After the computer system is either fully booted or powered off, retry the operation.

### HpeWolfram.1.0.UnauthorizedLoginAttempt
The login was not successful, because the supplied credentials could not be authorized.

| | |
|:---|:---|
|Message Format|"The login was not successful, because the supplied credentials could not be authorized."
|Severity|Warning
|Resolution|Log in with authorized user name and password credentials.

### HpeWolfram.1.0.UnsupportedMediaType
Indicates that the media type used or specified is unsupported.

| | |
|:---|:---|
|Message Format|"Indicates that the media type used or specified is unsupported."
|Severity|Critical
|Resolution|Provide or use the right media type and try the operation again.

### HpeWolfram.1.0.UnsupportedOperationInSystemBIOS
This operation is not supported by the current version of the system BIOS.

| | |
|:---|:---|
|Message Format|"This operation is not supported by the current version of the system BIOS."
|Severity|Warning
|Resolution|None.

### HpeWolfram.1.0.UpgradeRunning
Calls are blocked because upgrade is in progress.

| | |
|:---|:---|
|Message Format|"Calls are blocked because upgrade is in progress."
|Severity|Warning
|Resolution|No action required

### HpeWolfram.1.0.UserAlreadyExist
A User Account with the specified user name already exists.

| | |
|:---|:---|
|Message Format|"A User Account with the specified user name already exists."
|Severity|Warning
|Resolution|Try a different user or login user name.

### HpeWolfram.1.0.UserInitiatedRefreshAllStarted
The user has initiated a refresh of all the servers and groups.

| | |
|:---|:---|
|Message Format|"User Initiated refresh of all the servers and groups has started"
|Severity|OK
|Resolution|No action required

### HpeWolfram.1.0.UserLimitExceeded
Unable to create a new User Account as the number of user accounts exceed the maximum number allowed by the implementation.

| | |
|:---|:---|
|Message Format|"Unable to create a new User Account as the number of user accounts exceed the maximum number allowed by the implementation."
|Severity|Warning
|Resolution|Before creating a new user account, reduce the number of existing user accounts.

### iLO.2.0.AHSDisabled
Modifying AHS properties is not possible with AHS disabled.

| | |
|:---|:---|
|Message Format|"Modifying AHS properties is not possible with AHS disabled."
|Severity|Warning
|Resolution|Enable AHS, and then modify the AHS properties.

### iLO.2.0.Accepted
Indicates that one or more properties were correctly changed, but may not be in effect yet.

| | |
|:---|:---|
|Message Format|"Indicates that one or more properties were correctly changed, but may not be in effect yet."
|Severity|OK
|Resolution|None

### iLO.2.0.ActionParameterValueNotInList
Indicates that the correct value type was supplied for the action parameter, but the value is not supported. (The value is not in the enumeration list.)

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is not in the list of valid values."
|Severity|Warning
|Resolution|Choose a value from the enumeration list and resubmit the request if the operation failed.

### iLO.2.0.AlertMailFeatureDisabled
AlertMail feature is disabled.

| | |
|:---|:---|
|Message Format|"AlertMail feature is disabled."
|Severity|Warning
|Resolution|Enable AlertMail feature to send test alert message.

### iLO.2.0.AlreadyInProgress
An operation is already in progress.

| | |
|:---|:---|
|Message Format|"An operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current operation to complete, and then retry the operation.

### iLO.2.0.AlreadyUpToDate


| | |
|:---|:---|
|Message Format|"The update did not occur because the component was already up to date."
|Severity|Warning
|Resolution|None.

### iLO.2.0.ArrayPropertyOutOfBound
The number of items in the array exceeds the maximum number supported.

| | |
|:---|:---|
|Message Format|"An array %1 was supplied with %2 items that exceeds the maximum supported count of %3."
|Severity|Warning
|Resolution|Retry the operation using the correct number of items for the array.

### iLO.2.0.BatteryBackupUnitSettingsDisabled
Battery Backup Unit settings are currently disabled.

| | |
|:---|:---|
|Message Format|"Battery Backup Unit settings are disabled when the system is configured for Scalable Persistent Memory."
|Severity|Warning
|Resolution|Disable Scalable Persistent Memory functionality in the system ROM RBSU to re-enable Battery Backup Unit settings.

### iLO.2.0.BiosActionTBD
The BIOS action supplied in the POST operation is not yet implemented.

| | |
|:---|:---|
|Message Format|"The BIOS action %1 is not implemented yet."
|Severity|Critical
|Resolution|The action was invalid or the wrong resource was the target. See the implementation documentation for assistance.

### iLO.2.0.BiosPasswordInfoInvalid
The stored BIOS password information is invalid. A system reboot is neccessary to retore password defaults.

| | |
|:---|:---|
|Message Format|"The stored BIOS password information is invalid.  Reboot system."
|Severity|Critical
|Resolution|The system will need to be rebooted to restore BIOS password information to defaults.

### iLO.2.0.BiosPasswordMismatch
The provided OldPassword does not match the stored BIOS password.

| | |
|:---|:---|
|Message Format|"The provided OldPassword does not match the stored BIOS password."
|Severity|Critical
|Resolution|Retry the action with the matching password.

### iLO.2.0.CannotRemoveLicense
Cannot remove iLO Standard/iLO Standard for BladeSystem license.

| | |
|:---|:---|
|Message Format|"Cannot remove iLO Standard/iLO Standard for BladeSystem license."
|Severity|Warning
|Resolution|None.

### iLO.2.0.ComponentUploadAlreadyInProgress
A component upload operation is already in progress.

| | |
|:---|:---|
|Message Format|"A component upload operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current component upload to complete, and then retry the operation.

### iLO.2.0.ComponentUploadFailed
A component upload operation failed.

| | |
|:---|:---|
|Message Format|"A component upload operation failed."
|Severity|Warning
|Resolution|Wait for the current component upload to complete, and then retry the operation.

### iLO.2.0.DemoLicenseKeyPreviouslyInstalled
A demo license was previously installed.

| | |
|:---|:---|
|Message Format|"A demo license was previously installed."
|Severity|Warning
|Resolution|None.

### iLO.2.0.DeviceResetRequired
Indicates that one or more properties were correctly changed, but will not take effect until device is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until the device is reset."
|Severity|Warning
|Resolution|Reset the device for the settings to take effect.

### iLO.2.0.DiagsTestAlreadyRunning
A diagnostics self test is already running.

| | |
|:---|:---|
|Message Format|"A diagnostics self test is already running."
|Severity|Warning
|Resolution|Stop the running test and try again.

### iLO.2.0.ESKMServersNotConfigured
Enterprise Secure Key Manager Servers are not configured.

| | |
|:---|:---|
|Message Format|"Enterprise Secure Key Manager Servers are not configured."
|Severity|OK
|Resolution|None.

### iLO.2.0.ETagTooLong
The supplied ETag is too long. The maximum supported ETag length is 63 bytes.

| | |
|:---|:---|
|Message Format|"The supplied ETag is too long. The maximum supported ETag length is 63 bytes."
|Severity|Warning
|Resolution|Retry the operation using an ETag with a length of 63 bytes or less.

### iLO.2.0.EmptyDNSName
DNS name is empty.

| | |
|:---|:---|
|Message Format|"Empty DNS name."
|Severity|Warning
|Resolution|Retry the request with a valid DNS name.

### iLO.2.0.ErrorIntializingESKM
Failed to initialize ESKM.

| | |
|:---|:---|
|Message Format|"Failed to initialize ESKM."
|Severity|Warning
|Resolution|Check if Account Group, Local CA Certificate Name, Login Name and Password are correct and try again.

### iLO.2.0.EventLogCleared
Event log cleared successfully.

| | |
|:---|:---|
|Message Format|"Event log cleared successfully."
|Severity|OK
|Resolution|None.

### iLO.2.0.EventSubscriptionModified
The event subscription was modified successfully.

| | |
|:---|:---|
|Message Format|"The event subscription was modified successfully."
|Severity|OK
|Resolution|None.

### iLO.2.0.EventSubscriptionRemoved
The event subscription was removed successfully.

| | |
|:---|:---|
|Message Format|"The event subscription was removed successfully."
|Severity|OK
|Resolution|None.

### iLO.2.0.ExtendedInfo
Indicates that extended information is available.

| | |
|:---|:---|
|Message Format|"See @Message.ExtendedInfo for more information."
|Severity|OK
|Resolution|See @Message.ExtendedInfo for more information.

### iLO.2.0.FWFlashSuccessTPMOverrideEnabled
A Trusted Module is  detected in this system. If you have not performed the proper OS encryption procedures, you will lose access to your data if recovery key is not available. Recommended procedure is to suspend encryption software prior to System ROM or Option ROM firmware flash. TPMOverrideFlag is enabled and firmware flash initiated.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module is detected in this system. Updating the System ROM or Option Card Firmware may have impact to measurements stored in the TM and may have impact to security functionality on the platform which depends on these measurements."
|Severity|OK
|Resolution|None.

### iLO.2.0.FWFlashSuccessTrustedModuleOverrideEnabled
A Trusted Module (type unspecified) is installed in the system and TPMOverrideFlag is enabled. Firmware flash initiated.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module (type unspecified) has been detected in this system. If you have not performed the proper OS encryption procedures, you will lose access to your data if recovery key is not available. Recommended procedure for Microsoft Windows(R) BitLocker(TM) is to "suspend" BitLocker prior to System ROM or Option ROM firmware flash."
|Severity|OK
|Resolution|None.

### iLO.2.0.FWFlashTPMOverrideFlagRequired
A Trusted Module is  detected in this system. Failure to perform proper OS encryption procedures will result in loss of access to your data if recovery key is not available. Recommended procedure is to suspend encryption software prior to System ROM or Option ROM firmware flash. If you do not have your recovery key or have not suspended encryption software, cancel this firmware upload. Failure to follow these instructions will result in loss of access to your data. To continue with firmware flash TPMOverrideFlag is required.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module is detected in this system. Updating the System ROM or Option Card Firmware may have impact to measurements stored in the TM and may have impact to security functionality on the platform which depends on these measurements."
|Severity|Warning
|Resolution|Please set the TPMOverrideFlag to true and try again.

### iLO.2.0.FWFlashTrustedModuleOverrideFlagRequired
A Trusted Module (type unspecified) is installed in the system, TPMOverrideFlag is required for firmware flash to proceed.

| | |
|:---|:---|
|Message Format|"CAUTION: A Trusted Module (type unspecified) has been detected in this system. Failure to perform proper OS encryption procedures will result in loss of access to your data if recovery key is not available. Recommended procedure for Microsoft Windows(R) BitLocker(TM) is to "suspend" BitLocker prior to System ROM or Option ROM firmware flash. If you do not have your recovery key or have not suspended BitLocker, exit this flash: Failure to follow these instructions will result in loss of access to your data."
|Severity|Warning
|Resolution|Please set the TPMOverrideFlag to true and try again.

### iLO.2.0.FirmwareFlashAlreadyInProgress
A firmware upgrade operation is already in progress.

| | |
|:---|:---|
|Message Format|"A firmware flash operation is already in progress."
|Severity|Warning
|Resolution|Wait for the current firmware flash to complete, and then retry the operation.

### iLO.2.0.GeneratingCertificate
Generating the X509 Certificate.

| | |
|:---|:---|
|Message Format|"X509 Certificate is being generated and the process might take up to 10 minutes."
|Severity|OK
|Resolution|None.

### iLO.2.0.ICRUInvalidAddress
ICRU returned invalid address for translation.

| | |
|:---|:---|
|Message Format|"ICRU returned invalid address for translation."
|Severity|Warning
|Resolution|Input valid address for translation.

### iLO.2.0.ICRUNotSupported
ICRU feature or function is not supported on the system.

| | |
|:---|:---|
|Message Format|"ICRU feature or function is not supported on the system."
|Severity|Warning
|Resolution|None.

### iLO.2.0.IPv6ConfigurationError
The specified IPv6 configuration caused an error.

| | |
|:---|:---|
|Message Format|"The specified IPv6 configuration was in error due to %1."
|Severity|Warning
|Resolution|Resolve the indicated error in the configuration data.

### iLO.2.0.ImportCertSuccessful
Import Certificate was successful.

| | |
|:---|:---|
|Message Format|"Import Certificate was successful."
|Severity|OK
|Resolution|None.

### iLO.2.0.ImportCertSuccessfuliLOResetinProgress
Import Certificate was successful and the management processor is being reset.

| | |
|:---|:---|
|Message Format|"Import Certificate was successful. Management Processor reset is in progress to enable the new certificate."
|Severity|Warning
|Resolution|None.

### iLO.2.0.ImportCertificateFailed
Failed importing Certificate.

| | |
|:---|:---|
|Message Format|"Failed importing the X509 Certificate."
|Severity|Warning
|Resolution|Retry the operation with proper Certificate information.

### iLO.2.0.ImportSSOParamError
Not a valid parameter.

| | |
|:---|:---|
|Message Format|"Invalid Parameter."
|Severity|Warning
|Resolution|Retry the request with valid parameters.

### iLO.2.0.ImportSSOUriError
Not a valid Uri to import SSO certificate.

| | |
|:---|:---|
|Message Format|"Invalid Uri."
|Severity|Warning
|Resolution|Retry the request with valid URI.

### iLO.2.0.IndicatorLedInvalidStateChange
The request to change the state of the Indicator LED cannot be granted because the current state is either Blinking or is Unknown.

| | |
|:---|:---|
|Message Format|"The Indicator LED cannot be changed when its state is Blinking or Unknown."
|Severity|Warning
|Resolution|Please wait until the server has completed its reserved state.

### iLO.2.0.InstallSetWriteError
The InstallSet write failed.

| | |
|:---|:---|
|Message Format|"The InstallSet write of %1 failed."
|Severity|Warning
|Resolution|Ensure a valid name for the item and that space exists to hold the item.

### iLO.2.0.InterfaceDisabledResetRequired
Disabling one or more interfaces/features will cause certain functionalities to be not available. Please refer to User Guide for details on the implications. Changes will not take effect until the management processor is reset

| | |
|:---|:---|
|Message Format|"CAUTION: Disabling one or more interfaces/features will cause certain functionalities to be not available. Please refer to User Guide for details on the implications. Changes will not take effect until the management processor is reset"
|Severity|OK
|Resolution|None.

### iLO.2.0.InternalErrorWithParam
The operation was not successful due to an internal service error (shown), but the service is still operational.

| | |
|:---|:---|
|Message Format|"The operation was not successful due to an internal service error (%1), but the service is still operational."
|Severity|Critical
|Resolution|Retry the operation. If the problem persists, consider resetting the service.

### iLO.2.0.InvalidConfigurationSpecified
The specified configuration is not valid.

| | |
|:---|:---|
|Message Format|"The specified configuration is not valid."
|Severity|Warning
|Resolution|Correct the configuration, and then retry the operation.

### iLO.2.0.InvalidConfigurationSpecifiedForFederation
iLO Federation Management cannot be supported in the current configuration.

| | |
|:---|:---|
|Message Format|"iLO Federation Management cannot be supported in the current configuration."
|Severity|Warning
|Resolution|Review the management processor network settings or Onboard Administrator settings and refer to the User Guide.

### iLO.2.0.InvalidEngineID
EngineID should be a hexadecimal number starting with 0x (for example, 0x0102030405abcdef). The string length should be an even number, greater than or equal to 6 characters (excluding the "0x"), and less than or equal to 32 characters.

| | |
|:---|:---|
|Message Format|"EngineID should be a hexadecimal number starting with 0x (for example, 0x0102030405abcdef). The string length should be an even number, greater than or equal to 6 characters (excluding the "0x"), and less than or equal to 32 characters."
|Severity|Warning
|Resolution|Retry the operation using an EngineID within the specified parameters.

### iLO.2.0.InvalidIndex
The Index is not valid.

| | |
|:---|:---|
|Message Format|"The Index provided is not valid."
|Severity|Warning
|Resolution|Adhere to the indexes supported in the self links.

### iLO.2.0.InvalidLicenseKey
The license key is not valid.

| | |
|:---|:---|
|Message Format|"The license key is not valid."
|Severity|Warning
|Resolution|Retry the operation using a valid license key.

### iLO.2.0.InvalidOperationForAutoPowerOnState
The operation was not successful because the current auto power on mode specifies power is to remain off.

| | |
|:---|:---|
|Message Format|"The auto power on delay cannot be set because power is configured to remain off."
|Severity|Warning
|Resolution|Verify that the system auto power on mode is set to turn power on or follow the previous power setting.

### iLO.2.0.InvalidOperationForSystemState
The operation was not successful due to the current power state (for example, attempting to turn the power off when it is already off).

| | |
|:---|:---|
|Message Format|"The operation was not successful due to the current power state."
|Severity|Warning
|Resolution|Verify that the system is in the correct power state, and then retry the operation.

### iLO.2.0.InvalidPassphraseLength
The passphrase must contain 8 to 49 characters.

| | |
|:---|:---|
|Message Format|"%1 must contain 8 to 49 characters."
|Severity|Warning
|Resolution|Correct the passphrase, and then retry the operation.

### iLO.2.0.InvalidPasswordLength
The password length is not valid.

| | |
|:---|:---|
|Message Format|"A valid password must contain between %1 to %2 characters."
|Severity|Critical
|Resolution|Retry the operation using a corrected password.

### iLO.2.0.LicenseKeyNotSupported
The use of a license key is not supported on this system.

| | |
|:---|:---|
|Message Format|"The use of a license key is not supported on this system."
|Severity|Warning
|Resolution|None.

### iLO.2.0.LicenseKeyRequired
A license key is required to use this operation or feature.

| | |
|:---|:---|
|Message Format|"A license key is required to use this operation or feature."
|Severity|Warning
|Resolution|Install a license key to use this feature.

### iLO.2.0.LoginAttemptDelayed
The login was not successful, so the service enforces a delay before another login is allowed.

| | |
|:---|:---|
|Message Format|"The login was not successful, so the service enforces a delay before another login is allowed."
|Severity|Warning
|Resolution|Wait for the delay time to expire, and then retry the login.

### iLO.2.0.LoginAttemptDelayedSeconds
The login was not successful, so the service enforces a delay before another login is allowed.

| | |
|:---|:---|
|Message Format|"The login was not successful, so the service enforces a %1 second delay before another login is allowed."
|Severity|Warning
|Resolution|None.

### iLO.2.0.MaxProviders
The maximum number of providers are already registered.

| | |
|:---|:---|
|Message Format|"The maximum number of providers are already registered."
|Severity|Warning
|Resolution|None.

### iLO.2.0.MaxVirtualMediaConnectionEstablished
No more Virtual Media connections are available, because the maximum number of connections are already established.

| | |
|:---|:---|
|Message Format|"No more Virtual Media connections are available, because the maximum number of connections are already established."
|Severity|Warning
|Resolution|Close an established Virtual Media connection, and then retry creating or opening another connection.

### iLO.2.0.MembistVariablesNotSupported
Membist variables are not supported on the system.

| | |
|:---|:---|
|Message Format|"Membist variables are not supported on the system."
|Severity|Warning
|Resolution|None.

### iLO.2.0.NoEventSubscriptions
There are no event subscriptions registerd.

| | |
|:---|:---|
|Message Format|"The opeartion can not be completed because there are no event subscribers."
|Severity|Warning
|Resolution|

### iLO.2.0.NoPowerMetering
No support for power metering available on platform.

| | |
|:---|:---|
|Message Format|"No support for power metering available on platform."
|Severity|OK
|Resolution|Enable Power Metering on platform if supported.

### iLO.2.0.NoSNMPAlertDestinationsConfigured
No SNMP alert destinations are configured.

| | |
|:---|:---|
|Message Format|"No SNMP alert destinations are configured."
|Severity|Warning
|Resolution|Disable SNMP pass-thru, modify the property, and then re-enable SNMP pass-thru.

### iLO.2.0.NoSamples
No power history samples are available.

| | |
|:---|:---|
|Message Format|"No power history samples are available."
|Severity|OK
|Resolution|To accumulate power history samples, power on the server, and then wait at least 5 minutes.

### iLO.2.0.NoScriptedVirtualMediaConnectionAvailable
No scripted virtual media connections exist to perform the operation.

| | |
|:---|:---|
|Message Format|"No scripted virtual media connections exist to perform the operation."
|Severity|Warning
|Resolution|Create or open a scripted virtual media connection, and then retry the operation.

### iLO.2.0.NoSpaceforDNSName
No space to store DNS name.

| | |
|:---|:---|
|Message Format|"No space to store DNS name."
|Severity|Warning
|Resolution|Make sure SSO database has enough space to store DNS name.

### iLO.2.0.NoVirtualMediaConnectionAvailable
No Virtual Media connections exist to perform the operation.

| | |
|:---|:---|
|Message Format|"No Virtual Media connections exist to perform the operation."
|Severity|Warning
|Resolution|Create or open a Virtual Media connection, and then retry the operation.

### iLO.2.0.NotSupportedOnNIC
This property is not supported by the indicated network port.

| | |
|:---|:---|
|Message Format|"%1 is not supported on the %2 Network Port."
|Severity|Warning
|Resolution|Do not specify this property on the indicated network port.

### iLO.2.0.NotValidIPAddrOrDNS
The value for the property is not a valid IPv4/v6 address or DNS name.

| | |
|:---|:---|
|Message Format|"The value for property %1 is not a valid IPv4/v6 address or DNS name."
|Severity|Warning
|Resolution|Correct the IPv4/v6 address or DNS name, and then retry the operation.

### iLO.2.0.NotValidIPAddress
The value for the property is not a valid IP address.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid IP address for %2"
|Severity|Warning
|Resolution|Use a valid IP address.

### iLO.2.0.NotValidSubnetMask
The value for the property is not a valid subnet mask.

| | |
|:---|:---|
|Message Format|"The value %1 is not a valid subnet mask for %2"
|Severity|Warning
|Resolution|Use a valid subnet mask.

### iLO.2.0.OperationWillCompleteAfterSystemPOST
The value for the property will be applied after System BIOS POST completes.

| | |
|:---|:---|
|Message Format|"The value for property %1 will be changed after the System BIOS completes POST."
|Severity|Information
|Resolution|Wait to see the change in value until after the System BIOS completes POST.

### iLO.2.0.PowerCapOACntrld
The enclosure Onboard Administrator is currently managing the power cap.

| | |
|:---|:---|
|Message Format|"The enclosure Onboard Administrator is currently managing the power cap."
|Severity|Warning
|Resolution|Use Onboard Administrator to Manage the PowerCap

### iLO.2.0.PowerCapROMCntrld
The System ROM is currently managing the power cap.

| | |
|:---|:---|
|Message Format|"The System ROM is currently managing the power cap."
|Severity|Warning
|Resolution|Enable RESTful API management of the power cap in System ROM

### iLO.2.0.PowerValueBadParam
The power cap value is not valid.

| | |
|:---|:---|
|Message Format|"The power cap value is not valid."
|Severity|Warning
|Resolution|Retry the operation using a corrected value.

### iLO.2.0.PowerValueInvalidCalibrationData
The request to set the power cap failed. Invalid power cap calibration data. The Power Cap feature is currently unavailable.

| | |
|:---|:---|
|Message Format|"The request to set the power cap failed. Invalid power cap calibration data. The Power Cap feature is currently unavailable"
|Severity|Warning
|Resolution|Restart the server to retrieve calibration data from initial POST.

### iLO.2.0.PowerValueNotOptimal
Power caps set below the specified percentage threshold may become unreachable due to changes in the server. It is not recommended to set a cap for less than this threshold.

| | |
|:---|:---|
|Message Format|"Power caps set below the specified percentage threshold may become unreachable due to changes in the server. It is not recommended to set a cap for less than %1%."
|Severity|Warning
|Resolution|Please provide an optimal value in integer considering the power cap range.

### iLO.2.0.PowerValueUnAvailable
Advanced power capping is not currently available due to the system configuration or state.

| | |
|:---|:---|
|Message Format|"Advanced power capping is not currently available due to the system configuration or state."
|Severity|Warning
|Resolution|Change the system configuration or wait for the system to become fully initialized, and then retry the operation.

### iLO.2.0.PowerValueUnSupported
Advanced power capping is not supported on this system.

| | |
|:---|:---|
|Message Format|"Advanced power capping is not supported on this system."
|Severity|Warning
|Resolution|None.

### iLO.2.0.PrimaryESKMServerAccessible
Only the primary ESKM server is accessible.

| | |
|:---|:---|
|Message Format|"No redundancy. Only the primary ESKM server is accessible."
|Severity|OK
|Resolution|None.

### iLO.2.0.PrimarySecondaryAddressesResolveToSameServer
Primary and secondary ESKM server addresses resolve to the same server.

| | |
|:---|:---|
|Message Format|"No redundancy. Primary and secondary ESKM server addresses resolve to the same server."
|Severity|OK
|Resolution|None.

### iLO.2.0.PrimarySecondaryESKMServersAccessible
Both primary and secondary ESKM servers are accessible.

| | |
|:---|:---|
|Message Format|"Redundant solution: Both primary and secondary ESKM servers are accessible."
|Severity|OK
|Resolution|None.

### iLO.2.0.PropertyNotWritableOrUnknown
The request included a value for a  read-only or unknown property.

| | |
|:---|:---|
|Message Format|"The property %1 is a read-only property and cannot be assigned a value, or not valid for this resource."
|Severity|Warning
|Resolution|If the operation did not complete, remove the property from the request body and resubmit the request.

### iLO.2.0.PropertyValueBadParam
The property value is not valid.

| | |
|:---|:---|
|Message Format|"The property value is not valid."
|Severity|Warning
|Resolution|Retry the operation using a corrected value.

### iLO.2.0.PropertyValueExceedsMaxLength
The value for the property exceeds the maximum length.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 exceeds the maximum length of %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### iLO.2.0.PropertyValueIncompatible
The value for the property is the correct type, but this value is incompatible with the current value of another property.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is incompatible with the value for property %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### iLO.2.0.PropertyValueOutOfRange
The value for the property is out of range.

| | |
|:---|:---|
|Message Format|"The value %1 for the property %2 is out of range %3."
|Severity|Warning
|Resolution|Correct the value for the property in the request body, and then retry the operation.

### iLO.2.0.PropertyValueRequired
Indicates that a property was required but not specified.

| | |
|:---|:---|
|Message Format|"%1 requires Property %2 to be specified."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### iLO.2.0.RecoveryInstallSetRequired
A recovery install set is required for this action.

| | |
|:---|:---|
|Message Format|"No recovery install set present."
|Severity|Critical
|Resolution|Create a recovery install set (install set with IsRecovery property set true).

### iLO.2.0.RepairNotSupported
IML event with this severity is not supported to be repaired. IML events with Critical or Warning severities can marked as repaired.

| | |
|:---|:---|
|Message Format|"IML event with %1 severity is not supported to be repaired. IML events with Critical or Warning severities can marked as repaired."
|Severity|Warning
|Resolution|Please do not try to repair IML events with severity other than Critical or Warning.

### iLO.2.0.RequiredPropertyMissing
Indicates that a required property is not specified.

| | |
|:---|:---|
|Message Format|"Required Property %1 needs to be specifed."
|Severity|Warning
|Resolution|Include the required property in the request body and then retry the operation.

### iLO.2.0.ResetInProgress
A management processor reset is in progress.

| | |
|:---|:---|
|Message Format|"A management processor reset is in progress."
|Severity|Warning
|Resolution|Wait for management processor reset to complete, and then retry the operation.

### iLO.2.0.ResetRequired
One or more properties were changed, but these changes will not take effect until the management processor is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed, but these changes will not take effect until the management processor is reset."
|Severity|Warning
|Resolution|To enable the changed properties, reset the management processor.

### iLO.2.0.ResourceBeingFlashed
The change to the requested resource failed because the resource is being flashed.

| | |
|:---|:---|
|Message Format|"The change to the requested resource failed because the resource is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### iLO.2.0.ResourceInUseWithDetail
The change could not be made because the resource was in use or in a transitioning state.

| | |
|:---|:---|
|Message Format|"The change to the resource failed because the resource is in use or in transition."
|Severity|Warning
|Resolution|Retry the request.

### iLO.2.0.ResourceTemporarilyUnavailable
The resource is temporarily unavailable because the firmware is being flashed.

| | |
|:---|:---|
|Message Format|"The resource is temporarily unavailable because the firmware is being flashed."
|Severity|Warning
|Resolution|Retry the operation when the firmware upgrade has completed.

### iLO.2.0.SMBIOSRecordNotFound
The SMBIOS record type is not found or is not supported on the system.

| | |
|:---|:---|
|Message Format|"The SMBIOS record type %1 is not found or is not supported on the system."
|Severity|Warning
|Resolution|Reset the system to update the SMBIOS records. If the problem persists then the SMBIOS record type is not supported.

### iLO.2.0.SNMPAlertDisabled
The operation could not be completed because SNMP alerts are disabled.

| | |
|:---|:---|
|Message Format|"The operation could not be completed because SNMP alerts are disabled."
|Severity|Warning
|Resolution|Enable SNMP alerts and retry the operation.

### iLO.2.0.SNMPDisabled
Modifying SNMP properties is not possible with SNMP disabled.

| | |
|:---|:---|
|Message Format|"Modifying SNMP properties is not possible with SNMP disabled."
|Severity|Warning
|Resolution|Enable SNMP, and then modify the SNMP properties.

### iLO.2.0.SNMPTestAlertFailed
The SNMP Test Alert did not send successfully.

| | |
|:---|:---|
|Message Format|"The SNMP Test Alert did not send successfully."
|Severity|Warning
|Resolution|Verify the test alert content and retry.

### iLO.2.0.SNTPConfigurationManagedByDHCPAndIsReadOnly
SNTP configuration is currently managed by DHCP and is therefore read-only.

| | |
|:---|:---|
|Message Format|"%1 cannot be changed while DHCP is configured to provide SNTP settings."
|Severity|Warning
|Resolution|Disable SNTP configuration options in both DHCPv4 and DHCPv6 (see /Managers/n/NICs), and then reconfigure SNTP as desired with static settings.

### iLO.2.0.SSOCertficateEmpty
SSO Certificate is Empty.

| | |
|:---|:---|
|Message Format|"Empty SSO Certificate."
|Severity|Warning
|Resolution|None.

### iLO.2.0.SSOCertificateReadError
SSO Certificate Read Error.

| | |
|:---|:---|
|Message Format|"Error reading SSO certificate."
|Severity|Warning
|Resolution|Retry the request with valid SSO certificate.

### iLO.2.0.SSONoSpaceError
No space to store SSO certificate.

| | |
|:---|:---|
|Message Format|"No space to store SSO certificate."
|Severity|Warning
|Resolution|Make sure SSO database has enough space to store SSO certificate.

### iLO.2.0.SSORecordNotFound
SSO Record Not Found.

| | |
|:---|:---|
|Message Format|"SSO Record Not Found."
|Severity|Warning
|Resolution|None.

### iLO.2.0.SecondaryESKMServerAccessible
Only the secondary ESKM server is accessible.

| | |
|:---|:---|
|Message Format|"No redundancy. Only the secondary ESKM server is accessible."
|Severity|OK
|Resolution|None.

### iLO.2.0.SuccessFeedback
The operation completed successfully.

| | |
|:---|:---|
|Message Format|"The operation completed successfully."
|Severity|OK
|Resolution|None

### iLO.2.0.SyslogFeatureDisabled
Remote Syslog feature is disabled.

| | |
|:---|:---|
|Message Format|"Remote syslog feature is disabled."
|Severity|Warning
|Resolution|Enable remote syslog feature to send test syslog message.

### iLO.2.0.SystemPowerOffRequired
The system has to be powered off to perform this operation. AutoPowerOn must be set to achieve a power restore.

| | |
|:---|:---|
|Message Format|"The system has to be powered off to perform this operation."
|Severity|OK
|Resolution|Power off the system to perform this operation.

### iLO.2.0.SystemResetRequired
The system properties were correctly changed, but will not take effect until the system is reset.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until system is reset."
|Severity|Warning
|Resolution|Reset system for the settings to take effect.

### iLO.2.0.TokenRequired
Proper 'X-HPRESTFULAPI-AuthToken' authorization token not provided.

| | |
|:---|:---|
|Message Format|"Proper 'X-HPRESTFULAPI-AuthToken' authorization token not provided."
|Severity|Critical
|Resolution|Create proper 'X-HPRESTFULAPI-AuthToken' authorization token. Send token in using the proper HTTP header.

### iLO.2.0.UnableModifyRights
Unable to modify user rights.

| | |
|:---|:---|
|Message Format|"Unable to modify user rights."
|Severity|Warning
|Resolution|None.

### iLO.2.0.UnableToModifyDueToMissingComponent
The value for the property cannot be changed because a related hardware component is not installed.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed because a related hardware component is not installed."
|Severity|Warning
|Resolution|Install the hardware component and retry the operation.

### iLO.2.0.UnableToModifyDuringSystemPOST
The value for the property cannot be changed while the computer system BIOS is in POST.

| | |
|:---|:---|
|Message Format|"The value for property %1 cannot be changed while the computer system BIOS is in POST."
|Severity|Warning
|Resolution|After the computer system is either fully booted or powered off, retry the operation.

### iLO.2.0.UnauthorizedLoginAttempt
The login was not successful, because the supplied credentials could not be authorized.

| | |
|:---|:---|
|Message Format|"The login was not successful, because the supplied credentials could not be authorized."
|Severity|Warning
|Resolution|Log in with authorized user name and password credentials.

### iLO.2.0.UnsupportedOperation
This operation is not supported by RIS for the current system.

| | |
|:---|:---|
|Message Format|"This operation is not supported by RIS for the current system."
|Severity|Warning
|Resolution|None.

### iLO.2.0.UnsupportedOperationInLegacyBootMode
This operation is not supported when the system Boot Mode is set to Legacy BIOS.

| | |
|:---|:---|
|Message Format|" This operation is not supported when the system Boot Mode is set to Legacy BIOS."
|Severity|Warning
|Resolution|Change the Boot Mode to UEFI and retry the operation.

### iLO.2.0.UnsupportedOperationInSystemBIOS
This operation is not supported by the current version of the system BIOS.

| | |
|:---|:---|
|Message Format|"This operation is not supported by the current version of the system BIOS."
|Severity|Warning
|Resolution|None.

### iLO.2.0.UpdateBadParameter


| | |
|:---|:---|
|Message Format|"The update failed because a bad parameter was supplied."
|Severity|Warning
|Resolution|Supply correct parameters to the component and retry the update.

### iLO.2.0.UpdateCancelled


| | |
|:---|:---|
|Message Format|"The update was canceled by the update process."
|Severity|Warning
|Resolution|Retry the update.

### iLO.2.0.UpdateDependencyFailure


| | |
|:---|:---|
|Message Format|"The update did not complete because the component failed a dependency check."
|Severity|Warning
|Resolution|Install any dependent components first and then retry this update.

### iLO.2.0.UpdateFailed


| | |
|:---|:---|
|Message Format|"The update failed with a component specific error (%1)."
|Severity|Warning
|Resolution|Retry the update after remedying the component error.

### iLO.2.0.UpdateInPOST


| | |
|:---|:---|
|Message Format|"System must not be booted past POST in order to perform this update"
|Severity|Warning
|Resolution|Boot to UEFI and retry the update.

### iLO.2.0.UpdateInterrupted


| | |
|:---|:---|
|Message Format|"The update was interrupted."
|Severity|Warning
|Resolution|Retry the update.

### iLO.2.0.UpdateInvalidFile


| | |
|:---|:---|
|Message Format|"The update operation failed because the file is not valid."
|Severity|Warning
|Resolution|Remove and re-add the component to the repository and try the operation again.

### iLO.2.0.UpdateInvalidOS


| | |
|:---|:---|
|Message Format|"The update did not occur because the running OS is not valid."
|Severity|Warning
|Resolution|Retry the update while running the correct OS.

### iLO.2.0.UpdateNotApplicable


| | |
|:---|:---|
|Message Format|"The task was not completed because the component was not applicable to this system."
|Severity|Warning
|Resolution|None.

### iLO.2.0.UpdateRepositoryUnavailable


| | |
|:---|:---|
|Message Format|"The update operation failed because the component repository is unavailable."
|Severity|Warning
|Resolution|None.

### iLO.2.0.UpdateTaskQueueFull
The Invoke action was not successful because the update task queue is full.

| | |
|:---|:---|
|Message Format|"The Invoke action was not successful because the update task queue is full."
|Severity|Critical
|Resolution|Remove completed tasks from the update task queue to retry the operation.

### iLO.2.0.UpdateTaskQueueWriteError
The UpdateTaskQueue write failed.

| | |
|:---|:---|
|Message Format|"The UpdateTaskQueue write of %1 failed."
|Severity|Warning
|Resolution|Ensure a valid name for the item and that space exists to hold the item.

### iLO.2.0.UpdateTemporarilyUnavailable


| | |
|:---|:---|
|Message Format|"The system is temporarily unable to perform this update"
|Severity|Warning
|Resolution|Retry the update, ensuring that power state is stable.

### iLO.2.0.UpdateWithPowerOff


| | |
|:---|:---|
|Message Format|"System power must be off to perform this update"
|Severity|Warning
|Resolution|Power system on and retry the update.

### iLO.2.0.UpdateWithPowerOn


| | |
|:---|:---|
|Message Format|"System power must be on to perform this update"
|Severity|Warning
|Resolution|Power system on and retry the update.

### iLO.2.0.UserAlreadyExist
The user or login user name already exists.

| | |
|:---|:---|
|Message Format|"The user or login user name already exists."
|Severity|Warning
|Resolution|Try a different user or login user name.

### iLO.2.0.UserNameAlreadyExists
Duplicate SNMPv3 User.

| | |
|:---|:---|
|Message Format|"The username %1 already exists in the list"
|Severity|Warning
|Resolution|Enter a different name and try again.

### iLO.2.0.VirtualMediaIsDisabled
Virtual Media has been disabled.

| | |
|:---|:---|
|Message Format|"Virtual Media has been disabled."
|Severity|Warning
|Resolution|Enable Virtual Media to perform this operation.

### iLO.2.0.iLOResetAndSystemRebootRequired
Indicates that one or more properties were correctly changed, but will not take effect until device is reset and system is rebooted.

| | |
|:---|:---|
|Message Format|"One or more properties were changed and will not take effect until the device is reset and system is rebooted"
|Severity|Warning
|Resolution|Reset the management processor and reboot the server.

### iLO.2.0.iLOServicePortIsDisabled
The Service Port is disabled. Other Service Port properties cannot be changed.

| | |
|:---|:---|
|Message Format|"The Service Port is disabled. Other Service Port properties cannot be changed."
|Severity|Warning
|Resolution|Enable Service Port to modify other Service Port properties.
