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

from openbb_client.models.y_finance_balance_sheet_data import YFinanceBalanceSheetData

class TestYFinanceBalanceSheetData(unittest.TestCase):
    """YFinanceBalanceSheetData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> YFinanceBalanceSheetData:
        """Test YFinanceBalanceSheetData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `YFinanceBalanceSheetData`
        """
        model = YFinanceBalanceSheetData()
        if include_optional:
            return YFinanceBalanceSheetData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fiscal_period = '',
                fiscal_year = 56
            )
        else:
            return YFinanceBalanceSheetData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testYFinanceBalanceSheetData(self):
        """Test YFinanceBalanceSheetData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
