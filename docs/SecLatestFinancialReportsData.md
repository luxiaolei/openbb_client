# SecLatestFinancialReportsData

SEC Latest Financial Reports Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_date** | **date** | The date of the filing. | 
**period_ending** | **date** |  | [optional] 
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**cik** | **str** |  | [optional] 
**sic** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** | URL to the filing page. | 
**items** | **str** |  | [optional] 
**index_headers** | **str** | URL to the index headers file. | 
**complete_submission** | **str** | URL to the complete submission text file. | 
**metadata** | **str** |  | [optional] 
**financial_report** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.sec_latest_financial_reports_data import SecLatestFinancialReportsData

# TODO update the JSON string below
json = "{}"
# create an instance of SecLatestFinancialReportsData from a JSON string
sec_latest_financial_reports_data_instance = SecLatestFinancialReportsData.from_json(json)
# print the JSON string representation of the object
print(SecLatestFinancialReportsData.to_json())

# convert the object into a dict
sec_latest_financial_reports_data_dict = sec_latest_financial_reports_data_instance.to_dict()
# create an instance of SecLatestFinancialReportsData from a dict
sec_latest_financial_reports_data_from_dict = SecLatestFinancialReportsData.from_dict(sec_latest_financial_reports_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


