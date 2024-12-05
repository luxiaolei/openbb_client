# FredUofMichiganData

FRED University of Michigan Survey Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**consumer_sentiment** | **float** |  | [optional] 
**inflation_expectation** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_uof_michigan_data import FredUofMichiganData

# TODO update the JSON string below
json = "{}"
# create an instance of FredUofMichiganData from a JSON string
fred_uof_michigan_data_instance = FredUofMichiganData.from_json(json)
# print the JSON string representation of the object
print(FredUofMichiganData.to_json())

# convert the object into a dict
fred_uof_michigan_data_dict = fred_uof_michigan_data_instance.to_dict()
# create an instance of FredUofMichiganData from a dict
fred_uof_michigan_data_from_dict = FredUofMichiganData.from_dict(fred_uof_michigan_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


