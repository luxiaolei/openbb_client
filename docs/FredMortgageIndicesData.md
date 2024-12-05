# FredMortgageIndicesData

FRED Mortgage Indices Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rate** | **float** | Mortgage rate. | 

## Example

```python
from openbb_client.models.fred_mortgage_indices_data import FredMortgageIndicesData

# TODO update the JSON string below
json = "{}"
# create an instance of FredMortgageIndicesData from a JSON string
fred_mortgage_indices_data_instance = FredMortgageIndicesData.from_json(json)
# print the JSON string representation of the object
print(FredMortgageIndicesData.to_json())

# convert the object into a dict
fred_mortgage_indices_data_dict = fred_mortgage_indices_data_instance.to_dict()
# create an instance of FredMortgageIndicesData from a dict
fred_mortgage_indices_data_from_dict = FredMortgageIndicesData.from_dict(fred_mortgage_indices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


