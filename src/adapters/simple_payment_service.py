from typing import Optional
from domain.entities import Payment
from domain.ports.orders_repository.schema import UpsertRoundModel
from domain.ports.payment_service import PaymentService

class SimplePaymentService(PaymentService):
  __TAXES = 0.18

  def calculate_payment(self, rounds: list[UpsertRoundModel], discount: Optional[float] = 0) -> Payment:
    total, subtotal = 0, 0

    for round in rounds:
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