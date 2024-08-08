from pydantic import BaseModel


class PayOrderRequest(BaseModel):
    discounts: float = 0.0
