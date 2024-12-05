# FREDTreasuryConstantMaturityData

FRED Treasury Constant Maturity Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fred_treasury_constant_maturity_data import FREDTreasuryConstantMaturityData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDTreasuryConstantMaturityData from a JSON string
fred_treasury_constant_maturity_data_instance = FREDTreasuryConstantMaturityData.from_json(json)
# print the JSON string representation of the object
print(FREDTreasuryConstantMaturityData.to_json())

# convert the object into a dict
fred_treasury_constant_maturity_data_dict = fred_treasury_constant_maturity_data_instance.to_dict()
# create an instance of FREDTreasuryConstantMaturityData from a dict
fred_treasury_constant_maturity_data_from_dict = FREDTreasuryConstantMaturityData.from_dict(fred_treasury_constant_maturity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


