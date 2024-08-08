from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from domain.entities import RoundItem


class UpdateRoundRequest(BaseModel):
    items: list[RoundItem]


class UpdateOrderRequest(BaseModel):
    discounts: float = 0.0
    rounds: list[UpdateRoundRequest]
