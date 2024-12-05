# FMPCurrencySnapshotsData

FMP Currency Snapshots Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** | The base, or domestic, currency. | 
**counter_currency** | **str** | The counter, or foreign, currency. | 
**last_rate** | **float** | The exchange rate, relative to the base currency. Rates are expressed as the amount of foreign currency received from selling one unit of the base currency, or the quantity of foreign currency required to purchase one unit of the domestic currency. To inverse the perspective, set the &#39;quote_type&#39; parameter as &#39;direct&#39;. | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**prev_close** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**ma_50** | **float** |  | [optional] 
**ma_200** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**last_rate_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_currency_snapshots_data import FMPCurrencySnapshotsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCurrencySnapshotsData from a JSON string
fmp_currency_snapshots_data_instance = FMPCurrencySnapshotsData.from_json(json)
# print the JSON string representation of the object
print(FMPCurrencySnapshotsData.to_json())

# convert the object into a dict
fmp_currency_snapshots_data_dict = fmp_currency_snapshots_data_instance.to_dict()
# create an instance of FMPCurrencySnapshotsData from a dict
fmp_currency_snapshots_data_from_dict = FMPCurrencySnapshotsData.from_dict(fmp_currency_snapshots_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


