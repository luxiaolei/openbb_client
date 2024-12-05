# OpenbbFredModelsUsYieldCurveFREDYieldCurveData

FRED US Yield Curve Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity** | **float** | Maturity of the treasury rate in years. | 
**rate** | **float** | Associated rate given in decimal form (0.05 is 5%) | 

## Example

```python
from openbb_client.models.openbb_fred_models_us_yield_curve_fred_yield_curve_data import OpenbbFredModelsUsYieldCurveFREDYieldCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of OpenbbFredModelsUsYieldCurveFREDYieldCurveData from a JSON string
openbb_fred_models_us_yield_curve_fred_yield_curve_data_instance = OpenbbFredModelsUsYieldCurveFREDYieldCurveData.from_json(json)
# print the JSON string representation of the object
print(OpenbbFredModelsUsYieldCurveFREDYieldCurveData.to_json())

# convert the object into a dict
openbb_fred_models_us_yield_curve_fred_yield_curve_data_dict = openbb_fred_models_us_yield_curve_fred_yield_curve_data_instance.to_dict()
# create an instance of OpenbbFredModelsUsYieldCurveFREDYieldCurveData from a dict
openbb_fred_models_us_yield_curve_fred_yield_curve_data_from_dict = OpenbbFredModelsUsYieldCurveFREDYieldCurveData.from_dict(openbb_fred_models_us_yield_curve_fred_yield_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


