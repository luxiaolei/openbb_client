# FMPEtfEquityExposureData

FMP ETF Equity Exposure Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_symbol** | **str** | The symbol of the equity requested. | 
**etf_symbol** | **str** | The symbol of the ETF with exposure to the requested equity. | 
**shares** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**market_value** | [**MarketValue**](MarketValue.md) |  | [optional] 

## Example

```python
from openbb_client.models.fmp_etf_equity_exposure_data import FMPEtfEquityExposureData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEtfEquityExposureData from a JSON string
fmp_etf_equity_exposure_data_instance = FMPEtfEquityExposureData.from_json(json)
# print the JSON string representation of the object
print(FMPEtfEquityExposureData.to_json())

# convert the object into a dict
fmp_etf_equity_exposure_data_dict = fmp_etf_equity_exposure_data_instance.to_dict()
# create an instance of FMPEtfEquityExposureData from a dict
fmp_etf_equity_exposure_data_from_dict = FMPEtfEquityExposureData.from_dict(fmp_etf_equity_exposure_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


