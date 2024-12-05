# IntrinioEquityQuoteData

Intrinio Equity Quote Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**asset_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**bid** | **float** |  | [optional] 
**bid_size** | **int** |  | [optional] 
**bid_exchange** | **str** |  | [optional] 
**ask** | **float** |  | [optional] 
**ask_size** | **int** |  | [optional] 
**ask_exchange** | **str** |  | [optional] 
**quote_conditions** | [**QuoteConditions**](QuoteConditions.md) |  | [optional] 
**quote_indicators** | [**QuoteIndicators**](QuoteIndicators.md) |  | [optional] 
**sales_conditions** | [**SalesConditions**](SalesConditions.md) |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**market_center** | **str** |  | [optional] 
**participant_timestamp** | **datetime** |  | [optional] 
**trf_timestamp** | **datetime** |  | [optional] 
**sip_timestamp** | **datetime** |  | [optional] 
**last_price** | **float** |  | [optional] 
**last_tick** | **str** |  | [optional] 
**last_size** | **int** |  | [optional] 
**last_timestamp** | **datetime** |  | [optional] 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | [**Volume**](Volume.md) |  | [optional] 
**exchange_volume** | [**ExchangeVolume**](ExchangeVolume.md) |  | [optional] 
**prev_close** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**is_darkpool** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**updated_on** | **datetime** | Date and Time when the data was last updated. | 
**security** | [**IntrinioSecurity**](IntrinioSecurity.md) |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_equity_quote_data import IntrinioEquityQuoteData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioEquityQuoteData from a JSON string
intrinio_equity_quote_data_instance = IntrinioEquityQuoteData.from_json(json)
# print the JSON string representation of the object
print(IntrinioEquityQuoteData.to_json())

# convert the object into a dict
intrinio_equity_quote_data_dict = intrinio_equity_quote_data_instance.to_dict()
# create an instance of IntrinioEquityQuoteData from a dict
intrinio_equity_quote_data_from_dict = IntrinioEquityQuoteData.from_dict(intrinio_equity_quote_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


