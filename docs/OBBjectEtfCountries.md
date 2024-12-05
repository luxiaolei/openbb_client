# OBBjectEtfCountries

OBBject with results of type EtfCountries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPEtfCountriesData]**](FMPEtfCountriesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_countries import OBBjectEtfCountries

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfCountries from a JSON string
ob_bject_etf_countries_instance = OBBjectEtfCountries.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfCountries.to_json())

# convert the object into a dict
ob_bject_etf_countries_dict = ob_bject_etf_countries_instance.to_dict()
# create an instance of OBBjectEtfCountries from a dict
ob_bject_etf_countries_from_dict = OBBjectEtfCountries.from_dict(ob_bject_etf_countries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


