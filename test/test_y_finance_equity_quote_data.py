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

from openbb_client.models.y_finance_equity_quote_data import YFinanceEquityQuoteData

class TestYFinanceEquityQuoteData(unittest.TestCase):
    """YFinanceEquityQuoteData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> YFinanceEquityQuoteData:
        """Test YFinanceEquityQuoteData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `YFinanceEquityQuoteData`
        """
        model = YFinanceEquityQuoteData()
        if include_optional:
            return YFinanceEquityQuoteData(
                symbol = '',
                asset_type = '',
                name = '',
                exchange = '',
                bid = 1.337,
                bid_size = 56,
                bid_exchange = '',
                ask = 1.337,
                ask_size = 56,
                ask_exchange = '',
                quote_conditions = None,
                quote_indicators = None,
                sales_conditions = None,
                sequence_number = 56,
                market_center = '',
                participant_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                trf_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sip_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_price = 1.337,
                last_tick = '',
                last_size = 56,
                last_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                open = 1.337,
                high = 1.337,
                low = 1.337,
                close = 1.337,
                volume = None,
                exchange_volume = None,
                prev_close = 1.337,
                change = 1.337,
                change_percent = 1.337,
                year_high = 1.337,
                year_low = 1.337,
                ma_50d = 1.337,
                ma_200d = 1.337,
                volume_average = 1.337,
                volume_average_10d = 1.337,
                currency = ''
            )
        else:
            return YFinanceEquityQuoteData(
                symbol = '',
        )
        """

    def testYFinanceEquityQuoteData(self):
        """Test YFinanceEquityQuoteData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
