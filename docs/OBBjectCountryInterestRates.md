# OBBjectCountryInterestRates

OBBject with results of type CountryInterestRates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OecdCountryInterestRatesData]**](OecdCountryInterestRatesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_country_interest_rates import OBBjectCountryInterestRates

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCountryInterestRates from a JSON string
ob_bject_country_interest_rates_instance = OBBjectCountryInterestRates.from_json(json)
# print the JSON string representation of the object
print(OBBjectCountryInterestRates.to_json())

# convert the object into a dict
ob_bject_country_interest_rates_dict = ob_bject_country_interest_rates_instance.to_dict()
# create an instance of OBBjectCountryInterestRates from a dict
ob_bject_country_interest_rates_from_dict = OBBjectCountryInterestRates.from_dict(ob_bject_country_interest_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


