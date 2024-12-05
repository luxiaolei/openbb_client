# OBBjectEquityQuote

OBBject with results of type EquityQuote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEquityQuoteResultsInner]**](OBBjectEquityQuoteResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_quote import OBBjectEquityQuote

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityQuote from a JSON string
ob_bject_equity_quote_instance = OBBjectEquityQuote.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityQuote.to_json())

# convert the object into a dict
ob_bject_equity_quote_dict = ob_bject_equity_quote_instance.to_dict()
# create an instance of OBBjectEquityQuote from a dict
ob_bject_equity_quote_from_dict = OBBjectEquityQuote.from_dict(ob_bject_equity_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


