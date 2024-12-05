# FmpIntrinioSec

A specific date to get data for. Entering a date will attempt to return the NPORT-P filing for the entered date. This needs to be _exactly_ the date of the filing. Use the holdings_date command/endpoint to find available filing dates for the ETF. (provider: fmp);     A specific date to get data for. (provider: intrinio);     A specific date to get data for.  The date represents the period ending. The date entered will return the closest filing. (provider: sec)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.fmp_intrinio_sec import FmpIntrinioSec

# TODO update the JSON string below
json = "{}"
# create an instance of FmpIntrinioSec from a JSON string
fmp_intrinio_sec_instance = FmpIntrinioSec.from_json(json)
# print the JSON string representation of the object
print(FmpIntrinioSec.to_json())

# convert the object into a dict
fmp_intrinio_sec_dict = fmp_intrinio_sec_instance.to_dict()
# create an instance of FmpIntrinioSec from a dict
fmp_intrinio_sec_from_dict = FmpIntrinioSec.from_dict(fmp_intrinio_sec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


