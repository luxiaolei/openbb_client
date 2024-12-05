# FMPIndexConstituentsData

FMP Index Constituents Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**sector** | **str** | Sector the constituent company in the index belongs to. | 
**sub_sector** | **str** |  | [optional] 
**headquarter** | **str** |  | [optional] 
**date_first_added** | [**DateFirstAdded**](DateFirstAdded.md) |  | [optional] 
**cik** | **int** |  | [optional] 
**founded** | [**Founded**](Founded.md) |  | [optional] 

## Example

```python
from openbb_client.models.fmp_index_constituents_data import FMPIndexConstituentsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPIndexConstituentsData from a JSON string
fmp_index_constituents_data_instance = FMPIndexConstituentsData.from_json(json)
# print the JSON string representation of the object
print(FMPIndexConstituentsData.to_json())

# convert the object into a dict
fmp_index_constituents_data_dict = fmp_index_constituents_data_instance.to_dict()
# create an instance of FMPIndexConstituentsData from a dict
fmp_index_constituents_data_from_dict = FMPIndexConstituentsData.from_dict(fmp_index_constituents_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


