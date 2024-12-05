# ImfDirectionOfTradeData

IMF Direction Of Trade Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | 
**counterpart** | **str** | Counterpart country or region to the trade. | 
**title** | **str** |  | [optional] 
**value** | **float** | Trade value. | 
**scale** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.imf_direction_of_trade_data import ImfDirectionOfTradeData

# TODO update the JSON string below
json = "{}"
# create an instance of ImfDirectionOfTradeData from a JSON string
imf_direction_of_trade_data_instance = ImfDirectionOfTradeData.from_json(json)
# print the JSON string representation of the object
print(ImfDirectionOfTradeData.to_json())

# convert the object into a dict
imf_direction_of_trade_data_dict = imf_direction_of_trade_data_instance.to_dict()
# create an instance of ImfDirectionOfTradeData from a dict
imf_direction_of_trade_data_from_dict = ImfDirectionOfTradeData.from_dict(imf_direction_of_trade_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


