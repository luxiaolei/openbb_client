# FMPCalendarEarningsData

FMP Earnings Calendar Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_date** | **date** | The date of the earnings report. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**eps_previous** | **float** |  | [optional] 
**eps_consensus** | **float** |  | [optional] 
**eps_actual** | **float** |  | [optional] 
**revenue_actual** | **float** |  | [optional] 
**revenue_consensus** | **float** |  | [optional] 
**period_ending** | **date** |  | [optional] 
**reporting_time** | **str** |  | [optional] 
**updated_date** | **date** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_calendar_earnings_data import FMPCalendarEarningsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCalendarEarningsData from a JSON string
fmp_calendar_earnings_data_instance = FMPCalendarEarningsData.from_json(json)
# print the JSON string representation of the object
print(FMPCalendarEarningsData.to_json())

# convert the object into a dict
fmp_calendar_earnings_data_dict = fmp_calendar_earnings_data_instance.to_dict()
# create an instance of FMPCalendarEarningsData from a dict
fmp_calendar_earnings_data_from_dict = FMPCalendarEarningsData.from_dict(fmp_calendar_earnings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


