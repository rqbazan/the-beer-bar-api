from domain.entities import Order, Round
from domain.ports.orders_repository.schema import UpsertRoundModel


def order_to_rounds_model(order: Order) -> list[UpsertRoundModel]:
    return list(map(lambda r: UpsertRoundModel(items=r.items), order.rounds))
