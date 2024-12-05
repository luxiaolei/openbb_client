# PolygonBalanceSheetData

Polygon Balance Sheet Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**accounts_receivable** | **float** |  | [optional] 
**marketable_securities** | **float** |  | [optional] 
**prepaid_expenses** | **float** |  | [optional] 
**other_current_assets** | **float** |  | [optional] 
**total_current_assets** | **float** |  | [optional] 
**property_plant_equipment_net** | **float** |  | [optional] 
**inventory** | **float** |  | [optional] 
**other_non_current_assets** | **float** |  | [optional] 
**total_non_current_assets** | **float** |  | [optional] 
**intangible_assets** | **float** |  | [optional] 
**total_assets** | **float** |  | [optional] 
**accounts_payable** | **float** |  | [optional] 
**employee_wages** | **float** |  | [optional] 
**other_current_liabilities** | **float** |  | [optional] 
**total_current_liabilities** | **float** |  | [optional] 
**other_non_current_liabilities** | **float** |  | [optional] 
**total_non_current_liabilities** | **float** |  | [optional] 
**long_term_debt** | **float** |  | [optional] 
**total_liabilities** | **float** |  | [optional] 
**minority_interest** | **float** |  | [optional] 
**temporary_equity_attributable_to_parent** | **float** |  | [optional] 
**equity_attributable_to_parent** | **float** |  | [optional] 
**temporary_equity** | **float** |  | [optional] 
**preferred_stock** | **float** |  | [optional] 
**redeemable_non_controlling_interest** | **float** |  | [optional] 
**redeemable_non_controlling_interest_other** | **float** |  | [optional] 
**total_shareholders_equity** | **float** |  | [optional] 
**total_equity** | **float** |  | [optional] 
**total_liabilities_and_shareholders_equity** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_balance_sheet_data import PolygonBalanceSheetData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonBalanceSheetData from a JSON string
polygon_balance_sheet_data_instance = PolygonBalanceSheetData.from_json(json)
# print the JSON string representation of the object
print(PolygonBalanceSheetData.to_json())

# convert the object into a dict
polygon_balance_sheet_data_dict = polygon_balance_sheet_data_instance.to_dict()
# create an instance of PolygonBalanceSheetData from a dict
polygon_balance_sheet_data_from_dict = PolygonBalanceSheetData.from_dict(polygon_balance_sheet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


