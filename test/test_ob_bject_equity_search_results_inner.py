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

from openbb_client.models.ob_bject_equity_search_results_inner import OBBjectEquitySearchResultsInner

class TestOBBjectEquitySearchResultsInner(unittest.TestCase):
    """OBBjectEquitySearchResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OBBjectEquitySearchResultsInner:
        """Test OBBjectEquitySearchResultsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OBBjectEquitySearchResultsInner`
        """
        model = OBBjectEquitySearchResultsInner()
        if include_optional:
            return OBBjectEquitySearchResultsInner(
                symbol = '',
                name = '',
                cik = '',
                lei = '',
                intrinio_id = ''
            )
        else:
            return OBBjectEquitySearchResultsInner(
                cik = '',
                lei = '',
                intrinio_id = '',
        )
        """

    def testOBBjectEquitySearchResultsInner(self):
        """Test OBBjectEquitySearchResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
