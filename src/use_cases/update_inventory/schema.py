from pydantic import BaseModel
from domain.entities import InventoryItem


class UpdateInventoryRequest(BaseModel):
    beers: list[InventoryItem]
