from uuid import UUID

class OrderNotFoundError(Exception):
  def __init__(self, order_id: UUID) -> None:
    super().__init__(f'Order with id <{order_id}> not found')