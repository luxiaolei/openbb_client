# OBBjectCountryProfile

OBBject with results of type CountryProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[EconDbCountryProfileData]**](EconDbCountryProfileData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_country_profile import OBBjectCountryProfile

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCountryProfile from a JSON string
ob_bject_country_profile_instance = OBBjectCountryProfile.from_json(json)
# print the JSON string representation of the object
print(OBBjectCountryProfile.to_json())

# convert the object into a dict
ob_bject_country_profile_dict = ob_bject_country_profile_instance.to_dict()
# create an instance of OBBjectCountryProfile from a dict
ob_bject_country_profile_from_dict = OBBjectCountryProfile.from_dict(ob_bject_country_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


