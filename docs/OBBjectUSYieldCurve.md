# OBBjectUSYieldCurve

OBBject with results of type USYieldCurve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OpenbbFredModelsUsYieldCurveFREDYieldCurveData]**](OpenbbFredModelsUsYieldCurveFREDYieldCurveData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_us_yield_curve import OBBjectUSYieldCurve

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectUSYieldCurve from a JSON string
ob_bject_us_yield_curve_instance = OBBjectUSYieldCurve.from_json(json)
# print the JSON string representation of the object
print(OBBjectUSYieldCurve.to_json())

# convert the object into a dict
ob_bject_us_yield_curve_dict = ob_bject_us_yield_curve_instance.to_dict()
# create an instance of OBBjectUSYieldCurve from a dict
ob_bject_us_yield_curve_from_dict = OBBjectUSYieldCurve.from_dict(ob_bject_us_yield_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


