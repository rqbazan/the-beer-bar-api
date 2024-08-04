from datetime import datetime
from domain.entities import Inventory
from domain.ports.inventory_repository import InventoryRepository
from .schema import UpdateInventoryRequest

class UpdateInventoryUseCase:
    def __init__(self, inventory_repository: InventoryRepository):
        self.inventory_repository = inventory_repository

    async def execute(self, request: UpdateInventoryRequest):
        new_inventory = Inventory(
            updated_at=datetime.now(),
            beers=request.beers
        )

        await self.inventory_repository.save(new_inventory)