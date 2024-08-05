from pydantic import BaseModel
from domain.ports.order_presenter.schema import OrderResponse

class GetAllOrdersResponse(BaseModel):
    orders: list[OrderResponse]