# OECDGdpNominalData

OECD Nominal GDP Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** | The country represented by the GDP value. | [optional] 
**value** | [**Value9**](Value9.md) |  | 

## Example

```python
from openbb_client.models.oecd_gdp_nominal_data import OECDGdpNominalData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDGdpNominalData from a JSON string
oecd_gdp_nominal_data_instance = OECDGdpNominalData.from_json(json)
# print the JSON string representation of the object
print(OECDGdpNominalData.to_json())

# convert the object into a dict
oecd_gdp_nominal_data_dict = oecd_gdp_nominal_data_instance.to_dict()
# create an instance of OECDGdpNominalData from a dict
oecd_gdp_nominal_data_from_dict = OECDGdpNominalData.from_dict(oecd_gdp_nominal_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


