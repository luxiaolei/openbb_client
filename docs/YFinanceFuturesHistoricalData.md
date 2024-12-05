# YFinanceFuturesHistoricalData

Yahoo Finance Futures Historical Price Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. | 
**open** | **float** | The open price. | 
**high** | **float** | The high price. | 
**low** | **float** | The low price. | 
**close** | **float** | The close price. | 
**volume** | **float** | The trading volume. | 

## Example

```python
from openbb_client.models.y_finance_futures_historical_data import YFinanceFuturesHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceFuturesHistoricalData from a JSON string
y_finance_futures_historical_data_instance = YFinanceFuturesHistoricalData.from_json(json)
# print the JSON string representation of the object
print(YFinanceFuturesHistoricalData.to_json())

# convert the object into a dict
y_finance_futures_historical_data_dict = y_finance_futures_historical_data_instance.to_dict()
# create an instance of YFinanceFuturesHistoricalData from a dict
y_finance_futures_historical_data_from_dict = YFinanceFuturesHistoricalData.from_dict(y_finance_futures_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


