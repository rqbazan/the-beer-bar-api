from uuid import UUID
from typing import Any, Optional
from domain.ports.inventory_repository import InventoryRepository
from domain.entities import Inventory, InventoryItem

class InMemoryInventoryRepository(InventoryRepository):
  inventory: Inventory

  def __init__(self, inventory: Inventory) -> None:
    self.inventory = inventory

  async def getAll(self) -> Inventory:
    return self.inventory
  
  async def getById(self, product_id: UUID) -> Optional[InventoryItem]:
    return next((beer for beer in self.inventory.beers if beer.id == product_id), None)
  
  async def getByIds(self, product_ids: list[UUID]) -> dict[UUID, InventoryItem]:
    items = [self.getById(id) for id in product_ids]
    return {item.id: item for item in items if item is not None}

  async def search(self, **filters: Any) -> list[InventoryItem]:
    product_name_filter = filters.get('product_name')
    search_predicate = lambda beer: product_name_filter in beer.product_name

    return list(filter(search_predicate, self.inventory.beers))
  
  async def save(self, inventory: Inventory) -> None:
    self.inventory = inventory
