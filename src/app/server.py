from fastapi import FastAPI
from app.routes.v1 import inventory, orders

def create_server():
  app = FastAPI()

  app.include_router(inventory.router)
  app.include_router(orders.router)

  orders.add_errors_handlers(app)

  return app