# coding: utf-8

"""
    OpenBB Platform API

    Investment research for everyone, anywhere.

    The version of the OpenAPI document: 1
    Contact: hello@openbb.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IntrinioEquityInfoData(BaseModel):
    """
    Intrinio Equity Info Data.
    """ # noqa: E501
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    name: Optional[StrictStr] = None
    cik: Optional[StrictStr] = None
    cusip: Optional[StrictStr] = None
    isin: Optional[StrictStr] = None
    lei: Optional[StrictStr] = None
    legal_name: Optional[StrictStr] = None
    stock_exchange: Optional[StrictStr] = None
    sic: Optional[StrictInt] = None
    short_description: Optional[StrictStr] = None
    long_description: Optional[StrictStr] = None
    ceo: Optional[StrictStr] = None
    company_url: Optional[StrictStr] = None
    business_address: Optional[StrictStr] = None
    mailing_address: Optional[StrictStr] = None
    business_phone_no: Optional[StrictStr] = None
    hq_address_1: Optional[StrictStr] = None
    hq_address_2: Optional[StrictStr] = None
    hq_address_city: Optional[StrictStr] = None
    hq_address_postal_code: Optional[StrictStr] = None
    hq_state: Optional[StrictStr] = None
    hq_country: Optional[StrictStr] = None
    inc_state: Optional[StrictStr] = None
    inc_country: Optional[StrictStr] = None
    employees: Optional[StrictInt] = None
    entity_legal_form: Optional[StrictStr] = None
    entity_status: Optional[StrictStr] = None
    latest_filing_date: Optional[date] = None
    irs_number: Optional[StrictStr] = None
    sector: Optional[StrictStr] = None
    industry_category: Optional[StrictStr] = None
    industry_group: Optional[StrictStr] = None
    template: Optional[StrictStr] = None
    standardized_active: Optional[StrictBool] = None
    first_fundamental_date: Optional[date] = None
    last_fundamental_date: Optional[date] = None
    first_stock_price_date: Optional[date] = None
    last_stock_price_date: Optional[date] = None
    id: Optional[StrictStr] = Field(default=None, description="Intrinio ID for the company.")
    thea_enabled: Optional[StrictBool] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "name", "cik", "cusip", "isin", "lei", "legal_name", "stock_exchange", "sic", "short_description", "long_description", "ceo", "company_url", "business_address", "mailing_address", "business_phone_no", "hq_address_1", "hq_address_2", "hq_address_city", "hq_address_postal_code", "hq_state", "hq_country", "inc_state", "inc_country", "employees", "entity_legal_form", "entity_status", "latest_filing_date", "irs_number", "sector", "industry_category", "industry_group", "template", "standardized_active", "first_fundamental_date", "last_fundamental_date", "first_stock_price_date", "last_stock_price_date", "id", "thea_enabled"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IntrinioEquityInfoData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if cik (nullable) is None
        # and model_fields_set contains the field
        if self.cik is None and "cik" in self.model_fields_set:
            _dict['cik'] = None

        # set to None if cusip (nullable) is None
        # and model_fields_set contains the field
        if self.cusip is None and "cusip" in self.model_fields_set:
            _dict['cusip'] = None

        # set to None if isin (nullable) is None
        # and model_fields_set contains the field
        if self.isin is None and "isin" in self.model_fields_set:
            _dict['isin'] = None

        # set to None if lei (nullable) is None
        # and model_fields_set contains the field
        if self.lei is None and "lei" in self.model_fields_set:
            _dict['lei'] = None

        # set to None if legal_name (nullable) is None
        # and model_fields_set contains the field
        if self.legal_name is None and "legal_name" in self.model_fields_set:
            _dict['legal_name'] = None

        # set to None if stock_exchange (nullable) is None
        # and model_fields_set contains the field
        if self.stock_exchange is None and "stock_exchange" in self.model_fields_set:
            _dict['stock_exchange'] = None

        # set to None if sic (nullable) is None
        # and model_fields_set contains the field
        if self.sic is None and "sic" in self.model_fields_set:
            _dict['sic'] = None

        # set to None if short_description (nullable) is None
        # and model_fields_set contains the field
        if self.short_description is None and "short_description" in self.model_fields_set:
            _dict['short_description'] = None

        # set to None if long_description (nullable) is None
        # and model_fields_set contains the field
        if self.long_description is None and "long_description" in self.model_fields_set:
            _dict['long_description'] = None

        # set to None if ceo (nullable) is None
        # and model_fields_set contains the field
        if self.ceo is None and "ceo" in self.model_fields_set:
            _dict['ceo'] = None

        # set to None if company_url (nullable) is None
        # and model_fields_set contains the field
        if self.company_url is None and "company_url" in self.model_fields_set:
            _dict['company_url'] = None

        # set to None if business_address (nullable) is None
        # and model_fields_set contains the field
        if self.business_address is None and "business_address" in self.model_fields_set:
            _dict['business_address'] = None

        # set to None if mailing_address (nullable) is None
        # and model_fields_set contains the field
        if self.mailing_address is None and "mailing_address" in self.model_fields_set:
            _dict['mailing_address'] = None

        # set to None if business_phone_no (nullable) is None
        # and model_fields_set contains the field
        if self.business_phone_no is None and "business_phone_no" in self.model_fields_set:
            _dict['business_phone_no'] = None

        # set to None if hq_address_1 (nullable) is None
        # and model_fields_set contains the field
        if self.hq_address_1 is None and "hq_address_1" in self.model_fields_set:
            _dict['hq_address_1'] = None

        # set to None if hq_address_2 (nullable) is None
        # and model_fields_set contains the field
        if self.hq_address_2 is None and "hq_address_2" in self.model_fields_set:
            _dict['hq_address_2'] = None

        # set to None if hq_address_city (nullable) is None
        # and model_fields_set contains the field
        if self.hq_address_city is None and "hq_address_city" in self.model_fields_set:
            _dict['hq_address_city'] = None

        # set to None if hq_address_postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.hq_address_postal_code is None and "hq_address_postal_code" in self.model_fields_set:
            _dict['hq_address_postal_code'] = None

        # set to None if hq_state (nullable) is None
        # and model_fields_set contains the field
        if self.hq_state is None and "hq_state" in self.model_fields_set:
            _dict['hq_state'] = None

        # set to None if hq_country (nullable) is None
        # and model_fields_set contains the field
        if self.hq_country is None and "hq_country" in self.model_fields_set:
            _dict['hq_country'] = None

        # set to None if inc_state (nullable) is None
        # and model_fields_set contains the field
        if self.inc_state is None and "inc_state" in self.model_fields_set:
            _dict['inc_state'] = None

        # set to None if inc_country (nullable) is None
        # and model_fields_set contains the field
        if self.inc_country is None and "inc_country" in self.model_fields_set:
            _dict['inc_country'] = None

        # set to None if employees (nullable) is None
        # and model_fields_set contains the field
        if self.employees is None and "employees" in self.model_fields_set:
            _dict['employees'] = None

        # set to None if entity_legal_form (nullable) is None
        # and model_fields_set contains the field
        if self.entity_legal_form is None and "entity_legal_form" in self.model_fields_set:
            _dict['entity_legal_form'] = None

        # set to None if entity_status (nullable) is None
        # and model_fields_set contains the field
        if self.entity_status is None and "entity_status" in self.model_fields_set:
            _dict['entity_status'] = None

        # set to None if latest_filing_date (nullable) is None
        # and model_fields_set contains the field
        if self.latest_filing_date is None and "latest_filing_date" in self.model_fields_set:
            _dict['latest_filing_date'] = None

        # set to None if irs_number (nullable) is None
        # and model_fields_set contains the field
        if self.irs_number is None and "irs_number" in self.model_fields_set:
            _dict['irs_number'] = None

        # set to None if sector (nullable) is None
        # and model_fields_set contains the field
        if self.sector is None and "sector" in self.model_fields_set:
            _dict['sector'] = None

        # set to None if industry_category (nullable) is None
        # and model_fields_set contains the field
        if self.industry_category is None and "industry_category" in self.model_fields_set:
            _dict['industry_category'] = None

        # set to None if industry_group (nullable) is None
        # and model_fields_set contains the field
        if self.industry_group is None and "industry_group" in self.model_fields_set:
            _dict['industry_group'] = None

        # set to None if template (nullable) is None
        # and model_fields_set contains the field
        if self.template is None and "template" in self.model_fields_set:
            _dict['template'] = None

        # set to None if standardized_active (nullable) is None
        # and model_fields_set contains the field
        if self.standardized_active is None and "standardized_active" in self.model_fields_set:
            _dict['standardized_active'] = None

        # set to None if first_fundamental_date (nullable) is None
        # and model_fields_set contains the field
        if self.first_fundamental_date is None and "first_fundamental_date" in self.model_fields_set:
            _dict['first_fundamental_date'] = None

        # set to None if last_fundamental_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_fundamental_date is None and "last_fundamental_date" in self.model_fields_set:
            _dict['last_fundamental_date'] = None

        # set to None if first_stock_price_date (nullable) is None
        # and model_fields_set contains the field
        if self.first_stock_price_date is None and "first_stock_price_date" in self.model_fields_set:
            _dict['first_stock_price_date'] = None

        # set to None if last_stock_price_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_stock_price_date is None and "last_stock_price_date" in self.model_fields_set:
            _dict['last_stock_price_date'] = None

        # set to None if thea_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.thea_enabled is None and "thea_enabled" in self.model_fields_set:
            _dict['thea_enabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntrinioEquityInfoData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "name": obj.get("name"),
            "cik": obj.get("cik"),
            "cusip": obj.get("cusip"),
            "isin": obj.get("isin"),
            "lei": obj.get("lei"),
            "legal_name": obj.get("legal_name"),
            "stock_exchange": obj.get("stock_exchange"),
            "sic": obj.get("sic"),
            "short_description": obj.get("short_description"),
            "long_description": obj.get("long_description"),
            "ceo": obj.get("ceo"),
            "company_url": obj.get("company_url"),
            "business_address": obj.get("business_address"),
            "mailing_address": obj.get("mailing_address"),
            "business_phone_no": obj.get("business_phone_no"),
            "hq_address_1": obj.get("hq_address_1"),
            "hq_address_2": obj.get("hq_address_2"),
            "hq_address_city": obj.get("hq_address_city"),
            "hq_address_postal_code": obj.get("hq_address_postal_code"),
            "hq_state": obj.get("hq_state"),
            "hq_country": obj.get("hq_country"),
            "inc_state": obj.get("inc_state"),
            "inc_country": obj.get("inc_country"),
            "employees": obj.get("employees"),
            "entity_legal_form": obj.get("entity_legal_form"),
            "entity_status": obj.get("entity_status"),
            "latest_filing_date": obj.get("latest_filing_date"),
            "irs_number": obj.get("irs_number"),
            "sector": obj.get("sector"),
            "industry_category": obj.get("industry_category"),
            "industry_group": obj.get("industry_group"),
            "template": obj.get("template"),
            "standardized_active": obj.get("standardized_active"),
            "first_fundamental_date": obj.get("first_fundamental_date"),
            "last_fundamental_date": obj.get("last_fundamental_date"),
            "first_stock_price_date": obj.get("first_stock_price_date"),
            "last_stock_price_date": obj.get("last_stock_price_date"),
            "id": obj.get("id"),
            "thea_enabled": obj.get("thea_enabled")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


