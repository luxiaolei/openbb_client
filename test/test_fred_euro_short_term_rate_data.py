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

from openbb_client.models.fred_euro_short_term_rate_data import FredEuroShortTermRateData

class TestFredEuroShortTermRateData(unittest.TestCase):
    """FredEuroShortTermRateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FredEuroShortTermRateData:
        """Test FredEuroShortTermRateData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FredEuroShortTermRateData`
        """
        model = FredEuroShortTermRateData()
        if include_optional:
            return FredEuroShortTermRateData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                rate = 1.337,
                percentile_25 = 1.337,
                percentile_75 = 1.337,
                volume = 1.337,
                transactions = 56,
                number_of_banks = 56,
                large_bank_share_of_volume = 1.337
            )
        else:
            return FredEuroShortTermRateData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                rate = 1.337,
        )
        """

    def testFredEuroShortTermRateData(self):
        """Test FredEuroShortTermRateData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
