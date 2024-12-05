# SecForm13FHRData

SEC Form 13F-HR Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end-of-quarter date of the filing. | 
**issuer** | **str** | The name of the issuer. | 
**cusip** | **str** | The CUSIP of the security. | 
**asset_class** | **str** | The title of the asset class for the security. | 
**security_type** | **str** |  | [optional] 
**option_type** | **str** |  | [optional] 
**investment_discretion** | **str** |  | [optional] 
**voting_authority_sole** | **int** |  | [optional] 
**voting_authority_shared** | **int** |  | [optional] 
**voting_authority_none** | **int** |  | [optional] 
**principal_amount** | **int** | The total number of shares of the class of security or the principal amount of such class. Defined by the &#39;security_type&#39;. Only long positions are reported | 
**value** | **int** | The fair market value of the holding of the particular class of security. The value reported for options is the fair market value of the underlying security with respect to the number of shares controlled. Values are rounded to the nearest US dollar and use the closing price of the last trading day of the calendar year or quarter. | 
**weight** | **float** | The weight of the security relative to the market value of all securities in the filing , as a normalized percent. | 

## Example

```python
from openbb_client.models.sec_form13_fhr_data import SecForm13FHRData

# TODO update the JSON string below
json = "{}"
# create an instance of SecForm13FHRData from a JSON string
sec_form13_fhr_data_instance = SecForm13FHRData.from_json(json)
# print the JSON string representation of the object
print(SecForm13FHRData.to_json())

# convert the object into a dict
sec_form13_fhr_data_dict = sec_form13_fhr_data_instance.to_dict()
# create an instance of SecForm13FHRData from a dict
sec_form13_fhr_data_from_dict = SecForm13FHRData.from_dict(sec_form13_fhr_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


