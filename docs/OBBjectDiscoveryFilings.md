# OBBjectDiscoveryFilings

OBBject with results of type DiscoveryFilings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPDiscoveryFilingsData]**](FMPDiscoveryFilingsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_discovery_filings import OBBjectDiscoveryFilings

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectDiscoveryFilings from a JSON string
ob_bject_discovery_filings_instance = OBBjectDiscoveryFilings.from_json(json)
# print the JSON string representation of the object
print(OBBjectDiscoveryFilings.to_json())

# convert the object into a dict
ob_bject_discovery_filings_dict = ob_bject_discovery_filings_instance.to_dict()
# create an instance of OBBjectDiscoveryFilings from a dict
ob_bject_discovery_filings_from_dict = OBBjectDiscoveryFilings.from_dict(ob_bject_discovery_filings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


