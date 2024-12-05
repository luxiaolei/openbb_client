# OBBjectCryptoHistorical

OBBject with results of type CryptoHistorical

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectCryptoHistoricalResultsInner]**](OBBjectCryptoHistoricalResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_crypto_historical import OBBjectCryptoHistorical

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCryptoHistorical from a JSON string
ob_bject_crypto_historical_instance = OBBjectCryptoHistorical.from_json(json)
# print the JSON string representation of the object
print(OBBjectCryptoHistorical.to_json())

# convert the object into a dict
ob_bject_crypto_historical_dict = ob_bject_crypto_historical_instance.to_dict()
# create an instance of OBBjectCryptoHistorical from a dict
ob_bject_crypto_historical_from_dict = OBBjectCryptoHistorical.from_dict(ob_bject_crypto_historical_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


