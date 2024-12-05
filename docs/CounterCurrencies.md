# CounterCurrencies

An optional list of counter currency symbols to filter for. None returns all.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.counter_currencies import CounterCurrencies

# TODO update the JSON string below
json = "{}"
# create an instance of CounterCurrencies from a JSON string
counter_currencies_instance = CounterCurrencies.from_json(json)
# print the JSON string representation of the object
print(CounterCurrencies.to_json())

# convert the object into a dict
counter_currencies_dict = counter_currencies_instance.to_dict()
# create an instance of CounterCurrencies from a dict
counter_currencies_from_dict = CounterCurrencies.from_dict(counter_currencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


