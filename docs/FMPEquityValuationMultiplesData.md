# FMPEquityValuationMultiplesData

FMP Equity Valuation Multiples Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**revenue_per_share_ttm** | **float** |  | [optional] 
**net_income_per_share_ttm** | **float** |  | [optional] 
**operating_cash_flow_per_share_ttm** | **float** |  | [optional] 
**free_cash_flow_per_share_ttm** | **float** |  | [optional] 
**cash_per_share_ttm** | **float** |  | [optional] 
**book_value_per_share_ttm** | **float** |  | [optional] 
**tangible_book_value_per_share_ttm** | **float** |  | [optional] 
**shareholders_equity_per_share_ttm** | **float** |  | [optional] 
**interest_debt_per_share_ttm** | **float** |  | [optional] 
**market_cap_ttm** | **float** |  | [optional] 
**enterprise_value_ttm** | **float** |  | [optional] 
**pe_ratio_ttm** | **float** |  | [optional] 
**price_to_sales_ratio_ttm** | **float** |  | [optional] 
**pocf_ratio_ttm** | **float** |  | [optional] 
**pfcf_ratio_ttm** | **float** |  | [optional] 
**pb_ratio_ttm** | **float** |  | [optional] 
**ptb_ratio_ttm** | **float** |  | [optional] 
**ev_to_sales_ttm** | **float** |  | [optional] 
**enterprise_value_over_ebitda_ttm** | **float** |  | [optional] 
**ev_to_operating_cash_flow_ttm** | **float** |  | [optional] 
**ev_to_free_cash_flow_ttm** | **float** |  | [optional] 
**earnings_yield_ttm** | **float** |  | [optional] 
**free_cash_flow_yield_ttm** | **float** |  | [optional] 
**debt_to_equity_ttm** | **float** |  | [optional] 
**debt_to_assets_ttm** | **float** |  | [optional] 
**net_debt_to_ebitda_ttm** | **float** |  | [optional] 
**current_ratio_ttm** | **float** |  | [optional] 
**interest_coverage_ttm** | **float** |  | [optional] 
**income_quality_ttm** | **float** |  | [optional] 
**dividend_yield_ttm** | **float** |  | [optional] 
**dividend_yield_percentage_ttm** | **float** |  | [optional] 
**dividend_to_market_cap_ttm** | **float** |  | [optional] 
**dividend_per_share_ttm** | **float** |  | [optional] 
**payout_ratio_ttm** | **float** |  | [optional] 
**sales_general_and_administrative_to_revenue_ttm** | **float** |  | [optional] 
**research_and_development_to_revenue_ttm** | **float** |  | [optional] 
**intangibles_to_total_assets_ttm** | **float** |  | [optional] 
**capex_to_operating_cash_flow_ttm** | **float** |  | [optional] 
**capex_to_revenue_ttm** | **float** |  | [optional] 
**capex_to_depreciation_ttm** | **float** |  | [optional] 
**stock_based_compensation_to_revenue_ttm** | **float** |  | [optional] 
**graham_number_ttm** | **float** |  | [optional] 
**roic_ttm** | **float** |  | [optional] 
**return_on_tangible_assets_ttm** | **float** |  | [optional] 
**graham_net_net_ttm** | **float** |  | [optional] 
**working_capital_ttm** | **float** |  | [optional] 
**tangible_asset_value_ttm** | **float** |  | [optional] 
**net_current_asset_value_ttm** | **float** |  | [optional] 
**invested_capital_ttm** | **float** |  | [optional] 
**average_receivables_ttm** | **float** |  | [optional] 
**average_payables_ttm** | **float** |  | [optional] 
**average_inventory_ttm** | **float** |  | [optional] 
**days_sales_outstanding_ttm** | **float** |  | [optional] 
**days_payables_outstanding_ttm** | **float** |  | [optional] 
**days_of_inventory_on_hand_ttm** | **float** |  | [optional] 
**receivables_turnover_ttm** | **float** |  | [optional] 
**payables_turnover_ttm** | **float** |  | [optional] 
**inventory_turnover_ttm** | **float** |  | [optional] 
**roe_ttm** | **float** |  | [optional] 
**capex_per_share_ttm** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_equity_valuation_multiples_data import FMPEquityValuationMultiplesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEquityValuationMultiplesData from a JSON string
fmp_equity_valuation_multiples_data_instance = FMPEquityValuationMultiplesData.from_json(json)
# print the JSON string representation of the object
print(FMPEquityValuationMultiplesData.to_json())

# convert the object into a dict
fmp_equity_valuation_multiples_data_dict = fmp_equity_valuation_multiples_data_instance.to_dict()
# create an instance of FMPEquityValuationMultiplesData from a dict
fmp_equity_valuation_multiples_data_from_dict = FMPEquityValuationMultiplesData.from_dict(fmp_equity_valuation_multiples_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


