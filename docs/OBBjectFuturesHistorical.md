# OBBjectFuturesHistorical

OBBject with results of type FuturesHistorical

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFinanceFuturesHistoricalData]**](YFinanceFuturesHistoricalData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_futures_historical import OBBjectFuturesHistorical

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectFuturesHistorical from a JSON string
ob_bject_futures_historical_instance = OBBjectFuturesHistorical.from_json(json)
# print the JSON string representation of the object
print(OBBjectFuturesHistorical.to_json())

# convert the object into a dict
ob_bject_futures_historical_dict = ob_bject_futures_historical_instance.to_dict()
# create an instance of OBBjectFuturesHistorical from a dict
ob_bject_futures_historical_from_dict = OBBjectFuturesHistorical.from_dict(ob_bject_futures_historical_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


