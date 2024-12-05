# OBBjectBalanceSheetGrowth

OBBject with results of type BalanceSheetGrowth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPBalanceSheetGrowthData]**](FMPBalanceSheetGrowthData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_balance_sheet_growth import OBBjectBalanceSheetGrowth

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectBalanceSheetGrowth from a JSON string
ob_bject_balance_sheet_growth_instance = OBBjectBalanceSheetGrowth.from_json(json)
# print the JSON string representation of the object
print(OBBjectBalanceSheetGrowth.to_json())

# convert the object into a dict
ob_bject_balance_sheet_growth_dict = ob_bject_balance_sheet_growth_instance.to_dict()
# create an instance of OBBjectBalanceSheetGrowth from a dict
ob_bject_balance_sheet_growth_from_dict = OBBjectBalanceSheetGrowth.from_dict(ob_bject_balance_sheet_growth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


