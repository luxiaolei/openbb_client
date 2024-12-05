# FREDSelectedTreasuryBillData

FRED Selected Treasury Bill Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fred_selected_treasury_bill_data import FREDSelectedTreasuryBillData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDSelectedTreasuryBillData from a JSON string
fred_selected_treasury_bill_data_instance = FREDSelectedTreasuryBillData.from_json(json)
# print the JSON string representation of the object
print(FREDSelectedTreasuryBillData.to_json())

# convert the object into a dict
fred_selected_treasury_bill_data_dict = fred_selected_treasury_bill_data_instance.to_dict()
# create an instance of FREDSelectedTreasuryBillData from a dict
fred_selected_treasury_bill_data_from_dict = FREDSelectedTreasuryBillData.from_dict(fred_selected_treasury_bill_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


