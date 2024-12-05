# OBBjectRssLitigation

OBBject with results of type RssLitigation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[SecRssLitigationData]**](SecRssLitigationData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_rss_litigation import OBBjectRssLitigation

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectRssLitigation from a JSON string
ob_bject_rss_litigation_instance = OBBjectRssLitigation.from_json(json)
# print the JSON string representation of the object
print(OBBjectRssLitigation.to_json())

# convert the object into a dict
ob_bject_rss_litigation_dict = ob_bject_rss_litigation_instance.to_dict()
# create an instance of OBBjectRssLitigation from a dict
ob_bject_rss_litigation_from_dict = OBBjectRssLitigation.from_dict(ob_bject_rss_litigation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


