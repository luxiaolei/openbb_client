# IntrinioCalendarIpoData

Intrinio IPO Calendar Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**ipo_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**offer_amount** | **float** |  | [optional] 
**share_price** | **float** |  | [optional] 
**share_price_lowest** | **float** |  | [optional] 
**share_price_highest** | **float** |  | [optional] 
**share_count** | **int** |  | [optional] 
**share_count_lowest** | **int** |  | [optional] 
**share_count_highest** | **int** |  | [optional] 
**announcement_url** | **str** |  | [optional] 
**sec_report_url** | **str** |  | [optional] 
**open_price** | **float** |  | [optional] 
**close_price** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**day_change** | **float** |  | [optional] 
**week_change** | **float** |  | [optional] 
**month_change** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**company** | [**IntrinioCompany**](IntrinioCompany.md) |  | [optional] 
**security** | [**IntrinioSecurity**](IntrinioSecurity.md) |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_calendar_ipo_data import IntrinioCalendarIpoData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioCalendarIpoData from a JSON string
intrinio_calendar_ipo_data_instance = IntrinioCalendarIpoData.from_json(json)
# print the JSON string representation of the object
print(IntrinioCalendarIpoData.to_json())

# convert the object into a dict
intrinio_calendar_ipo_data_dict = intrinio_calendar_ipo_data_instance.to_dict()
# create an instance of IntrinioCalendarIpoData from a dict
intrinio_calendar_ipo_data_from_dict = IntrinioCalendarIpoData.from_dict(intrinio_calendar_ipo_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


