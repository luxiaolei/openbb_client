# OBBjectSONIA

OBBject with results of type SONIA

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDSONIAData]**](FREDSONIAData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_sonia import OBBjectSONIA

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSONIA from a JSON string
ob_bject_sonia_instance = OBBjectSONIA.from_json(json)
# print the JSON string representation of the object
print(OBBjectSONIA.to_json())

# convert the object into a dict
ob_bject_sonia_dict = ob_bject_sonia_instance.to_dict()
# create an instance of OBBjectSONIA from a dict
ob_bject_sonia_from_dict = OBBjectSONIA.from_dict(ob_bject_sonia_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


