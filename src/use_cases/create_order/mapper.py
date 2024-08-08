from domain.ports.orders_repository.schema import UpsertRoundModel
from .schema import CreateOrderRequest


def create_order_request_to_rounds_model(
    request: CreateOrderRequest,
) -> list[UpsertRoundModel]:
    return list(map(lambda r: UpsertRoundModel(r.items), request.rounds))
