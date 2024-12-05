# FederalReserveCentralBankHoldingsData

Federal Reserve Central Bank Holdings Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**security_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_aggreated** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**maturity_date** | **date** |  | [optional] 
**term** | **str** |  | [optional] 
**face_value** | **float** |  | [optional] 
**par_value** | **float** |  | [optional] 
**coupon** | **float** |  | [optional] 
**spread** | **float** |  | [optional] 
**percent_outstanding** | **float** |  | [optional] 
**bills** | **float** |  | [optional] 
**frn** | **float** |  | [optional] 
**notes_and_bonds** | **float** |  | [optional] 
**tips** | **float** |  | [optional] 
**mbs** | **float** |  | [optional] 
**cmbs** | **float** |  | [optional] 
**agencies** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**inflation_compensation** | **float** |  | [optional] 
**change_prior_week** | **float** |  | [optional] 
**change_prior_year** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.federal_reserve_central_bank_holdings_data import FederalReserveCentralBankHoldingsData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReserveCentralBankHoldingsData from a JSON string
federal_reserve_central_bank_holdings_data_instance = FederalReserveCentralBankHoldingsData.from_json(json)
# print the JSON string representation of the object
print(FederalReserveCentralBankHoldingsData.to_json())

# convert the object into a dict
federal_reserve_central_bank_holdings_data_dict = federal_reserve_central_bank_holdings_data_instance.to_dict()
# create an instance of FederalReserveCentralBankHoldingsData from a dict
federal_reserve_central_bank_holdings_data_from_dict = FederalReserveCentralBankHoldingsData.from_dict(federal_reserve_central_bank_holdings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


