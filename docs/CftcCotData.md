# CftcCotData

CFTC Commitment of Traders Reports Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**report_week** | **str** |  | [optional] 
**market_and_exchange_names** | **str** |  | [optional] 
**cftc_contract_market_code** | **str** |  | [optional] 
**cftc_market_code** | **str** |  | [optional] 
**cftc_region_code** | **str** |  | [optional] 
**cftc_commodity_code** | **str** |  | [optional] 
**cftc_contract_market_code_quotes** | **str** |  | [optional] 
**cftc_market_code_quotes** | **str** |  | [optional] 
**cftc_commodity_code_quotes** | **str** |  | [optional] 
**cftc_subgroup_code** | **str** |  | [optional] 
**commodity** | **str** |  | [optional] 
**commodity_group** | **str** |  | [optional] 
**commodity_subgroup** | **str** |  | [optional] 
**futonly_or_combined** | **str** |  | [optional] 
**contract_units** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.cftc_cot_data import CftcCotData

# TODO update the JSON string below
json = "{}"
# create an instance of CftcCotData from a JSON string
cftc_cot_data_instance = CftcCotData.from_json(json)
# print the JSON string representation of the object
print(CftcCotData.to_json())

# convert the object into a dict
cftc_cot_data_dict = cftc_cot_data_instance.to_dict()
# create an instance of CftcCotData from a dict
cftc_cot_data_from_dict = CftcCotData.from_dict(cftc_cot_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


