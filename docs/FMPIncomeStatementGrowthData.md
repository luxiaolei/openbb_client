# FMPIncomeStatementGrowthData

FMP Income Statement Growth Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**growth_revenue** | **float** |  | [optional] 
**growth_cost_of_revenue** | **float** |  | [optional] 
**growth_gross_profit** | **float** |  | [optional] 
**growth_gross_profit_margin** | **float** |  | [optional] 
**growth_general_and_admin_expense** | **float** |  | [optional] 
**growth_research_and_development_expense** | **float** |  | [optional] 
**growth_selling_and_marketing_expense** | **float** |  | [optional] 
**growth_other_expenses** | **float** |  | [optional] 
**growth_operating_expenses** | **float** |  | [optional] 
**growth_cost_and_expenses** | **float** |  | [optional] 
**growth_interest_expense** | **float** |  | [optional] 
**growth_depreciation_and_amortization** | **float** |  | [optional] 
**growth_ebitda** | **float** |  | [optional] 
**growth_ebitda_margin** | **float** |  | [optional] 
**growth_operating_income** | **float** |  | [optional] 
**growth_operating_income_margin** | **float** |  | [optional] 
**growth_total_other_income_expenses_net** | **float** |  | [optional] 
**growth_income_before_tax** | **float** |  | [optional] 
**growth_income_before_tax_margin** | **float** |  | [optional] 
**growth_income_tax_expense** | **float** |  | [optional] 
**growth_consolidated_net_income** | **float** |  | [optional] 
**growth_net_income_margin** | **float** |  | [optional] 
**growth_basic_earings_per_share** | **float** |  | [optional] 
**growth_diluted_earnings_per_share** | **float** |  | [optional] 
**growth_weighted_average_basic_shares_outstanding** | **float** |  | [optional] 
**growth_weighted_average_diluted_shares_outstanding** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_income_statement_growth_data import FMPIncomeStatementGrowthData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPIncomeStatementGrowthData from a JSON string
fmp_income_statement_growth_data_instance = FMPIncomeStatementGrowthData.from_json(json)
# print the JSON string representation of the object
print(FMPIncomeStatementGrowthData.to_json())

# convert the object into a dict
fmp_income_statement_growth_data_dict = fmp_income_statement_growth_data_instance.to_dict()
# create an instance of FMPIncomeStatementGrowthData from a dict
fmp_income_statement_growth_data_from_dict = FMPIncomeStatementGrowthData.from_dict(fmp_income_statement_growth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


