# FederalReserveYieldCurveData

FederalReserve Yield Curve Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**maturity** | **str** | Maturity length of the security. | 
**maturity_years** | **float** |  | 

## Example

```python
from openbb_client.models.federal_reserve_yield_curve_data import FederalReserveYieldCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReserveYieldCurveData from a JSON string
federal_reserve_yield_curve_data_instance = FederalReserveYieldCurveData.from_json(json)
# print the JSON string representation of the object
print(FederalReserveYieldCurveData.to_json())

# convert the object into a dict
federal_reserve_yield_curve_data_dict = federal_reserve_yield_curve_data_instance.to_dict()
# create an instance of FederalReserveYieldCurveData from a dict
federal_reserve_yield_curve_data_from_dict = FederalReserveYieldCurveData.from_dict(federal_reserve_yield_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


