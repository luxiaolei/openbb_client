# OBBjectEquityScreenerResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**price** | **float** |  | 
**change** | **float** | Change in price. | 
**percent_change** | **float** | Percent change. | 
**volume** | **int** |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**previous_close** | **float** |  | [optional] 
**ma_50** | **float** |  | [optional] 
**ma_200** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**market_cap** | **int** |  | [optional] 
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
**sector** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**beta** | **float** |  | [optional] 
**last_annual_dividend** | **float** |  | [optional] 
**exchange_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**is_etf** | **bool** |  | [optional] 
**actively_trading** | **bool** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_screener_results_inner import OBBjectEquityScreenerResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityScreenerResultsInner from a JSON string
ob_bject_equity_screener_results_inner_instance = OBBjectEquityScreenerResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityScreenerResultsInner.to_json())

# convert the object into a dict
ob_bject_equity_screener_results_inner_dict = ob_bject_equity_screener_results_inner_instance.to_dict()
# create an instance of OBBjectEquityScreenerResultsInner from a dict
ob_bject_equity_screener_results_inner_from_dict = OBBjectEquityScreenerResultsInner.from_dict(ob_bject_equity_screener_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


