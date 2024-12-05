# QuoteIndicators

Indicators or indicator codes applicable to the participant quote related to the price bands for the issue, or the affect the quote has on the NBBO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.quote_indicators import QuoteIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteIndicators from a JSON string
quote_indicators_instance = QuoteIndicators.from_json(json)
# print the JSON string representation of the object
print(QuoteIndicators.to_json())

# convert the object into a dict
quote_indicators_dict = quote_indicators_instance.to_dict()
# create an instance of QuoteIndicators from a dict
quote_indicators_from_dict = QuoteIndicators.from_dict(quote_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


