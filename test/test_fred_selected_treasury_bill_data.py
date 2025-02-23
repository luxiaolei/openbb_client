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

from openbb_client.models.fred_selected_treasury_bill_data import FREDSelectedTreasuryBillData

class TestFREDSelectedTreasuryBillData(unittest.TestCase):
    """FREDSelectedTreasuryBillData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FREDSelectedTreasuryBillData:
        """Test FREDSelectedTreasuryBillData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FREDSelectedTreasuryBillData`
        """
        model = FREDSelectedTreasuryBillData()
        if include_optional:
            return FREDSelectedTreasuryBillData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                rate = 1.337
            )
        else:
            return FREDSelectedTreasuryBillData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                rate = 1.337,
        )
        """

    def testFREDSelectedTreasuryBillData(self):
        """Test FREDSelectedTreasuryBillData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
