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

from openbb_client.models.ob_bject_non_farm_payrolls import OBBjectNonFarmPayrolls

class TestOBBjectNonFarmPayrolls(unittest.TestCase):
    """OBBjectNonFarmPayrolls unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OBBjectNonFarmPayrolls:
        """Test OBBjectNonFarmPayrolls
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OBBjectNonFarmPayrolls`
        """
        model = OBBjectNonFarmPayrolls()
        if include_optional:
            return OBBjectNonFarmPayrolls(
                id = '',
                results = [
                    { }
                    ],
                provider = '',
                warnings = [
                    openbb_client.models.warning_.Warning_(
                        category = '', 
                        message = '', )
                    ],
                chart = openbb_client.models.chart.Chart(
                    content = openbb_client.models.content.content(), 
                    format = '', 
                    fig = null, ),
                extra = openbb_client.models.extra.Extra()
            )
        else:
            return OBBjectNonFarmPayrolls(
        )
        """

    def testOBBjectNonFarmPayrolls(self):
        """Test OBBjectNonFarmPayrolls"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
