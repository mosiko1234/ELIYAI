from fastapi.testclient import TestClient
from backend.document_processing.app import app
from unittest.mock import patch

client = TestClient(app)

@patch("backend.document_processing.ocr.OCRProcessor.process_image")
def test_process_document(mock_process_image):
    mock_process_image.return_value = "Extracted text from document"
    
    response = client.post("/process-document", files={"file": ("test_image.png", b"fake_image_data", "image/png")})

    assert response.status_code == 200
    assert response.json()["extracted_text"] == "Extracted text from document"
