# OBBjectCompareCompanyFacts

OBBject with results of type CompareCompanyFacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[SecCompareCompanyFactsData]**](SecCompareCompanyFactsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_compare_company_facts import OBBjectCompareCompanyFacts

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCompareCompanyFacts from a JSON string
ob_bject_compare_company_facts_instance = OBBjectCompareCompanyFacts.from_json(json)
# print the JSON string representation of the object
print(OBBjectCompareCompanyFacts.to_json())

# convert the object into a dict
ob_bject_compare_company_facts_dict = ob_bject_compare_company_facts_instance.to_dict()
# create an instance of OBBjectCompareCompanyFacts from a dict
ob_bject_compare_company_facts_from_dict = OBBjectCompareCompanyFacts.from_dict(ob_bject_compare_company_facts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


