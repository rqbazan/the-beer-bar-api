from domain.ports.orders_repository import OrdersRepository
from .schema import GetAllOrdersResponse

class GetAllOrdersUseCase():
    def __init__(self, orders_repository: OrdersRepository):
        self.orders_repository = orders_repository

    async def execute(self):
        orders = await self.orders_repository.getAll()
        return GetAllOrdersResponse(orders=orders)