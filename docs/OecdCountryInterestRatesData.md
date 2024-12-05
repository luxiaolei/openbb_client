# OecdCountryInterestRatesData

OECD Country Interest Rates Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | [optional] 
**value** | **float** | The interest rate value. | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.oecd_country_interest_rates_data import OecdCountryInterestRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of OecdCountryInterestRatesData from a JSON string
oecd_country_interest_rates_data_instance = OecdCountryInterestRatesData.from_json(json)
# print the JSON string representation of the object
print(OecdCountryInterestRatesData.to_json())

# convert the object into a dict
oecd_country_interest_rates_data_dict = oecd_country_interest_rates_data_instance.to_dict()
# create an instance of OecdCountryInterestRatesData from a dict
oecd_country_interest_rates_data_from_dict = OecdCountryInterestRatesData.from_dict(oecd_country_interest_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


