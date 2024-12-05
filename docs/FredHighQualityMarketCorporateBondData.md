# FredHighQualityMarketCorporateBondData

FRED High Quality Market Corporate Bond Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** | Interest rate. | 
**maturity** | **str** | Maturity. | 

## Example

```python
from openbb_client.models.fred_high_quality_market_corporate_bond_data import FredHighQualityMarketCorporateBondData

# TODO update the JSON string below
json = "{}"
# create an instance of FredHighQualityMarketCorporateBondData from a JSON string
fred_high_quality_market_corporate_bond_data_instance = FredHighQualityMarketCorporateBondData.from_json(json)
# print the JSON string representation of the object
print(FredHighQualityMarketCorporateBondData.to_json())

# convert the object into a dict
fred_high_quality_market_corporate_bond_data_dict = fred_high_quality_market_corporate_bond_data_instance.to_dict()
# create an instance of FredHighQualityMarketCorporateBondData from a dict
fred_high_quality_market_corporate_bond_data_from_dict = FredHighQualityMarketCorporateBondData.from_dict(fred_high_quality_market_corporate_bond_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


