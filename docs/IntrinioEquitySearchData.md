# IntrinioEquitySearchData

Intrinio Equity Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**cik** | **str** |  | 
**lei** | **str** |  | 
**intrinio_id** | **str** | The Intrinio ID of the company. | 

## Example

```python
from openbb_client.models.intrinio_equity_search_data import IntrinioEquitySearchData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioEquitySearchData from a JSON string
intrinio_equity_search_data_instance = IntrinioEquitySearchData.from_json(json)
# print the JSON string representation of the object
print(IntrinioEquitySearchData.to_json())

# convert the object into a dict
intrinio_equity_search_data_dict = intrinio_equity_search_data_instance.to_dict()
# create an instance of IntrinioEquitySearchData from a dict
intrinio_equity_search_data_from_dict = IntrinioEquitySearchData.from_dict(intrinio_equity_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


