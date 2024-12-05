# OBBjectHistoricalMarketCapResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**market_cap** | [**MarketCap**](MarketCap.md) |  | 

## Example

```python
from openbb_client.models.ob_bject_historical_market_cap_results_inner import OBBjectHistoricalMarketCapResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectHistoricalMarketCapResultsInner from a JSON string
ob_bject_historical_market_cap_results_inner_instance = OBBjectHistoricalMarketCapResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectHistoricalMarketCapResultsInner.to_json())

# convert the object into a dict
ob_bject_historical_market_cap_results_inner_dict = ob_bject_historical_market_cap_results_inner_instance.to_dict()
# create an instance of OBBjectHistoricalMarketCapResultsInner from a dict
ob_bject_historical_market_cap_results_inner_from_dict = OBBjectHistoricalMarketCapResultsInner.from_dict(ob_bject_historical_market_cap_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


