from fastapi.testclient import TestClient
from backend.ai_document_generation.app import app
from unittest.mock import patch

client = TestClient(app)

@patch("backend.ai_document_generation.openai_client.OpenAIClient.generate_document")
def test_generate_document(mock_generate_document):
    mock_generate_document.return_value = "Generated legal document content"

    response = client.post("/generate-document", json={"prompt": "Create a contract for lease agreement"})
    
    assert response.status_code == 200
    assert response.json()["document"] == "Generated legal document content"
