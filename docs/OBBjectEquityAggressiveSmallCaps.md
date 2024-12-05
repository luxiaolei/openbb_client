# OBBjectEquityAggressiveSmallCaps

OBBject with results of type EquityAggressiveSmallCaps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFAggressiveSmallCapsData]**](YFAggressiveSmallCapsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_aggressive_small_caps import OBBjectEquityAggressiveSmallCaps

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityAggressiveSmallCaps from a JSON string
ob_bject_equity_aggressive_small_caps_instance = OBBjectEquityAggressiveSmallCaps.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityAggressiveSmallCaps.to_json())

# convert the object into a dict
ob_bject_equity_aggressive_small_caps_dict = ob_bject_equity_aggressive_small_caps_instance.to_dict()
# create an instance of OBBjectEquityAggressiveSmallCaps from a dict
ob_bject_equity_aggressive_small_caps_from_dict = OBBjectEquityAggressiveSmallCaps.from_dict(ob_bject_equity_aggressive_small_caps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


