# OBBjectHistoricalMarketCap

OBBject with results of type HistoricalMarketCap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectHistoricalMarketCapResultsInner]**](OBBjectHistoricalMarketCapResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_historical_market_cap import OBBjectHistoricalMarketCap

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectHistoricalMarketCap from a JSON string
ob_bject_historical_market_cap_instance = OBBjectHistoricalMarketCap.from_json(json)
# print the JSON string representation of the object
print(OBBjectHistoricalMarketCap.to_json())

# convert the object into a dict
ob_bject_historical_market_cap_dict = ob_bject_historical_market_cap_instance.to_dict()
# create an instance of OBBjectHistoricalMarketCap from a dict
ob_bject_historical_market_cap_from_dict = OBBjectHistoricalMarketCap.from_dict(ob_bject_historical_market_cap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


