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

from openbb_client.models.fmp_currency_historical_data import FMPCurrencyHistoricalData

class TestFMPCurrencyHistoricalData(unittest.TestCase):
    """FMPCurrencyHistoricalData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FMPCurrencyHistoricalData:
        """Test FMPCurrencyHistoricalData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FMPCurrencyHistoricalData`
        """
        model = FMPCurrencyHistoricalData()
        if include_optional:
            return FMPCurrencyHistoricalData(
                var_date = None,
                open = 1.337,
                high = 1.337,
                low = 1.337,
                close = 1.337,
                volume = 1.337,
                vwap = 1.337,
                adj_close = 1.337,
                change = 1.337,
                change_percent = 1.337
            )
        else:
            return FMPCurrencyHistoricalData(
                var_date = None,
                open = 1.337,
                high = 1.337,
                low = 1.337,
                close = 1.337,
        )
        """

    def testFMPCurrencyHistoricalData(self):
        """Test FMPCurrencyHistoricalData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
