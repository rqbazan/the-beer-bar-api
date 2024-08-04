from domain.entities import InventoryItem
from pydantic import BaseModel

class GetAllInventoryResponse(BaseModel):
    beers: list[InventoryItem]