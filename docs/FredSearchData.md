# FredSearchData

FRED Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_id** | **str** |  | [optional] 
**series_id** | **str** |  | [optional] 
**series_group** | **str** |  | [optional] 
**region_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**observation_start** | **date** |  | [optional] 
**observation_end** | **date** |  | [optional] 
**frequency** | **str** |  | [optional] 
**frequency_short** | **str** |  | [optional] 
**units** | **str** |  | [optional] 
**units_short** | **str** |  | [optional] 
**seasonal_adjustment** | **str** |  | [optional] 
**seasonal_adjustment_short** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**popularity** | **int** |  | [optional] 
**group_popularity** | **int** |  | [optional] 
**realtime_start** | **date** |  | [optional] 
**realtime_end** | **date** |  | [optional] 
**notes** | **str** |  | [optional] 
**press_release** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fred_search_data import FredSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of FredSearchData from a JSON string
fred_search_data_instance = FredSearchData.from_json(json)
# print the JSON string representation of the object
print(FredSearchData.to_json())

# convert the object into a dict
fred_search_data_dict = fred_search_data_instance.to_dict()
# create an instance of FredSearchData from a dict
fred_search_data_from_dict = FredSearchData.from_dict(fred_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


