# OBBjectYieldCurveResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**maturity** | **str** | Maturity length of the security. | 
**maturity_years** | **float** |  | 

## Example

```python
from openbb_client.models.ob_bject_yield_curve_results_inner import OBBjectYieldCurveResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectYieldCurveResultsInner from a JSON string
ob_bject_yield_curve_results_inner_instance = OBBjectYieldCurveResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectYieldCurveResultsInner.to_json())

# convert the object into a dict
ob_bject_yield_curve_results_inner_dict = ob_bject_yield_curve_results_inner_instance.to_dict()
# create an instance of OBBjectYieldCurveResultsInner from a dict
ob_bject_yield_curve_results_inner_from_dict = OBBjectYieldCurveResultsInner.from_dict(ob_bject_yield_curve_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


