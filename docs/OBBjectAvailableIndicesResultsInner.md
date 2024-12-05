# OBBjectAvailableIndicesResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**code** | **str** | ID code for keying the index in the OpenBB Terminal. | 
**symbol** | **str** | Symbol for the index. | 
**stock_exchange** | **str** | Stock exchange where the index is listed. | 
**exchange_short_name** | **str** | Short name of the stock exchange where the index is listed. | 

## Example

```python
from openbb_client.models.ob_bject_available_indices_results_inner import OBBjectAvailableIndicesResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectAvailableIndicesResultsInner from a JSON string
ob_bject_available_indices_results_inner_instance = OBBjectAvailableIndicesResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectAvailableIndicesResultsInner.to_json())

# convert the object into a dict
ob_bject_available_indices_results_inner_dict = ob_bject_available_indices_results_inner_instance.to_dict()
# create an instance of OBBjectAvailableIndicesResultsInner from a dict
ob_bject_available_indices_results_inner_from_dict = OBBjectAvailableIndicesResultsInner.from_dict(ob_bject_available_indices_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


