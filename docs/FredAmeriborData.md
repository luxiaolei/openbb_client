# FredAmeriborData

FRED AMERIBOR Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**maturity** | **str** | Maturity length of the item. | 
**rate** | **float** | Interest rate. | 
**title** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fred_ameribor_data import FredAmeriborData

# TODO update the JSON string below
json = "{}"
# create an instance of FredAmeriborData from a JSON string
fred_ameribor_data_instance = FredAmeriborData.from_json(json)
# print the JSON string representation of the object
print(FredAmeriborData.to_json())

# convert the object into a dict
fred_ameribor_data_dict = fred_ameribor_data_instance.to_dict()
# create an instance of FredAmeriborData from a dict
fred_ameribor_data_from_dict = FredAmeriborData.from_dict(fred_ameribor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


