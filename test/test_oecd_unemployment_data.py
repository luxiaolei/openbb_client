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

from openbb_client.models.oecd_unemployment_data import OECDUnemploymentData

class TestOECDUnemploymentData(unittest.TestCase):
    """OECDUnemploymentData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OECDUnemploymentData:
        """Test OECDUnemploymentData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OECDUnemploymentData`
        """
        model = OECDUnemploymentData()
        if include_optional:
            return OECDUnemploymentData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                country = '',
                value = 1.337
            )
        else:
            return OECDUnemploymentData(
        )
        """

    def testOECDUnemploymentData(self):
        """Test OECDUnemploymentData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
