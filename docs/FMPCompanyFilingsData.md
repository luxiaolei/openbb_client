# FMPCompanyFilingsData

FMP Company Filings Data.

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

## Example

```python
from openbb_client.models.fmp_company_filings_data import FMPCompanyFilingsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCompanyFilingsData from a JSON string
fmp_company_filings_data_instance = FMPCompanyFilingsData.from_json(json)
# print the JSON string representation of the object
print(FMPCompanyFilingsData.to_json())

# convert the object into a dict
fmp_company_filings_data_dict = fmp_company_filings_data_instance.to_dict()
# create an instance of FMPCompanyFilingsData from a dict
fmp_company_filings_data_from_dict = FMPCompanyFilingsData.from_dict(fmp_company_filings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


