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

from openbb_client.models.fmp_etf_holdings_data import FMPEtfHoldingsData

class TestFMPEtfHoldingsData(unittest.TestCase):
    """FMPEtfHoldingsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FMPEtfHoldingsData:
        """Test FMPEtfHoldingsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FMPEtfHoldingsData`
        """
        model = FMPEtfHoldingsData()
        if include_optional:
            return FMPEtfHoldingsData(
                symbol = '',
                name = '',
                lei = '',
                title = '',
                cusip = '',
                isin = '',
                balance = 56,
                units = None,
                currency = '',
                value = 1.337,
                weight = 1.337,
                payoff_profile = '',
                asset_category = '',
                issuer_category = '',
                country = '',
                is_restricted = '',
                fair_value_level = 56,
                is_cash_collateral = '',
                is_non_cash_collateral = '',
                is_loan_by_fund = '',
                cik = '',
                acceptance_datetime = '',
                updated = None
            )
        else:
            return FMPEtfHoldingsData(
        )
        """

    def testFMPEtfHoldingsData(self):
        """Test FMPEtfHoldingsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
