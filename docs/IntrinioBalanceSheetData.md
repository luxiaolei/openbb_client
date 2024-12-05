# IntrinioBalanceSheetData

Intrinio Balance Sheet Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**reported_currency** | **str** |  | [optional] 
**cash_and_cash_equivalents** | **float** |  | [optional] 
**cash_and_due_from_banks** | **float** |  | [optional] 
**restricted_cash** | **float** |  | [optional] 
**short_term_investments** | **float** |  | [optional] 
**federal_funds_sold** | **float** |  | [optional] 
**accounts_receivable** | **float** |  | [optional] 
**note_and_lease_receivable** | **float** |  | [optional] 
**inventories** | **float** |  | [optional] 
**customer_and_other_receivables** | **float** |  | [optional] 
**interest_bearing_deposits_at_other_banks** | **float** |  | [optional] 
**time_deposits_placed_and_other_short_term_investments** | **float** |  | [optional] 
**trading_account_securities** | **float** |  | [optional] 
**loans_and_leases** | **float** |  | [optional] 
**allowance_for_loan_and_lease_losses** | **float** |  | [optional] 
**current_deferred_refundable_income_taxes** | **float** |  | [optional] 
**other_current_assets** | **float** |  | [optional] 
**loans_and_leases_net_of_allowance** | **float** |  | [optional] 
**accrued_investment_income** | **float** |  | [optional] 
**other_current_non_operating_assets** | **float** |  | [optional] 
**loans_held_for_sale** | **float** |  | [optional] 
**prepaid_expenses** | **float** |  | [optional] 
**total_current_assets** | **float** |  | [optional] 
**plant_property_equipment_gross** | **float** |  | [optional] 
**accumulated_depreciation** | **float** |  | [optional] 
**premises_and_equipment_net** | **float** |  | [optional] 
**plant_property_equipment_net** | **float** |  | [optional] 
**long_term_investments** | **float** |  | [optional] 
**mortgage_servicing_rights** | **float** |  | [optional] 
**unearned_premiums_asset** | **float** |  | [optional] 
**non_current_note_lease_receivables** | **float** |  | [optional] 
**deferred_acquisition_cost** | **float** |  | [optional] 
**goodwill** | **float** |  | [optional] 
**separate_account_business_assets** | **float** |  | [optional] 
**non_current_deferred_refundable_income_taxes** | **float** |  | [optional] 
**intangible_assets** | **float** |  | [optional] 
**employee_benefit_assets** | **float** |  | [optional] 
**other_assets** | **float** |  | [optional] 
**other_non_current_operating_assets** | **float** |  | [optional] 
**other_non_current_non_operating_assets** | **float** |  | [optional] 
**interest_bearing_deposits** | **float** |  | [optional] 
**total_non_current_assets** | **float** |  | [optional] 
**total_assets** | **float** |  | [optional] 
**non_interest_bearing_deposits** | **float** |  | [optional] 
**federal_funds_purchased_and_securities_sold** | **float** |  | [optional] 
**bankers_acceptance_outstanding** | **float** |  | [optional] 
**short_term_debt** | **float** |  | [optional] 
**accounts_payable** | **float** |  | [optional] 
**current_deferred_revenue** | **float** |  | [optional] 
**current_deferred_payable_income_tax_liabilities** | **float** |  | [optional] 
**accrued_interest_payable** | **float** |  | [optional] 
**accrued_expenses** | **float** |  | [optional] 
**other_short_term_payables** | **float** |  | [optional] 
**customer_deposits** | **float** |  | [optional] 
**dividends_payable** | **float** |  | [optional] 
**claims_and_claim_expense** | **float** |  | [optional] 
**future_policy_benefits** | **float** |  | [optional] 
**current_employee_benefit_liabilities** | **float** |  | [optional] 
**unearned_premiums_liability** | **float** |  | [optional] 
**other_taxes_payable** | **float** |  | [optional] 
**policy_holder_funds** | **float** |  | [optional] 
**other_current_liabilities** | **float** |  | [optional] 
**other_current_non_operating_liabilities** | **float** |  | [optional] 
**separate_account_business_liabilities** | **float** |  | [optional] 
**total_current_liabilities** | **float** |  | [optional] 
**long_term_debt** | **float** |  | [optional] 
**other_long_term_liabilities** | **float** |  | [optional] 
**non_current_deferred_revenue** | **float** |  | [optional] 
**non_current_deferred_payable_income_tax_liabilities** | **float** |  | [optional] 
**non_current_employee_benefit_liabilities** | **float** |  | [optional] 
**other_non_current_operating_liabilities** | **float** |  | [optional] 
**other_non_current_non_operating_liabilities** | **float** |  | [optional] 
**total_non_current_liabilities** | **float** |  | [optional] 
**capital_lease_obligations** | **float** |  | [optional] 
**asset_retirement_reserve_litigation_obligation** | **float** |  | [optional] 
**total_liabilities** | **float** |  | [optional] 
**commitments_contingencies** | **float** |  | [optional] 
**redeemable_non_controlling_interest** | **float** |  | [optional] 
**preferred_stock** | **float** |  | [optional] 
**common_stock** | **float** |  | [optional] 
**retained_earnings** | **float** |  | [optional] 
**treasury_stock** | **float** |  | [optional] 
**accumulated_other_comprehensive_income** | **float** |  | [optional] 
**participating_policy_holder_equity** | **float** |  | [optional] 
**other_equity_adjustments** | **float** |  | [optional] 
**total_common_equity** | **float** |  | [optional] 
**total_preferred_common_equity** | **float** |  | [optional] 
**non_controlling_interest** | **float** |  | [optional] 
**total_equity_non_controlling_interests** | **float** |  | [optional] 
**total_liabilities_shareholders_equity** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_balance_sheet_data import IntrinioBalanceSheetData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioBalanceSheetData from a JSON string
intrinio_balance_sheet_data_instance = IntrinioBalanceSheetData.from_json(json)
# print the JSON string representation of the object
print(IntrinioBalanceSheetData.to_json())

# convert the object into a dict
intrinio_balance_sheet_data_dict = intrinio_balance_sheet_data_instance.to_dict()
# create an instance of IntrinioBalanceSheetData from a dict
intrinio_balance_sheet_data_from_dict = IntrinioBalanceSheetData.from_dict(intrinio_balance_sheet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


