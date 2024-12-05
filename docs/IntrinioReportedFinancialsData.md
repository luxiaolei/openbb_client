# IntrinioReportedFinancialsData

Intrinio Reported Financials Data.  The fields for this model are generated dynamically from the XBRL tags in the Intrinio response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The ending date of the reporting period. | 
**fiscal_period** | **str** | The fiscal period of the report (e.g. FY, Q1, etc.). | 
**fiscal_year** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_reported_financials_data import IntrinioReportedFinancialsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioReportedFinancialsData from a JSON string
intrinio_reported_financials_data_instance = IntrinioReportedFinancialsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioReportedFinancialsData.to_json())

# convert the object into a dict
intrinio_reported_financials_data_dict = intrinio_reported_financials_data_instance.to_dict()
# create an instance of IntrinioReportedFinancialsData from a dict
intrinio_reported_financials_data_from_dict = IntrinioReportedFinancialsData.from_dict(intrinio_reported_financials_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


