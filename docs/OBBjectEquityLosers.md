# OBBjectEquityLosers

OBBject with results of type EquityLosers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFLosersData]**](YFLosersData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_losers import OBBjectEquityLosers

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityLosers from a JSON string
ob_bject_equity_losers_instance = OBBjectEquityLosers.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityLosers.to_json())

# convert the object into a dict
ob_bject_equity_losers_dict = ob_bject_equity_losers_instance.to_dict()
# create an instance of OBBjectEquityLosers from a dict
ob_bject_equity_losers_from_dict = OBBjectEquityLosers.from_dict(ob_bject_equity_losers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


