# OBBjectCentralBankHoldings

OBBject with results of type CentralBankHoldings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FederalReserveCentralBankHoldingsData]**](FederalReserveCentralBankHoldingsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_central_bank_holdings import OBBjectCentralBankHoldings

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCentralBankHoldings from a JSON string
ob_bject_central_bank_holdings_instance = OBBjectCentralBankHoldings.from_json(json)
# print the JSON string representation of the object
print(OBBjectCentralBankHoldings.to_json())

# convert the object into a dict
ob_bject_central_bank_holdings_dict = ob_bject_central_bank_holdings_instance.to_dict()
# create an instance of OBBjectCentralBankHoldings from a dict
ob_bject_central_bank_holdings_from_dict = OBBjectCentralBankHoldings.from_dict(ob_bject_central_bank_holdings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


