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

from openbb_client.models.intrinio_equity_search_data import IntrinioEquitySearchData

class TestIntrinioEquitySearchData(unittest.TestCase):
    """IntrinioEquitySearchData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioEquitySearchData:
        """Test IntrinioEquitySearchData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioEquitySearchData`
        """
        model = IntrinioEquitySearchData()
        if include_optional:
            return IntrinioEquitySearchData(
                symbol = '',
                name = '',
                cik = '',
                lei = '',
                intrinio_id = ''
            )
        else:
            return IntrinioEquitySearchData(
                cik = '',
                lei = '',
                intrinio_id = '',
        )
        """

    def testIntrinioEquitySearchData(self):
        """Test IntrinioEquitySearchData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
