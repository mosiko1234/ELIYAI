from fastapi.testclient import TestClient
from backend.client_management.app import app

client = TestClient(app)

def test_create_client():
    response = client.post("/clients", json={
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890",
        "cases": ["Case 1", "Case 2"]
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Client created successfully"
