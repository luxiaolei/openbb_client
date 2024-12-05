# OBBjectSharePriceIndex

OBBject with results of type SharePriceIndex

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OECDSharePriceIndexData]**](OECDSharePriceIndexData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_share_price_index import OBBjectSharePriceIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSharePriceIndex from a JSON string
ob_bject_share_price_index_instance = OBBjectSharePriceIndex.from_json(json)
# print the JSON string representation of the object
print(OBBjectSharePriceIndex.to_json())

# convert the object into a dict
ob_bject_share_price_index_dict = ob_bject_share_price_index_instance.to_dict()
# create an instance of OBBjectSharePriceIndex from a dict
ob_bject_share_price_index_from_dict = OBBjectSharePriceIndex.from_dict(ob_bject_share_price_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


