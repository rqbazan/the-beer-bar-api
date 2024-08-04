from domain.entities import Order
from pydantic import BaseModel

class GetAllOrdersResponse(BaseModel):
    orders: list[Order]