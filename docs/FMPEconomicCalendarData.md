# FMPEconomicCalendarData

FMP Economics Calendar Data.  Source: https://site.financialmodelingprep.com/developer/docs/economic-calendar-api

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**country** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**importance** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**consensus** | [**Consensus**](Consensus.md) |  | [optional] 
**previous** | [**Previous**](Previous.md) |  | [optional] 
**revised** | [**Revised**](Revised.md) |  | [optional] 
**actual** | [**Actual**](Actual.md) |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_economic_calendar_data import FMPEconomicCalendarData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEconomicCalendarData from a JSON string
fmp_economic_calendar_data_instance = FMPEconomicCalendarData.from_json(json)
# print the JSON string representation of the object
print(FMPEconomicCalendarData.to_json())

# convert the object into a dict
fmp_economic_calendar_data_dict = fmp_economic_calendar_data_instance.to_dict()
# create an instance of FMPEconomicCalendarData from a dict
fmp_economic_calendar_data_from_dict = FMPEconomicCalendarData.from_dict(fmp_economic_calendar_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


