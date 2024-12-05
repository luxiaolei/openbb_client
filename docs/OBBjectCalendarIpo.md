# OBBjectCalendarIpo

OBBject with results of type CalendarIpo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[IntrinioCalendarIpoData]**](IntrinioCalendarIpoData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_calendar_ipo import OBBjectCalendarIpo

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCalendarIpo from a JSON string
ob_bject_calendar_ipo_instance = OBBjectCalendarIpo.from_json(json)
# print the JSON string representation of the object
print(OBBjectCalendarIpo.to_json())

# convert the object into a dict
ob_bject_calendar_ipo_dict = ob_bject_calendar_ipo_instance.to_dict()
# create an instance of OBBjectCalendarIpo from a dict
ob_bject_calendar_ipo_from_dict = OBBjectCalendarIpo.from_dict(ob_bject_calendar_ipo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


