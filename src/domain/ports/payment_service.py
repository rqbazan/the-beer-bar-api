from abc import ABC, abstractmethod
from typing import Optional
from domain.entities import Payment
from domain.ports.orders_repository.schema import UpsertRoundModel

class PaymentService(ABC):
    @abstractmethod
    def calculate_payment(self, rounds: list[UpsertRoundModel], discount: Optional[float] = 0) -> Payment:
        pass