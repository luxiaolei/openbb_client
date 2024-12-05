# YFinanceEquityScreenerData

YFinance Equity Screener Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**price** | **float** | Last price. | 
**change** | **float** | Change in price. | 
**percent_change** | **float** | Percent change. | 
**volume** | [**Volume1**](Volume1.md) |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**previous_close** | **float** |  | [optional] 
**ma_50** | **float** |  | [optional] 
**ma_200** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**shares_outstanding** | **float** |  | [optional] 
**book_value** | **float** |  | [optional] 
**price_to_book** | **float** |  | [optional] 
**eps_ttm** | **float** |  | [optional] 
**eps_forward** | **float** |  | [optional] 
**pe_forward** | **float** |  | [optional] 
**dividend_yield** | **float** |  | [optional] 
**exchange** | **str** |  | [optional] 
**exchange_timezone** | **str** |  | [optional] 
**earnings_date** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_equity_screener_data import YFinanceEquityScreenerData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceEquityScreenerData from a JSON string
y_finance_equity_screener_data_instance = YFinanceEquityScreenerData.from_json(json)
# print the JSON string representation of the object
print(YFinanceEquityScreenerData.to_json())

# convert the object into a dict
y_finance_equity_screener_data_dict = y_finance_equity_screener_data_instance.to_dict()
# create an instance of YFinanceEquityScreenerData from a dict
y_finance_equity_screener_data_from_dict = YFinanceEquityScreenerData.from_dict(y_finance_equity_screener_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


