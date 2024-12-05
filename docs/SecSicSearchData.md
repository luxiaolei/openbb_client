# SecSicSearchData

SEC Standard Industrial Classification Code (SIC) Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sic** | **int** | Sector Industrial Code (SIC) | 
**industry** | **str** | Industry title. | 
**office** | **str** | Reporting office within the Corporate Finance Office | 

## Example

```python
from openbb_client.models.sec_sic_search_data import SecSicSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of SecSicSearchData from a JSON string
sec_sic_search_data_instance = SecSicSearchData.from_json(json)
# print the JSON string representation of the object
print(SecSicSearchData.to_json())

# convert the object into a dict
sec_sic_search_data_dict = sec_sic_search_data_instance.to_dict()
# create an instance of SecSicSearchData from a dict
sec_sic_search_data_from_dict = SecSicSearchData.from_dict(sec_sic_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


