# IntrinioCashFlowStatementData

Intrinio Cash Flow Statement Data.

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

## Example

```python
from openbb_client.models.intrinio_cash_flow_statement_data import IntrinioCashFlowStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioCashFlowStatementData from a JSON string
intrinio_cash_flow_statement_data_instance = IntrinioCashFlowStatementData.from_json(json)
# print the JSON string representation of the object
print(IntrinioCashFlowStatementData.to_json())

# convert the object into a dict
intrinio_cash_flow_statement_data_dict = intrinio_cash_flow_statement_data_instance.to_dict()
# create an instance of IntrinioCashFlowStatementData from a dict
intrinio_cash_flow_statement_data_from_dict = IntrinioCashFlowStatementData.from_dict(intrinio_cash_flow_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


