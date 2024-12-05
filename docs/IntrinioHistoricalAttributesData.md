# IntrinioHistoricalAttributesData

Intrinio Historical Attributes Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**tag** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_historical_attributes_data import IntrinioHistoricalAttributesData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioHistoricalAttributesData from a JSON string
intrinio_historical_attributes_data_instance = IntrinioHistoricalAttributesData.from_json(json)
# print the JSON string representation of the object
print(IntrinioHistoricalAttributesData.to_json())

# convert the object into a dict
intrinio_historical_attributes_data_dict = intrinio_historical_attributes_data_instance.to_dict()
# create an instance of IntrinioHistoricalAttributesData from a dict
intrinio_historical_attributes_data_from_dict = IntrinioHistoricalAttributesData.from_dict(intrinio_historical_attributes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


