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

from openbb_client.models.benzinga3 import Benzinga3

class TestBenzinga3(unittest.TestCase):
    """Benzinga3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Benzinga3:
        """Test Benzinga3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Benzinga3`
        """
        model = Benzinga3()
        if include_optional:
            return Benzinga3(
            )
        else:
            return Benzinga3(
        )
        """

    def testBenzinga3(self):
        """Test Benzinga3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
