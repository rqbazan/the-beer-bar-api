from uuid import UUID
from typing import Optional
from dataclasses import dataclass
from domain.entities import RoundItem, Payment, OrderItem, OrderStatus


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
    status: Optional[OrderStatus] = None
    payment: Optional[Payment] = None
    rounds: Optional[list[UpsertRoundModel]] = None
    items: Optional[list[OrderItem]] = None
