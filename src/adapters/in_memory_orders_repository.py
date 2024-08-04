from uuid import UUID, uuid4
from typing import Optional, Any
from datetime import datetime
from domain.ports.orders_repository import OrdersRepository
from domain.ports.orders_repository.schema import CreateOrderModel, UpdateOrderModel
from domain.ports.orders_repository.errors import OrderNotFoundError
from domain.entities import Order, Round
from domain.objects import OrderStatus

make_round = lambda r: Round(id=uuid4(), items=r.items)

class InMemoryOrdersRepository(OrdersRepository):
  orders: list[Order]

  def __init__(self, orders: list[Order]) -> None:
    self.orders = orders

  async def getAll(self) -> list[Order]:
    return self.orders

  async def getById(self, order_id: UUID) -> Optional[Order]:
    return next((order for order in self.orders if str(order.id) == str(order_id)), None)
  
  async def search(self, **filters: Any) -> list[Order]:
    order_code = filters.get('order_code')
    search_predicate = lambda order: order_code in order.code

    return list(filter(search_predicate, self.orders))

  async def create(self, model: CreateOrderModel) -> None:
    next_code = str(len(self.orders) + 1).rjust(6, '0')
    created_at = datetime.now()

    order = Order(
      id=uuid4(),
      code=next_code,
      created_at=created_at,
      updated_at=created_at,
      status=OrderStatus.NOT_PAID,
      payment=model.payment,
      items=[],
      rounds=list(map(make_round, model.rounds))
    )

    self.orders.append(order)

    return order

  async def update(self, model: UpdateOrderModel) -> None:
    order_to_update = await self.getById(model.order_id)

    if order_to_update is None:
      raise OrderNotFoundError(model.id)
  
    order_to_update.updated_at = datetime.now()
    order_to_update.payment = model.payment
    order_to_update.rounds = list(map(make_round, model.rounds))

    return order_to_update
