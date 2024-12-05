# YFinancePriceTargetConsensusData

YFinance Price Target Consensus Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**target_high** | **float** |  | [optional] 
**target_low** | **float** |  | [optional] 
**target_consensus** | **float** |  | [optional] 
**target_median** | **float** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**recommendation_mean** | **float** |  | [optional] 
**number_of_analysts** | **int** |  | [optional] 
**current_price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_price_target_consensus_data import YFinancePriceTargetConsensusData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinancePriceTargetConsensusData from a JSON string
y_finance_price_target_consensus_data_instance = YFinancePriceTargetConsensusData.from_json(json)
# print the JSON string representation of the object
print(YFinancePriceTargetConsensusData.to_json())

# convert the object into a dict
y_finance_price_target_consensus_data_dict = y_finance_price_target_consensus_data_instance.to_dict()
# create an instance of YFinancePriceTargetConsensusData from a dict
y_finance_price_target_consensus_data_from_dict = YFinancePriceTargetConsensusData.from_dict(y_finance_price_target_consensus_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


