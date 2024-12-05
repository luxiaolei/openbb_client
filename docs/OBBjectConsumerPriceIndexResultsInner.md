# OBBjectConsumerPriceIndexResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** |  | 
**value** | **float** | CPI index value or period change. | 
**expenditure** | **str** | Expenditure component of CPI. | 

## Example

```python
from openbb_client.models.ob_bject_consumer_price_index_results_inner import OBBjectConsumerPriceIndexResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectConsumerPriceIndexResultsInner from a JSON string
ob_bject_consumer_price_index_results_inner_instance = OBBjectConsumerPriceIndexResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectConsumerPriceIndexResultsInner.to_json())

# convert the object into a dict
ob_bject_consumer_price_index_results_inner_dict = ob_bject_consumer_price_index_results_inner_instance.to_dict()
# create an instance of OBBjectConsumerPriceIndexResultsInner from a dict
ob_bject_consumer_price_index_results_inner_from_dict = OBBjectConsumerPriceIndexResultsInner.from_dict(ob_bject_consumer_price_index_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


