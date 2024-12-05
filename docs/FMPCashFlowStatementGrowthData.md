# FMPCashFlowStatementGrowthData

FMP Cash Flow Statement Growth Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**growth_net_income** | **float** |  | [optional] 
**growth_depreciation_and_amortization** | **float** |  | [optional] 
**growth_deferred_income_tax** | **float** |  | [optional] 
**growth_stock_based_compensation** | **float** |  | [optional] 
**growth_change_in_working_capital** | **float** |  | [optional] 
**growth_account_receivables** | **float** |  | [optional] 
**growth_inventory** | **float** |  | [optional] 
**growth_account_payable** | **float** |  | [optional] 
**growth_other_working_capital** | **float** |  | [optional] 
**growth_other_non_cash_items** | **float** |  | [optional] 
**growth_net_cash_from_operating_activities** | **float** |  | [optional] 
**growth_purchase_of_property_plant_and_equipment** | **float** |  | [optional] 
**growth_acquisitions** | **float** |  | [optional] 
**growth_purchase_of_investment_securities** | **float** |  | [optional] 
**growth_sale_and_maturity_of_investments** | **float** |  | [optional] 
**growth_other_investing_activities** | **float** |  | [optional] 
**growth_net_cash_from_investing_activities** | **float** |  | [optional] 
**growth_repayment_of_debt** | **float** |  | [optional] 
**growth_common_stock_issued** | **float** |  | [optional] 
**growth_common_stock_repurchased** | **float** |  | [optional] 
**growth_dividends_paid** | **float** |  | [optional] 
**growth_other_financing_activities** | **float** |  | [optional] 
**growth_net_cash_from_financing_activities** | **float** |  | [optional] 
**growth_effect_of_exchange_rate_changes_on_cash** | **float** |  | [optional] 
**growth_net_change_in_cash_and_equivalents** | **float** |  | [optional] 
**growth_cash_at_beginning_of_period** | **float** |  | [optional] 
**growth_cash_at_end_of_period** | **float** |  | [optional] 
**growth_operating_cash_flow** | **float** |  | [optional] 
**growth_capital_expenditure** | **float** |  | [optional] 
**growth_free_cash_flow** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_cash_flow_statement_growth_data import FMPCashFlowStatementGrowthData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCashFlowStatementGrowthData from a JSON string
fmp_cash_flow_statement_growth_data_instance = FMPCashFlowStatementGrowthData.from_json(json)
# print the JSON string representation of the object
print(FMPCashFlowStatementGrowthData.to_json())

# convert the object into a dict
fmp_cash_flow_statement_growth_data_dict = fmp_cash_flow_statement_growth_data_instance.to_dict()
# create an instance of FMPCashFlowStatementGrowthData from a dict
fmp_cash_flow_statement_growth_data_from_dict = FMPCashFlowStatementGrowthData.from_dict(fmp_cash_flow_statement_growth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


