from uuid import UUID
from typing import Annotated
from fastapi import APIRouter, Depends, status, FastAPI, Request
from use_cases.get_orders.interactor import GetAllOrdersUseCase
from use_cases.create_order.interactor import CreateOrderUseCase
from use_cases.update_order.interactor import UpdateOrderUseCase
from use_cases.get_order.interactor import GetOrderByIdUseCase
from use_cases.pay_order.interactor import PayOrderUseCase
from use_cases.create_order.schema import CreateOrderRequest
from use_cases.update_order.schema import UpdateOrderRequest
from use_cases.pay_order.schema import PayOrderRequest
from use_cases.pay_order.errors import AlreadyPaidOrderError
from domain.ports.orders_repository.errors import NotFoundOrderError
from app.helpers.errors import format_error_response
from app.dependencies import (
    get_all_orders_use_case,
    get_create_order_use_case,
    get_update_order_use_case,
    get_order_by_id_use_case,
    get_pay_order_use_case,
)

router = APIRouter(prefix="/v1/orders")


@router.get("/")
async def get_orders(
    all_orders_use_case: Annotated[
        GetAllOrdersUseCase, Depends(get_all_orders_use_case)
    ]
):
    return await all_orders_use_case.execute()


@router.get("/{order_id}")
async def get_order_by_id(
    order_id: UUID,
    order_by_id_use_case: Annotated[
        GetOrderByIdUseCase, Depends(get_order_by_id_use_case)
    ],
):
    return await order_by_id_use_case.execute(order_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(
    data: CreateOrderRequest,
    create_order_use_case: Annotated[
        CreateOrderUseCase, Depends(get_create_order_use_case)
    ],
):
    return await create_order_use_case.execute(data)


@router.put("/{order_id}")
async def update_order(
    order_id: UUID,
    data: UpdateOrderRequest,
    update_order_use_case: Annotated[
        UpdateOrderUseCase, Depends(get_update_order_use_case)
    ],
):
    return await update_order_use_case.execute(order_id, data)


@router.put("/{order_id}/pay", status_code=status.HTTP_204_NO_CONTENT)
async def pay_order(
    order_id: UUID,
    data: PayOrderRequest,
    pay_order_use_case: Annotated[PayOrderUseCase, Depends(get_pay_order_use_case)],
):
    return await pay_order_use_case.execute(order_id, data)


def add_errors_handlers(app: FastAPI):
    @app.exception_handler(NotFoundOrderError)
    async def handle_order_not_found_error(_: Request, error: NotFoundOrderError):
        return format_error_response(error, status.HTTP_404_NOT_FOUND)

    @app.exception_handler(AlreadyPaidOrderError)
    async def handle_already_paid_order_error(_: Request, error: AlreadyPaidOrderError):
        return format_error_response(error, status.HTTP_400_BAD_REQUEST)

    return app
