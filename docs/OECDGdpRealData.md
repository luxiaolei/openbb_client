# OECDGdpRealData

OECD Real GDP Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** | The country represented by the Real GDP value. | [optional] 
**value** | [**Value10**](Value10.md) |  | 

## Example

```python
from openbb_client.models.oecd_gdp_real_data import OECDGdpRealData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDGdpRealData from a JSON string
oecd_gdp_real_data_instance = OECDGdpRealData.from_json(json)
# print the JSON string representation of the object
print(OECDGdpRealData.to_json())

# convert the object into a dict
oecd_gdp_real_data_dict = oecd_gdp_real_data_instance.to_dict()
# create an instance of OECDGdpRealData from a dict
oecd_gdp_real_data_from_dict = OECDGdpRealData.from_dict(oecd_gdp_real_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


