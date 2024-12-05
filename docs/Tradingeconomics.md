# Tradingeconomics

Get events by TradingEconomics Calendar ID. Multiple comma separated items allowed. (provider: tradingeconomics)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.tradingeconomics import Tradingeconomics

# TODO update the JSON string below
json = "{}"
# create an instance of Tradingeconomics from a JSON string
tradingeconomics_instance = Tradingeconomics.from_json(json)
# print the JSON string representation of the object
print(Tradingeconomics.to_json())

# convert the object into a dict
tradingeconomics_dict = tradingeconomics_instance.to_dict()
# create an instance of Tradingeconomics from a dict
tradingeconomics_from_dict = Tradingeconomics.from_dict(tradingeconomics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


