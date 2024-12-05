# OBBjectShareStatistics

OBBject with results of type ShareStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectShareStatisticsResultsInner]**](OBBjectShareStatisticsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_share_statistics import OBBjectShareStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectShareStatistics from a JSON string
ob_bject_share_statistics_instance = OBBjectShareStatistics.from_json(json)
# print the JSON string representation of the object
print(OBBjectShareStatistics.to_json())

# convert the object into a dict
ob_bject_share_statistics_dict = ob_bject_share_statistics_instance.to_dict()
# create an instance of OBBjectShareStatistics from a dict
ob_bject_share_statistics_from_dict = OBBjectShareStatistics.from_dict(ob_bject_share_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


