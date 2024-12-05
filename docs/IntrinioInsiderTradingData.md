# IntrinioInsiderTradingData

Intrinio Insider Trading Data.

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
**company_name** | **str** | Name of the company. | 
**conversion_exercise_price** | **float** |  | [optional] 
**deemed_execution_date** | **date** |  | [optional] 
**exercise_date** | **date** |  | [optional] 
**expiration_date** | **date** |  | [optional] 
**underlying_security_title** | **str** |  | [optional] 
**underlying_shares** | [**UnderlyingShares**](UnderlyingShares.md) |  | [optional] 
**nature_of_ownership** | **str** |  | [optional] 
**director** | **bool** |  | [optional] 
**officer** | **bool** |  | [optional] 
**ten_percent_owner** | **bool** |  | [optional] 
**other_relation** | **bool** |  | [optional] 
**derivative_transaction** | **bool** |  | [optional] 
**report_line_number** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_insider_trading_data import IntrinioInsiderTradingData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioInsiderTradingData from a JSON string
intrinio_insider_trading_data_instance = IntrinioInsiderTradingData.from_json(json)
# print the JSON string representation of the object
print(IntrinioInsiderTradingData.to_json())

# convert the object into a dict
intrinio_insider_trading_data_dict = intrinio_insider_trading_data_instance.to_dict()
# create an instance of IntrinioInsiderTradingData from a dict
intrinio_insider_trading_data_from_dict = IntrinioInsiderTradingData.from_dict(intrinio_insider_trading_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


