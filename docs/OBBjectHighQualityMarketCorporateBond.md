# OBBjectHighQualityMarketCorporateBond

OBBject with results of type HighQualityMarketCorporateBond

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredHighQualityMarketCorporateBondData]**](FredHighQualityMarketCorporateBondData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_high_quality_market_corporate_bond import OBBjectHighQualityMarketCorporateBond

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectHighQualityMarketCorporateBond from a JSON string
ob_bject_high_quality_market_corporate_bond_instance = OBBjectHighQualityMarketCorporateBond.from_json(json)
# print the JSON string representation of the object
print(OBBjectHighQualityMarketCorporateBond.to_json())

# convert the object into a dict
ob_bject_high_quality_market_corporate_bond_dict = ob_bject_high_quality_market_corporate_bond_instance.to_dict()
# create an instance of OBBjectHighQualityMarketCorporateBond from a dict
ob_bject_high_quality_market_corporate_bond_from_dict = OBBjectHighQualityMarketCorporateBond.from_dict(ob_bject_high_quality_market_corporate_bond_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


