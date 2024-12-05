# OBBjectInsiderTrading

OBBject with results of type InsiderTrading

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectInsiderTradingResultsInner]**](OBBjectInsiderTradingResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_insider_trading import OBBjectInsiderTrading

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectInsiderTrading from a JSON string
ob_bject_insider_trading_instance = OBBjectInsiderTrading.from_json(json)
# print the JSON string representation of the object
print(OBBjectInsiderTrading.to_json())

# convert the object into a dict
ob_bject_insider_trading_dict = ob_bject_insider_trading_instance.to_dict()
# create an instance of OBBjectInsiderTrading from a dict
ob_bject_insider_trading_from_dict = OBBjectInsiderTrading.from_dict(ob_bject_insider_trading_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


