# OBBjectOvernightBankFundingRate

OBBject with results of type OvernightBankFundingRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectOvernightBankFundingRateResultsInner]**](OBBjectOvernightBankFundingRateResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_overnight_bank_funding_rate import OBBjectOvernightBankFundingRate

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectOvernightBankFundingRate from a JSON string
ob_bject_overnight_bank_funding_rate_instance = OBBjectOvernightBankFundingRate.from_json(json)
# print the JSON string representation of the object
print(OBBjectOvernightBankFundingRate.to_json())

# convert the object into a dict
ob_bject_overnight_bank_funding_rate_dict = ob_bject_overnight_bank_funding_rate_instance.to_dict()
# create an instance of OBBjectOvernightBankFundingRate from a dict
ob_bject_overnight_bank_funding_rate_from_dict = OBBjectOvernightBankFundingRate.from_dict(ob_bject_overnight_bank_funding_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


