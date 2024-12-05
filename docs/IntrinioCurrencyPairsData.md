# IntrinioCurrencyPairsData

Intrinio Currency Available Pairs Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**base_currency** | **str** | ISO 4217 currency code of the base currency. | 
**quote_currency** | **str** | ISO 4217 currency code of the quote currency. | 

## Example

```python
from openbb_client.models.intrinio_currency_pairs_data import IntrinioCurrencyPairsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioCurrencyPairsData from a JSON string
intrinio_currency_pairs_data_instance = IntrinioCurrencyPairsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioCurrencyPairsData.to_json())

# convert the object into a dict
intrinio_currency_pairs_data_dict = intrinio_currency_pairs_data_instance.to_dict()
# create an instance of IntrinioCurrencyPairsData from a dict
intrinio_currency_pairs_data_from_dict = IntrinioCurrencyPairsData.from_dict(intrinio_currency_pairs_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


