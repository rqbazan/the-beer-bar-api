from uuid import UUID
from domain.entities import Order
from domain.ports.orders_repository import OrdersRepository

class GetOrderByIdUseCase:
    def __init__(self, orders_repository: OrdersRepository):
        self.orders_repository = orders_repository

    async def execute(self, order_id: UUID) -> Order:
        return await self.orders_repository.getById(order_id)