# OBBjectForm13FHR

OBBject with results of type Form13FHR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[SecForm13FHRData]**](SecForm13FHRData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_form13_fhr import OBBjectForm13FHR

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectForm13FHR from a JSON string
ob_bject_form13_fhr_instance = OBBjectForm13FHR.from_json(json)
# print the JSON string representation of the object
print(OBBjectForm13FHR.to_json())

# convert the object into a dict
ob_bject_form13_fhr_dict = ob_bject_form13_fhr_instance.to_dict()
# create an instance of OBBjectForm13FHR from a dict
ob_bject_form13_fhr_from_dict = OBBjectForm13FHR.from_dict(ob_bject_form13_fhr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


