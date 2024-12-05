# coding: utf-8

"""
    OpenBB Platform API

    Investment research for everyone, anywhere.

    The version of the OpenAPI document: 1
    Contact: hello@openbb.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openbb_client.models.openbb_fred_models_yield_curve_fred_yield_curve_data import OpenbbFredModelsYieldCurveFREDYieldCurveData

class TestOpenbbFredModelsYieldCurveFREDYieldCurveData(unittest.TestCase):
    """OpenbbFredModelsYieldCurveFREDYieldCurveData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenbbFredModelsYieldCurveFREDYieldCurveData:
        """Test OpenbbFredModelsYieldCurveFREDYieldCurveData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenbbFredModelsYieldCurveFREDYieldCurveData`
        """
        model = OpenbbFredModelsYieldCurveFREDYieldCurveData()
        if include_optional:
            return OpenbbFredModelsYieldCurveFREDYieldCurveData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                maturity = '',
                maturity_years = 1.337
            )
        else:
            return OpenbbFredModelsYieldCurveFREDYieldCurveData(
                maturity = '',
                maturity_years = 1.337,
        )
        """

    def testOpenbbFredModelsYieldCurveFREDYieldCurveData(self):
        """Test OpenbbFredModelsYieldCurveFREDYieldCurveData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
