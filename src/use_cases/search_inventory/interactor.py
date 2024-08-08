from typing import Any
from domain.ports.inventory_repository import InventoryRepository
from .schema import SearchInventoryRequest, SearchInventoryResponse


class SearchInventoryUseCase:
    def __init__(self, inventory_repository: InventoryRepository) -> None:
        self.inventory_repository = inventory_repository

    async def execute(self, request: SearchInventoryRequest) -> SearchInventoryResponse:
        search_items = await self.inventory_repository.search(
            product_name=request.product_name
        )

        return SearchInventoryResponse(beers=search_items)
