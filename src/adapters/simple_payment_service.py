from typing import Optional
from uuid import UUID
from domain.entities import Payment, Order, OrderItem
from domain.ports.orders_repository.schema import UpsertRoundModel
from domain.ports.payment_service import PaymentService

class SimplePaymentService(PaymentService):
  __TAXES = 0.18

  def __make_order_item(self, product_id: UUID, data: dict) -> OrderItem:
    return OrderItem(
      product_id=product_id,
      price_per_unit=data.get('price_per_unit'),
      total=data.get('price_per_unit') * data.get('quantity')
    )

  def calculate_payment(self, model: list[UpsertRoundModel], discount: Optional[float] = 0) -> Payment:
    total, subtotal = 0, 0

    for round in model:
      for item in round.items:
        price_without_taxes = item.price_per_unit / (1 + SimplePaymentService.__TAXES)
        subtotal += price_without_taxes * item.quantity
        total += item.price_per_unit * item.quantity

    taxes = total - subtotal
    total -= discount

    return Payment(
      total=total,
      subtotal=subtotal,
      taxes=taxes,
      discounts=discount
    )
  
  def calculate_order_items(self, order: Order) -> list[OrderItem]:
    store: dict[UUID, dict] = {}

    for round in order.rounds:
      for item in round.items:
        store[item.product_id] = {
          'price_per_unit': item.price_per_unit,
          'quantity': store.get(item.product_id, {}).get('quantity', 0) + item.quantity
        }

    return [self.__make_order_item(key, value) for key, value in store.items()]