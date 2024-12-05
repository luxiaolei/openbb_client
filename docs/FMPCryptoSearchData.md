# FMPCryptoSearchData

FMP Crypto Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. (Crypto) | 
**name** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**exchange_name** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_crypto_search_data import FMPCryptoSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCryptoSearchData from a JSON string
fmp_crypto_search_data_instance = FMPCryptoSearchData.from_json(json)
# print the JSON string representation of the object
print(FMPCryptoSearchData.to_json())

# convert the object into a dict
fmp_crypto_search_data_dict = fmp_crypto_search_data_instance.to_dict()
# create an instance of FMPCryptoSearchData from a dict
fmp_crypto_search_data_from_dict = FMPCryptoSearchData.from_dict(fmp_crypto_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


