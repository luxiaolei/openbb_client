# IntrinioFinancialRatiosData

Intrinio Financial Ratios Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **str** | The date of the data. | 
**fiscal_period** | **str** | Period of the financial ratios. | 
**fiscal_year** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_financial_ratios_data import IntrinioFinancialRatiosData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioFinancialRatiosData from a JSON string
intrinio_financial_ratios_data_instance = IntrinioFinancialRatiosData.from_json(json)
# print the JSON string representation of the object
print(IntrinioFinancialRatiosData.to_json())

# convert the object into a dict
intrinio_financial_ratios_data_dict = intrinio_financial_ratios_data_instance.to_dict()
# create an instance of IntrinioFinancialRatiosData from a dict
intrinio_financial_ratios_data_from_dict = IntrinioFinancialRatiosData.from_dict(intrinio_financial_ratios_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


