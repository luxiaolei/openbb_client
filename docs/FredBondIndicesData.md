# FredBondIndicesData

FRED Bond Indices Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**value** | **float** | Index values. | 
**maturity** | **str** |  | [optional] 
**title** | **str** | The title of the index. | 

## Example

```python
from openbb_client.models.fred_bond_indices_data import FredBondIndicesData

# TODO update the JSON string below
json = "{}"
# create an instance of FredBondIndicesData from a JSON string
fred_bond_indices_data_instance = FredBondIndicesData.from_json(json)
# print the JSON string representation of the object
print(FredBondIndicesData.to_json())

# convert the object into a dict
fred_bond_indices_data_dict = fred_bond_indices_data_instance.to_dict()
# create an instance of FredBondIndicesData from a dict
fred_bond_indices_data_from_dict = FredBondIndicesData.from_dict(fred_bond_indices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


