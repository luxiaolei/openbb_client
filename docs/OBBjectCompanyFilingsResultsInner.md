# OBBjectCompanyFilingsResultsInner


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
from openbb_client.models.ob_bject_company_filings_results_inner import OBBjectCompanyFilingsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCompanyFilingsResultsInner from a JSON string
ob_bject_company_filings_results_inner_instance = OBBjectCompanyFilingsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectCompanyFilingsResultsInner.to_json())

# convert the object into a dict
ob_bject_company_filings_results_inner_dict = ob_bject_company_filings_results_inner_instance.to_dict()
# create an instance of OBBjectCompanyFilingsResultsInner from a dict
ob_bject_company_filings_results_inner_from_dict = OBBjectCompanyFilingsResultsInner.from_dict(ob_bject_company_filings_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


