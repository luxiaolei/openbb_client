# SecEquityFtdData

SEC Equity FTD Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **date** |  | [optional] 
**symbol** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**price** | **float** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.sec_equity_ftd_data import SecEquityFtdData

# TODO update the JSON string below
json = "{}"
# create an instance of SecEquityFtdData from a JSON string
sec_equity_ftd_data_instance = SecEquityFtdData.from_json(json)
# print the JSON string representation of the object
print(SecEquityFtdData.to_json())

# convert the object into a dict
sec_equity_ftd_data_dict = sec_equity_ftd_data_instance.to_dict()
# create an instance of SecEquityFtdData from a dict
sec_equity_ftd_data_from_dict = SecEquityFtdData.from_dict(sec_equity_ftd_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


