# FredNonFarmPayrollsData

FRED NonFarm Payrolls Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**value** | **float** |  | 
**name** | **str** | The name of the series. | 
**element_id** | **str** | The element id in the parent/child relationship. | 
**parent_id** | **str** | The parent id in the parent/child relationship. | 
**children** | **str** |  | [optional] 
**level** | **int** | The indentation level of the element. | 

## Example

```python
from openbb_client.models.fred_non_farm_payrolls_data import FredNonFarmPayrollsData

# TODO update the JSON string below
json = "{}"
# create an instance of FredNonFarmPayrollsData from a JSON string
fred_non_farm_payrolls_data_instance = FredNonFarmPayrollsData.from_json(json)
# print the JSON string representation of the object
print(FredNonFarmPayrollsData.to_json())

# convert the object into a dict
fred_non_farm_payrolls_data_dict = fred_non_farm_payrolls_data_instance.to_dict()
# create an instance of FredNonFarmPayrollsData from a dict
fred_non_farm_payrolls_data_from_dict = FredNonFarmPayrollsData.from_dict(fred_non_farm_payrolls_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


