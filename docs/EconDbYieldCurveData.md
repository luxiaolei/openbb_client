# EconDbYieldCurveData

EconDB Yield Curve Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**maturity** | **str** | Maturity length of the security. | 
**maturity_years** | **float** |  | 

## Example

```python
from openbb_client.models.econ_db_yield_curve_data import EconDbYieldCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbYieldCurveData from a JSON string
econ_db_yield_curve_data_instance = EconDbYieldCurveData.from_json(json)
# print the JSON string representation of the object
print(EconDbYieldCurveData.to_json())

# convert the object into a dict
econ_db_yield_curve_data_dict = econ_db_yield_curve_data_instance.to_dict()
# create an instance of EconDbYieldCurveData from a dict
econ_db_yield_curve_data_from_dict = EconDbYieldCurveData.from_dict(econ_db_yield_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


