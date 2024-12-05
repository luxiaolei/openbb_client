# FMPEquityPeersData

FMP Equity Peers Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peers_list** | **List[str]** | A list of equity peers based on sector, exchange and market cap. | [optional] 

## Example

```python
from openbb_client.models.fmp_equity_peers_data import FMPEquityPeersData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEquityPeersData from a JSON string
fmp_equity_peers_data_instance = FMPEquityPeersData.from_json(json)
# print the JSON string representation of the object
print(FMPEquityPeersData.to_json())

# convert the object into a dict
fmp_equity_peers_data_dict = fmp_equity_peers_data_instance.to_dict()
# create an instance of FMPEquityPeersData from a dict
fmp_equity_peers_data_from_dict = FMPEquityPeersData.from_dict(fmp_equity_peers_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


