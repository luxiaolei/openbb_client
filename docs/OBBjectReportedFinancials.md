# OBBjectReportedFinancials

OBBject with results of type ReportedFinancials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[IntrinioReportedFinancialsData]**](IntrinioReportedFinancialsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_reported_financials import OBBjectReportedFinancials

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectReportedFinancials from a JSON string
ob_bject_reported_financials_instance = OBBjectReportedFinancials.from_json(json)
# print the JSON string representation of the object
print(OBBjectReportedFinancials.to_json())

# convert the object into a dict
ob_bject_reported_financials_dict = ob_bject_reported_financials_instance.to_dict()
# create an instance of OBBjectReportedFinancials from a dict
ob_bject_reported_financials_from_dict = OBBjectReportedFinancials.from_dict(ob_bject_reported_financials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


