# OBBjectSchemaFiles

OBBject with results of type SchemaFiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**SecSchemaFilesData**](SecSchemaFilesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_schema_files import OBBjectSchemaFiles

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSchemaFiles from a JSON string
ob_bject_schema_files_instance = OBBjectSchemaFiles.from_json(json)
# print the JSON string representation of the object
print(OBBjectSchemaFiles.to_json())

# convert the object into a dict
ob_bject_schema_files_dict = ob_bject_schema_files_instance.to_dict()
# create an instance of OBBjectSchemaFiles from a dict
ob_bject_schema_files_from_dict = OBBjectSchemaFiles.from_dict(ob_bject_schema_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


