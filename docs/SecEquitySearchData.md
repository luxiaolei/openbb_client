# SecEquitySearchData

SEC Equity Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**cik** | **str** | Central Index Key | 

## Example

```python
from openbb_client.models.sec_equity_search_data import SecEquitySearchData

# TODO update the JSON string below
json = "{}"
# create an instance of SecEquitySearchData from a JSON string
sec_equity_search_data_instance = SecEquitySearchData.from_json(json)
# print the JSON string representation of the object
print(SecEquitySearchData.to_json())

# convert the object into a dict
sec_equity_search_data_dict = sec_equity_search_data_instance.to_dict()
# create an instance of SecEquitySearchData from a dict
sec_equity_search_data_from_dict = SecEquitySearchData.from_dict(sec_equity_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


