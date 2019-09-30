# Introduction

The iLO Amplifier Pack RESTful API is a programming interface enabling state-of-the-art server management. This document contains helpful information about how to interact with the iLO Amplifier Pack RESTful API. The iLO Amplifier Pack RESTful API uses basic HTTP operations (GET, PUT, POST, DELETE, and PATCH) to submit or return a JSON formatted resource to or from a URI on iLO Amplifier Pack.

With modern scripting languages, you can easily write simple REST clients for RESTful APIs. Most languages, like Python, can transform JSON into internal-data structures, like dictionaries, allowing for easy access to data. This enables you to write custom code directly to the iLO Amplifier Pack RESTful API.
 
## Redfish Compliance

iLO Amplifier Pack implements the RESTful API as per Redfish Scalable Platforms API specification v1.4.0 [DSP0266](https://www.dmtf.org/sites/default/files/DSP0266_1.4.0.pdf). 


## RESTful APIs Architected Using Redfish®

The Redfish® Scalable Platforms Management API ("Redfish") is a standard that uses RESTful interface semantics to access data defined in model format to perform systems management. It is suitable for a wide range of servers, from stand-alone servers to rack mount and bladed environments, but it also scales equally well for large scale server environments.

The Redfish® standard API is designed to deliver simple and secure management for converged, hybrid IT and the Software Defined Data Center (SDDC). Both human readable and machine capable, Redfish leverages common Internet and web services standards to expose information directly to the modern tool chain.

## Key benefits of the iLO Amplifier Pack RESTful API

* Based on Redfish APIs which provides an interface using JSON Payload and Entity Data Model.
* Separation of protocol from the data model.
* Leverages the strength of Internet Protocol standards such as JSON, HTTP, OData, etc.
* Aggregated access of basic and detailed inventory of servers managed by iLO Amplifier Pack.
* Simplifies permforming actions on multiple servers and federation groups.
* Simplifies update management tasks on multiple servers.
