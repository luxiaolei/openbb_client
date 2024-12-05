# OBBjectEconomicCalendar

OBBject with results of type EconomicCalendar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEconomicCalendarResultsInner]**](OBBjectEconomicCalendarResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_economic_calendar import OBBjectEconomicCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEconomicCalendar from a JSON string
ob_bject_economic_calendar_instance = OBBjectEconomicCalendar.from_json(json)
# print the JSON string representation of the object
print(OBBjectEconomicCalendar.to_json())

# convert the object into a dict
ob_bject_economic_calendar_dict = ob_bject_economic_calendar_instance.to_dict()
# create an instance of OBBjectEconomicCalendar from a dict
ob_bject_economic_calendar_from_dict = OBBjectEconomicCalendar.from_dict(ob_bject_economic_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


