# OBBjectEtfEquityExposure

OBBject with results of type EtfEquityExposure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPEtfEquityExposureData]**](FMPEtfEquityExposureData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_equity_exposure import OBBjectEtfEquityExposure

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfEquityExposure from a JSON string
ob_bject_etf_equity_exposure_instance = OBBjectEtfEquityExposure.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfEquityExposure.to_json())

# convert the object into a dict
ob_bject_etf_equity_exposure_dict = ob_bject_etf_equity_exposure_instance.to_dict()
# create an instance of OBBjectEtfEquityExposure from a dict
ob_bject_etf_equity_exposure_from_dict = OBBjectEtfEquityExposure.from_dict(ob_bject_etf_equity_exposure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


