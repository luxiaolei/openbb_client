# FREDDiscountWindowPrimaryCreditRateData

FRED Discount Window Primary Credit Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fred_discount_window_primary_credit_rate_data import FREDDiscountWindowPrimaryCreditRateData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDDiscountWindowPrimaryCreditRateData from a JSON string
fred_discount_window_primary_credit_rate_data_instance = FREDDiscountWindowPrimaryCreditRateData.from_json(json)
# print the JSON string representation of the object
print(FREDDiscountWindowPrimaryCreditRateData.to_json())

# convert the object into a dict
fred_discount_window_primary_credit_rate_data_dict = fred_discount_window_primary_credit_rate_data_instance.to_dict()
# create an instance of FREDDiscountWindowPrimaryCreditRateData from a dict
fred_discount_window_primary_credit_rate_data_from_dict = FREDDiscountWindowPrimaryCreditRateData.from_dict(fred_discount_window_primary_credit_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


