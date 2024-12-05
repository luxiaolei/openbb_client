# OBBjectCompanyFilings

OBBject with results of type CompanyFilings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectCompanyFilingsResultsInner]**](OBBjectCompanyFilingsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_company_filings import OBBjectCompanyFilings

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCompanyFilings from a JSON string
ob_bject_company_filings_instance = OBBjectCompanyFilings.from_json(json)
# print the JSON string representation of the object
print(OBBjectCompanyFilings.to_json())

# convert the object into a dict
ob_bject_company_filings_dict = ob_bject_company_filings_instance.to_dict()
# create an instance of OBBjectCompanyFilings from a dict
ob_bject_company_filings_from_dict = OBBjectCompanyFilings.from_dict(ob_bject_company_filings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


