# YFinanceKeyExecutivesData

YFinance Key Executives Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Designation of the key executive. | 
**name** | **str** | Name of the key executive. | 
**pay** | **int** |  | [optional] 
**currency_pay** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**year_born** | **int** |  | [optional] 
**title_since** | **int** |  | [optional] 
**exercised_value** | **int** |  | [optional] 
**unexercised_value** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_key_executives_data import YFinanceKeyExecutivesData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceKeyExecutivesData from a JSON string
y_finance_key_executives_data_instance = YFinanceKeyExecutivesData.from_json(json)
# print the JSON string representation of the object
print(YFinanceKeyExecutivesData.to_json())

# convert the object into a dict
y_finance_key_executives_data_dict = y_finance_key_executives_data_instance.to_dict()
# create an instance of YFinanceKeyExecutivesData from a dict
y_finance_key_executives_data_from_dict = YFinanceKeyExecutivesData.from_dict(y_finance_key_executives_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


