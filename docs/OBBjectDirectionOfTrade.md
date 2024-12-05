# OBBjectDirectionOfTrade

OBBject with results of type DirectionOfTrade

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[ImfDirectionOfTradeData]**](ImfDirectionOfTradeData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_direction_of_trade import OBBjectDirectionOfTrade

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectDirectionOfTrade from a JSON string
ob_bject_direction_of_trade_instance = OBBjectDirectionOfTrade.from_json(json)
# print the JSON string representation of the object
print(OBBjectDirectionOfTrade.to_json())

# convert the object into a dict
ob_bject_direction_of_trade_dict = ob_bject_direction_of_trade_instance.to_dict()
# create an instance of OBBjectDirectionOfTrade from a dict
ob_bject_direction_of_trade_from_dict = OBBjectDirectionOfTrade.from_dict(ob_bject_direction_of_trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


