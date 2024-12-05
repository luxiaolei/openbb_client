# FMPKeyMetricsData

FMP Key Metrics Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**pe_ratio** | **float** |  | [optional] 
**period_ending** | **date** | Period ending date. | 
**fiscal_period** | **str** | Period of the data. | 
**calendar_year** | **int** |  | [optional] 
**revenue_per_share** | **float** |  | [optional] 
**capex_per_share** | **float** |  | [optional] 
**net_income_per_share** | **float** |  | [optional] 
**operating_cash_flow_per_share** | **float** |  | [optional] 
**free_cash_flow_per_share** | **float** |  | [optional] 
**cash_per_share** | **float** |  | [optional] 
**book_value_per_share** | **float** |  | [optional] 
**tangible_book_value_per_share** | **float** |  | [optional] 
**shareholders_equity_per_share** | **float** |  | [optional] 
**interest_debt_per_share** | **float** |  | [optional] 
**price_to_sales** | **float** |  | [optional] 
**price_to_operating_cash_flow** | **float** |  | [optional] 
**price_to_free_cash_flow** | **float** |  | [optional] 
**price_to_book** | **float** |  | [optional] 
**price_to_tangible_book** | **float** |  | [optional] 
**ev_to_sales** | **float** |  | [optional] 
**ev_to_ebitda** | **float** |  | [optional] 
**ev_to_operating_cash_flow** | **float** |  | [optional] 
**ev_to_free_cash_flow** | **float** |  | [optional] 
**earnings_yield** | **float** |  | [optional] 
**free_cash_flow_yield** | **float** |  | [optional] 
**debt_to_market_cap** | **float** |  | [optional] 
**debt_to_equity** | **float** |  | [optional] 
**debt_to_assets** | **float** |  | [optional] 
**net_debt_to_ebitda** | **float** |  | [optional] 
**current_ratio** | **float** |  | [optional] 
**interest_coverage** | **float** |  | [optional] 
**income_quality** | **float** |  | [optional] 
**payout_ratio** | **float** |  | [optional] 
**sales_general_and_administrative_to_revenue** | **float** |  | [optional] 
**research_and_developement_to_revenue** | **float** |  | [optional] 
**intangibles_to_total_assets** | **float** |  | [optional] 
**capex_to_operating_cash_flow** | **float** |  | [optional] 
**capex_to_revenue** | **float** |  | [optional] 
**capex_to_depreciation** | **float** |  | [optional] 
**stock_based_compensation_to_revenue** | **float** |  | [optional] 
**working_capital** | **float** |  | [optional] 
**tangible_asset_value** | **float** |  | [optional] 
**net_current_asset_value** | **float** |  | [optional] 
**enterprise_value** | **float** |  | [optional] 
**invested_capital** | **float** |  | [optional] 
**average_receivables** | **float** |  | [optional] 
**average_payables** | **float** |  | [optional] 
**average_inventory** | **float** |  | [optional] 
**days_sales_outstanding** | **float** |  | [optional] 
**days_payables_outstanding** | **float** |  | [optional] 
**days_of_inventory_on_hand** | **float** |  | [optional] 
**receivables_turnover** | **float** |  | [optional] 
**payables_turnover** | **float** |  | [optional] 
**inventory_turnover** | **float** |  | [optional] 
**return_on_equity** | **float** |  | [optional] 
**return_on_invested_capital** | **float** |  | [optional] 
**return_on_tangible_assets** | **float** |  | [optional] 
**dividend_yield** | **float** |  | [optional] 
**graham_number** | **float** |  | [optional] 
**graham_net_net** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_key_metrics_data import FMPKeyMetricsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPKeyMetricsData from a JSON string
fmp_key_metrics_data_instance = FMPKeyMetricsData.from_json(json)
# print the JSON string representation of the object
print(FMPKeyMetricsData.to_json())

# convert the object into a dict
fmp_key_metrics_data_dict = fmp_key_metrics_data_instance.to_dict()
# create an instance of FMPKeyMetricsData from a dict
fmp_key_metrics_data_from_dict = FMPKeyMetricsData.from_dict(fmp_key_metrics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


