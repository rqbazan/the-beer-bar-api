from pydantic import BaseModel
from domain.entities import InventoryItem


class SearchInventoryRequest(BaseModel):
    product_name: str


class SearchInventoryResponse(BaseModel):
    beers: list[InventoryItem]
