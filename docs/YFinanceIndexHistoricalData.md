# YFinanceIndexHistoricalData

YFinance Index Historical Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_index_historical_data import YFinanceIndexHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceIndexHistoricalData from a JSON string
y_finance_index_historical_data_instance = YFinanceIndexHistoricalData.from_json(json)
# print the JSON string representation of the object
print(YFinanceIndexHistoricalData.to_json())

# convert the object into a dict
y_finance_index_historical_data_dict = y_finance_index_historical_data_instance.to_dict()
# create an instance of YFinanceIndexHistoricalData from a dict
y_finance_index_historical_data_from_dict = YFinanceIndexHistoricalData.from_dict(y_finance_index_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


