# OECDSTIRData

OECD Short Term Interest Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**value** | **float** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.oecdstir_data import OECDSTIRData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDSTIRData from a JSON string
oecdstir_data_instance = OECDSTIRData.from_json(json)
# print the JSON string representation of the object
print(OECDSTIRData.to_json())

# convert the object into a dict
oecdstir_data_dict = oecdstir_data_instance.to_dict()
# create an instance of OECDSTIRData from a dict
oecdstir_data_from_dict = OECDSTIRData.from_dict(oecdstir_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


