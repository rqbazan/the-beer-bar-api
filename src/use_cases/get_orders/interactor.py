from domain.ports.orders_repository import OrdersRepository
from domain.ports.order_presenter import OrderPresenter
from .schema import GetAllOrdersResponse

class GetAllOrdersUseCase():
    def __init__(self, orders_repository: OrdersRepository, order_presenter: OrderPresenter):
        self.orders_repository = orders_repository
        self.order_presenter = order_presenter

    async def execute(self):
        orders = await self.orders_repository.getAll()
        decorated_orders = [self.order_presenter.present(order) for order in orders]

        return GetAllOrdersResponse(
            orders=decorated_orders
        )