# FMPPriceTargetConsensusData

FMP Price Target Consensus Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**target_high** | **float** |  | [optional] 
**target_low** | **float** |  | [optional] 
**target_consensus** | **float** |  | [optional] 
**target_median** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_price_target_consensus_data import FMPPriceTargetConsensusData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPPriceTargetConsensusData from a JSON string
fmp_price_target_consensus_data_instance = FMPPriceTargetConsensusData.from_json(json)
# print the JSON string representation of the object
print(FMPPriceTargetConsensusData.to_json())

# convert the object into a dict
fmp_price_target_consensus_data_dict = fmp_price_target_consensus_data_instance.to_dict()
# create an instance of FMPPriceTargetConsensusData from a dict
fmp_price_target_consensus_data_from_dict = FMPPriceTargetConsensusData.from_dict(fmp_price_target_consensus_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


