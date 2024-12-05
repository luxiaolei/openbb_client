# IntrinioSearchAttributesData

Intrinio Search Attributes Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the financial attribute. | 
**name** | **str** | Name of the financial attribute. | 
**tag** | **str** | Tag of the financial attribute. | 
**statement_code** | **str** | Code of the financial statement. | 
**statement_type** | **str** |  | [optional] 
**parent_name** | **str** |  | [optional] 
**sequence** | **int** |  | [optional] 
**factor** | **str** |  | [optional] 
**transaction** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_search_attributes_data import IntrinioSearchAttributesData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioSearchAttributesData from a JSON string
intrinio_search_attributes_data_instance = IntrinioSearchAttributesData.from_json(json)
# print the JSON string representation of the object
print(IntrinioSearchAttributesData.to_json())

# convert the object into a dict
intrinio_search_attributes_data_dict = intrinio_search_attributes_data_instance.to_dict()
# create an instance of IntrinioSearchAttributesData from a dict
intrinio_search_attributes_data_from_dict = IntrinioSearchAttributesData.from_dict(intrinio_search_attributes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


