# OBBjectIncomeStatementGrowth

OBBject with results of type IncomeStatementGrowth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPIncomeStatementGrowthData]**](FMPIncomeStatementGrowthData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_income_statement_growth import OBBjectIncomeStatementGrowth

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectIncomeStatementGrowth from a JSON string
ob_bject_income_statement_growth_instance = OBBjectIncomeStatementGrowth.from_json(json)
# print the JSON string representation of the object
print(OBBjectIncomeStatementGrowth.to_json())

# convert the object into a dict
ob_bject_income_statement_growth_dict = ob_bject_income_statement_growth_instance.to_dict()
# create an instance of OBBjectIncomeStatementGrowth from a dict
ob_bject_income_statement_growth_from_dict = OBBjectIncomeStatementGrowth.from_dict(ob_bject_income_statement_growth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


