# FredSurveyOfEconomicConditionsChicagoData

FRED Survey Of Economic Conditions - Chicago - Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**activity_index** | **float** |  | [optional] 
**one_year_outlook** | **float** |  | [optional] 
**manufacturing_activity** | **float** |  | [optional] 
**non_manufacturing_activity** | **float** |  | [optional] 
**capital_expenditures_expectations** | **float** |  | [optional] 
**hiring_expectations** | **float** |  | [optional] 
**current_hiring** | **float** |  | [optional] 
**labor_costs** | **float** |  | [optional] 
**non_labor_costs** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_survey_of_economic_conditions_chicago_data import FredSurveyOfEconomicConditionsChicagoData

# TODO update the JSON string below
json = "{}"
# create an instance of FredSurveyOfEconomicConditionsChicagoData from a JSON string
fred_survey_of_economic_conditions_chicago_data_instance = FredSurveyOfEconomicConditionsChicagoData.from_json(json)
# print the JSON string representation of the object
print(FredSurveyOfEconomicConditionsChicagoData.to_json())

# convert the object into a dict
fred_survey_of_economic_conditions_chicago_data_dict = fred_survey_of_economic_conditions_chicago_data_instance.to_dict()
# create an instance of FredSurveyOfEconomicConditionsChicagoData from a dict
fred_survey_of_economic_conditions_chicago_data_from_dict = FredSurveyOfEconomicConditionsChicagoData.from_dict(fred_survey_of_economic_conditions_chicago_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


