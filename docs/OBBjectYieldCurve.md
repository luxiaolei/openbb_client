# OBBjectYieldCurve

OBBject with results of type YieldCurve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectYieldCurveResultsInner]**](OBBjectYieldCurveResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_yield_curve import OBBjectYieldCurve

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectYieldCurve from a JSON string
ob_bject_yield_curve_instance = OBBjectYieldCurve.from_json(json)
# print the JSON string representation of the object
print(OBBjectYieldCurve.to_json())

# convert the object into a dict
ob_bject_yield_curve_dict = ob_bject_yield_curve_instance.to_dict()
# create an instance of OBBjectYieldCurve from a dict
ob_bject_yield_curve_from_dict = OBBjectYieldCurve.from_dict(ob_bject_yield_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


