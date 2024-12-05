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

from openbb_client.models.oecdstir_data import OECDSTIRData

class TestOECDSTIRData(unittest.TestCase):
    """OECDSTIRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OECDSTIRData:
        """Test OECDSTIRData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OECDSTIRData`
        """
        model = OECDSTIRData()
        if include_optional:
            return OECDSTIRData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                value = 1.337,
                country = ''
            )
        else:
            return OECDSTIRData(
        )
        """

    def testOECDSTIRData(self):
        """Test OECDSTIRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
