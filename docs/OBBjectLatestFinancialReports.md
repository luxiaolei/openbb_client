# OBBjectLatestFinancialReports

OBBject with results of type LatestFinancialReports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[SecLatestFinancialReportsData]**](SecLatestFinancialReportsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_latest_financial_reports import OBBjectLatestFinancialReports

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectLatestFinancialReports from a JSON string
ob_bject_latest_financial_reports_instance = OBBjectLatestFinancialReports.from_json(json)
# print the JSON string representation of the object
print(OBBjectLatestFinancialReports.to_json())

# convert the object into a dict
ob_bject_latest_financial_reports_dict = ob_bject_latest_financial_reports_instance.to_dict()
# create an instance of OBBjectLatestFinancialReports from a dict
ob_bject_latest_financial_reports_from_dict = OBBjectLatestFinancialReports.from_dict(ob_bject_latest_financial_reports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


