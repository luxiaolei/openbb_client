# EiaShortTermEnergyOutlookData

EIA Short Term Energy Outlook Data Model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**table** | **str** |  | [optional] 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**order** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**value** | [**Value4**](Value4.md) |  | 
**unit** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.eia_short_term_energy_outlook_data import EiaShortTermEnergyOutlookData

# TODO update the JSON string below
json = "{}"
# create an instance of EiaShortTermEnergyOutlookData from a JSON string
eia_short_term_energy_outlook_data_instance = EiaShortTermEnergyOutlookData.from_json(json)
# print the JSON string representation of the object
print(EiaShortTermEnergyOutlookData.to_json())

# convert the object into a dict
eia_short_term_energy_outlook_data_dict = eia_short_term_energy_outlook_data_instance.to_dict()
# create an instance of EiaShortTermEnergyOutlookData from a dict
eia_short_term_energy_outlook_data_from_dict = EiaShortTermEnergyOutlookData.from_dict(eia_short_term_energy_outlook_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


