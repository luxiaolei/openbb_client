# FMPDiscoveryFilingsData

FMP Discovery Filings Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**cik** | **str** | Central Index Key (CIK) for the requested entity. | 
**title** | **str** | Title of the filing. | 
**var_date** | **datetime** | The date of the data. | 
**form_type** | **str** | The form type of the filing | 
**link** | **str** | URL to the filing page on the SEC site. | 

## Example

```python
from openbb_client.models.fmp_discovery_filings_data import FMPDiscoveryFilingsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPDiscoveryFilingsData from a JSON string
fmp_discovery_filings_data_instance = FMPDiscoveryFilingsData.from_json(json)
# print the JSON string representation of the object
print(FMPDiscoveryFilingsData.to_json())

# convert the object into a dict
fmp_discovery_filings_data_dict = fmp_discovery_filings_data_instance.to_dict()
# create an instance of FMPDiscoveryFilingsData from a dict
fmp_discovery_filings_data_from_dict = FMPDiscoveryFilingsData.from_dict(fmp_discovery_filings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


