# OBBjectEtfHoldings

OBBject with results of type EtfHoldings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEtfHoldingsResultsInner]**](OBBjectEtfHoldingsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_holdings import OBBjectEtfHoldings

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfHoldings from a JSON string
ob_bject_etf_holdings_instance = OBBjectEtfHoldings.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfHoldings.to_json())

# convert the object into a dict
ob_bject_etf_holdings_dict = ob_bject_etf_holdings_instance.to_dict()
# create an instance of OBBjectEtfHoldings from a dict
ob_bject_etf_holdings_from_dict = OBBjectEtfHoldings.from_dict(ob_bject_etf_holdings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


