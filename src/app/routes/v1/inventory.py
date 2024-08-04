from typing import Annotated
from fastapi import APIRouter, Depends, status
from use_cases.search_inventory.schema import SearchInventoryRequest
from use_cases.get_all_inventory.interactor import GetAllInventoryUseCase
from use_cases.search_inventory.interactor import SearchInventoryUseCase
from use_cases.update_inventory.interactor import UpdateInventoryUseCase
from use_cases.update_inventory.schema import UpdateInventoryRequest
from app.dependencies import get_search_inventory_use_case, get_all_inventory_use_case, get_update_inventory_use_case

router = APIRouter(prefix="/v1/inventory")

@router.get("/")
async def search_inventory(all_inventory_use_case: Annotated[GetAllInventoryUseCase, Depends(get_all_inventory_use_case)]):
  return await all_inventory_use_case.execute()

@router.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_inventory(data: UpdateInventoryRequest, update_inventory_use_case: Annotated[UpdateInventoryUseCase, Depends(get_update_inventory_use_case)]):
  await update_inventory_use_case.execute(data)

@router.get("/search")
async def search_inventory(q: str, search_inventory_use_case: Annotated[SearchInventoryUseCase, Depends(get_search_inventory_use_case)]):
  request = SearchInventoryRequest(product_name=q)
  return  await search_inventory_use_case.execute(request)
