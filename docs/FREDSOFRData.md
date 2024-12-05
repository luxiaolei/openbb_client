# FREDSOFRData

FRED SOFR Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** | Effective federal funds rate. | 
**percentile_1** | **float** |  | [optional] 
**percentile_25** | **float** |  | [optional] 
**percentile_75** | **float** |  | [optional] 
**percentile_99** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 
**average_30d** | **float** |  | [optional] 
**average_90d** | **float** |  | [optional] 
**average_180d** | **float** |  | [optional] 
**index** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fredsofr_data import FREDSOFRData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDSOFRData from a JSON string
fredsofr_data_instance = FREDSOFRData.from_json(json)
# print the JSON string representation of the object
print(FREDSOFRData.to_json())

# convert the object into a dict
fredsofr_data_dict = fredsofr_data_instance.to_dict()
# create an instance of FREDSOFRData from a dict
fredsofr_data_from_dict = FREDSOFRData.from_dict(fredsofr_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


