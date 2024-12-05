# SecCikMapData

SEC CIK Mapping Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cik** | [**Cik**](Cik.md) |  | [optional] 

## Example

```python
from openbb_client.models.sec_cik_map_data import SecCikMapData

# TODO update the JSON string below
json = "{}"
# create an instance of SecCikMapData from a JSON string
sec_cik_map_data_instance = SecCikMapData.from_json(json)
# print the JSON string representation of the object
print(SecCikMapData.to_json())

# convert the object into a dict
sec_cik_map_data_dict = sec_cik_map_data_instance.to_dict()
# create an instance of SecCikMapData from a dict
sec_cik_map_data_from_dict = SecCikMapData.from_dict(sec_cik_map_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


