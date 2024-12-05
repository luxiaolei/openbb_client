# FMPIncomeStatementData

FMP Income Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**accepted_date** | **datetime** |  | [optional] 
**reported_currency** | **str** |  | [optional] 
**revenue** | **float** |  | [optional] 
**cost_of_revenue** | **float** |  | [optional] 
**gross_profit** | **float** |  | [optional] 
**gross_profit_margin** | **float** |  | [optional] 
**general_and_admin_expense** | **float** |  | [optional] 
**research_and_development_expense** | **float** |  | [optional] 
**selling_and_marketing_expense** | **float** |  | [optional] 
**selling_general_and_admin_expense** | **float** |  | [optional] 
**other_expenses** | **float** |  | [optional] 
**total_operating_expenses** | **float** |  | [optional] 
**cost_and_expenses** | **float** |  | [optional] 
**interest_income** | **float** |  | [optional] 
**total_interest_expense** | **float** |  | [optional] 
**depreciation_and_amortization** | **float** |  | [optional] 
**ebitda** | **float** |  | [optional] 
**ebitda_margin** | **float** |  | [optional] 
**total_operating_income** | **float** |  | [optional] 
**operating_income_margin** | **float** |  | [optional] 
**total_other_income_expenses** | **float** |  | [optional] 
**total_pre_tax_income** | **float** |  | [optional] 
**pre_tax_income_margin** | **float** |  | [optional] 
**income_tax_expense** | **float** |  | [optional] 
**consolidated_net_income** | **float** |  | [optional] 
**net_income_margin** | **float** |  | [optional] 
**basic_earnings_per_share** | **float** |  | [optional] 
**diluted_earnings_per_share** | **float** |  | [optional] 
**weighted_average_basic_shares_outstanding** | **float** |  | [optional] 
**weighted_average_diluted_shares_outstanding** | **float** |  | [optional] 
**link** | **str** |  | [optional] 
**final_link** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_income_statement_data import FMPIncomeStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPIncomeStatementData from a JSON string
fmp_income_statement_data_instance = FMPIncomeStatementData.from_json(json)
# print the JSON string representation of the object
print(FMPIncomeStatementData.to_json())

# convert the object into a dict
fmp_income_statement_data_dict = fmp_income_statement_data_instance.to_dict()
# create an instance of FMPIncomeStatementData from a dict
fmp_income_statement_data_from_dict = FMPIncomeStatementData.from_dict(fmp_income_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


