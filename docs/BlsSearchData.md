# BlsSearchData

BLS Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**title** | **str** |  | [optional] 
**survey_name** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.bls_search_data import BlsSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of BlsSearchData from a JSON string
bls_search_data_instance = BlsSearchData.from_json(json)
# print the JSON string representation of the object
print(BlsSearchData.to_json())

# convert the object into a dict
bls_search_data_dict = bls_search_data_instance.to_dict()
# create an instance of BlsSearchData from a dict
bls_search_data_from_dict = BlsSearchData.from_dict(bls_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


