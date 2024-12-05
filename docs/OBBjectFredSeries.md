# OBBjectFredSeries

OBBject with results of type FredSeries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectFredSeriesResultsInner]**](OBBjectFredSeriesResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_fred_series import OBBjectFredSeries

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectFredSeries from a JSON string
ob_bject_fred_series_instance = OBBjectFredSeries.from_json(json)
# print the JSON string representation of the object
print(OBBjectFredSeries.to_json())

# convert the object into a dict
ob_bject_fred_series_dict = ob_bject_fred_series_instance.to_dict()
# create an instance of OBBjectFredSeries from a dict
ob_bject_fred_series_from_dict = OBBjectFredSeries.from_dict(ob_bject_fred_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


