# OBBjectAvailableIndices

OBBject with results of type AvailableIndices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectAvailableIndicesResultsInner]**](OBBjectAvailableIndicesResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_available_indices import OBBjectAvailableIndices

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectAvailableIndices from a JSON string
ob_bject_available_indices_instance = OBBjectAvailableIndices.from_json(json)
# print the JSON string representation of the object
print(OBBjectAvailableIndices.to_json())

# convert the object into a dict
ob_bject_available_indices_dict = ob_bject_available_indices_instance.to_dict()
# create an instance of OBBjectAvailableIndices from a dict
ob_bject_available_indices_from_dict = OBBjectAvailableIndices.from_dict(ob_bject_available_indices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


