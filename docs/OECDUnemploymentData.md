# OECDUnemploymentData

OECD Unemployment Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**country** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.oecd_unemployment_data import OECDUnemploymentData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDUnemploymentData from a JSON string
oecd_unemployment_data_instance = OECDUnemploymentData.from_json(json)
# print the JSON string representation of the object
print(OECDUnemploymentData.to_json())

# convert the object into a dict
oecd_unemployment_data_dict = oecd_unemployment_data_instance.to_dict()
# create an instance of OECDUnemploymentData from a dict
oecd_unemployment_data_from_dict = OECDUnemploymentData.from_dict(oecd_unemployment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


