# OBBjectCalendarDividend

OBBject with results of type CalendarDividend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPCalendarDividendData]**](FMPCalendarDividendData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_calendar_dividend import OBBjectCalendarDividend

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCalendarDividend from a JSON string
ob_bject_calendar_dividend_instance = OBBjectCalendarDividend.from_json(json)
# print the JSON string representation of the object
print(OBBjectCalendarDividend.to_json())

# convert the object into a dict
ob_bject_calendar_dividend_dict = ob_bject_calendar_dividend_instance.to_dict()
# create an instance of OBBjectCalendarDividend from a dict
ob_bject_calendar_dividend_from_dict = OBBjectCalendarDividend.from_dict(ob_bject_calendar_dividend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


