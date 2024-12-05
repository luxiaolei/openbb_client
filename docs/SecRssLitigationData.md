# SecRssLitigationData

SEC Litigation RSS Feed Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**published** | **datetime** | The date of publication. | 
**title** | **str** | The title of the release. | 
**summary** | **str** | Short summary of the release. | 
**id** | **str** | The identifier associated with the release. | 
**link** | **str** | URL to the release. | 

## Example

```python
from openbb_client.models.sec_rss_litigation_data import SecRssLitigationData

# TODO update the JSON string below
json = "{}"
# create an instance of SecRssLitigationData from a JSON string
sec_rss_litigation_data_instance = SecRssLitigationData.from_json(json)
# print the JSON string representation of the object
print(SecRssLitigationData.to_json())

# convert the object into a dict
sec_rss_litigation_data_dict = sec_rss_litigation_data_instance.to_dict()
# create an instance of SecRssLitigationData from a dict
sec_rss_litigation_data_from_dict = SecRssLitigationData.from_dict(sec_rss_litigation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


