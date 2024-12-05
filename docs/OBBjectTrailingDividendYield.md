# OBBjectTrailingDividendYield

OBBject with results of type TrailingDividendYield

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[TiingoTrailingDivYieldData]**](TiingoTrailingDivYieldData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_trailing_dividend_yield import OBBjectTrailingDividendYield

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectTrailingDividendYield from a JSON string
ob_bject_trailing_dividend_yield_instance = OBBjectTrailingDividendYield.from_json(json)
# print the JSON string representation of the object
print(OBBjectTrailingDividendYield.to_json())

# convert the object into a dict
ob_bject_trailing_dividend_yield_dict = ob_bject_trailing_dividend_yield_instance.to_dict()
# create an instance of OBBjectTrailingDividendYield from a dict
ob_bject_trailing_dividend_yield_from_dict = OBBjectTrailingDividendYield.from_dict(ob_bject_trailing_dividend_yield_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


