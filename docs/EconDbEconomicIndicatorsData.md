# EconDbEconomicIndicatorsData

EconDB Economic Indicators Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol_root** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 

## Example

```python
from openbb_client.models.econ_db_economic_indicators_data import EconDbEconomicIndicatorsData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbEconomicIndicatorsData from a JSON string
econ_db_economic_indicators_data_instance = EconDbEconomicIndicatorsData.from_json(json)
# print the JSON string representation of the object
print(EconDbEconomicIndicatorsData.to_json())

# convert the object into a dict
econ_db_economic_indicators_data_dict = econ_db_economic_indicators_data_instance.to_dict()
# create an instance of EconDbEconomicIndicatorsData from a dict
econ_db_economic_indicators_data_from_dict = EconDbEconomicIndicatorsData.from_dict(econ_db_economic_indicators_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


