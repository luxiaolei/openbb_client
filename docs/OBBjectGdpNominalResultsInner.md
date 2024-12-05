# OBBjectGdpNominalResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** | The country represented by the GDP value. | [optional] 
**value** | [**Value9**](Value9.md) |  | 
**nominal_growth_qoq** | **float** | Nominal GDP growth rate quarter over quarter. | 
**nominal_growth_yoy** | **float** | Nominal GDP growth rate year over year. | 

## Example

```python
from openbb_client.models.ob_bject_gdp_nominal_results_inner import OBBjectGdpNominalResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectGdpNominalResultsInner from a JSON string
ob_bject_gdp_nominal_results_inner_instance = OBBjectGdpNominalResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectGdpNominalResultsInner.to_json())

# convert the object into a dict
ob_bject_gdp_nominal_results_inner_dict = ob_bject_gdp_nominal_results_inner_instance.to_dict()
# create an instance of OBBjectGdpNominalResultsInner from a dict
ob_bject_gdp_nominal_results_inner_from_dict = OBBjectGdpNominalResultsInner.from_dict(ob_bject_gdp_nominal_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


