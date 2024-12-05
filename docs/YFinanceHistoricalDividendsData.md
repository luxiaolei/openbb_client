# YFinanceHistoricalDividendsData

YFinance Historical Dividends Data. All data is split-adjusted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_dividend_date** | **date** | The ex-dividend date - the date on which the stock begins trading without rights to the dividend. | 
**amount** | **float** | The dividend amount per share. | 

## Example

```python
from openbb_client.models.y_finance_historical_dividends_data import YFinanceHistoricalDividendsData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceHistoricalDividendsData from a JSON string
y_finance_historical_dividends_data_instance = YFinanceHistoricalDividendsData.from_json(json)
# print the JSON string representation of the object
print(YFinanceHistoricalDividendsData.to_json())

# convert the object into a dict
y_finance_historical_dividends_data_dict = y_finance_historical_dividends_data_instance.to_dict()
# create an instance of YFinanceHistoricalDividendsData from a dict
y_finance_historical_dividends_data_from_dict = YFinanceHistoricalDividendsData.from_dict(y_finance_historical_dividends_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


