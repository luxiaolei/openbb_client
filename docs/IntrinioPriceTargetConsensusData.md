# IntrinioPriceTargetConsensusData

Intrinio Price Target Consensus  Data.

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

## Example

```python
from openbb_client.models.intrinio_price_target_consensus_data import IntrinioPriceTargetConsensusData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioPriceTargetConsensusData from a JSON string
intrinio_price_target_consensus_data_instance = IntrinioPriceTargetConsensusData.from_json(json)
# print the JSON string representation of the object
print(IntrinioPriceTargetConsensusData.to_json())

# convert the object into a dict
intrinio_price_target_consensus_data_dict = intrinio_price_target_consensus_data_instance.to_dict()
# create an instance of IntrinioPriceTargetConsensusData from a dict
intrinio_price_target_consensus_data_from_dict = IntrinioPriceTargetConsensusData.from_dict(intrinio_price_target_consensus_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


