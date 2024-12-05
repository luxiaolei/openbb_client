# OBBjectPriceTargetConsensusResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**target_high** | **float** |  | [optional] 
**target_low** | **float** |  | [optional] 
**target_consensus** | **float** |  | [optional] 
**target_median** | **float** |  | [optional] 
**standard_deviation** | **float** |  | [optional] 
**total_anaylsts** | **int** |  | [optional] 
**raised** | **int** |  | [optional] 
**lowered** | **int** |  | [optional] 
**most_recent_date** | **date** |  | [optional] 
**industry_group_number** | **int** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**recommendation_mean** | **float** |  | [optional] 
**number_of_analysts** | **int** |  | [optional] 
**current_price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_price_target_consensus_results_inner import OBBjectPriceTargetConsensusResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPriceTargetConsensusResultsInner from a JSON string
ob_bject_price_target_consensus_results_inner_instance = OBBjectPriceTargetConsensusResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectPriceTargetConsensusResultsInner.to_json())

# convert the object into a dict
ob_bject_price_target_consensus_results_inner_dict = ob_bject_price_target_consensus_results_inner_instance.to_dict()
# create an instance of OBBjectPriceTargetConsensusResultsInner from a dict
ob_bject_price_target_consensus_results_inner_from_dict = OBBjectPriceTargetConsensusResultsInner.from_dict(ob_bject_price_target_consensus_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


