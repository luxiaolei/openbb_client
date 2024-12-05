# FmpHistoricalMarketCapData

FMP Historical Market Cap Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**market_cap** | [**MarketCap**](MarketCap.md) |  | 

## Example

```python
from openbb_client.models.fmp_historical_market_cap_data import FmpHistoricalMarketCapData

# TODO update the JSON string below
json = "{}"
# create an instance of FmpHistoricalMarketCapData from a JSON string
fmp_historical_market_cap_data_instance = FmpHistoricalMarketCapData.from_json(json)
# print the JSON string representation of the object
print(FmpHistoricalMarketCapData.to_json())

# convert the object into a dict
fmp_historical_market_cap_data_dict = fmp_historical_market_cap_data_instance.to_dict()
# create an instance of FmpHistoricalMarketCapData from a dict
fmp_historical_market_cap_data_from_dict = FmpHistoricalMarketCapData.from_dict(fmp_historical_market_cap_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


