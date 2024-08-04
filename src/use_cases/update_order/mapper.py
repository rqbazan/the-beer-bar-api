from domain.ports.orders_repository.schema import UpsertRoundModel
from .schema import UpdateOrderRequest

def update_order_request_to_rounds_model(request: UpdateOrderRequest) -> list[UpsertRoundModel]:
  return list(map(lambda r: UpsertRoundModel(r.items), request.rounds))
