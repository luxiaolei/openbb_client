# ExchangeVolume

Volume of shares exchanged during the trading day on the specific exchange.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.exchange_volume import ExchangeVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeVolume from a JSON string
exchange_volume_instance = ExchangeVolume.from_json(json)
# print the JSON string representation of the object
print(ExchangeVolume.to_json())

# convert the object into a dict
exchange_volume_dict = exchange_volume_instance.to_dict()
# create an instance of ExchangeVolume from a dict
exchange_volume_from_dict = ExchangeVolume.from_dict(exchange_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


