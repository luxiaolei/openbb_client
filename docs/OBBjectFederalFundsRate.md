# OBBjectFederalFundsRate

OBBject with results of type FederalFundsRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectFederalFundsRateResultsInner]**](OBBjectFederalFundsRateResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_federal_funds_rate import OBBjectFederalFundsRate

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectFederalFundsRate from a JSON string
ob_bject_federal_funds_rate_instance = OBBjectFederalFundsRate.from_json(json)
# print the JSON string representation of the object
print(OBBjectFederalFundsRate.to_json())

# convert the object into a dict
ob_bject_federal_funds_rate_dict = ob_bject_federal_funds_rate_instance.to_dict()
# create an instance of OBBjectFederalFundsRate from a dict
ob_bject_federal_funds_rate_from_dict = OBBjectFederalFundsRate.from_dict(ob_bject_federal_funds_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


