# OBBjectEtfHoldingsDate

OBBject with results of type EtfHoldingsDate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPEtfHoldingsDateData]**](FMPEtfHoldingsDateData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_holdings_date import OBBjectEtfHoldingsDate

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfHoldingsDate from a JSON string
ob_bject_etf_holdings_date_instance = OBBjectEtfHoldingsDate.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfHoldingsDate.to_json())

# convert the object into a dict
ob_bject_etf_holdings_date_dict = ob_bject_etf_holdings_date_instance.to_dict()
# create an instance of OBBjectEtfHoldingsDate from a dict
ob_bject_etf_holdings_date_from_dict = OBBjectEtfHoldingsDate.from_dict(ob_bject_etf_holdings_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


