# SecSchemaFilesData

SEC Schema Files List Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[str]** | Dictionary of URLs to SEC Schema Files | 

## Example

```python
from openbb_client.models.sec_schema_files_data import SecSchemaFilesData

# TODO update the JSON string below
json = "{}"
# create an instance of SecSchemaFilesData from a JSON string
sec_schema_files_data_instance = SecSchemaFilesData.from_json(json)
# print the JSON string representation of the object
print(SecSchemaFilesData.to_json())

# convert the object into a dict
sec_schema_files_data_dict = sec_schema_files_data_instance.to_dict()
# create an instance of SecSchemaFilesData from a dict
sec_schema_files_data_from_dict = SecSchemaFilesData.from_dict(sec_schema_files_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


