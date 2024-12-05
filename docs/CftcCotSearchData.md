# CftcCotSearchData

CFTC Commitment of Traders Reports Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | CFTC market contract code of the report. | 
**name** | **str** | Name of the underlying asset. | 
**category** | **str** |  | [optional] 
**subcategory** | **str** |  | [optional] 
**units** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**commodity** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.cftc_cot_search_data import CftcCotSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of CftcCotSearchData from a JSON string
cftc_cot_search_data_instance = CftcCotSearchData.from_json(json)
# print the JSON string representation of the object
print(CftcCotSearchData.to_json())

# convert the object into a dict
cftc_cot_search_data_dict = cftc_cot_search_data_instance.to_dict()
# create an instance of CftcCotSearchData from a dict
cftc_cot_search_data_from_dict = CftcCotSearchData.from_dict(cftc_cot_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


