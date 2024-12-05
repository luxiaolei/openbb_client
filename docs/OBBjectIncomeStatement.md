# OBBjectIncomeStatement

OBBject with results of type IncomeStatement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectIncomeStatementResultsInner]**](OBBjectIncomeStatementResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_income_statement import OBBjectIncomeStatement

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectIncomeStatement from a JSON string
ob_bject_income_statement_instance = OBBjectIncomeStatement.from_json(json)
# print the JSON string representation of the object
print(OBBjectIncomeStatement.to_json())

# convert the object into a dict
ob_bject_income_statement_dict = ob_bject_income_statement_instance.to_dict()
# create an instance of OBBjectIncomeStatement from a dict
ob_bject_income_statement_from_dict = OBBjectIncomeStatement.from_dict(ob_bject_income_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


