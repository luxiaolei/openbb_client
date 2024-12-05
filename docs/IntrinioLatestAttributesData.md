# IntrinioLatestAttributesData

Intrinio Latest Attributes Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**tag** | **str** |  | [optional] 
**value** | [**Value7**](Value7.md) |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_latest_attributes_data import IntrinioLatestAttributesData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioLatestAttributesData from a JSON string
intrinio_latest_attributes_data_instance = IntrinioLatestAttributesData.from_json(json)
# print the JSON string representation of the object
print(IntrinioLatestAttributesData.to_json())

# convert the object into a dict
intrinio_latest_attributes_data_dict = intrinio_latest_attributes_data_instance.to_dict()
# create an instance of IntrinioLatestAttributesData from a dict
intrinio_latest_attributes_data_from_dict = IntrinioLatestAttributesData.from_dict(intrinio_latest_attributes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


