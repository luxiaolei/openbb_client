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

from openbb_client.models.intrinio_options_snapshots_data import IntrinioOptionsSnapshotsData

class TestIntrinioOptionsSnapshotsData(unittest.TestCase):
    """IntrinioOptionsSnapshotsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioOptionsSnapshotsData:
        """Test IntrinioOptionsSnapshotsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioOptionsSnapshotsData`
        """
        model = IntrinioOptionsSnapshotsData()
        if include_optional:
            return IntrinioOptionsSnapshotsData(
                underlying_symbol = [
                    ''
                    ],
                contract_symbol = [
                    ''
                    ],
                expiration = [
                    datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
                    ],
                dte = [
                    56
                    ],
                strike = [
                    1.337
                    ],
                option_type = [
                    ''
                    ],
                volume = [
                    56
                    ],
                open_interest = [
                    56
                    ],
                last_price = [
                    1.337
                    ],
                last_size = [
                    56
                    ],
                last_timestamp = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                open = [
                    1.337
                    ],
                high = [
                    1.337
                    ],
                low = [
                    1.337
                    ],
                close = [
                    1.337
                    ],
                bid = [
                    1.337
                    ],
                bid_size = [
                    56
                    ],
                bid_timestamp = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                ask = [
                    1.337
                    ],
                ask_size = [
                    56
                    ],
                ask_timestamp = [
                    datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
                    ],
                total_bid_volume = [
                    56
                    ],
                bid_high = [
                    1.337
                    ],
                bid_low = [
                    1.337
                    ],
                total_ask_volume = [
                    56
                    ],
                ask_high = [
                    1.337
                    ],
                ask_low = [
                    1.337
                    ]
            )
        else:
            return IntrinioOptionsSnapshotsData(
                underlying_symbol = [
                    ''
                    ],
                contract_symbol = [
                    ''
                    ],
                expiration = [
                    datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
                    ],
                strike = [
                    1.337
                    ],
                option_type = [
                    ''
                    ],
        )
        """

    def testIntrinioOptionsSnapshotsData(self):
        """Test IntrinioOptionsSnapshotsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
