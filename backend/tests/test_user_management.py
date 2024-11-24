from fastapi.testclient import TestClient
from backend.user_management.app import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

def test_login_user():
    client.post("/register", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]
