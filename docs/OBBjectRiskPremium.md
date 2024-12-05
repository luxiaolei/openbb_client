# OBBjectRiskPremium

OBBject with results of type RiskPremium

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPRiskPremiumData]**](FMPRiskPremiumData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_risk_premium import OBBjectRiskPremium

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectRiskPremium from a JSON string
ob_bject_risk_premium_instance = OBBjectRiskPremium.from_json(json)
# print the JSON string representation of the object
print(OBBjectRiskPremium.to_json())

# convert the object into a dict
ob_bject_risk_premium_dict = ob_bject_risk_premium_instance.to_dict()
# create an instance of OBBjectRiskPremium from a dict
ob_bject_risk_premium_from_dict = OBBjectRiskPremium.from_dict(ob_bject_risk_premium_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


