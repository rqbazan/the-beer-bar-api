import json
from uuid import UUID
from datetime import datetime
import functools
from typing import Annotated
from fastapi import Depends
from use_cases.get_all_inventory.interactor import GetAllInventoryUseCase
from use_cases.search_inventory.interactor import SearchInventoryUseCase
from use_cases.update_inventory.interactor import UpdateInventoryUseCase
from use_cases.get_orders.interactor import GetAllOrdersUseCase
from use_cases.create_order.interactor import CreateOrderUseCase
from use_cases.update_order.interactor import UpdateOrderUseCase
from use_cases.get_order.interactor import GetOrderByIdUseCase
from adapters.in_memory_inventory_repository import InMemoryInventoryRepository
from adapters.in_memory_orders_repository import InMemoryOrdersRepository
from adapters.simple_payment_service import SimplePaymentService
from adapters.simple_order_presenter import SimpleOrderPresenter
from domain.ports.inventory_repository import InventoryRepository
from domain.ports.orders_repository import OrdersRepository
from domain.ports.payment_service import PaymentService
from domain.ports.order_presenter import OrderPresenter
from domain.entities import Inventory, InventoryItem, Order, Payment, OrderItem, Round, RoundItem
from domain.objects import OrderStatus

@functools.cache
def get_inventory_repository() -> InventoryRepository:
    with open('data/inventory.json') as json_file:
        mapper = lambda item: InventoryItem(**item)
        json_data = json.load(json_file)

        initial_inventory = Inventory(
            updated_at=json_data.get('updated_at'),
            beers=list(map(mapper, json_data.get('beers')))
        )
    
        return InMemoryInventoryRepository(initial_inventory)

@functools.cache
def get_orders_repository() -> OrdersRepository:
    def make_order(item):
        make_item = lambda x: OrderItem(**x)

        make_round_item = lambda x: RoundItem(
            product_id=UUID(x.get('product_id')),
            price_per_unit=x.get('price_per_unit'),
            quantity=x.get('quantity')
        )
        
        make_round = lambda x: Round(
            items=list(map(make_round_item, x.get('items'))),
            id=UUID(x.get('id'))
        )

        return Order(
            id=UUID(item.get('id')),
            code=item.get('code'),
            created_at=datetime.fromisoformat(item.get('created_at')),
            updated_at=datetime.fromisoformat(item.get('updated_at')),
            status=OrderStatus(item.get('status')),
            items=list(map(make_item, item.get('items'))),
            rounds=list(map(make_round, item.get('rounds'))),
            payment=Payment(
                total=item.get('payment').get('total'),
                subtotal=item.get('payment').get('subtotal'),
                taxes=item.get('payment').get('taxes'),
                discounts=item.get('payment').get('discounts')
            )
        )

    with open('data/orders.json') as json_file:
        json_data = json.load(json_file)
        initial_orders = list(map(make_order, json_data.get('orders')))
        
        return InMemoryOrdersRepository(initial_orders)

def get_search_inventory_use_case(inventory_repository: Annotated[InventoryRepository, Depends(get_inventory_repository)]) -> SearchInventoryUseCase:
    return SearchInventoryUseCase(inventory_repository)

def get_all_inventory_use_case(inventory_repository: Annotated[InventoryRepository, Depends(get_inventory_repository)]) -> GetAllInventoryUseCase:
    return GetAllInventoryUseCase(inventory_repository)

def get_update_inventory_use_case(inventory_repository: Annotated[InventoryRepository, Depends(get_inventory_repository)]) -> UpdateInventoryUseCase:
    return UpdateInventoryUseCase(inventory_repository)

def get_payment_service() -> PaymentService:
    return SimplePaymentService()

def get_order_presenter() -> OrderPresenter:
    return SimpleOrderPresenter()

def get_all_orders_use_case(
        orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)],
        order_presenter: Annotated[OrderPresenter, Depends(get_order_presenter)]) -> GetAllOrdersUseCase: 
    return GetAllOrdersUseCase(orders_repository, order_presenter)

def get_order_by_id_use_case(
        orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)],
        order_presenter: Annotated[OrderPresenter, Depends(get_order_presenter)]) -> GetOrderByIdUseCase:
    return GetOrderByIdUseCase(orders_repository, order_presenter)

def get_create_order_use_case(
        orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)],
        payment_service: Annotated[PaymentService, Depends(get_payment_service)],
        order_presenter: Annotated[OrderPresenter, Depends(get_order_presenter)]) -> CreateOrderUseCase:
    return CreateOrderUseCase(orders_repository, payment_service, order_presenter)

def get_update_order_use_case(
        orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)],
        payment_service: Annotated[PaymentService, Depends(get_payment_service)],
        order_presenter: Annotated[OrderPresenter, Depends(get_order_presenter)]) -> UpdateOrderUseCase:
    return UpdateOrderUseCase(orders_repository, payment_service, order_presenter)