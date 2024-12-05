# OBBjectCashFlowStatementResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**reported_currency** | **str** |  | [optional] 
**net_income_continuing_operations** | **float** |  | [optional] 
**net_income_discontinued_operations** | **float** |  | [optional] 
**net_income** | **float** |  | [optional] 
**provision_for_loan_losses** | **float** |  | [optional] 
**provision_for_credit_losses** | **float** |  | [optional] 
**depreciation_expense** | **float** |  | [optional] 
**amortization_expense** | **float** |  | [optional] 
**share_based_compensation** | **float** |  | [optional] 
**non_cash_adjustments_to_reconcile_net_income** | **float** |  | [optional] 
**changes_in_operating_assets_and_liabilities** | **float** |  | [optional] 
**net_cash_from_continuing_operating_activities** | **float** |  | [optional] 
**net_cash_from_discontinued_operating_activities** | **float** |  | [optional] 
**net_cash_from_operating_activities** | **float** |  | [optional] 
**divestitures** | **float** |  | [optional] 
**sale_of_property_plant_and_equipment** | **float** |  | [optional] 
**acquisitions** | **float** |  | [optional] 
**purchase_of_investments** | **float** |  | [optional] 
**purchase_of_investment_securities** | **float** |  | [optional] 
**sale_and_maturity_of_investments** | **float** |  | [optional] 
**loans_held_for_sale** | **float** |  | [optional] 
**purchase_of_property_plant_and_equipment** | **float** |  | [optional] 
**other_investing_activities** | **float** |  | [optional] 
**net_cash_from_continuing_investing_activities** | **float** |  | [optional] 
**net_cash_from_discontinued_investing_activities** | **float** |  | [optional] 
**net_cash_from_investing_activities** | **float** |  | [optional] 
**payment_of_dividends** | **float** |  | [optional] 
**repurchase_of_common_equity** | **float** |  | [optional] 
**repurchase_of_preferred_equity** | **float** |  | [optional] 
**issuance_of_common_equity** | **float** |  | [optional] 
**issuance_of_preferred_equity** | **float** |  | [optional] 
**issuance_of_debt** | **float** |  | [optional] 
**repayment_of_debt** | **float** |  | [optional] 
**other_financing_activities** | **float** |  | [optional] 
**cash_interest_received** | **float** |  | [optional] 
**net_change_in_deposits** | **float** |  | [optional] 
**net_increase_in_fed_funds_sold** | **float** |  | [optional] 
**net_cash_from_continuing_financing_activities** | **float** |  | [optional] 
**net_cash_from_discontinued_financing_activities** | **float** |  | [optional] 
**net_cash_from_financing_activities** | **float** |  | [optional] 
**effect_of_exchange_rate_changes** | **float** |  | [optional] 
**other_net_changes_in_cash** | **float** |  | [optional] 
**net_change_in_cash_and_equivalents** | **float** |  | [optional] 
**cash_income_taxes_paid** | **float** |  | [optional] 
**cash_interest_paid** | **float** |  | [optional] 
**net_cash_flow_from_operating_activities_continuing** | **float** |  | [optional] 
**net_cash_flow_from_operating_activities_discontinued** | **float** |  | [optional] 
**net_cash_flow_from_operating_activities** | **float** |  | [optional] 
**net_cash_flow_from_investing_activities_continuing** | **float** |  | [optional] 
**net_cash_flow_from_investing_activities_discontinued** | **float** |  | [optional] 
**net_cash_flow_from_investing_activities** | **float** |  | [optional] 
**net_cash_flow_from_financing_activities_continuing** | **float** |  | [optional] 
**net_cash_flow_from_financing_activities_discontinued** | **float** |  | [optional] 
**net_cash_flow_from_financing_activities** | **float** |  | [optional] 
**net_cash_flow_continuing** | **float** |  | [optional] 
**net_cash_flow_discontinued** | **float** |  | [optional] 
**exchange_gains_losses** | **float** |  | [optional] 
**net_cash_flow** | **float** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**accepted_date** | **datetime** |  | [optional] 
**depreciation_and_amortization** | **float** |  | [optional] 
**deferred_income_tax** | **float** |  | [optional] 
**stock_based_compensation** | **float** |  | [optional] 
**change_in_working_capital** | **float** |  | [optional] 
**change_in_account_receivables** | **float** |  | [optional] 
**change_in_inventory** | **float** |  | [optional] 
**change_in_account_payable** | **float** |  | [optional] 
**change_in_other_working_capital** | **float** |  | [optional] 
**change_in_other_non_cash_items** | **float** |  | [optional] 
**effect_of_exchange_rate_changes_on_cash** | **float** |  | [optional] 
**cash_at_beginning_of_period** | **float** |  | [optional] 
**cash_at_end_of_period** | **float** |  | [optional] 
**operating_cash_flow** | **float** |  | [optional] 
**capital_expenditure** | **float** |  | [optional] 
**free_cash_flow** | **float** |  | [optional] 
**link** | **str** |  | [optional] 
**final_link** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_cash_flow_statement_results_inner import OBBjectCashFlowStatementResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCashFlowStatementResultsInner from a JSON string
ob_bject_cash_flow_statement_results_inner_instance = OBBjectCashFlowStatementResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectCashFlowStatementResultsInner.to_json())

# convert the object into a dict
ob_bject_cash_flow_statement_results_inner_dict = ob_bject_cash_flow_statement_results_inner_instance.to_dict()
# create an instance of OBBjectCashFlowStatementResultsInner from a dict
ob_bject_cash_flow_statement_results_inner_from_dict = OBBjectCashFlowStatementResultsInner.from_dict(ob_bject_cash_flow_statement_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


