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

from openbb_client.models.intrinio_tiingo1 import IntrinioTiingo1

class TestIntrinioTiingo1(unittest.TestCase):
    """IntrinioTiingo1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioTiingo1:
        """Test IntrinioTiingo1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioTiingo1`
        """
        model = IntrinioTiingo1()
        if include_optional:
            return IntrinioTiingo1(
            )
        else:
            return IntrinioTiingo1(
        )
        """

    def testIntrinioTiingo1(self):
        """Test IntrinioTiingo1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
