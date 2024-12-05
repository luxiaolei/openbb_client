# SecCompanyFilingsData

SEC Company Filings Data.

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
**report_date** | **date** |  | [optional] 
**act** | [**Act**](Act.md) |  | [optional] 
**items** | [**Items**](Items.md) |  | [optional] 
**primary_doc_description** | **str** |  | [optional] 
**primary_doc** | **str** |  | [optional] 
**accession_number** | [**AccessionNumber**](AccessionNumber.md) |  | [optional] 
**file_number** | [**FileNumber**](FileNumber.md) |  | [optional] 
**film_number** | [**FilmNumber**](FilmNumber.md) |  | [optional] 
**is_inline_xbrl** | [**IsInlineXbrl**](IsInlineXbrl.md) |  | [optional] 
**is_xbrl** | [**IsXbrl**](IsXbrl.md) |  | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 
**complete_submission_url** | **str** |  | [optional] 
**filing_detail_url** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.sec_company_filings_data import SecCompanyFilingsData

# TODO update the JSON string below
json = "{}"
# create an instance of SecCompanyFilingsData from a JSON string
sec_company_filings_data_instance = SecCompanyFilingsData.from_json(json)
# print the JSON string representation of the object
print(SecCompanyFilingsData.to_json())

# convert the object into a dict
sec_company_filings_data_dict = sec_company_filings_data_instance.to_dict()
# create an instance of SecCompanyFilingsData from a dict
sec_company_filings_data_from_dict = SecCompanyFilingsData.from_dict(sec_company_filings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


