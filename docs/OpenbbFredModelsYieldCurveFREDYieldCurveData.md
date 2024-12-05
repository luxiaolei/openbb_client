# OpenbbFredModelsYieldCurveFREDYieldCurveData

FRED Yield Curve Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**maturity** | **str** | Maturity length of the security. | 
**maturity_years** | **float** |  | 

## Example

```python
from openbb_client.models.openbb_fred_models_yield_curve_fred_yield_curve_data import OpenbbFredModelsYieldCurveFREDYieldCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of OpenbbFredModelsYieldCurveFREDYieldCurveData from a JSON string
openbb_fred_models_yield_curve_fred_yield_curve_data_instance = OpenbbFredModelsYieldCurveFREDYieldCurveData.from_json(json)
# print the JSON string representation of the object
print(OpenbbFredModelsYieldCurveFREDYieldCurveData.to_json())

# convert the object into a dict
openbb_fred_models_yield_curve_fred_yield_curve_data_dict = openbb_fred_models_yield_curve_fred_yield_curve_data_instance.to_dict()
# create an instance of OpenbbFredModelsYieldCurveFREDYieldCurveData from a dict
openbb_fred_models_yield_curve_fred_yield_curve_data_from_dict = OpenbbFredModelsYieldCurveFREDYieldCurveData.from_dict(openbb_fred_models_yield_curve_fred_yield_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


