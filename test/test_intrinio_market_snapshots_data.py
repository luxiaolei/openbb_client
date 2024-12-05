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

from openbb_client.models.intrinio_market_snapshots_data import IntrinioMarketSnapshotsData

class TestIntrinioMarketSnapshotsData(unittest.TestCase):
    """IntrinioMarketSnapshotsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioMarketSnapshotsData:
        """Test IntrinioMarketSnapshotsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioMarketSnapshotsData`
        """
        model = IntrinioMarketSnapshotsData()
        if include_optional:
            return IntrinioMarketSnapshotsData(
                symbol = '',
                open = 1.337,
                high = 1.337,
                low = 1.337,
                close = 1.337,
                volume = 56,
                prev_close = 1.337,
                change = 1.337,
                change_percent = 1.337,
                last_price = 1.337,
                last_size = 56,
                last_volume = 56,
                last_trade_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                bid_size = 56,
                bid_price = 1.337,
                ask_price = 1.337,
                ask_size = 56,
                last_bid_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_ask_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return IntrinioMarketSnapshotsData(
                symbol = '',
        )
        """

    def testIntrinioMarketSnapshotsData(self):
        """Test IntrinioMarketSnapshotsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
