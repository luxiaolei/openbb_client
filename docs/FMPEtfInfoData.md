# FMPEtfInfoData

FMP ETF Info Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. (ETF) | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**inception_date** | **str** |  | 
**issuer** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**domicile** | **str** |  | [optional] 
**asset_class** | **str** |  | [optional] 
**aum** | **float** |  | [optional] 
**nav** | **float** |  | [optional] 
**nav_currency** | **str** |  | [optional] 
**expense_ratio** | **float** |  | [optional] 
**holdings_count** | **int** |  | [optional] 
**avg_volume** | **float** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_etf_info_data import FMPEtfInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEtfInfoData from a JSON string
fmp_etf_info_data_instance = FMPEtfInfoData.from_json(json)
# print the JSON string representation of the object
print(FMPEtfInfoData.to_json())

# convert the object into a dict
fmp_etf_info_data_dict = fmp_etf_info_data_instance.to_dict()
# create an instance of FMPEtfInfoData from a dict
fmp_etf_info_data_from_dict = FMPEtfInfoData.from_dict(fmp_etf_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


