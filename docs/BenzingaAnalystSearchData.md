# BenzingaAnalystSearchData

Benzinga Analyst Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated** | **datetime** |  | [optional] 
**firm_name** | **str** |  | [optional] 
**name_first** | **str** |  | [optional] 
**name_last** | **str** |  | [optional] 
**name_full** | **str** | Analyst full name. | 
**analyst_id** | **str** |  | [optional] 
**firm_id** | **str** |  | [optional] 
**smart_score** | **float** |  | [optional] 
**overall_success_rate** | **float** |  | [optional] 
**overall_avg_return_percentile** | **float** |  | [optional] 
**total_ratings_percentile** | **float** |  | [optional] 
**total_ratings** | **int** |  | [optional] 
**overall_gain_count** | **int** |  | [optional] 
**overall_loss_count** | **int** |  | [optional] 
**overall_average_return** | **float** |  | [optional] 
**overall_std_dev** | **float** |  | [optional] 
**gain_count_1m** | **int** |  | [optional] 
**loss_count_1m** | **int** |  | [optional] 
**average_return_1m** | **float** |  | [optional] 
**std_dev_1m** | **float** |  | [optional] 
**smart_score_1m** | **float** |  | [optional] 
**success_rate_1m** | **float** |  | [optional] 
**gain_count_3m** | **int** |  | [optional] 
**loss_count_3m** | **int** |  | [optional] 
**average_return_3m** | **float** |  | [optional] 
**std_dev_3m** | **float** |  | [optional] 
**smart_score_3m** | **float** |  | [optional] 
**success_rate_3m** | **float** |  | [optional] 
**gain_count_6m** | **int** |  | [optional] 
**loss_count_6m** | **int** |  | [optional] 
**average_return_6m** | **float** |  | [optional] 
**std_dev_6m** | **float** |  | [optional] 
**gain_count_9m** | **int** |  | [optional] 
**loss_count_9m** | **int** |  | [optional] 
**average_return_9m** | **float** |  | [optional] 
**std_dev_9m** | **float** |  | [optional] 
**smart_score_9m** | **float** |  | [optional] 
**success_rate_9m** | **float** |  | [optional] 
**gain_count_1y** | **int** |  | [optional] 
**loss_count_1y** | **int** |  | [optional] 
**average_return_1y** | **float** |  | [optional] 
**std_dev_1y** | **float** |  | [optional] 
**smart_score_1y** | **float** |  | [optional] 
**success_rate_1y** | **float** |  | [optional] 
**gain_count_2y** | **int** |  | [optional] 
**loss_count_2y** | **int** |  | [optional] 
**average_return_2y** | **float** |  | [optional] 
**std_dev_2y** | **float** |  | [optional] 
**smart_score_2y** | **float** |  | [optional] 
**success_rate_2y** | **float** |  | [optional] 
**gain_count_3y** | **int** |  | [optional] 
**loss_count_3y** | **int** |  | [optional] 
**average_return_3y** | **float** |  | [optional] 
**std_dev_3y** | **float** |  | [optional] 
**smart_score_3y** | **float** |  | [optional] 
**success_rate_3y** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.benzinga_analyst_search_data import BenzingaAnalystSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of BenzingaAnalystSearchData from a JSON string
benzinga_analyst_search_data_instance = BenzingaAnalystSearchData.from_json(json)
# print the JSON string representation of the object
print(BenzingaAnalystSearchData.to_json())

# convert the object into a dict
benzinga_analyst_search_data_dict = benzinga_analyst_search_data_instance.to_dict()
# create an instance of BenzingaAnalystSearchData from a dict
benzinga_analyst_search_data_from_dict = BenzingaAnalystSearchData.from_dict(benzinga_analyst_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


