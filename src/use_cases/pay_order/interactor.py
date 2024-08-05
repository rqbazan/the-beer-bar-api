from uuid import UUID
from domain.ports.orders_repository import OrdersRepository
from domain.ports.orders_repository.errors import OrderNotFoundError
from domain.ports.orders_repository.schema import UpdateOrderModel
from domain.ports.payment_service import PaymentService
from domain.objects import OrderStatus
from .schema import PayOrderRequest
from .mapper import order_to_rounds_model
from .errors import OrderAlreadyPaidError

class PayOrderUseCase:
    def __init__(self, orders_repository: OrdersRepository, payment_service: PaymentService):
        self.orders_repository = orders_repository
        self.payment_service = payment_service

    async def execute(self, order_id: UUID, request: PayOrderRequest) -> None:
      order = await self.orders_repository.getById(order_id)

      if not order:
        raise OrderNotFoundError(order_id)
      
      if order.status == OrderStatus.PAID:
        raise OrderAlreadyPaidError(order_id)
      
      rounds_model = order_to_rounds_model(order)
      payment = self.payment_service.calculate_payment(rounds_model, request.discount)
      order_items = self.payment_service.calculate_order_items(order)

      model = UpdateOrderModel(
        order_id=order.id,
        payment=payment,
        items=order_items,
        status=OrderStatus.PAID
      )

      await self.orders_repository.update(model)
