# OBBjectCOT

OBBject with results of type COT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[CftcCotData]**](CftcCotData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_cot import OBBjectCOT

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCOT from a JSON string
ob_bject_cot_instance = OBBjectCOT.from_json(json)
# print the JSON string representation of the object
print(OBBjectCOT.to_json())

# convert the object into a dict
ob_bject_cot_dict = ob_bject_cot_instance.to_dict()
# create an instance of OBBjectCOT from a dict
ob_bject_cot_from_dict = OBBjectCOT.from_dict(ob_bject_cot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


