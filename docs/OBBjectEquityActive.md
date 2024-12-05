# OBBjectEquityActive

OBBject with results of type EquityActive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFActiveData]**](YFActiveData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_active import OBBjectEquityActive

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityActive from a JSON string
ob_bject_equity_active_instance = OBBjectEquityActive.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityActive.to_json())

# convert the object into a dict
ob_bject_equity_active_dict = ob_bject_equity_active_instance.to_dict()
# create an instance of OBBjectEquityActive from a dict
ob_bject_equity_active_from_dict = OBBjectEquityActive.from_dict(ob_bject_equity_active_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


