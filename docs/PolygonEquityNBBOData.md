# PolygonEquityNBBOData

Polygon Equity NBBO data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_exchange** | **str** | The exchange ID for the ask. | 
**ask** | **float** | The last ask price. | 
**ask_size** | **int** |          The ask size. This represents the number of round lot orders at the given ask price.         The normal round lot size is 100 shares.         An ask size of 2 means there are 200 shares available to purchase at the given ask price.          | 
**bid_size** | **int** | The bid size in round lots. | 
**bid** | **float** | The last bid price. | 
**bid_exchange** | **str** | The exchange ID for the bid. | 
**tape** | **str** |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**indicators** | **List[int]** |  | [optional] 
**sequence_num** | **int** |  | [optional] 
**participant_timestamp** | **datetime** |  | [optional] 
**sip_timestamp** | **datetime** |  | [optional] 
**trf_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_equity_nbbo_data import PolygonEquityNBBOData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonEquityNBBOData from a JSON string
polygon_equity_nbbo_data_instance = PolygonEquityNBBOData.from_json(json)
# print the JSON string representation of the object
print(PolygonEquityNBBOData.to_json())

# convert the object into a dict
polygon_equity_nbbo_data_dict = polygon_equity_nbbo_data_instance.to_dict()
# create an instance of PolygonEquityNBBOData from a dict
polygon_equity_nbbo_data_from_dict = PolygonEquityNBBOData.from_dict(polygon_equity_nbbo_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


