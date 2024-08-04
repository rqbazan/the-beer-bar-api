from typing import List, Optional
from uuid import UUID
from datetime import datetime
from dataclasses import dataclass
from .objects import OrderStatus

@dataclass
class InventoryItem:
  id: UUID
  product_name: str
  price_per_unit: float
  quantity: int

@dataclass
class Inventory:
  updated_at: datetime
  beers: List[InventoryItem]

@dataclass
class RoundItem:
  product_id: UUID
  price_per_unit: float
  quantity: int

@dataclass
class Round:
  id: UUID
  items: list[RoundItem]

@dataclass
class Payment:
  total: float
  subtotal: float
  taxes: float
  discounts: float

@dataclass
class OrderItem:
  product_id: UUID
  price_per_unit: float
  total: float

@dataclass
class Order:
  id: UUID
  code: str
  created_at: datetime
  updated_at: datetime
  status: OrderStatus
  payment: Optional[Payment]
  items: list[OrderItem]
  rounds: list[Round]
