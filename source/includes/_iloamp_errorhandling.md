# Error messages and registries

> HTTP response 400

```json
{
    "@odata.type": "#ExtendedInfo.1.0.0.ExtendedInfo",
    "error": {
        "@Message.ExtendedInfo": [
            {
                "@odata.type": "#Message.1.0.0.Message",
                "MessageId": "HpeWolfram.1.0.InvalidActivationKey"
            }
        ],
        "code": "Wolfram.1.0.ExtendedInfo",
        "message": "See @Message.ExtendedInfo for more information."
    }
}
```

```
"InvalidActivationKey": {
    "Description": "Invalid Activation Key",
    "Message": "Invalid Activation Key",
    "Severity": "Warning",
    "NumberOfArgs": 0,
    "ParamTypes": [],
    "Resolution": "Retry Installation with a valid Activation Key"
}
```

Error messages appear in iLO Amplifier Pack RESTful API as an immediate response to an HTTP operation. 

All error cases use a basic error JSON structure called `ExtendedInfo`.  The most important property in `ExtendedInfo` is `MessageId`, a string containing a lookup key into a message registry.

`MessageId` helps to keep the iLO Amplifier Pack service small by keeping much of the explanatory text for an error out of the code. Instead, iLO Amplifier Pack supplies an `ExtendedInfo` response, where the `MessageId` provides enough information so that you can look up more details from another file.

For example, if you `POST` to the iLO Amplifier Pack license service to install an iLO Amplifier Pack license, but you supply an incorrect `LicenceKey` string, iLO Amplifier Pack responds with an error similar to the following:

HTTP response 400 is the standard RESTful API response to an error. In the example above, the error is easy to understand, but some errors are not easy to understand. To display a more meaningful error message, parse the string `HpeWolfram.1.0.InvalidActivationKey` into the following
components:

* `HpeWolfram.1.0`—This is the base name of the message registry to consult. Look for a matching registry file.
* `InvalidActivationKey`—This is the lookup key into the message registry.

The search returns a result similar to the following:

Many error messages can also return parameters. These parameters may be plugged into the
strings in the registry to form detailed messages tailored to the instance of the error message.







