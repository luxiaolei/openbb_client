# FredTipsYieldsData

FRED TIPS Yields Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**due** | **date** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **float** | The yield value. | [optional] 

## Example

```python
from openbb_client.models.fred_tips_yields_data import FredTipsYieldsData

# TODO update the JSON string below
json = "{}"
# create an instance of FredTipsYieldsData from a JSON string
fred_tips_yields_data_instance = FredTipsYieldsData.from_json(json)
# print the JSON string representation of the object
print(FredTipsYieldsData.to_json())

# convert the object into a dict
fred_tips_yields_data_dict = fred_tips_yields_data_instance.to_dict()
# create an instance of FredTipsYieldsData from a dict
fred_tips_yields_data_from_dict = FredTipsYieldsData.from_dict(fred_tips_yields_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


