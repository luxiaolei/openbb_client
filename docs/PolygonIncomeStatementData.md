# PolygonIncomeStatementData

Polygon Income Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**revenue** | **float** |  | [optional] 
**cost_of_revenue_goods** | **float** |  | [optional] 
**cost_of_revenue_services** | **float** |  | [optional] 
**cost_of_revenue** | **float** |  | [optional] 
**gross_profit** | **float** |  | [optional] 
**provisions_for_loan_lease_and_other_losses** | **float** |  | [optional] 
**depreciation_and_amortization** | **float** |  | [optional] 
**income_tax_expense_benefit_current** | **float** |  | [optional] 
**deferred_tax_benefit** | **float** |  | [optional] 
**benefits_costs_expenses** | **float** |  | [optional] 
**selling_general_and_administrative_expense** | **float** |  | [optional] 
**research_and_development** | **float** |  | [optional] 
**costs_and_expenses** | **float** |  | [optional] 
**other_operating_expenses** | **float** |  | [optional] 
**operating_expenses** | **float** |  | [optional] 
**operating_income** | **float** |  | [optional] 
**non_operating_income** | **float** |  | [optional] 
**interest_and_dividend_income** | **float** |  | [optional] 
**total_interest_expense** | **float** |  | [optional] 
**interest_and_debt_expense** | **float** |  | [optional] 
**net_interest_income** | **float** |  | [optional] 
**interest_income_after_provision_for_losses** | **float** |  | [optional] 
**non_interest_expense** | **float** |  | [optional] 
**non_interest_income** | **float** |  | [optional] 
**income_from_discontinued_operations_net_of_tax_on_disposal** | **float** |  | [optional] 
**income_from_discontinued_operations_net_of_tax** | **float** |  | [optional] 
**income_before_equity_method_investments** | **float** |  | [optional] 
**income_from_equity_method_investments** | **float** |  | [optional] 
**total_pre_tax_income** | **float** |  | [optional] 
**income_tax_expense** | **float** |  | [optional] 
**income_after_tax** | **float** |  | [optional] 
**consolidated_net_income** | **float** |  | [optional] 
**net_income_attributable_noncontrolling_interest** | **float** |  | [optional] 
**net_income_attributable_to_parent** | **float** |  | [optional] 
**net_income_attributable_to_common_shareholders** | **float** |  | [optional] 
**participating_securities_earnings** | **float** |  | [optional] 
**undistributed_earnings_allocated_to_participating_securities** | **float** |  | [optional] 
**common_stock_dividends** | **float** |  | [optional] 
**preferred_stock_dividends_and_other_adjustments** | **float** |  | [optional] 
**basic_earnings_per_share** | **float** |  | [optional] 
**diluted_earnings_per_share** | **float** |  | [optional] 
**weighted_average_basic_shares_outstanding** | **float** |  | [optional] 
**weighted_average_diluted_shares_outstanding** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_income_statement_data import PolygonIncomeStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonIncomeStatementData from a JSON string
polygon_income_statement_data_instance = PolygonIncomeStatementData.from_json(json)
# print the JSON string representation of the object
print(PolygonIncomeStatementData.to_json())

# convert the object into a dict
polygon_income_statement_data_dict = polygon_income_statement_data_instance.to_dict()
# create an instance of PolygonIncomeStatementData from a dict
polygon_income_statement_data_from_dict = PolygonIncomeStatementData.from_dict(polygon_income_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


