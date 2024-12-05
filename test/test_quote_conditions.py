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

from openbb_client.models.quote_conditions import QuoteConditions

class TestQuoteConditions(unittest.TestCase):
    """QuoteConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteConditions:
        """Test QuoteConditions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteConditions`
        """
        model = QuoteConditions()
        if include_optional:
            return QuoteConditions(
            )
        else:
            return QuoteConditions(
        )
        """

    def testQuoteConditions(self):
        """Test QuoteConditions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
