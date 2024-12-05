# FederalReserveSOFRData

FederalReserve FED Data.

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

## Example

```python
from openbb_client.models.federal_reserve_sofr_data import FederalReserveSOFRData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReserveSOFRData from a JSON string
federal_reserve_sofr_data_instance = FederalReserveSOFRData.from_json(json)
# print the JSON string representation of the object
print(FederalReserveSOFRData.to_json())

# convert the object into a dict
federal_reserve_sofr_data_dict = federal_reserve_sofr_data_instance.to_dict()
# create an instance of FederalReserveSOFRData from a dict
federal_reserve_sofr_data_from_dict = FederalReserveSOFRData.from_dict(federal_reserve_sofr_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


