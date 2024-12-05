# FMPFinancialRatiosData

FMP Financial Ratios Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **str** | The date of the data. | 
**fiscal_period** | **str** | Period of the financial ratios. | 
**fiscal_year** | **int** |  | [optional] 
**current_ratio** | **float** |  | [optional] 
**quick_ratio** | **float** |  | [optional] 
**cash_ratio** | **float** |  | [optional] 
**days_of_sales_outstanding** | **float** |  | [optional] 
**days_of_inventory_outstanding** | **float** |  | [optional] 
**operating_cycle** | **float** |  | [optional] 
**days_of_payables_outstanding** | **float** |  | [optional] 
**cash_conversion_cycle** | **float** |  | [optional] 
**gross_profit_margin** | **float** |  | [optional] 
**operating_profit_margin** | **float** |  | [optional] 
**pretax_profit_margin** | **float** |  | [optional] 
**net_profit_margin** | **float** |  | [optional] 
**effective_tax_rate** | **float** |  | [optional] 
**return_on_assets** | **float** |  | [optional] 
**return_on_equity** | **float** |  | [optional] 
**return_on_capital_employed** | **float** |  | [optional] 
**net_income_per_ebt** | **float** |  | [optional] 
**ebt_per_ebit** | **float** |  | [optional] 
**ebit_per_revenue** | **float** |  | [optional] 
**debt_ratio** | **float** |  | [optional] 
**debt_equity_ratio** | **float** |  | [optional] 
**long_term_debt_to_capitalization** | **float** |  | [optional] 
**total_debt_to_capitalization** | **float** |  | [optional] 
**interest_coverage** | **float** |  | [optional] 
**cash_flow_to_debt_ratio** | **float** |  | [optional] 
**company_equity_multiplier** | **float** |  | [optional] 
**receivables_turnover** | **float** |  | [optional] 
**payables_turnover** | **float** |  | [optional] 
**inventory_turnover** | **float** |  | [optional] 
**fixed_asset_turnover** | **float** |  | [optional] 
**asset_turnover** | **float** |  | [optional] 
**operating_cash_flow_per_share** | **float** |  | [optional] 
**free_cash_flow_per_share** | **float** |  | [optional] 
**cash_per_share** | **float** |  | [optional] 
**payout_ratio** | **float** |  | [optional] 
**operating_cash_flow_sales_ratio** | **float** |  | [optional] 
**free_cash_flow_operating_cash_flow_ratio** | **float** |  | [optional] 
**cash_flow_coverage_ratios** | **float** |  | [optional] 
**short_term_coverage_ratios** | **float** |  | [optional] 
**capital_expenditure_coverage_ratio** | **float** |  | [optional] 
**dividend_paid_and_capex_coverage_ratio** | **float** |  | [optional] 
**dividend_payout_ratio** | **float** |  | [optional] 
**price_book_value_ratio** | **float** |  | [optional] 
**price_to_book_ratio** | **float** |  | [optional] 
**price_to_sales_ratio** | **float** |  | [optional] 
**price_earnings_ratio** | **float** |  | [optional] 
**price_to_free_cash_flows_ratio** | **float** |  | [optional] 
**price_to_operating_cash_flows_ratio** | **float** |  | [optional] 
**price_cash_flow_ratio** | **float** |  | [optional] 
**price_earnings_to_growth_ratio** | **float** |  | [optional] 
**price_sales_ratio** | **float** |  | [optional] 
**dividend_yield** | **float** |  | [optional] 
**dividend_yield_percentage** | **float** |  | [optional] 
**dividend_per_share** | **float** |  | [optional] 
**enterprise_value_multiple** | **float** |  | [optional] 
**price_fair_value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_financial_ratios_data import FMPFinancialRatiosData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPFinancialRatiosData from a JSON string
fmp_financial_ratios_data_instance = FMPFinancialRatiosData.from_json(json)
# print the JSON string representation of the object
print(FMPFinancialRatiosData.to_json())

# convert the object into a dict
fmp_financial_ratios_data_dict = fmp_financial_ratios_data_instance.to_dict()
# create an instance of FMPFinancialRatiosData from a dict
fmp_financial_ratios_data_from_dict = FMPFinancialRatiosData.from_dict(fmp_financial_ratios_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


