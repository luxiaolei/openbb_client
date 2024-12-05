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

from openbb_client.models.ob_bject_price_target_results_inner import OBBjectPriceTargetResultsInner

class TestOBBjectPriceTargetResultsInner(unittest.TestCase):
    """OBBjectPriceTargetResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OBBjectPriceTargetResultsInner:
        """Test OBBjectPriceTargetResultsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OBBjectPriceTargetResultsInner`
        """
        model = OBBjectPriceTargetResultsInner()
        if include_optional:
            return OBBjectPriceTargetResultsInner(
                published_date = None,
                published_time = '',
                symbol = '',
                exchange = '',
                company_name = '',
                analyst_name = '',
                analyst_firm = '',
                currency = '',
                price_target = 1.337,
                adj_price_target = 1.337,
                price_target_previous = 1.337,
                previous_adj_price_target = 1.337,
                price_when_posted = 1.337,
                rating_current = '',
                rating_previous = '',
                action = 'Downgrades',
                news_url = '',
                news_title = '',
                news_publisher = '',
                news_base_url = '',
                action_change = 'Announces',
                importance = 0,
                notes = '',
                analyst_id = '',
                url_news = '',
                url_analyst = '',
                id = '',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return OBBjectPriceTargetResultsInner(
                published_date = None,
                symbol = '',
        )
        """

    def testOBBjectPriceTargetResultsInner(self):
        """Test OBBjectPriceTargetResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
