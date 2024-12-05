# OBBjectBalanceOfPayments

OBBject with results of type BalanceOfPayments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredBalanceOfPaymentsData]**](FredBalanceOfPaymentsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_balance_of_payments import OBBjectBalanceOfPayments

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectBalanceOfPayments from a JSON string
ob_bject_balance_of_payments_instance = OBBjectBalanceOfPayments.from_json(json)
# print the JSON string representation of the object
print(OBBjectBalanceOfPayments.to_json())

# convert the object into a dict
ob_bject_balance_of_payments_dict = ob_bject_balance_of_payments_instance.to_dict()
# create an instance of OBBjectBalanceOfPayments from a dict
ob_bject_balance_of_payments_from_dict = OBBjectBalanceOfPayments.from_dict(ob_bject_balance_of_payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


