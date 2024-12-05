# OBBjectBalanceSheet

OBBject with results of type BalanceSheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectBalanceSheetResultsInner]**](OBBjectBalanceSheetResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_balance_sheet import OBBjectBalanceSheet

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectBalanceSheet from a JSON string
ob_bject_balance_sheet_instance = OBBjectBalanceSheet.from_json(json)
# print the JSON string representation of the object
print(OBBjectBalanceSheet.to_json())

# convert the object into a dict
ob_bject_balance_sheet_dict = ob_bject_balance_sheet_instance.to_dict()
# create an instance of OBBjectBalanceSheet from a dict
ob_bject_balance_sheet_from_dict = OBBjectBalanceSheet.from_dict(ob_bject_balance_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


