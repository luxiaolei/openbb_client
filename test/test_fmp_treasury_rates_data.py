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

from openbb_client.models.fmp_treasury_rates_data import FMPTreasuryRatesData

class TestFMPTreasuryRatesData(unittest.TestCase):
    """FMPTreasuryRatesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FMPTreasuryRatesData:
        """Test FMPTreasuryRatesData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FMPTreasuryRatesData`
        """
        model = FMPTreasuryRatesData()
        if include_optional:
            return FMPTreasuryRatesData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                week_4 = 1.337,
                month_1 = 1.337,
                month_2 = 1.337,
                month_3 = 1.337,
                month_6 = 1.337,
                year_1 = 1.337,
                year_2 = 1.337,
                year_3 = 1.337,
                year_5 = 1.337,
                year_7 = 1.337,
                year_10 = 1.337,
                year_20 = 1.337,
                year_30 = 1.337
            )
        else:
            return FMPTreasuryRatesData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testFMPTreasuryRatesData(self):
        """Test FMPTreasuryRatesData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
