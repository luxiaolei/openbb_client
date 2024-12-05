# FredReleaseTableData

FRED Release Table Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**level** | **int** |  | [optional] 
**element_type** | **str** |  | [optional] 
**line** | **int** |  | [optional] 
**element_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**children** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_release_table_data import FredReleaseTableData

# TODO update the JSON string below
json = "{}"
# create an instance of FredReleaseTableData from a JSON string
fred_release_table_data_instance = FredReleaseTableData.from_json(json)
# print the JSON string representation of the object
print(FredReleaseTableData.to_json())

# convert the object into a dict
fred_release_table_data_dict = fred_release_table_data_instance.to_dict()
# create an instance of FredReleaseTableData from a dict
fred_release_table_data_from_dict = FredReleaseTableData.from_dict(fred_release_table_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


