from uuid import UUID
from abc import ABC, abstractmethod
from typing import Any, Optional
from domain.entities import Order
from .schema import CreateOrderModel, UpdateOrderModel


class OrdersRepository(ABC):
    @abstractmethod
    async def getAll(self) -> list[Order]:
        raise NotImplementedError

    @abstractmethod
    async def getById(self, order_id: UUID) -> Optional[Order]:
        raise NotImplementedError

    @abstractmethod
    async def search(self, **filters: Any) -> list[Order]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, model: CreateOrderModel) -> Order:
        raise NotImplementedError

    @abstractmethod
    async def update(self, model: UpdateOrderModel) -> Order:
        raise NotImplementedError
