# OBBjectCashFlowStatement

OBBject with results of type CashFlowStatement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectCashFlowStatementResultsInner]**](OBBjectCashFlowStatementResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_cash_flow_statement import OBBjectCashFlowStatement

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCashFlowStatement from a JSON string
ob_bject_cash_flow_statement_instance = OBBjectCashFlowStatement.from_json(json)
# print the JSON string representation of the object
print(OBBjectCashFlowStatement.to_json())

# convert the object into a dict
ob_bject_cash_flow_statement_dict = ob_bject_cash_flow_statement_instance.to_dict()
# create an instance of OBBjectCashFlowStatement from a dict
ob_bject_cash_flow_statement_from_dict = OBBjectCashFlowStatement.from_dict(ob_bject_cash_flow_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


