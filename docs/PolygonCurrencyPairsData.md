# PolygonCurrencyPairsData

Polygon Currency Available Pairs Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**base_currency_symbol** | **str** |  | [optional] 
**base_currency_name** | **str** |  | [optional] 
**market** | **str** | Name of the trading market. Always &#39;fx&#39;. | 
**locale** | **str** | Locale of the currency pair. | 
**last_updated** | **date** |  | [optional] 
**delisted** | **date** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_currency_pairs_data import PolygonCurrencyPairsData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonCurrencyPairsData from a JSON string
polygon_currency_pairs_data_instance = PolygonCurrencyPairsData.from_json(json)
# print the JSON string representation of the object
print(PolygonCurrencyPairsData.to_json())

# convert the object into a dict
polygon_currency_pairs_data_dict = polygon_currency_pairs_data_instance.to_dict()
# create an instance of PolygonCurrencyPairsData from a dict
polygon_currency_pairs_data_from_dict = PolygonCurrencyPairsData.from_dict(polygon_currency_pairs_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


