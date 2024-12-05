# IntrinioIncomeStatementData

Intrinio Income Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**reported_currency** | **str** |  | [optional] 
**revenue** | **float** |  | [optional] 
**operating_revenue** | **float** |  | [optional] 
**cost_of_revenue** | **float** |  | [optional] 
**operating_cost_of_revenue** | **float** |  | [optional] 
**gross_profit** | **float** |  | [optional] 
**gross_profit_margin** | **float** |  | [optional] 
**provision_for_credit_losses** | **float** |  | [optional] 
**research_and_development_expense** | **float** |  | [optional] 
**selling_general_and_admin_expense** | **float** |  | [optional] 
**salaries_and_employee_benefits** | **float** |  | [optional] 
**marketing_expense** | **float** |  | [optional] 
**net_occupancy_and_equipment_expense** | **float** |  | [optional] 
**other_operating_expenses** | **float** |  | [optional] 
**depreciation_expense** | **float** |  | [optional] 
**amortization_expense** | **float** |  | [optional] 
**amortization_of_deferred_policy_acquisition_costs** | **float** |  | [optional] 
**exploration_expense** | **float** |  | [optional] 
**depletion_expense** | **float** |  | [optional] 
**total_operating_expenses** | **float** |  | [optional] 
**total_operating_income** | **float** |  | [optional] 
**deposits_and_money_market_investments_interest_income** | **float** |  | [optional] 
**federal_funds_sold_and_securities_borrowed_interest_income** | **float** |  | [optional] 
**investment_securities_interest_income** | **float** |  | [optional] 
**loans_and_leases_interest_income** | **float** |  | [optional] 
**trading_account_interest_income** | **float** |  | [optional] 
**other_interest_income** | **float** |  | [optional] 
**total_non_interest_income** | **float** |  | [optional] 
**interest_and_investment_income** | **float** |  | [optional] 
**short_term_borrowings_interest_expense** | **float** |  | [optional] 
**long_term_debt_interest_expense** | **float** |  | [optional] 
**capitalized_lease_obligations_interest_expense** | **float** |  | [optional] 
**deposits_interest_expense** | **float** |  | [optional] 
**federal_funds_purchased_and_securities_sold_interest_expense** | **float** |  | [optional] 
**other_interest_expense** | **float** |  | [optional] 
**total_interest_expense** | **float** |  | [optional] 
**net_interest_income** | **float** |  | [optional] 
**other_non_interest_income** | **float** |  | [optional] 
**investment_banking_income** | **float** |  | [optional] 
**trust_fees_by_commissions** | **float** |  | [optional] 
**premiums_earned** | **float** |  | [optional] 
**insurance_policy_acquisition_costs** | **float** |  | [optional] 
**current_and_future_benefits** | **float** |  | [optional] 
**property_and_liability_insurance_claims** | **float** |  | [optional] 
**total_non_interest_expense** | **float** |  | [optional] 
**net_realized_and_unrealized_capital_gains_on_investments** | **float** |  | [optional] 
**other_gains** | **float** |  | [optional] 
**non_operating_income** | **float** |  | [optional] 
**other_income** | **float** |  | [optional] 
**other_revenue** | **float** |  | [optional] 
**extraordinary_income** | **float** |  | [optional] 
**total_other_income** | **float** |  | [optional] 
**ebitda** | **float** |  | [optional] 
**ebitda_margin** | **float** |  | [optional] 
**total_pre_tax_income** | **float** |  | [optional] 
**ebit** | **float** |  | [optional] 
**pre_tax_income_margin** | **float** |  | [optional] 
**income_tax_expense** | **float** |  | [optional] 
**impairment_charge** | **float** |  | [optional] 
**restructuring_charge** | **float** |  | [optional] 
**service_charges_on_deposit_accounts** | **float** |  | [optional] 
**other_service_charges** | **float** |  | [optional] 
**other_special_charges** | **float** |  | [optional] 
**other_cost_of_revenue** | **float** |  | [optional] 
**net_income_continuing_operations** | **float** |  | [optional] 
**net_income_discontinued_operations** | **float** |  | [optional] 
**consolidated_net_income** | **float** |  | [optional] 
**other_adjustments_to_consolidated_net_income** | **float** |  | [optional] 
**other_adjustment_to_net_income_attributable_to_common_shareholders** | **float** |  | [optional] 
**net_income_attributable_to_noncontrolling_interest** | **float** |  | [optional] 
**net_income_attributable_to_common_shareholders** | **float** |  | [optional] 
**basic_earnings_per_share** | **float** |  | [optional] 
**diluted_earnings_per_share** | **float** |  | [optional] 
**basic_and_diluted_earnings_per_share** | **float** |  | [optional] 
**cash_dividends_to_common_per_share** | **float** |  | [optional] 
**preferred_stock_dividends_declared** | **float** |  | [optional] 
**weighted_average_basic_shares_outstanding** | **float** |  | [optional] 
**weighted_average_diluted_shares_outstanding** | **float** |  | [optional] 
**weighted_average_basic_and_diluted_shares_outstanding** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_income_statement_data import IntrinioIncomeStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioIncomeStatementData from a JSON string
intrinio_income_statement_data_instance = IntrinioIncomeStatementData.from_json(json)
# print the JSON string representation of the object
print(IntrinioIncomeStatementData.to_json())

# convert the object into a dict
intrinio_income_statement_data_dict = intrinio_income_statement_data_instance.to_dict()
# create an instance of IntrinioIncomeStatementData from a dict
intrinio_income_statement_data_from_dict = IntrinioIncomeStatementData.from_dict(intrinio_income_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


