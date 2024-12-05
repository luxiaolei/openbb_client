# YFinanceIncomeStatementData

Yahoo Finance Income Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_income_statement_data import YFinanceIncomeStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceIncomeStatementData from a JSON string
y_finance_income_statement_data_instance = YFinanceIncomeStatementData.from_json(json)
# print the JSON string representation of the object
print(YFinanceIncomeStatementData.to_json())

# convert the object into a dict
y_finance_income_statement_data_dict = y_finance_income_statement_data_instance.to_dict()
# create an instance of YFinanceIncomeStatementData from a dict
y_finance_income_statement_data_from_dict = YFinanceIncomeStatementData.from_dict(y_finance_income_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


