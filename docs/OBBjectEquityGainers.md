# OBBjectEquityGainers

OBBject with results of type EquityGainers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFGainersData]**](YFGainersData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_gainers import OBBjectEquityGainers

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityGainers from a JSON string
ob_bject_equity_gainers_instance = OBBjectEquityGainers.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityGainers.to_json())

# convert the object into a dict
ob_bject_equity_gainers_dict = ob_bject_equity_gainers_instance.to_dict()
# create an instance of OBBjectEquityGainers from a dict
ob_bject_equity_gainers_from_dict = OBBjectEquityGainers.from_dict(ob_bject_equity_gainers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


