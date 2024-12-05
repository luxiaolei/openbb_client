# OBBjectConsumerPriceIndex

OBBject with results of type ConsumerPriceIndex

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectConsumerPriceIndexResultsInner]**](OBBjectConsumerPriceIndexResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_consumer_price_index import OBBjectConsumerPriceIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectConsumerPriceIndex from a JSON string
ob_bject_consumer_price_index_instance = OBBjectConsumerPriceIndex.from_json(json)
# print the JSON string representation of the object
print(OBBjectConsumerPriceIndex.to_json())

# convert the object into a dict
ob_bject_consumer_price_index_dict = ob_bject_consumer_price_index_instance.to_dict()
# create an instance of OBBjectConsumerPriceIndex from a dict
ob_bject_consumer_price_index_from_dict = OBBjectConsumerPriceIndex.from_dict(ob_bject_consumer_price_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


