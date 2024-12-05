# OBBjectKeyExecutives

OBBject with results of type KeyExecutives

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectKeyExecutivesResultsInner]**](OBBjectKeyExecutivesResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_key_executives import OBBjectKeyExecutives

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectKeyExecutives from a JSON string
ob_bject_key_executives_instance = OBBjectKeyExecutives.from_json(json)
# print the JSON string representation of the object
print(OBBjectKeyExecutives.to_json())

# convert the object into a dict
ob_bject_key_executives_dict = ob_bject_key_executives_instance.to_dict()
# create an instance of OBBjectKeyExecutives from a dict
ob_bject_key_executives_from_dict = OBBjectKeyExecutives.from_dict(ob_bject_key_executives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


