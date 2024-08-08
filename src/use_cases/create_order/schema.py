from pydantic import BaseModel
from typing import Optional
from domain.entities import RoundItem


class CreateRoundRequest(BaseModel):
    items: list[RoundItem]


class CreateOrderRequest(BaseModel):
    discounts: float = 0.0
    rounds: list[CreateRoundRequest]
