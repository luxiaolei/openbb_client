# FMPEarningsCallTranscriptData

FMP Earnings Call Transcript Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**quarter** | **int** | Quarter of the earnings call transcript. | 
**year** | **int** | Year of the earnings call transcript. | 
**var_date** | **datetime** | The date of the data. | 
**content** | **str** | Content of the earnings call transcript. | 

## Example

```python
from openbb_client.models.fmp_earnings_call_transcript_data import FMPEarningsCallTranscriptData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEarningsCallTranscriptData from a JSON string
fmp_earnings_call_transcript_data_instance = FMPEarningsCallTranscriptData.from_json(json)
# print the JSON string representation of the object
print(FMPEarningsCallTranscriptData.to_json())

# convert the object into a dict
fmp_earnings_call_transcript_data_dict = fmp_earnings_call_transcript_data_instance.to_dict()
# create an instance of FMPEarningsCallTranscriptData from a dict
fmp_earnings_call_transcript_data_from_dict = FMPEarningsCallTranscriptData.from_dict(fmp_earnings_call_transcript_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


