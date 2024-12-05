# OBBjectEtfInfo

OBBject with results of type EtfInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEtfInfoResultsInner]**](OBBjectEtfInfoResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_info import OBBjectEtfInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfInfo from a JSON string
ob_bject_etf_info_instance = OBBjectEtfInfo.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfInfo.to_json())

# convert the object into a dict
ob_bject_etf_info_dict = ob_bject_etf_info_instance.to_dict()
# create an instance of OBBjectEtfInfo from a dict
ob_bject_etf_info_from_dict = OBBjectEtfInfo.from_dict(ob_bject_etf_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


