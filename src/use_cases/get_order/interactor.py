from uuid import UUID
from domain.entities import Order
from domain.ports.orders_repository import OrdersRepository
from domain.ports.order_presenter import OrderPresenter

class GetOrderByIdUseCase:
    def __init__(self, orders_repository: OrdersRepository, order_presenter: OrderPresenter):
        self.orders_repository = orders_repository
        self.order_presenter = order_presenter

    async def execute(self, order_id: UUID) -> Order:
        order = await self.orders_repository.getById(order_id)
        return self.order_presenter.present(order)