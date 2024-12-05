# FREDMoodyCorporateBondIndexData

FRED Moody Corporate Bond Index Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fred_moody_corporate_bond_index_data import FREDMoodyCorporateBondIndexData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDMoodyCorporateBondIndexData from a JSON string
fred_moody_corporate_bond_index_data_instance = FREDMoodyCorporateBondIndexData.from_json(json)
# print the JSON string representation of the object
print(FREDMoodyCorporateBondIndexData.to_json())

# convert the object into a dict
fred_moody_corporate_bond_index_data_dict = fred_moody_corporate_bond_index_data_instance.to_dict()
# create an instance of FREDMoodyCorporateBondIndexData from a dict
fred_moody_corporate_bond_index_data_from_dict = FREDMoodyCorporateBondIndexData.from_dict(fred_moody_corporate_bond_index_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


