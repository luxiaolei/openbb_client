# FMPHistoricalEmployeesData

FMP Historical Employees Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**cik** | **int** | Central Index Key (CIK) for the requested entity. | 
**acceptance_time** | **datetime** | Time of acceptance of the company employee. | 
**period_of_report** | **date** | Date of reporting of the company employee. | 
**company_name** | **str** | Registered name of the company to retrieve the historical employees of. | 
**form_type** | **str** | Form type of the company employee. | 
**filing_date** | **date** | Filing date of the company employee | 
**employee_count** | **int** | Count of employees of the company. | 
**source** | **str** | Source URL which retrieves this data for the company. | 

## Example

```python
from openbb_client.models.fmp_historical_employees_data import FMPHistoricalEmployeesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPHistoricalEmployeesData from a JSON string
fmp_historical_employees_data_instance = FMPHistoricalEmployeesData.from_json(json)
# print the JSON string representation of the object
print(FMPHistoricalEmployeesData.to_json())

# convert the object into a dict
fmp_historical_employees_data_dict = fmp_historical_employees_data_instance.to_dict()
# create an instance of FMPHistoricalEmployeesData from a dict
fmp_historical_employees_data_from_dict = FMPHistoricalEmployeesData.from_dict(fmp_historical_employees_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


