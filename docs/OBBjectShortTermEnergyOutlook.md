# OBBjectShortTermEnergyOutlook

OBBject with results of type ShortTermEnergyOutlook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[EiaShortTermEnergyOutlookData]**](EiaShortTermEnergyOutlookData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_short_term_energy_outlook import OBBjectShortTermEnergyOutlook

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectShortTermEnergyOutlook from a JSON string
ob_bject_short_term_energy_outlook_instance = OBBjectShortTermEnergyOutlook.from_json(json)
# print the JSON string representation of the object
print(OBBjectShortTermEnergyOutlook.to_json())

# convert the object into a dict
ob_bject_short_term_energy_outlook_dict = ob_bject_short_term_energy_outlook_instance.to_dict()
# create an instance of OBBjectShortTermEnergyOutlook from a dict
ob_bject_short_term_energy_outlook_from_dict = OBBjectShortTermEnergyOutlook.from_dict(ob_bject_short_term_energy_outlook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


