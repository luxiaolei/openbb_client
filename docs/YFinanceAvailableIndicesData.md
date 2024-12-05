# YFinanceAvailableIndicesData

Yahoo Finance Available Indices Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**code** | **str** | ID code for keying the index in the OpenBB Terminal. | 
**symbol** | **str** | Symbol for the index. | 

## Example

```python
from openbb_client.models.y_finance_available_indices_data import YFinanceAvailableIndicesData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceAvailableIndicesData from a JSON string
y_finance_available_indices_data_instance = YFinanceAvailableIndicesData.from_json(json)
# print the JSON string representation of the object
print(YFinanceAvailableIndicesData.to_json())

# convert the object into a dict
y_finance_available_indices_data_dict = y_finance_available_indices_data_instance.to_dict()
# create an instance of YFinanceAvailableIndicesData from a dict
y_finance_available_indices_data_from_dict = YFinanceAvailableIndicesData.from_dict(y_finance_available_indices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


