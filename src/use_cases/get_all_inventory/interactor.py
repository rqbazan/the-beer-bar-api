from domain.ports.inventory_repository import InventoryRepository
from .schema import GetAllInventoryResponse


class GetAllInventoryUseCase:
    def __init__(self, inventory_repository: InventoryRepository):
        self.inventory_repository = inventory_repository

    async def execute(self) -> GetAllInventoryResponse:
        inventory = await self.inventory_repository.getAll()
        return GetAllInventoryResponse(beers=inventory.beers)
