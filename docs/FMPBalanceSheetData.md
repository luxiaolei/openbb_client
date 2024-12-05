# FMPBalanceSheetData

FMP Balance Sheet Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**accepted_date** | **datetime** |  | [optional] 
**reported_currency** | **str** |  | [optional] 
**cash_and_cash_equivalents** | **float** |  | [optional] 
**short_term_investments** | **float** |  | [optional] 
**cash_and_short_term_investments** | **float** |  | [optional] 
**net_receivables** | **float** |  | [optional] 
**inventory** | **float** |  | [optional] 
**other_current_assets** | **float** |  | [optional] 
**total_current_assets** | **float** |  | [optional] 
**plant_property_equipment_net** | **float** |  | [optional] 
**goodwill** | **float** |  | [optional] 
**intangible_assets** | **float** |  | [optional] 
**goodwill_and_intangible_assets** | **float** |  | [optional] 
**long_term_investments** | **float** |  | [optional] 
**tax_assets** | **float** |  | [optional] 
**other_non_current_assets** | **float** |  | [optional] 
**non_current_assets** | **float** |  | [optional] 
**other_assets** | **float** |  | [optional] 
**total_assets** | **float** |  | [optional] 
**accounts_payable** | **float** |  | [optional] 
**short_term_debt** | **float** |  | [optional] 
**tax_payables** | **float** |  | [optional] 
**current_deferred_revenue** | **float** |  | [optional] 
**other_current_liabilities** | **float** |  | [optional] 
**total_current_liabilities** | **float** |  | [optional] 
**long_term_debt** | **float** |  | [optional] 
**deferred_revenue_non_current** | **float** |  | [optional] 
**deferred_tax_liabilities_non_current** | **float** |  | [optional] 
**other_non_current_liabilities** | **float** |  | [optional] 
**total_non_current_liabilities** | **float** |  | [optional] 
**other_liabilities** | **float** |  | [optional] 
**capital_lease_obligations** | **float** |  | [optional] 
**total_liabilities** | **float** |  | [optional] 
**preferred_stock** | **float** |  | [optional] 
**common_stock** | **float** |  | [optional] 
**retained_earnings** | **float** |  | [optional] 
**accumulated_other_comprehensive_income** | **float** |  | [optional] 
**other_shareholders_equity** | **float** |  | [optional] 
**other_total_shareholders_equity** | **float** |  | [optional] 
**total_common_equity** | **float** |  | [optional] 
**total_equity_non_controlling_interests** | **float** |  | [optional] 
**total_liabilities_and_shareholders_equity** | **float** |  | [optional] 
**minority_interest** | **float** |  | [optional] 
**total_liabilities_and_total_equity** | **float** |  | [optional] 
**total_investments** | **float** |  | [optional] 
**total_debt** | **float** |  | [optional] 
**net_debt** | **float** |  | [optional] 
**link** | **str** |  | [optional] 
**final_link** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_balance_sheet_data import FMPBalanceSheetData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPBalanceSheetData from a JSON string
fmp_balance_sheet_data_instance = FMPBalanceSheetData.from_json(json)
# print the JSON string representation of the object
print(FMPBalanceSheetData.to_json())

# convert the object into a dict
fmp_balance_sheet_data_dict = fmp_balance_sheet_data_instance.to_dict()
# create an instance of FMPBalanceSheetData from a dict
fmp_balance_sheet_data_from_dict = FMPBalanceSheetData.from_dict(fmp_balance_sheet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


