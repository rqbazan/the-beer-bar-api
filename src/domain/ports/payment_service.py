from abc import ABC, abstractmethod
from typing import Optional
from domain.entities import Payment, OrderItem, Order
from domain.ports.orders_repository.schema import UpsertRoundModel

class PaymentService(ABC):
    @abstractmethod
    def calculate_payment(self, model: list[UpsertRoundModel], discount: Optional[float] = 0) -> Payment:
        pass

    @abstractmethod
    def calculate_order_items(self, order: Order) -> list[OrderItem]:
        pass