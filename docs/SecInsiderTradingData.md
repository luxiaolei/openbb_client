# SecInsiderTradingData

SEC Insider Trading Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**company_cik** | [**CompanyCik**](CompanyCik.md) |  | [optional] 
**filing_date** | [**FilingDate**](FilingDate.md) |  | [optional] 
**transaction_date** | **date** |  | [optional] 
**owner_cik** | [**OwnerCik**](OwnerCik.md) |  | [optional] 
**owner_name** | **str** |  | [optional] 
**owner_title** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**acquisition_or_disposition** | **str** |  | [optional] 
**security_type** | **str** |  | [optional] 
**securities_owned** | **float** |  | [optional] 
**securities_transacted** | **float** |  | [optional] 
**transaction_price** | **float** |  | [optional] 
**filing_url** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**form** | [**Form**](Form.md) |  | [optional] 
**director** | **bool** |  | [optional] 
**officer** | **bool** |  | [optional] 
**ten_percent_owner** | **bool** |  | [optional] 
**other** | **bool** |  | [optional] 
**other_text** | **str** |  | [optional] 
**transaction_timeliness** | **str** |  | [optional] 
**ownership_type** | **str** |  | [optional] 
**nature_of_ownership** | **str** |  | [optional] 
**exercise_date** | **date** |  | [optional] 
**expiration_date** | **date** |  | [optional] 
**deemed_execution_date** | **date** |  | [optional] 
**underlying_security_title** | **str** |  | [optional] 
**underlying_security_shares** | **float** |  | [optional] 
**underlying_security_value** | **float** |  | [optional] 
**conversion_exercise_price** | **float** |  | [optional] 
**transaction_value** | **float** |  | [optional] 
**value_owned** | **float** |  | [optional] 
**footnote** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.sec_insider_trading_data import SecInsiderTradingData

# TODO update the JSON string below
json = "{}"
# create an instance of SecInsiderTradingData from a JSON string
sec_insider_trading_data_instance = SecInsiderTradingData.from_json(json)
# print the JSON string representation of the object
print(SecInsiderTradingData.to_json())

# convert the object into a dict
sec_insider_trading_data_dict = sec_insider_trading_data_instance.to_dict()
# create an instance of SecInsiderTradingData from a dict
sec_insider_trading_data_from_dict = SecInsiderTradingData.from_dict(sec_insider_trading_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


