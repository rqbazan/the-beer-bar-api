from domain.ports.orders_repository import OrdersRepository
from domain.ports.payment_service import PaymentService
from domain.ports.orders_repository.schema import CreateOrderModel
from .schema import CreateOrderRequest
from .mapper import create_order_request_to_rounds_model

class CreateOrderUseCase:
  def __init__(self, orders_repository: OrdersRepository, payment_service: PaymentService):
    self.orders_repository = orders_repository
    self.payment_service = payment_service

  async def execute(self, request: CreateOrderRequest):
    rounds_model = create_order_request_to_rounds_model(request)
    payment = self.payment_service.calculate_payment(rounds_model, request.discount)
    model = CreateOrderModel(rounds=rounds_model, payment=payment)

    return await self.orders_repository.create(model)