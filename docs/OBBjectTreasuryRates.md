# OBBjectTreasuryRates

OBBject with results of type TreasuryRates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectTreasuryRatesResultsInner]**](OBBjectTreasuryRatesResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_treasury_rates import OBBjectTreasuryRates

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectTreasuryRates from a JSON string
ob_bject_treasury_rates_instance = OBBjectTreasuryRates.from_json(json)
# print the JSON string representation of the object
print(OBBjectTreasuryRates.to_json())

# convert the object into a dict
ob_bject_treasury_rates_dict = ob_bject_treasury_rates_instance.to_dict()
# create an instance of OBBjectTreasuryRates from a dict
ob_bject_treasury_rates_from_dict = OBBjectTreasuryRates.from_dict(ob_bject_treasury_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


