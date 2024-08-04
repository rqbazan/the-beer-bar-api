from uuid import UUID
from dataclasses import dataclass
from domain.entities import RoundItem, Payment

@dataclass
class UpsertRoundModel:
  items: list[RoundItem]

@dataclass
class CreateOrderModel:
  payment: Payment
  rounds: list[UpsertRoundModel]

@dataclass
class UpdateOrderModel:
  order_id: UUID
  payment: Payment
  rounds: list[UpsertRoundModel]