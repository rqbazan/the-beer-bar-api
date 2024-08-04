from uuid import UUID
from domain.ports.orders_repository import OrdersRepository
from domain.ports.orders_repository.errors import OrderNotFoundError
from domain.ports.orders_repository.schema import UpdateOrderModel
from domain.ports.payment_service import PaymentService
from .schema import UpdateOrderRequest
from .mapper import update_order_request_to_rounds_model

class UpdateOrderUseCase:
  def __init__(self, orders_repository: OrdersRepository, payment_service: PaymentService):
    self.orders_repository = orders_repository
    self.payment_service = payment_service

  async def execute(self, order_id: UUID, request: UpdateOrderRequest):
    order = await self.orders_repository.getById(order_id)

    if not order:
      raise OrderNotFoundError(order_id)
      
    rounds_model = update_order_request_to_rounds_model(request)
    payment = self.payment_service.calculate_payment(rounds_model, request.discount)
    model = UpdateOrderModel(
      order_id=order.id,
      rounds=rounds_model,
      payment=payment
    )

    return await self.orders_repository.update(model)