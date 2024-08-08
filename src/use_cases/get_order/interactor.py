from uuid import UUID
from domain.entities import Order
from domain.ports.order_presenter.schema import OrderResponse
from domain.ports.orders_repository import OrdersRepository
from domain.ports.order_presenter import OrderPresenter
from domain.ports.orders_repository.errors import NotFoundOrderError


class GetOrderByIdUseCase:
    def __init__(
        self, orders_repository: OrdersRepository, order_presenter: OrderPresenter
    ):
        self.orders_repository = orders_repository
        self.order_presenter = order_presenter

    async def execute(self, order_id: UUID) -> OrderResponse:
        order = await self.orders_repository.getById(order_id)

        if order is None:
            raise NotFoundOrderError(order_id)

        return self.order_presenter.present(order)
