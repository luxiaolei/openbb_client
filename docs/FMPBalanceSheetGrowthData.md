# FMPBalanceSheetGrowthData

FMP Balance Sheet Growth Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**growth_cash_and_cash_equivalents** | **float** |  | [optional] 
**growth_short_term_investments** | **float** |  | [optional] 
**growth_cash_and_short_term_investments** | **float** |  | [optional] 
**growth_net_receivables** | **float** |  | [optional] 
**growth_inventory** | **float** |  | [optional] 
**growth_other_current_assets** | **float** |  | [optional] 
**growth_total_current_assets** | **float** |  | [optional] 
**growth_property_plant_equipment_net** | **float** |  | 
**growth_goodwill** | **float** |  | 
**growth_intangible_assets** | **float** |  | 
**growth_goodwill_and_intangible_assets** | **float** |  | 
**growth_long_term_investments** | **float** |  | [optional] 
**growth_tax_assets** | **float** |  | [optional] 
**growth_other_non_current_assets** | **float** |  | [optional] 
**growth_total_non_current_assets** | **float** |  | [optional] 
**growth_other_assets** | **float** |  | [optional] 
**growth_total_assets** | **float** |  | [optional] 
**growth_account_payables** | **float** |  | [optional] 
**growth_short_term_debt** | **float** |  | [optional] 
**growth_tax_payables** | **float** |  | [optional] 
**growth_deferred_revenue** | **float** |  | [optional] 
**growth_other_current_liabilities** | **float** |  | [optional] 
**growth_total_current_liabilities** | **float** |  | [optional] 
**growth_long_term_debt** | **float** |  | [optional] 
**growth_deferred_revenue_non_current** | **float** |  | [optional] 
**growth_deferrred_tax_liabilities_non_current** | **float** |  | [optional] 
**growth_other_non_current_liabilities** | **float** |  | [optional] 
**growth_total_non_current_liabilities** | **float** |  | [optional] 
**growth_other_liabilities** | **float** |  | 
**growth_total_liabilities** | **float** |  | 
**growth_common_stock** | **float** |  | 
**growth_retained_earnings** | **float** |  | 
**growth_accumulated_other_comprehensive_income** | **float** |  | 
**growth_other_total_shareholders_equity** | **float** |  | [optional] 
**growth_total_shareholders_equity** | **float** |  | [optional] 
**growth_total_liabilities_and_shareholders_equity** | **float** |  | [optional] 
**growth_total_investments** | **float** |  | [optional] 
**growth_total_debt** | **float** |  | [optional] 
**growth_net_debt** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_balance_sheet_growth_data import FMPBalanceSheetGrowthData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPBalanceSheetGrowthData from a JSON string
fmp_balance_sheet_growth_data_instance = FMPBalanceSheetGrowthData.from_json(json)
# print the JSON string representation of the object
print(FMPBalanceSheetGrowthData.to_json())

# convert the object into a dict
fmp_balance_sheet_growth_data_dict = fmp_balance_sheet_growth_data_instance.to_dict()
# create an instance of FMPBalanceSheetGrowthData from a dict
fmp_balance_sheet_growth_data_from_dict = FMPBalanceSheetGrowthData.from_dict(fmp_balance_sheet_growth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


