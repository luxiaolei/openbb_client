# OBBjectCommercialPaper

OBBject with results of type CommercialPaper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDCommercialPaperData]**](FREDCommercialPaperData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_commercial_paper import OBBjectCommercialPaper

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCommercialPaper from a JSON string
ob_bject_commercial_paper_instance = OBBjectCommercialPaper.from_json(json)
# print the JSON string representation of the object
print(OBBjectCommercialPaper.to_json())

# convert the object into a dict
ob_bject_commercial_paper_dict = ob_bject_commercial_paper_instance.to_dict()
# create an instance of OBBjectCommercialPaper from a dict
ob_bject_commercial_paper_from_dict = OBBjectCommercialPaper.from_dict(ob_bject_commercial_paper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


