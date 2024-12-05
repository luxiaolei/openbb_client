# FREDSelectedTreasuryConstantMaturityData

FRED Selected Treasury Constant Maturity Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fred_selected_treasury_constant_maturity_data import FREDSelectedTreasuryConstantMaturityData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDSelectedTreasuryConstantMaturityData from a JSON string
fred_selected_treasury_constant_maturity_data_instance = FREDSelectedTreasuryConstantMaturityData.from_json(json)
# print the JSON string representation of the object
print(FREDSelectedTreasuryConstantMaturityData.to_json())

# convert the object into a dict
fred_selected_treasury_constant_maturity_data_dict = fred_selected_treasury_constant_maturity_data_instance.to_dict()
# create an instance of FREDSelectedTreasuryConstantMaturityData from a dict
fred_selected_treasury_constant_maturity_data_from_dict = FREDSelectedTreasuryConstantMaturityData.from_dict(fred_selected_treasury_constant_maturity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


