# OBBjectSearchAttributes

OBBject with results of type SearchAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[IntrinioSearchAttributesData]**](IntrinioSearchAttributesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_search_attributes import OBBjectSearchAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSearchAttributes from a JSON string
ob_bject_search_attributes_instance = OBBjectSearchAttributes.from_json(json)
# print the JSON string representation of the object
print(OBBjectSearchAttributes.to_json())

# convert the object into a dict
ob_bject_search_attributes_dict = ob_bject_search_attributes_instance.to_dict()
# create an instance of OBBjectSearchAttributes from a dict
ob_bject_search_attributes_from_dict = OBBjectSearchAttributes.from_dict(ob_bject_search_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


