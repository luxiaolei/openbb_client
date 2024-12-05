# OBBjectEquityScreener

OBBject with results of type EquityScreener

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEquityScreenerResultsInner]**](OBBjectEquityScreenerResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_screener import OBBjectEquityScreener

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityScreener from a JSON string
ob_bject_equity_screener_instance = OBBjectEquityScreener.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityScreener.to_json())

# convert the object into a dict
ob_bject_equity_screener_dict = ob_bject_equity_screener_instance.to_dict()
# create an instance of OBBjectEquityScreener from a dict
ob_bject_equity_screener_from_dict = OBBjectEquityScreener.from_dict(ob_bject_equity_screener_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


