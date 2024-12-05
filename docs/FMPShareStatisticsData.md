# FMPShareStatisticsData

FMP Share Statistics Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**var_date** | **date** |  | [optional] 
**free_float** | **float** |  | [optional] 
**float_shares** | **float** |  | [optional] 
**outstanding_shares** | **float** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_share_statistics_data import FMPShareStatisticsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPShareStatisticsData from a JSON string
fmp_share_statistics_data_instance = FMPShareStatisticsData.from_json(json)
# print the JSON string representation of the object
print(FMPShareStatisticsData.to_json())

# convert the object into a dict
fmp_share_statistics_data_dict = fmp_share_statistics_data_instance.to_dict()
# create an instance of FMPShareStatisticsData from a dict
fmp_share_statistics_data_from_dict = FMPShareStatisticsData.from_dict(fmp_share_statistics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


