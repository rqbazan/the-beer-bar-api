from typing import Optional
from domain.ports.order_presenter import OrderPresenter
from domain.ports.order_presenter.schema import *
from domain.entities import Order, Payment, OrderItem, Round, RoundItem


def format_price(price: float) -> str:
    return f"{price:.2f}"


def format_payment(payment: Optional[Payment]) -> PaymentResponse:
    if payment is None:
        return PaymentResponse(
            total="0.00", subtotal="0.00", taxes="0.00", discounts="0.00"
        )

    return PaymentResponse(
        total=format_price(payment.total),
        subtotal=format_price(payment.subtotal),
        taxes=format_price(payment.taxes),
        discounts=format_price(payment.discounts),
    )


def format_order_item(item: OrderItem) -> OrderItemResponse:
    return OrderItemResponse(
        product_id=item.product_id,
        price_per_unit=format_price(item.price_per_unit),
        total=format_price(item.total),
    )


def format_round_item(item: RoundItem) -> RoundItemResponse:
    return RoundItemResponse(
        product_id=item.product_id,
        price_per_unit=format_price(item.price_per_unit),
        quantity=item.quantity,
    )


def format_round(round: Round) -> RoundResponse:
    return RoundResponse(id=round.id, items=list(map(format_round_item, round.items)))


class SimpleOrderPresenter(OrderPresenter):
    def present(self, order: Order) -> OrderResponse:
        return OrderResponse(
            id=order.id,
            code=order.code,
            created_at=str(order.created_at),
            updated_at=str(order.updated_at),
            status=str(order.status),
            payment=format_payment(order.payment),
            items=list(map(format_order_item, order.items)),
            rounds=list(map(format_round, order.rounds)),
        )
