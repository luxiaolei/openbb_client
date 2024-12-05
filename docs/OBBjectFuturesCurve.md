# OBBjectFuturesCurve

OBBject with results of type FuturesCurve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFinanceFuturesCurveData]**](YFinanceFuturesCurveData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_futures_curve import OBBjectFuturesCurve

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectFuturesCurve from a JSON string
ob_bject_futures_curve_instance = OBBjectFuturesCurve.from_json(json)
# print the JSON string representation of the object
print(OBBjectFuturesCurve.to_json())

# convert the object into a dict
ob_bject_futures_curve_dict = ob_bject_futures_curve_instance.to_dict()
# create an instance of OBBjectFuturesCurve from a dict
ob_bject_futures_curve_from_dict = OBBjectFuturesCurve.from_dict(ob_bject_futures_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


