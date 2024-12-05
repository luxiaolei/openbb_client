# OBBjectTipsYields

OBBject with results of type TipsYields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredTipsYieldsData]**](FredTipsYieldsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_tips_yields import OBBjectTipsYields

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectTipsYields from a JSON string
ob_bject_tips_yields_instance = OBBjectTipsYields.from_json(json)
# print the JSON string representation of the object
print(OBBjectTipsYields.to_json())

# convert the object into a dict
ob_bject_tips_yields_dict = ob_bject_tips_yields_instance.to_dict()
# create an instance of OBBjectTipsYields from a dict
ob_bject_tips_yields_from_dict = OBBjectTipsYields.from_dict(ob_bject_tips_yields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


