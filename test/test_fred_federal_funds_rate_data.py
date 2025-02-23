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

from openbb_client.models.fred_federal_funds_rate_data import FredFederalFundsRateData

class TestFredFederalFundsRateData(unittest.TestCase):
    """FredFederalFundsRateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FredFederalFundsRateData:
        """Test FredFederalFundsRateData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FredFederalFundsRateData`
        """
        model = FredFederalFundsRateData()
        if include_optional:
            return FredFederalFundsRateData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                rate = 1.337,
                target_range_upper = 1.337,
                target_range_lower = 1.337,
                percentile_1 = 1.337,
                percentile_25 = 1.337,
                percentile_75 = 1.337,
                percentile_99 = 1.337,
                volume = 1.337
            )
        else:
            return FredFederalFundsRateData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                rate = 1.337,
        )
        """

    def testFredFederalFundsRateData(self):
        """Test FredFederalFundsRateData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
