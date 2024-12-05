# EiaPetroleumStatusReportData

EIA Petroleum Status Report Data Model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**table** | **str** |  | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**order** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**value** | [**Value4**](Value4.md) |  | 
**unit** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.eia_petroleum_status_report_data import EiaPetroleumStatusReportData

# TODO update the JSON string below
json = "{}"
# create an instance of EiaPetroleumStatusReportData from a JSON string
eia_petroleum_status_report_data_instance = EiaPetroleumStatusReportData.from_json(json)
# print the JSON string representation of the object
print(EiaPetroleumStatusReportData.to_json())

# convert the object into a dict
eia_petroleum_status_report_data_dict = eia_petroleum_status_report_data_instance.to_dict()
# create an instance of EiaPetroleumStatusReportData from a dict
eia_petroleum_status_report_data_from_dict = EiaPetroleumStatusReportData.from_dict(eia_petroleum_status_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


