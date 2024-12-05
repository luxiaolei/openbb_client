# OBBjectHistoricalDividends

OBBject with results of type HistoricalDividends

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectHistoricalDividendsResultsInner]**](OBBjectHistoricalDividendsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_historical_dividends import OBBjectHistoricalDividends

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectHistoricalDividends from a JSON string
ob_bject_historical_dividends_instance = OBBjectHistoricalDividends.from_json(json)
# print the JSON string representation of the object
print(OBBjectHistoricalDividends.to_json())

# convert the object into a dict
ob_bject_historical_dividends_dict = ob_bject_historical_dividends_instance.to_dict()
# create an instance of OBBjectHistoricalDividends from a dict
ob_bject_historical_dividends_from_dict = OBBjectHistoricalDividends.from_dict(ob_bject_historical_dividends_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


