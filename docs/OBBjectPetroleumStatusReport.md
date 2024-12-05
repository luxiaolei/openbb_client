# OBBjectPetroleumStatusReport

OBBject with results of type PetroleumStatusReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[EiaPetroleumStatusReportData]**](EiaPetroleumStatusReportData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_petroleum_status_report import OBBjectPetroleumStatusReport

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPetroleumStatusReport from a JSON string
ob_bject_petroleum_status_report_instance = OBBjectPetroleumStatusReport.from_json(json)
# print the JSON string representation of the object
print(OBBjectPetroleumStatusReport.to_json())

# convert the object into a dict
ob_bject_petroleum_status_report_dict = ob_bject_petroleum_status_report_instance.to_dict()
# create an instance of OBBjectPetroleumStatusReport from a dict
ob_bject_petroleum_status_report_from_dict = OBBjectPetroleumStatusReport.from_dict(ob_bject_petroleum_status_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


