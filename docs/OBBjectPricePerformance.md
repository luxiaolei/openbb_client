# OBBjectPricePerformance

OBBject with results of type PricePerformance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPPricePerformanceData]**](FMPPricePerformanceData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_price_performance import OBBjectPricePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPricePerformance from a JSON string
ob_bject_price_performance_instance = OBBjectPricePerformance.from_json(json)
# print the JSON string representation of the object
print(OBBjectPricePerformance.to_json())

# convert the object into a dict
ob_bject_price_performance_dict = ob_bject_price_performance_instance.to_dict()
# create an instance of OBBjectPricePerformance from a dict
ob_bject_price_performance_from_dict = OBBjectPricePerformance.from_dict(ob_bject_price_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


