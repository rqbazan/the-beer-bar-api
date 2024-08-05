from abc import ABC, abstractmethod
from domain.entities import Order
from .schema import OrderResponse

class OrderPresenter(ABC):
    @abstractmethod
    def present(self, order: Order) -> OrderResponse:
        raise NotImplementedError