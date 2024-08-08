from typing import Optional
from uuid import UUID
from domain.entities import Payment, Round, OrderItem
from domain.ports.orders_repository.schema import UpsertRoundModel
from domain.ports.payment_service import PaymentService


class SimplePaymentService(PaymentService):
    __TAXES_PERCENT = 0.18

    def __make_order_item(self, product_id: UUID, data: dict) -> OrderItem:
        price_per_unit = float(data.get("price_per_unit") or 0)
        quantity = int(data.get("quantity") or 0)

        return OrderItem(
            product_id=product_id,
            price_per_unit=price_per_unit,
            total=price_per_unit * quantity,
        )

    def calculate_payment(
        self, rounds: list[UpsertRoundModel], discounts: float = 0
    ) -> Payment:
        total, subtotal = 0, 0

        for round in rounds:
            for item in round.items:
                price_without_taxes = item.price_per_unit / (
                    1 + SimplePaymentService.__TAXES_PERCENT
                )
                subtotal += price_without_taxes * item.quantity
                total += item.price_per_unit * item.quantity

        taxes = total - subtotal
        total -= discounts

        return Payment(total=total, subtotal=subtotal, taxes=taxes, discounts=discounts)

    def calculate_order_items(self, rounds: list[UpsertRoundModel]) -> list[OrderItem]:
        store: dict[UUID, dict] = {}

        for round in rounds:
            for item in round.items:
                store[item.product_id] = {
                    "price_per_unit": item.price_per_unit,
                    "quantity": store.get(item.product_id, {}).get("quantity", 0)
                    + item.quantity,
                }

        return [self.__make_order_item(key, value) for key, value in store.items()]
