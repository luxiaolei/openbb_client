# SecSymbolMapData

SEC symbol map Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 

## Example

```python
from openbb_client.models.sec_symbol_map_data import SecSymbolMapData

# TODO update the JSON string below
json = "{}"
# create an instance of SecSymbolMapData from a JSON string
sec_symbol_map_data_instance = SecSymbolMapData.from_json(json)
# print the JSON string representation of the object
print(SecSymbolMapData.to_json())

# convert the object into a dict
sec_symbol_map_data_dict = sec_symbol_map_data_instance.to_dict()
# create an instance of SecSymbolMapData from a dict
sec_symbol_map_data_from_dict = SecSymbolMapData.from_dict(sec_symbol_map_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


