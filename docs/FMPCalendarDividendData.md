# FMPCalendarDividendData

FMP Dividend Calendar Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_dividend_date** | **date** | The ex-dividend date - the date on which the stock begins trading without rights to the dividend. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**amount** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**record_date** | **date** |  | [optional] 
**payment_date** | **date** |  | [optional] 
**declaration_date** | **date** |  | [optional] 
**adjusted_amount** | **float** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_calendar_dividend_data import FMPCalendarDividendData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCalendarDividendData from a JSON string
fmp_calendar_dividend_data_instance = FMPCalendarDividendData.from_json(json)
# print the JSON string representation of the object
print(FMPCalendarDividendData.to_json())

# convert the object into a dict
fmp_calendar_dividend_data_dict = fmp_calendar_dividend_data_instance.to_dict()
# create an instance of FMPCalendarDividendData from a dict
fmp_calendar_dividend_data_from_dict = FMPCalendarDividendData.from_dict(fmp_calendar_dividend_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


