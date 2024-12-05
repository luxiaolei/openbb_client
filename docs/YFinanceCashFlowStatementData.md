# YFinanceCashFlowStatementData

Yahoo Finance Cash Flow Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_cash_flow_statement_data import YFinanceCashFlowStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceCashFlowStatementData from a JSON string
y_finance_cash_flow_statement_data_instance = YFinanceCashFlowStatementData.from_json(json)
# print the JSON string representation of the object
print(YFinanceCashFlowStatementData.to_json())

# convert the object into a dict
y_finance_cash_flow_statement_data_dict = y_finance_cash_flow_statement_data_instance.to_dict()
# create an instance of YFinanceCashFlowStatementData from a dict
y_finance_cash_flow_statement_data_from_dict = YFinanceCashFlowStatementData.from_dict(y_finance_cash_flow_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


