# OBBjectSelectedTreasuryConstantMaturity

OBBject with results of type SelectedTreasuryConstantMaturity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDSelectedTreasuryConstantMaturityData]**](FREDSelectedTreasuryConstantMaturityData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_selected_treasury_constant_maturity import OBBjectSelectedTreasuryConstantMaturity

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSelectedTreasuryConstantMaturity from a JSON string
ob_bject_selected_treasury_constant_maturity_instance = OBBjectSelectedTreasuryConstantMaturity.from_json(json)
# print the JSON string representation of the object
print(OBBjectSelectedTreasuryConstantMaturity.to_json())

# convert the object into a dict
ob_bject_selected_treasury_constant_maturity_dict = ob_bject_selected_treasury_constant_maturity_instance.to_dict()
# create an instance of OBBjectSelectedTreasuryConstantMaturity from a dict
ob_bject_selected_treasury_constant_maturity_from_dict = OBBjectSelectedTreasuryConstantMaturity.from_dict(ob_bject_selected_treasury_constant_maturity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


