# FREDEuropeanCentralBankInterestRatesData

FRED European Central Bank Interest Rates Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fred_european_central_bank_interest_rates_data import FREDEuropeanCentralBankInterestRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDEuropeanCentralBankInterestRatesData from a JSON string
fred_european_central_bank_interest_rates_data_instance = FREDEuropeanCentralBankInterestRatesData.from_json(json)
# print the JSON string representation of the object
print(FREDEuropeanCentralBankInterestRatesData.to_json())

# convert the object into a dict
fred_european_central_bank_interest_rates_data_dict = fred_european_central_bank_interest_rates_data_instance.to_dict()
# create an instance of FREDEuropeanCentralBankInterestRatesData from a dict
fred_european_central_bank_interest_rates_data_from_dict = FREDEuropeanCentralBankInterestRatesData.from_dict(fred_european_central_bank_interest_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


