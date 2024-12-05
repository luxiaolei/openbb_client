# IntrinioCompanyFilingsData

Intrinio Company Filings Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filing_date** | **date** | The date of the filing. | 
**accepted_date** | **datetime** |  | [optional] 
**symbol** | **str** |  | [optional] 
**cik** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**filing_url** | **str** |  | [optional] 
**report_url** | **str** | URL to the actual report. | 
**id** | **str** | Intrinio ID of the filing. | 
**period_end_date** | **date** |  | [optional] 
**sec_unique_id** | **str** | SEC unique ID of the filing. | 
**instance_url** | **str** |  | [optional] 
**industry_group** | **str** | Industry group of the company. | 
**industry_category** | **str** | Industry category of the company. | 

## Example

```python
from openbb_client.models.intrinio_company_filings_data import IntrinioCompanyFilingsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioCompanyFilingsData from a JSON string
intrinio_company_filings_data_instance = IntrinioCompanyFilingsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioCompanyFilingsData.to_json())

# convert the object into a dict
intrinio_company_filings_data_dict = intrinio_company_filings_data_instance.to_dict()
# create an instance of IntrinioCompanyFilingsData from a dict
intrinio_company_filings_data_from_dict = IntrinioCompanyFilingsData.from_dict(intrinio_company_filings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


