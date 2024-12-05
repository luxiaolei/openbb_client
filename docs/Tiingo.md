# Tiingo

To limit the query to a subset of exchanges e.g. ['POLONIEX', 'GDAX'] Multiple comma separated items allowed. (provider: tiingo)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.tiingo import Tiingo

# TODO update the JSON string below
json = "{}"
# create an instance of Tiingo from a JSON string
tiingo_instance = Tiingo.from_json(json)
# print the JSON string representation of the object
print(Tiingo.to_json())

# convert the object into a dict
tiingo_dict = tiingo_instance.to_dict()
# create an instance of Tiingo from a dict
tiingo_from_dict = Tiingo.from_dict(tiingo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


