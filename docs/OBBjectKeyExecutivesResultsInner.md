# OBBjectKeyExecutivesResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Designation of the key executive. | 
**name** | **str** | Name of the key executive. | 
**pay** | **int** |  | [optional] 
**currency_pay** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**year_born** | **int** |  | [optional] 
**title_since** | **int** |  | [optional] 
**exercised_value** | **int** |  | [optional] 
**unexercised_value** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_key_executives_results_inner import OBBjectKeyExecutivesResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectKeyExecutivesResultsInner from a JSON string
ob_bject_key_executives_results_inner_instance = OBBjectKeyExecutivesResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectKeyExecutivesResultsInner.to_json())

# convert the object into a dict
ob_bject_key_executives_results_inner_dict = ob_bject_key_executives_results_inner_instance.to_dict()
# create an instance of OBBjectKeyExecutivesResultsInner from a dict
ob_bject_key_executives_results_inner_from_dict = OBBjectKeyExecutivesResultsInner.from_dict(ob_bject_key_executives_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


