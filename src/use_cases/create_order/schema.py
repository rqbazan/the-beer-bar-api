from pydantic import BaseModel
from typing import Optional
from domain.entities import RoundItem

class CreateRoundRequest(BaseModel):
  items: list[RoundItem]

class CreateOrderRequest(BaseModel):
  discount: Optional[float] = 0.0
  rounds: list[CreateRoundRequest]