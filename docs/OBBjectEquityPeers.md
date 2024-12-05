# OBBjectEquityPeers

OBBject with results of type EquityPeers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**FMPEquityPeersData**](FMPEquityPeersData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_peers import OBBjectEquityPeers

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityPeers from a JSON string
ob_bject_equity_peers_instance = OBBjectEquityPeers.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityPeers.to_json())

# convert the object into a dict
ob_bject_equity_peers_dict = ob_bject_equity_peers_instance.to_dict()
# create an instance of OBBjectEquityPeers from a dict
ob_bject_equity_peers_from_dict = OBBjectEquityPeers.from_dict(ob_bject_equity_peers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


