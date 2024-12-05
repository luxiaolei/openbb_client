# SecInstitutionsSearchData

SEC Institutions Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**cik** | [**Cik2**](Cik2.md) |  | [optional] 

## Example

```python
from openbb_client.models.sec_institutions_search_data import SecInstitutionsSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of SecInstitutionsSearchData from a JSON string
sec_institutions_search_data_instance = SecInstitutionsSearchData.from_json(json)
# print the JSON string representation of the object
print(SecInstitutionsSearchData.to_json())

# convert the object into a dict
sec_institutions_search_data_dict = sec_institutions_search_data_instance.to_dict()
# create an instance of SecInstitutionsSearchData from a dict
sec_institutions_search_data_from_dict = SecInstitutionsSearchData.from_dict(sec_institutions_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


