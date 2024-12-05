# OBBjectEtfPricePerformance

OBBject with results of type EtfPricePerformance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEtfPricePerformanceResultsInner]**](OBBjectEtfPricePerformanceResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_price_performance import OBBjectEtfPricePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfPricePerformance from a JSON string
ob_bject_etf_price_performance_instance = OBBjectEtfPricePerformance.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfPricePerformance.to_json())

# convert the object into a dict
ob_bject_etf_price_performance_dict = ob_bject_etf_price_performance_instance.to_dict()
# create an instance of OBBjectEtfPricePerformance from a dict
ob_bject_etf_price_performance_from_dict = OBBjectEtfPricePerformance.from_dict(ob_bject_etf_price_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


