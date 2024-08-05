from uuid import UUID

class OrderAlreadyPaidError(Exception):
    def __init__(self, order_id: UUID) -> None:
        super().__init__(f"Order {order_id} is already paid")