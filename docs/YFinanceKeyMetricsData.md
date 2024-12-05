# YFinanceKeyMetricsData

YFinance Key Metrics Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**pe_ratio** | **float** |  | [optional] 
**forward_pe** | **float** |  | [optional] 
**peg_ratio** | **float** |  | [optional] 
**peg_ratio_ttm** | **float** |  | [optional] 
**eps_ttm** | **float** |  | [optional] 
**eps_forward** | **float** |  | [optional] 
**enterprise_to_ebitda** | **float** |  | [optional] 
**earnings_growth** | **float** |  | [optional] 
**earnings_growth_quarterly** | **float** |  | [optional] 
**revenue_per_share** | **float** |  | [optional] 
**revenue_growth** | **float** |  | [optional] 
**enterprise_to_revenue** | **float** |  | [optional] 
**cash_per_share** | **float** |  | [optional] 
**quick_ratio** | **float** |  | [optional] 
**current_ratio** | **float** |  | [optional] 
**debt_to_equity** | **float** |  | [optional] 
**gross_margin** | **float** |  | [optional] 
**operating_margin** | **float** |  | [optional] 
**ebitda_margin** | **float** |  | [optional] 
**profit_margin** | **float** |  | [optional] 
**return_on_assets** | **float** |  | [optional] 
**return_on_equity** | **float** |  | [optional] 
**dividend_yield** | **float** |  | [optional] 
**dividend_yield_5y_avg** | **float** |  | [optional] 
**payout_ratio** | **float** |  | [optional] 
**book_value** | **float** |  | [optional] 
**price_to_book** | **float** |  | [optional] 
**enterprise_value** | **int** |  | [optional] 
**overall_risk** | **float** |  | [optional] 
**audit_risk** | **float** |  | [optional] 
**board_risk** | **float** |  | [optional] 
**compensation_risk** | **float** |  | [optional] 
**shareholder_rights_risk** | **float** |  | [optional] 
**beta** | **float** |  | [optional] 
**price_return_1y** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_key_metrics_data import YFinanceKeyMetricsData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceKeyMetricsData from a JSON string
y_finance_key_metrics_data_instance = YFinanceKeyMetricsData.from_json(json)
# print the JSON string representation of the object
print(YFinanceKeyMetricsData.to_json())

# convert the object into a dict
y_finance_key_metrics_data_dict = y_finance_key_metrics_data_instance.to_dict()
# create an instance of YFinanceKeyMetricsData from a dict
y_finance_key_metrics_data_from_dict = YFinanceKeyMetricsData.from_dict(y_finance_key_metrics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


