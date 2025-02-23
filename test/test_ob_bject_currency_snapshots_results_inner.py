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

from openbb_client.models.ob_bject_currency_snapshots_results_inner import OBBjectCurrencySnapshotsResultsInner

class TestOBBjectCurrencySnapshotsResultsInner(unittest.TestCase):
    """OBBjectCurrencySnapshotsResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OBBjectCurrencySnapshotsResultsInner:
        """Test OBBjectCurrencySnapshotsResultsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OBBjectCurrencySnapshotsResultsInner`
        """
        model = OBBjectCurrencySnapshotsResultsInner()
        if include_optional:
            return OBBjectCurrencySnapshotsResultsInner(
                base_currency = '',
                counter_currency = '',
                last_rate = 1.337,
                open = 1.337,
                high = 1.337,
                low = 1.337,
                close = 1.337,
                volume = 56,
                prev_close = 1.337,
                vwap = 1.337,
                change = 1.337,
                change_percent = 1.337,
                prev_open = 1.337,
                prev_high = 1.337,
                prev_low = 1.337,
                prev_volume = 1.337,
                prev_vwap = 1.337,
                bid = 1.337,
                ask = 1.337,
                minute_open = 1.337,
                minute_high = 1.337,
                minute_low = 1.337,
                minute_close = 1.337,
                minute_volume = 1.337,
                minute_vwap = 1.337,
                minute_transactions = 1.337,
                quote_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                minute_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ma_50 = 1.337,
                ma_200 = 1.337,
                year_high = 1.337,
                year_low = 1.337,
                last_rate_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return OBBjectCurrencySnapshotsResultsInner(
                base_currency = '',
                counter_currency = '',
                last_rate = 1.337,
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testOBBjectCurrencySnapshotsResultsInner(self):
        """Test OBBjectCurrencySnapshotsResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
