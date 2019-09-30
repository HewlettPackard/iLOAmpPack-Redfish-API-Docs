# RESTful Events and the Event Service
iLO Amplifier Pack now features an event subscription service that enables you to receive notifications when certain alerts occur in the iLOs discovered by iLO Amplifier Pack.
These notifications are in the form of HTTPS POST operations to a URI of your choice. The maximum number of
subscriptions that can be created is 8.

The event service is located in the data model at `/redfish/v1/EventService.` This resource includes
a link to a collection of subscriptions (called `EventSubscriptions` located at
`/redfish/v1/EventService/EventSubscriptions`).

## Modifying EventService ServiceEnabled
> POST /redfish/v1/EventService/

A field "ServiceEnabled" is provided at the EventService level, that can be used to stop/start notifications at the
configured subscription URIs. If this value is set to TRUE, notifications will be routed to all the subscriptions,
else it will be blocked for all subscriptions. It is set to TRUE by default.

```json
{
	"ServiceEnabled": false
}
```

**Example POST payload to enable/disable EventService**

* `ServiceEnabled` can be set to true or false based on choice.

## Subscribing for Events examples
> POST /redfish/v1/EventService/EventSubscriptions/

```json
{
	"Destination": "https://myeventreciever/eventreceiver",
	"EventTypes": [
	  "Alert"
	],
	"Protocol": "Redfish",
	"Context": "Context string",
	"Description": "Description String",
	"HttpHeaders":[
	  {
	  	"X-Auth-Token":"X-Auth-Token String",
	  }
	],
	"Oem" : {
		"Hpe" : {
	      		"DeliveryRetryAttempts": 3,
	      		"DeliveryRetryIntervalSeconds": 30,
	      		"NotificationCategory": {
	      			"Administration": true,
	      			"GeneralFailure": true,
	      			"HardwareFailure": true,
	      			"Maintenance": true,
	      			"Other": true,
	      			"Security": true,
	      			"Storage": true
	      		},
	      		"NotificationSeverity": {
	      			"Critical": true,
	      			"Info": true,
	      			"Warning": true
	      		}
	        }
	  }
}
```

In order to receive events, you must provide an HTTPS server accessible to iLO Amplifier Pack's network
with a URI you designate as the target for iLO Amplifier Pack initiated HTTPS POST operations.

Construct a JSON object conforming to the type `EventDestination` (see example) and
POST this to the collection indicated by the `EventSubscriptions` link at
`/redfish/v1/EventService/EventSubscriptions.` If you receive an HTTP 201 created
response, a new subscription has been added. Note that iLO Amplifier Pack does not test the destination URI
during this phase, so if the indicated URI is not valid, it will not be flagged until events are
emitted and the connection to the destination fails.

**Example POST payload to create a new subscription**

Much of the above content depends entirely upon your needs and setup:

* `Destination` must be an HTTPS URI accessible to iLO Amplifier Pack’s network.
* `EventTypes` can currently only be Alert.
* `HttpHeaders` gives you an opportunity to specify any arbitrary HTTP headers you need
for the event POST operation (e.g., X-Auth-Token). This will be a part of the payload during GET of Alerts.
* `Context` may be any string.
* `Description` may be any string.
* `Protocol` must be set to Redfish.
* `DeliveryRetryAttempts` indicates the number of retries that will be made to deliver an alert to a 
configured destination (In case the destination is not reachable). If a failure is observed even after this,
an entry will be made in the iLOAmplifier Alert logs. Default is set to 3. Can be modified to other values.
* `DeliveryRetryIntervalSeconds` indicates the number of seconds before which, each retry will be attempted.
Default is set to 30. Can be modified to other values.
* `NotificationCategory` gives you an opportunity to choose a specific category/set of categories for which
a notification need to be received. By default all the values are set to true.
* `NotificationSeverity` gives you an opportunity to choose a specific severity/set of severities for which
a notification needs to be received. By default all the values are set to true.

Consult the `EventDestination` schema for more details on each property.

## Submitting a Test Event
> POST /redfish/v1/EventService/Actions/EventService.SubmitTestEvent

Once the subscriptions are created, a test event can be posted to test if the subscription is working and 
you are able to recieve the events via iLO Amplifier Pack.

```json
{
            "EventId": "TestEventId",
            "EventTimestamp": "2019-07-29T15:13:49Z",
            "EventType": "Alert",
  			"Message": "Test Event",
            "MessageArgs": [
                "NoAMS",
                "Busy",
                "Cached"
            ],
            "MessageId": "iLOEvents.2.1.ServerPoweredOff",
            "OriginOfCondition": "/redfish/v1/Systems/1/",
            "Severity": "OK"
}
```
**Example POST payload to test a subscription**

* `EventId` must be set to string "TestEventId".
* `EventTimestamp` any arbitrary timestamp.
* `EventType` must be set to "Alert".
* `Message` any message string.
* `MessageArgs` array of any set of message arguments.
* `MessageId` any message id string.
* `OriginOfCondition` any arbitrary string.
* `Severity` send it for the one configured while creating the subscription.

