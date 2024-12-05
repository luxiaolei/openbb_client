# FMPYieldCurveData

FMP Yield Curve Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**maturity** | **str** | Maturity length of the security. | 
**maturity_years** | **float** |  | 

## Example

```python
from openbb_client.models.fmp_yield_curve_data import FMPYieldCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPYieldCurveData from a JSON string
fmp_yield_curve_data_instance = FMPYieldCurveData.from_json(json)
# print the JSON string representation of the object
print(FMPYieldCurveData.to_json())

# convert the object into a dict
fmp_yield_curve_data_dict = fmp_yield_curve_data_instance.to_dict()
# create an instance of FMPYieldCurveData from a dict
fmp_yield_curve_data_from_dict = FMPYieldCurveData.from_dict(fmp_yield_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


