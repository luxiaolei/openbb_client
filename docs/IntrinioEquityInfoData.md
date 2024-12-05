# IntrinioEquityInfoData

Intrinio Equity Info Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**cik** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**lei** | **str** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**stock_exchange** | **str** |  | [optional] 
**sic** | **int** |  | [optional] 
**short_description** | **str** |  | [optional] 
**long_description** | **str** |  | [optional] 
**ceo** | **str** |  | [optional] 
**company_url** | **str** |  | [optional] 
**business_address** | **str** |  | [optional] 
**mailing_address** | **str** |  | [optional] 
**business_phone_no** | **str** |  | [optional] 
**hq_address_1** | **str** |  | [optional] 
**hq_address_2** | **str** |  | [optional] 
**hq_address_city** | **str** |  | [optional] 
**hq_address_postal_code** | **str** |  | [optional] 
**hq_state** | **str** |  | [optional] 
**hq_country** | **str** |  | [optional] 
**inc_state** | **str** |  | [optional] 
**inc_country** | **str** |  | [optional] 
**employees** | **int** |  | [optional] 
**entity_legal_form** | **str** |  | [optional] 
**entity_status** | **str** |  | [optional] 
**latest_filing_date** | **date** |  | [optional] 
**irs_number** | **str** |  | [optional] 
**sector** | **str** |  | [optional] 
**industry_category** | **str** |  | [optional] 
**industry_group** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**standardized_active** | **bool** |  | [optional] 
**first_fundamental_date** | **date** |  | [optional] 
**last_fundamental_date** | **date** |  | [optional] 
**first_stock_price_date** | **date** |  | [optional] 
**last_stock_price_date** | **date** |  | [optional] 
**id** | **str** | Intrinio ID for the company. | [optional] 
**thea_enabled** | **bool** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_equity_info_data import IntrinioEquityInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioEquityInfoData from a JSON string
intrinio_equity_info_data_instance = IntrinioEquityInfoData.from_json(json)
# print the JSON string representation of the object
print(IntrinioEquityInfoData.to_json())

# convert the object into a dict
intrinio_equity_info_data_dict = intrinio_equity_info_data_instance.to_dict()
# create an instance of IntrinioEquityInfoData from a dict
intrinio_equity_info_data_from_dict = IntrinioEquityInfoData.from_dict(intrinio_equity_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


