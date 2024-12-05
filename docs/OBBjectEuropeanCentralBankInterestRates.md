# OBBjectEuropeanCentralBankInterestRates

OBBject with results of type EuropeanCentralBankInterestRates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDEuropeanCentralBankInterestRatesData]**](FREDEuropeanCentralBankInterestRatesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_european_central_bank_interest_rates import OBBjectEuropeanCentralBankInterestRates

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEuropeanCentralBankInterestRates from a JSON string
ob_bject_european_central_bank_interest_rates_instance = OBBjectEuropeanCentralBankInterestRates.from_json(json)
# print the JSON string representation of the object
print(OBBjectEuropeanCentralBankInterestRates.to_json())

# convert the object into a dict
ob_bject_european_central_bank_interest_rates_dict = ob_bject_european_central_bank_interest_rates_instance.to_dict()
# create an instance of OBBjectEuropeanCentralBankInterestRates from a dict
ob_bject_european_central_bank_interest_rates_from_dict = OBBjectEuropeanCentralBankInterestRates.from_dict(ob_bject_european_central_bank_interest_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


