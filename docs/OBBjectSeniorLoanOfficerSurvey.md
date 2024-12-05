# OBBjectSeniorLoanOfficerSurvey

OBBject with results of type SeniorLoanOfficerSurvey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredSeniorLoanOfficerSurveyData]**](FredSeniorLoanOfficerSurveyData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_senior_loan_officer_survey import OBBjectSeniorLoanOfficerSurvey

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSeniorLoanOfficerSurvey from a JSON string
ob_bject_senior_loan_officer_survey_instance = OBBjectSeniorLoanOfficerSurvey.from_json(json)
# print the JSON string representation of the object
print(OBBjectSeniorLoanOfficerSurvey.to_json())

# convert the object into a dict
ob_bject_senior_loan_officer_survey_dict = ob_bject_senior_loan_officer_survey_instance.to_dict()
# create an instance of OBBjectSeniorLoanOfficerSurvey from a dict
ob_bject_senior_loan_officer_survey_from_dict = OBBjectSeniorLoanOfficerSurvey.from_dict(ob_bject_senior_loan_officer_survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


