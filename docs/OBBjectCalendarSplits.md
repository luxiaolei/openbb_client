# OBBjectCalendarSplits

OBBject with results of type CalendarSplits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPCalendarSplitsData]**](FMPCalendarSplitsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_calendar_splits import OBBjectCalendarSplits

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCalendarSplits from a JSON string
ob_bject_calendar_splits_instance = OBBjectCalendarSplits.from_json(json)
# print the JSON string representation of the object
print(OBBjectCalendarSplits.to_json())

# convert the object into a dict
ob_bject_calendar_splits_dict = ob_bject_calendar_splits_instance.to_dict()
# create an instance of OBBjectCalendarSplits from a dict
ob_bject_calendar_splits_from_dict = OBBjectCalendarSplits.from_dict(ob_bject_calendar_splits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


