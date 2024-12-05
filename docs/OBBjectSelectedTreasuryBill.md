# OBBjectSelectedTreasuryBill

OBBject with results of type SelectedTreasuryBill

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDSelectedTreasuryBillData]**](FREDSelectedTreasuryBillData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_selected_treasury_bill import OBBjectSelectedTreasuryBill

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSelectedTreasuryBill from a JSON string
ob_bject_selected_treasury_bill_instance = OBBjectSelectedTreasuryBill.from_json(json)
# print the JSON string representation of the object
print(OBBjectSelectedTreasuryBill.to_json())

# convert the object into a dict
ob_bject_selected_treasury_bill_dict = ob_bject_selected_treasury_bill_instance.to_dict()
# create an instance of OBBjectSelectedTreasuryBill from a dict
ob_bject_selected_treasury_bill_from_dict = OBBjectSelectedTreasuryBill.from_dict(ob_bject_selected_treasury_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


