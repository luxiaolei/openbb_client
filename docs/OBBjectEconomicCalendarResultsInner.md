# OBBjectEconomicCalendarResultsInner


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
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_economic_calendar_results_inner import OBBjectEconomicCalendarResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEconomicCalendarResultsInner from a JSON string
ob_bject_economic_calendar_results_inner_instance = OBBjectEconomicCalendarResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectEconomicCalendarResultsInner.to_json())

# convert the object into a dict
ob_bject_economic_calendar_results_inner_dict = ob_bject_economic_calendar_results_inner_instance.to_dict()
# create an instance of OBBjectEconomicCalendarResultsInner from a dict
ob_bject_economic_calendar_results_inner_from_dict = OBBjectEconomicCalendarResultsInner.from_dict(ob_bject_economic_calendar_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


