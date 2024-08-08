from uuid import UUID
from typing import Optional
from pydantic import BaseModel


class PaymentResponse(BaseModel):
    total: str
    subtotal: str
    taxes: str
    discounts: str


class OrderItemResponse(BaseModel):
    product_id: UUID
    price_per_unit: str
    total: str


class RoundItemResponse(BaseModel):
    product_id: UUID
    price_per_unit: str
    quantity: int


class RoundResponse(BaseModel):
    id: UUID
    items: list[RoundItemResponse]


class OrderResponse(BaseModel):
    id: UUID
    code: str
    created_at: str
    updated_at: str
    status: str
    payment: PaymentResponse
    items: list[OrderItemResponse]
    rounds: list[RoundResponse]
