import json
from uuid import UUID
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
from domain.ports.inventory_repository import InventoryRepository
from domain.ports.orders_repository import OrdersRepository
from domain.ports.payment_service import PaymentService
from domain.entities import Inventory, InventoryItem, Order

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
    with open('data/orders.json') as json_file:
        mapper = lambda item: Order(**item)
        json_data = json.load(json_file)

        initial_orders = list(map(mapper, json_data.get('orders')))
    
        return InMemoryOrdersRepository(initial_orders)

def get_search_inventory_use_case(inventory_repository: Annotated[InventoryRepository, Depends(get_inventory_repository)]) -> SearchInventoryUseCase:
    return SearchInventoryUseCase(inventory_repository)

def get_all_inventory_use_case(inventory_repository: Annotated[InventoryRepository, Depends(get_inventory_repository)]) -> GetAllInventoryUseCase:
    return GetAllInventoryUseCase(inventory_repository)

def get_update_inventory_use_case(inventory_repository: Annotated[InventoryRepository, Depends(get_inventory_repository)]) -> UpdateInventoryUseCase:
    return UpdateInventoryUseCase(inventory_repository)

def get_all_orders_use_case(orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)]) -> GetAllOrdersUseCase: 
    return GetAllOrdersUseCase(orders_repository)

def get_order_by_id_use_case(orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)]) -> GetOrderByIdUseCase:
    return GetOrderByIdUseCase(orders_repository)

def get_payment_service() -> PaymentService:
    return SimplePaymentService()

def get_create_order_use_case(
        orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)],
        payment_service: Annotated[PaymentService, Depends(get_payment_service)]) -> CreateOrderUseCase:
    return CreateOrderUseCase(orders_repository, payment_service)

def get_update_order_use_case(
        orders_repository: Annotated[OrdersRepository, Depends(get_orders_repository)],
        payment_service: Annotated[PaymentService, Depends(get_payment_service)]) -> UpdateOrderUseCase:
    return UpdateOrderUseCase(orders_repository, payment_service)