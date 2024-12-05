# OECDLTIRData

OECD Long Term Interest Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**value** | **float** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.oecdltir_data import OECDLTIRData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDLTIRData from a JSON string
oecdltir_data_instance = OECDLTIRData.from_json(json)
# print the JSON string representation of the object
print(OECDLTIRData.to_json())

# convert the object into a dict
oecdltir_data_dict = oecdltir_data_instance.to_dict()
# create an instance of OECDLTIRData from a dict
oecdltir_data_from_dict = OECDLTIRData.from_dict(oecdltir_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


