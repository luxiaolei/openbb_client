# IntrinioShareStatisticsData

Intrinio Share Statistics Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**var_date** | **date** |  | [optional] 
**free_float** | **float** |  | [optional] 
**float_shares** | **float** |  | [optional] 
**outstanding_shares** | **float** |  | [optional] 
**source** | **str** |  | [optional] 
**adjusted_outstanding_shares** | **float** |  | [optional] 
**public_float** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_share_statistics_data import IntrinioShareStatisticsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioShareStatisticsData from a JSON string
intrinio_share_statistics_data_instance = IntrinioShareStatisticsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioShareStatisticsData.to_json())

# convert the object into a dict
intrinio_share_statistics_data_dict = intrinio_share_statistics_data_instance.to_dict()
# create an instance of IntrinioShareStatisticsData from a dict
intrinio_share_statistics_data_from_dict = IntrinioShareStatisticsData.from_dict(intrinio_share_statistics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


