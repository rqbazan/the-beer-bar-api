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
                    RoundItem(
                        product_id=uuid4(), price_per_unit=price_per_unit_a, quantity=2
                    ),
                    RoundItem(
                        product_id=uuid4(), price_per_unit=price_per_unit_b, quantity=3
                    ),
                ]
            )
        ],
    )

    assert (
        f"{payment.total:.2f}" == "94.40"
    )  # price_per_unit_a * 2 + price_per_unit_b * 3
    assert f"{payment.subtotal:.2f}" == "80.00"  # price_base_a * 2 + price_base_b * 3


def test_orders_items_calculation(payment_service: PaymentService):
    product_id_a, product_id_b = uuid4(), uuid4()
    price_per_unit_a, price_per_unit_b = 12, 20.5

    items = payment_service.calculate_order_items(
        rounds=[
            UpsertRoundModel(
                items=[
                    RoundItem(
                        product_id=product_id_a,
                        price_per_unit=price_per_unit_a,
                        quantity=1,
                    ),
                    RoundItem(
                        product_id=product_id_b,
                        price_per_unit=price_per_unit_b,
                        quantity=2,
                    ),
                ]
            ),
            UpsertRoundModel(
                items=[
                    RoundItem(
                        product_id=product_id_a,
                        price_per_unit=price_per_unit_a,
                        quantity=3,
                    ),
                ]
            ),
            UpsertRoundModel(
                items=[
                    RoundItem(
                        product_id=product_id_b,
                        price_per_unit=price_per_unit_b,
                        quantity=3,
                    ),
                ]
            ),
        ],
    )

    order_item_a = next(filter(lambda item: item.product_id == product_id_a, items))
    order_item_b = next(filter(lambda item: item.product_id == product_id_b, items))

    assert len(items) == 2
    assert order_item_a.total == 12 * 4
    assert order_item_b.total == 20.5 * 5
