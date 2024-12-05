# FMPCurrencyPairsData

FMP Currency Available Pairs Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol of the currency pair. | 
**name** | **str** |  | [optional] 
**currency** | **str** | Base currency of the currency pair. | 
**stock_exchange** | **str** |  | [optional] 
**exchange_short_name** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_currency_pairs_data import FMPCurrencyPairsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCurrencyPairsData from a JSON string
fmp_currency_pairs_data_instance = FMPCurrencyPairsData.from_json(json)
# print the JSON string representation of the object
print(FMPCurrencyPairsData.to_json())

# convert the object into a dict
fmp_currency_pairs_data_dict = fmp_currency_pairs_data_instance.to_dict()
# create an instance of FMPCurrencyPairsData from a dict
fmp_currency_pairs_data_from_dict = FMPCurrencyPairsData.from_dict(fmp_currency_pairs_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


