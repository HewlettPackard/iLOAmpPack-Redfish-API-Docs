# Resource Definitions

Each resource in the API has a "type" that defines its properties.  See the Redfish specification for `@odata.type` for details.

This section defines the supported types and lists the typical instances of each.  Because this API document is applicable to iLO Amplifier managing various HPE servers, you may find variations such as:

* properties implemented on one type of server and not another
* resources that are read only on one type of server and not another
* The number of resources of a particular type (e.g. multiple compute nodes or enclosing chassis)

## Collections

> GET https://{iLOAmpServer}/redfish/v1/systems/ showing a collection response (JSON)

```json
{
    "@odata.id": "/redfish/v1/systems/",
    "@odata.context": "/redfish/v1/$metadata/",
    "@odata.type": "#ComputerSystemCollection.ComputerSystemCollection",
    "Members@odata.count": 1,
    "Members": [
        {
            "@odata.id": "/redfish/v1/systems/1/"
        }
    ]
}
```

Many resource types in the API are members of "collections."  Collections are groups of similar resources and are typically an array of Member links.

Redfish does not define a generic collection "type" (@odata.type) but all collections are identical in structure.  A `ComputerSystemCollection` is identical in structure to a `ChassisCollection` although they have slightly different names.  Typically, collection types are suffixed with the word collection and are recognizable by the presense of the `Members` array of links.

Collections may be GET-only that may not be added to or removed from.  Examples of GET-only collections are the Systems collection at `/redfish/v1/systems/`.  In a typical systems collection describing physical hardware, it wouldn't make sense to be able to create or remove members using POST or DELETE.

Other collections may be editable.  Examples of these might be the Accounts collection at `/redfish/v1/accountservice/accounts`.  The API supports the addition or removal of user accounts.  To add a new member to an editable collection, perform an HTTP POST to the collection resource with a body consisting of the required JSON properties needed to create a new member (this does not necessarily require you to POST every property because many may take a unique service-assigned value or take a default value.)

For more information on collections see the Redfish 1.0 DMTF standard at [https://www.dmtf.org/standards/redfish](https:// www.dmtf.org/standards/redfish) and the example Python code:  [https://github.com/DMTF/python-redfish-library](https://github.com/DMTF/python-redfish-library). 


**Properties**

### Members@odata.count

**JSONPath**: `/Members@odata.count` (read only integer)

The number of members in the collection.

### Members[]

**JSONPath**: `/Members` (read only array of links)

The Members array consists of links (`@odata.id`) to the members of the collection.

