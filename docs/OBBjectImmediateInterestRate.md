# OBBjectImmediateInterestRate

OBBject with results of type ImmediateInterestRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OECDImmediateInterestRateData]**](OECDImmediateInterestRateData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_immediate_interest_rate import OBBjectImmediateInterestRate

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectImmediateInterestRate from a JSON string
ob_bject_immediate_interest_rate_instance = OBBjectImmediateInterestRate.from_json(json)
# print the JSON string representation of the object
print(OBBjectImmediateInterestRate.to_json())

# convert the object into a dict
ob_bject_immediate_interest_rate_dict = ob_bject_immediate_interest_rate_instance.to_dict()
# create an instance of OBBjectImmediateInterestRate from a dict
ob_bject_immediate_interest_rate_from_dict = OBBjectImmediateInterestRate.from_dict(ob_bject_immediate_interest_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


