import pytest
from uuid import uuid4
from domain.ports.payment_service import PaymentService
from domain.ports.orders_repository.schema import UpsertRoundModel
from domain.entities import RoundItem
from adapters.simple_payment_service import SimplePaymentService

TAXES = 0.18

@pytest.fixture
def payment_service() -> PaymentService:
    return SimplePaymentService()

def test_payment_calculation(payment_service: PaymentService):
  price_base_a, price_base_b = 10, 20
  price_per_unit_a = price_base_a + (price_base_a * TAXES)
  price_per_unit_b = price_base_b + (price_base_b * TAXES)

  payment = payment_service.calculate_payment(
    rounds=[
      UpsertRoundModel(
         items=[
            RoundItem(product_id=uuid4(), price_per_unit=price_per_unit_a, quantity=2),
            RoundItem(product_id=uuid4(), price_per_unit=price_per_unit_b, quantity=3),
         ]
      )
    ],
  )

  assert f"{payment.total:.2f}" == '94.40' # price_per_unit_a * 2 + price_per_unit_b * 3
  assert f"{payment.subtotal:.2f}" == '80.00' # price_base_a * 2 + price_base_b * 3