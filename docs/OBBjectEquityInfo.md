# OBBjectEquityInfo

OBBject with results of type EquityInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEquityInfoResultsInner]**](OBBjectEquityInfoResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_info import OBBjectEquityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityInfo from a JSON string
ob_bject_equity_info_instance = OBBjectEquityInfo.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityInfo.to_json())

# convert the object into a dict
ob_bject_equity_info_dict = ob_bject_equity_info_instance.to_dict()
# create an instance of OBBjectEquityInfo from a dict
ob_bject_equity_info_from_dict = OBBjectEquityInfo.from_dict(ob_bject_equity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


