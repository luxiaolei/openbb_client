# OBBjectGdpRealResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** | The country represented by the GDP value. | [optional] 
**value** | [**Value3**](Value3.md) |  | 
**real_growth_qoq** | **float** | Real GDP growth rate quarter over quarter. | 
**real_growth_yoy** | **float** | Real GDP growth rate year over year. | 

## Example

```python
from openbb_client.models.ob_bject_gdp_real_results_inner import OBBjectGdpRealResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectGdpRealResultsInner from a JSON string
ob_bject_gdp_real_results_inner_instance = OBBjectGdpRealResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectGdpRealResultsInner.to_json())

# convert the object into a dict
ob_bject_gdp_real_results_inner_dict = ob_bject_gdp_real_results_inner_instance.to_dict()
# create an instance of OBBjectGdpRealResultsInner from a dict
ob_bject_gdp_real_results_inner_from_dict = OBBjectGdpRealResultsInner.from_dict(ob_bject_gdp_real_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


