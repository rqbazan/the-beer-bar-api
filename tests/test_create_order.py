from fastapi.testclient import TestClient
from app.server import create_server

app = create_server()
client = TestClient(app)

def test_create_order():
    create_order_body = {
        "rounds": [
            {
                "items": [
                    {"product_id": "c5ebf5b6-97f9-4b62-821d-4be52286388b", "price_per_unit": 10, "quantity": 5},
                ]
            }
        ]
    }

    response = client.post("/v1/orders", json=create_order_body)
    assert response.status_code == 201
    
    created_json = response.json()

    response = client.get(f"/v1/orders/{created_json.get("id")}")
    assert response.status_code == 200