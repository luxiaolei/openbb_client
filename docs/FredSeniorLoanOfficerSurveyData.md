# FredSeniorLoanOfficerSurveyData

FRED Senior Loan Officer Opinion Survey Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**value** | **float** | Survey value. | 
**title** | **str** |  | 

## Example

```python
from openbb_client.models.fred_senior_loan_officer_survey_data import FredSeniorLoanOfficerSurveyData

# TODO update the JSON string below
json = "{}"
# create an instance of FredSeniorLoanOfficerSurveyData from a JSON string
fred_senior_loan_officer_survey_data_instance = FredSeniorLoanOfficerSurveyData.from_json(json)
# print the JSON string representation of the object
print(FredSeniorLoanOfficerSurveyData.to_json())

# convert the object into a dict
fred_senior_loan_officer_survey_data_dict = fred_senior_loan_officer_survey_data_instance.to_dict()
# create an instance of FredSeniorLoanOfficerSurveyData from a dict
fred_senior_loan_officer_survey_data_from_dict = FredSeniorLoanOfficerSurveyData.from_dict(fred_senior_loan_officer_survey_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


