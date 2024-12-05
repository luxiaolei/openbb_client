# IntrinioEtfHoldingsData

Intrinio ETF Holdings Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**security_type** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**ric** | **str** |  | [optional] 
**sedol** | **str** |  | [optional] 
**share_class_figi** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**maturity_date** | **date** |  | [optional] 
**contract_expiry_date** | **date** |  | [optional] 
**coupon** | **float** |  | [optional] 
**balance** | [**Balance**](Balance.md) |  | [optional] 
**unit** | **str** |  | [optional] 
**units_per_share** | **float** |  | [optional] 
**face_value** | **float** |  | [optional] 
**derivatives_value** | **float** |  | [optional] 
**value** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**updated** | **date** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_etf_holdings_data import IntrinioEtfHoldingsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioEtfHoldingsData from a JSON string
intrinio_etf_holdings_data_instance = IntrinioEtfHoldingsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioEtfHoldingsData.to_json())

# convert the object into a dict
intrinio_etf_holdings_data_dict = intrinio_etf_holdings_data_instance.to_dict()
# create an instance of IntrinioEtfHoldingsData from a dict
intrinio_etf_holdings_data_from_dict = IntrinioEtfHoldingsData.from_dict(intrinio_etf_holdings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


