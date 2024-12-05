# YFinanceShareStatisticsData

YFinance Share Statistics Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**var_date** | **date** |  | [optional] 
**free_float** | **float** |  | [optional] 
**float_shares** | **float** |  | [optional] 
**outstanding_shares** | **float** |  | [optional] 
**source** | **str** |  | [optional] 
**implied_shares_outstanding** | **int** |  | [optional] 
**short_interest** | **int** |  | [optional] 
**short_percent_of_float** | **float** |  | [optional] 
**days_to_cover** | **float** |  | [optional] 
**short_interest_prev_month** | **int** |  | [optional] 
**short_interest_prev_date** | **date** |  | [optional] 
**insider_ownership** | **float** |  | [optional] 
**institution_ownership** | **float** |  | [optional] 
**institution_float_ownership** | **float** |  | [optional] 
**institutions_count** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_share_statistics_data import YFinanceShareStatisticsData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceShareStatisticsData from a JSON string
y_finance_share_statistics_data_instance = YFinanceShareStatisticsData.from_json(json)
# print the JSON string representation of the object
print(YFinanceShareStatisticsData.to_json())

# convert the object into a dict
y_finance_share_statistics_data_dict = y_finance_share_statistics_data_instance.to_dict()
# create an instance of YFinanceShareStatisticsData from a dict
y_finance_share_statistics_data_from_dict = YFinanceShareStatisticsData.from_dict(y_finance_share_statistics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


