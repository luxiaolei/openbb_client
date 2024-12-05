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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openbb_client.models.intrinio_security import IntrinioSecurity
from typing import Optional, Set
from typing_extensions import Self

class IntrinioCompanyNewsData(BaseModel):
    """
    Intrinio Company News Data.
    """ # noqa: E501
    var_date: datetime = Field(description="The date of the data. Here it is the published date of the article.", alias="date")
    title: StrictStr = Field(description="Title of the article.")
    text: Optional[StrictStr] = None
    images: Optional[List[Dict[str, StrictStr]]] = None
    url: StrictStr = Field(description="URL to the article.")
    symbols: Optional[StrictStr] = None
    source: Optional[StrictStr] = None
    summary: Optional[StrictStr] = None
    topics: Optional[StrictStr] = None
    word_count: Optional[StrictInt] = None
    business_relevance: Optional[Union[StrictFloat, StrictInt]] = None
    sentiment: Optional[StrictStr] = None
    sentiment_confidence: Optional[Union[StrictFloat, StrictInt]] = None
    language: Optional[StrictStr] = None
    spam: Optional[StrictBool] = None
    copyright: Optional[StrictStr] = None
    id: StrictStr = Field(description="Article ID.")
    security: Optional[IntrinioSecurity] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["date", "title", "text", "images", "url", "symbols", "source", "summary", "topics", "word_count", "business_relevance", "sentiment", "sentiment_confidence", "language", "spam", "copyright", "id", "security"]

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
        """Create an instance of IntrinioCompanyNewsData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if symbols (nullable) is None
        # and model_fields_set contains the field
        if self.symbols is None and "symbols" in self.model_fields_set:
            _dict['symbols'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if summary (nullable) is None
        # and model_fields_set contains the field
        if self.summary is None and "summary" in self.model_fields_set:
            _dict['summary'] = None

        # set to None if topics (nullable) is None
        # and model_fields_set contains the field
        if self.topics is None and "topics" in self.model_fields_set:
            _dict['topics'] = None

        # set to None if word_count (nullable) is None
        # and model_fields_set contains the field
        if self.word_count is None and "word_count" in self.model_fields_set:
            _dict['word_count'] = None

        # set to None if business_relevance (nullable) is None
        # and model_fields_set contains the field
        if self.business_relevance is None and "business_relevance" in self.model_fields_set:
            _dict['business_relevance'] = None

        # set to None if sentiment (nullable) is None
        # and model_fields_set contains the field
        if self.sentiment is None and "sentiment" in self.model_fields_set:
            _dict['sentiment'] = None

        # set to None if sentiment_confidence (nullable) is None
        # and model_fields_set contains the field
        if self.sentiment_confidence is None and "sentiment_confidence" in self.model_fields_set:
            _dict['sentiment_confidence'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if spam (nullable) is None
        # and model_fields_set contains the field
        if self.spam is None and "spam" in self.model_fields_set:
            _dict['spam'] = None

        # set to None if copyright (nullable) is None
        # and model_fields_set contains the field
        if self.copyright is None and "copyright" in self.model_fields_set:
            _dict['copyright'] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict['security'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntrinioCompanyNewsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "title": obj.get("title"),
            "text": obj.get("text"),
            "images": obj.get("images"),
            "url": obj.get("url"),
            "symbols": obj.get("symbols"),
            "source": obj.get("source"),
            "summary": obj.get("summary"),
            "topics": obj.get("topics"),
            "word_count": obj.get("word_count"),
            "business_relevance": obj.get("business_relevance"),
            "sentiment": obj.get("sentiment"),
            "sentiment_confidence": obj.get("sentiment_confidence"),
            "language": obj.get("language"),
            "spam": obj.get("spam"),
            "copyright": obj.get("copyright"),
            "id": obj.get("id"),
            "security": IntrinioSecurity.from_dict(obj["security"]) if obj.get("security") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


