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

from openbb_client.models.polygon_currency_pairs_data import PolygonCurrencyPairsData

class TestPolygonCurrencyPairsData(unittest.TestCase):
    """PolygonCurrencyPairsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolygonCurrencyPairsData:
        """Test PolygonCurrencyPairsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolygonCurrencyPairsData`
        """
        model = PolygonCurrencyPairsData()
        if include_optional:
            return PolygonCurrencyPairsData(
                symbol = '',
                name = '',
                currency_symbol = '',
                base_currency_symbol = '',
                base_currency_name = '',
                market = '',
                locale = '',
                last_updated = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                delisted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return PolygonCurrencyPairsData(
                symbol = '',
                market = '',
                locale = '',
        )
        """

    def testPolygonCurrencyPairsData(self):
        """Test PolygonCurrencyPairsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
