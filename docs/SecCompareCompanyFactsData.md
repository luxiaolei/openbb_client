# SecCompareCompanyFactsData

SEC Compare Company Facts Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **float** | The reported value of the fact or concept. | 
**reported_date** | **date** |  | [optional] 
**period_beginning** | **date** |  | [optional] 
**period_ending** | **date** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**fiscal_period** | **str** |  | [optional] 
**cik** | [**Cik1**](Cik1.md) |  | 
**location** | **str** |  | [optional] 
**form** | **str** |  | [optional] 
**frame** | **str** |  | [optional] 
**accession** | **str** | SEC filing accession number associated with the reported fact or concept. | 
**fact** | **str** | The display name of the fact or concept. | 
**unit** | **str** | The unit of measurement for the fact or concept. | [optional] 

## Example

```python
from openbb_client.models.sec_compare_company_facts_data import SecCompareCompanyFactsData

# TODO update the JSON string below
json = "{}"
# create an instance of SecCompareCompanyFactsData from a JSON string
sec_compare_company_facts_data_instance = SecCompareCompanyFactsData.from_json(json)
# print the JSON string representation of the object
print(SecCompareCompanyFactsData.to_json())

# convert the object into a dict
sec_compare_company_facts_data_dict = sec_compare_company_facts_data_instance.to_dict()
# create an instance of SecCompareCompanyFactsData from a dict
sec_compare_company_facts_data_from_dict = SecCompareCompanyFactsData.from_dict(sec_compare_company_facts_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


