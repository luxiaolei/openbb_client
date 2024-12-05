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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openbb_client.models.fmp_historical_dividends_data import FMPHistoricalDividendsData
from openbb_client.models.intrinio_historical_dividends_data import IntrinioHistoricalDividendsData
from openbb_client.models.y_finance_historical_dividends_data import YFinanceHistoricalDividendsData
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

OBBJECTHISTORICALDIVIDENDSRESULTSINNER_ONE_OF_SCHEMAS = ["FMPHistoricalDividendsData", "IntrinioHistoricalDividendsData", "YFinanceHistoricalDividendsData"]

class OBBjectHistoricalDividendsResultsInner(BaseModel):
    """
    OBBjectHistoricalDividendsResultsInner
    """
    # data type: FMPHistoricalDividendsData
    oneof_schema_1_validator: Optional[FMPHistoricalDividendsData] = None
    # data type: YFinanceHistoricalDividendsData
    oneof_schema_2_validator: Optional[YFinanceHistoricalDividendsData] = None
    # data type: IntrinioHistoricalDividendsData
    oneof_schema_3_validator: Optional[IntrinioHistoricalDividendsData] = None
    actual_instance: Optional[Union[FMPHistoricalDividendsData, IntrinioHistoricalDividendsData, YFinanceHistoricalDividendsData]] = None
    one_of_schemas: Set[str] = { "FMPHistoricalDividendsData", "IntrinioHistoricalDividendsData", "YFinanceHistoricalDividendsData" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = OBBjectHistoricalDividendsResultsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: FMPHistoricalDividendsData
        if not isinstance(v, FMPHistoricalDividendsData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FMPHistoricalDividendsData`")
        else:
            match += 1
        # validate data type: YFinanceHistoricalDividendsData
        if not isinstance(v, YFinanceHistoricalDividendsData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `YFinanceHistoricalDividendsData`")
        else:
            match += 1
        # validate data type: IntrinioHistoricalDividendsData
        if not isinstance(v, IntrinioHistoricalDividendsData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IntrinioHistoricalDividendsData`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in OBBjectHistoricalDividendsResultsInner with oneOf schemas: FMPHistoricalDividendsData, IntrinioHistoricalDividendsData, YFinanceHistoricalDividendsData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in OBBjectHistoricalDividendsResultsInner with oneOf schemas: FMPHistoricalDividendsData, IntrinioHistoricalDividendsData, YFinanceHistoricalDividendsData. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into FMPHistoricalDividendsData
        try:
            instance.actual_instance = FMPHistoricalDividendsData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into YFinanceHistoricalDividendsData
        try:
            instance.actual_instance = YFinanceHistoricalDividendsData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IntrinioHistoricalDividendsData
        try:
            instance.actual_instance = IntrinioHistoricalDividendsData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into OBBjectHistoricalDividendsResultsInner with oneOf schemas: FMPHistoricalDividendsData, IntrinioHistoricalDividendsData, YFinanceHistoricalDividendsData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into OBBjectHistoricalDividendsResultsInner with oneOf schemas: FMPHistoricalDividendsData, IntrinioHistoricalDividendsData, YFinanceHistoricalDividendsData. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], FMPHistoricalDividendsData, IntrinioHistoricalDividendsData, YFinanceHistoricalDividendsData]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


