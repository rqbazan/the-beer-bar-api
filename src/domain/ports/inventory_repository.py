from uuid import UUID
from abc import ABC, abstractmethod
from typing import Any, Optional
from domain.entities import Inventory, InventoryItem


class InventoryRepository(ABC):
    @abstractmethod
    async def getAll(self) -> Inventory:
        raise NotImplementedError

    @abstractmethod
    async def getById(self, product_id: UUID) -> Optional[InventoryItem]:
        raise NotImplementedError

    @abstractmethod
    async def getByIds(self, product_ids: list[UUID]) -> dict[UUID, InventoryItem]:
        raise NotImplementedError

    @abstractmethod
    async def search(self, **filters: Any) -> list[InventoryItem]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, inventory: Inventory) -> None:
        raise NotImplementedError
