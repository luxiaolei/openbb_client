# EconDbAvailableIndicatorsData

EconDB Available Indicators Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol_root** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**iso** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**scale** | **str** |  | [optional] 
**multiplier** | **int** |  | 
**transformation** | **str** | Transformation type. | 
**source** | **str** |  | [optional] 
**first_date** | **date** |  | [optional] 
**last_date** | **date** |  | [optional] 
**last_insert_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.econ_db_available_indicators_data import EconDbAvailableIndicatorsData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbAvailableIndicatorsData from a JSON string
econ_db_available_indicators_data_instance = EconDbAvailableIndicatorsData.from_json(json)
# print the JSON string representation of the object
print(EconDbAvailableIndicatorsData.to_json())

# convert the object into a dict
econ_db_available_indicators_data_dict = econ_db_available_indicators_data_instance.to_dict()
# create an instance of EconDbAvailableIndicatorsData from a dict
econ_db_available_indicators_data_from_dict = EconDbAvailableIndicatorsData.from_dict(econ_db_available_indicators_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


