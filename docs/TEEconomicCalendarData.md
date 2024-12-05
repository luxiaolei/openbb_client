# TEEconomicCalendarData

Trading Economics Economic Calendar Data.

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
**forecast** | [**Forecast**](Forecast.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**reference_date** | **date** |  | [optional] 
**calendar_id** | **int** |  | [optional] 
**date_span** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**ticker** | **str** |  | [optional] 
**te_url** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.te_economic_calendar_data import TEEconomicCalendarData

# TODO update the JSON string below
json = "{}"
# create an instance of TEEconomicCalendarData from a JSON string
te_economic_calendar_data_instance = TEEconomicCalendarData.from_json(json)
# print the JSON string representation of the object
print(TEEconomicCalendarData.to_json())

# convert the object into a dict
te_economic_calendar_data_dict = te_economic_calendar_data_instance.to_dict()
# create an instance of TEEconomicCalendarData from a dict
te_economic_calendar_data_from_dict = TEEconomicCalendarData.from_dict(te_economic_calendar_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


