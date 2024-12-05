# FMPEquityQuoteData

FMP Equity Quote Data.

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
**price_avg_50** | **float** |  | [optional] 
**price_avg_200** | **float** |  | [optional] 
**avg_volume** | **int** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**shares_outstanding** | **int** |  | [optional] 
**eps** | **float** |  | [optional] 
**pe** | **float** |  | [optional] 
**earnings_announcement** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_equity_quote_data import FMPEquityQuoteData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEquityQuoteData from a JSON string
fmp_equity_quote_data_instance = FMPEquityQuoteData.from_json(json)
# print the JSON string representation of the object
print(FMPEquityQuoteData.to_json())

# convert the object into a dict
fmp_equity_quote_data_dict = fmp_equity_quote_data_instance.to_dict()
# create an instance of FMPEquityQuoteData from a dict
fmp_equity_quote_data_from_dict = FMPEquityQuoteData.from_dict(fmp_equity_quote_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


