# OBBjectSOFRResultsInner


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
from openbb_client.models.ob_bject_sofr_results_inner import OBBjectSOFRResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSOFRResultsInner from a JSON string
ob_bject_sofr_results_inner_instance = OBBjectSOFRResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectSOFRResultsInner.to_json())

# convert the object into a dict
ob_bject_sofr_results_inner_dict = ob_bject_sofr_results_inner_instance.to_dict()
# create an instance of OBBjectSOFRResultsInner from a dict
ob_bject_sofr_results_inner_from_dict = OBBjectSOFRResultsInner.from_dict(ob_bject_sofr_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


