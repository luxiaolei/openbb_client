# FMPCalendarSplitsData

FMP Calendar Splits Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**label** | **str** | Label of the stock splits. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**numerator** | **float** | Numerator of the stock splits. | 
**denominator** | **float** | Denominator of the stock splits. | 

## Example

```python
from openbb_client.models.fmp_calendar_splits_data import FMPCalendarSplitsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCalendarSplitsData from a JSON string
fmp_calendar_splits_data_instance = FMPCalendarSplitsData.from_json(json)
# print the JSON string representation of the object
print(FMPCalendarSplitsData.to_json())

# convert the object into a dict
fmp_calendar_splits_data_dict = fmp_calendar_splits_data_instance.to_dict()
# create an instance of FMPCalendarSplitsData from a dict
fmp_calendar_splits_data_from_dict = FMPCalendarSplitsData.from_dict(fmp_calendar_splits_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


