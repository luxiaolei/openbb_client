# OBBjectEarningsCallTranscript

OBBject with results of type EarningsCallTranscript

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPEarningsCallTranscriptData]**](FMPEarningsCallTranscriptData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_earnings_call_transcript import OBBjectEarningsCallTranscript

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEarningsCallTranscript from a JSON string
ob_bject_earnings_call_transcript_instance = OBBjectEarningsCallTranscript.from_json(json)
# print the JSON string representation of the object
print(OBBjectEarningsCallTranscript.to_json())

# convert the object into a dict
ob_bject_earnings_call_transcript_dict = ob_bject_earnings_call_transcript_instance.to_dict()
# create an instance of OBBjectEarningsCallTranscript from a dict
ob_bject_earnings_call_transcript_from_dict = OBBjectEarningsCallTranscript.from_dict(ob_bject_earnings_call_transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


