# OBBjectPriceTargetConsensus

OBBject with results of type PriceTargetConsensus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectPriceTargetConsensusResultsInner]**](OBBjectPriceTargetConsensusResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_price_target_consensus import OBBjectPriceTargetConsensus

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPriceTargetConsensus from a JSON string
ob_bject_price_target_consensus_instance = OBBjectPriceTargetConsensus.from_json(json)
# print the JSON string representation of the object
print(OBBjectPriceTargetConsensus.to_json())

# convert the object into a dict
ob_bject_price_target_consensus_dict = ob_bject_price_target_consensus_instance.to_dict()
# create an instance of OBBjectPriceTargetConsensus from a dict
ob_bject_price_target_consensus_from_dict = OBBjectPriceTargetConsensus.from_dict(ob_bject_price_target_consensus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


