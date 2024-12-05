# FMPEtfCountriesData

FMP ETF Countries Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The country of the exposure.  Corresponding values are normalized percentage points. | 

## Example

```python
from openbb_client.models.fmp_etf_countries_data import FMPEtfCountriesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEtfCountriesData from a JSON string
fmp_etf_countries_data_instance = FMPEtfCountriesData.from_json(json)
# print the JSON string representation of the object
print(FMPEtfCountriesData.to_json())

# convert the object into a dict
fmp_etf_countries_data_dict = fmp_etf_countries_data_instance.to_dict()
# create an instance of FMPEtfCountriesData from a dict
fmp_etf_countries_data_from_dict = FMPEtfCountriesData.from_dict(fmp_etf_countries_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


