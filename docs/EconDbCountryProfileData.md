# EconDbCountryProfileData

EconDB Country Profile Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**population** | **int** |  | [optional] 
**gdp_usd** | **float** |  | [optional] 
**gdp_qoq** | **float** |  | [optional] 
**gdp_yoy** | **float** |  | [optional] 
**cpi_yoy** | **float** |  | [optional] 
**core_yoy** | **float** |  | [optional] 
**retail_sales_yoy** | **float** |  | [optional] 
**industrial_production_yoy** | **float** |  | [optional] 
**policy_rate** | **float** |  | [optional] 
**yield_10y** | **float** |  | [optional] 
**govt_debt_gdp** | **float** |  | [optional] 
**current_account_gdp** | **float** |  | [optional] 
**jobless_rate** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.econ_db_country_profile_data import EconDbCountryProfileData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbCountryProfileData from a JSON string
econ_db_country_profile_data_instance = EconDbCountryProfileData.from_json(json)
# print the JSON string representation of the object
print(EconDbCountryProfileData.to_json())

# convert the object into a dict
econ_db_country_profile_data_dict = econ_db_country_profile_data_instance.to_dict()
# create an instance of EconDbCountryProfileData from a dict
econ_db_country_profile_data_from_dict = EconDbCountryProfileData.from_dict(econ_db_country_profile_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


