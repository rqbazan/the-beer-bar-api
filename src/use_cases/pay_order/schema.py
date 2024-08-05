from typing import Optional
from pydantic import BaseModel

class PayOrderRequest(BaseModel):
  discount: Optional[float] = 0.0