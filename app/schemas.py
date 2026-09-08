from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class Currency(str, Enum):
    SAR = "SAR"
    USD = "USD"


class RequestCreate(BaseModel):
    requester_name: str = Field(min_length=2, max_length=100)
    department: str = Field(min_length=2, max_length=100)
    title: str = Field(min_length=5, max_length=150)
    description: str = Field(min_length=20, max_length=2000)
    estimated_value: Decimal = Field(gt=0)
    currency: Currency = Currency.SAR