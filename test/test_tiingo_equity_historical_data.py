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

from openbb_client.models.tiingo_equity_historical_data import TiingoEquityHistoricalData

class TestTiingoEquityHistoricalData(unittest.TestCase):
    """TiingoEquityHistoricalData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TiingoEquityHistoricalData:
        """Test TiingoEquityHistoricalData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TiingoEquityHistoricalData`
        """
        model = TiingoEquityHistoricalData()
        if include_optional:
            return TiingoEquityHistoricalData(
                var_date = None,
                open = 1.337,
                high = 1.337,
                low = 1.337,
                close = 1.337,
                volume = None,
                vwap = 1.337,
                adj_open = 1.337,
                adj_high = 1.337,
                adj_low = 1.337,
                adj_close = 1.337,
                adj_volume = 1.337,
                split_ratio = 1.337,
                dividend = 1.337
            )
        else:
            return TiingoEquityHistoricalData(
                var_date = None,
                open = 1.337,
                high = 1.337,
                low = 1.337,
                close = 1.337,
        )
        """

    def testTiingoEquityHistoricalData(self):
        """Test TiingoEquityHistoricalData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
