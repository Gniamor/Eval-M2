# test_app.py
import pytest
from fastapi.testclient import TestClient
from app import app  # Make sure this imports your FastAPI app

client = TestClient(app)

def test_read_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
