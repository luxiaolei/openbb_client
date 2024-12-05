# IntrinioHistoricalMarketCapData

Intrinio Historical MarketCap Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**market_cap** | [**MarketCap**](MarketCap.md) |  | 

## Example

```python
from openbb_client.models.intrinio_historical_market_cap_data import IntrinioHistoricalMarketCapData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioHistoricalMarketCapData from a JSON string
intrinio_historical_market_cap_data_instance = IntrinioHistoricalMarketCapData.from_json(json)
# print the JSON string representation of the object
print(IntrinioHistoricalMarketCapData.to_json())

# convert the object into a dict
intrinio_historical_market_cap_data_dict = intrinio_historical_market_cap_data_instance.to_dict()
# create an instance of IntrinioHistoricalMarketCapData from a dict
intrinio_historical_market_cap_data_from_dict = IntrinioHistoricalMarketCapData.from_dict(intrinio_historical_market_cap_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


