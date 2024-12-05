# OBBjectKeyMetrics

OBBject with results of type KeyMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectKeyMetricsResultsInner]**](OBBjectKeyMetricsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_key_metrics import OBBjectKeyMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectKeyMetrics from a JSON string
ob_bject_key_metrics_instance = OBBjectKeyMetrics.from_json(json)
# print the JSON string representation of the object
print(OBBjectKeyMetrics.to_json())

# convert the object into a dict
ob_bject_key_metrics_dict = ob_bject_key_metrics_instance.to_dict()
# create an instance of OBBjectKeyMetrics from a dict
ob_bject_key_metrics_from_dict = OBBjectKeyMetrics.from_dict(ob_bject_key_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


