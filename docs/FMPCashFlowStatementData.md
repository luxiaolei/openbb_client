# FMPCashFlowStatementData

FMP Cash Flow Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**accepted_date** | **datetime** |  | [optional] 
**reported_currency** | **str** |  | [optional] 
**net_income** | **float** |  | [optional] 
**depreciation_and_amortization** | **float** |  | [optional] 
**deferred_income_tax** | **float** |  | [optional] 
**stock_based_compensation** | **float** |  | [optional] 
**change_in_working_capital** | **float** |  | [optional] 
**change_in_account_receivables** | **float** |  | [optional] 
**change_in_inventory** | **float** |  | [optional] 
**change_in_account_payable** | **float** |  | [optional] 
**change_in_other_working_capital** | **float** |  | [optional] 
**change_in_other_non_cash_items** | **float** |  | [optional] 
**net_cash_from_operating_activities** | **float** |  | [optional] 
**purchase_of_property_plant_and_equipment** | **float** |  | [optional] 
**acquisitions** | **float** |  | [optional] 
**purchase_of_investment_securities** | **float** |  | [optional] 
**sale_and_maturity_of_investments** | **float** |  | [optional] 
**other_investing_activities** | **float** |  | [optional] 
**net_cash_from_investing_activities** | **float** |  | [optional] 
**repayment_of_debt** | **float** |  | [optional] 
**issuance_of_common_equity** | **float** |  | [optional] 
**repurchase_of_common_equity** | **float** |  | [optional] 
**payment_of_dividends** | **float** |  | [optional] 
**other_financing_activities** | **float** |  | [optional] 
**net_cash_from_financing_activities** | **float** |  | [optional] 
**effect_of_exchange_rate_changes_on_cash** | **float** |  | [optional] 
**net_change_in_cash_and_equivalents** | **float** |  | [optional] 
**cash_at_beginning_of_period** | **float** |  | [optional] 
**cash_at_end_of_period** | **float** |  | [optional] 
**operating_cash_flow** | **float** |  | [optional] 
**capital_expenditure** | **float** |  | [optional] 
**free_cash_flow** | **float** |  | [optional] 
**link** | **str** |  | [optional] 
**final_link** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_cash_flow_statement_data import FMPCashFlowStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCashFlowStatementData from a JSON string
fmp_cash_flow_statement_data_instance = FMPCashFlowStatementData.from_json(json)
# print the JSON string representation of the object
print(FMPCashFlowStatementData.to_json())

# convert the object into a dict
fmp_cash_flow_statement_data_dict = fmp_cash_flow_statement_data_instance.to_dict()
# create an instance of FMPCashFlowStatementData from a dict
fmp_cash_flow_statement_data_from_dict = FMPCashFlowStatementData.from_dict(fmp_cash_flow_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


