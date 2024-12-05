# FMPRiskPremiumData

FMP Risk Premium Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Market country. | 
**continent** | **str** |  | [optional] 
**total_equity_risk_premium** | **float** |  | [optional] 
**country_risk_premium** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_risk_premium_data import FMPRiskPremiumData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPRiskPremiumData from a JSON string
fmp_risk_premium_data_instance = FMPRiskPremiumData.from_json(json)
# print the JSON string representation of the object
print(FMPRiskPremiumData.to_json())

# convert the object into a dict
fmp_risk_premium_data_dict = fmp_risk_premium_data_instance.to_dict()
# create an instance of FMPRiskPremiumData from a dict
fmp_risk_premium_data_from_dict = FMPRiskPremiumData.from_dict(fmp_risk_premium_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


