# OECDCPIData

OECD CPI Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** |  | 
**value** | **float** | CPI index value or period change. | 
**expenditure** | **str** | Expenditure component of CPI. | 

## Example

```python
from openbb_client.models.oecdcpi_data import OECDCPIData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDCPIData from a JSON string
oecdcpi_data_instance = OECDCPIData.from_json(json)
# print the JSON string representation of the object
print(OECDCPIData.to_json())

# convert the object into a dict
oecdcpi_data_dict = oecdcpi_data_instance.to_dict()
# create an instance of OECDCPIData from a dict
oecdcpi_data_from_dict = OECDCPIData.from_dict(oecdcpi_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


