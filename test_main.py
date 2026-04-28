from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_sum():
    response = client.get("/sum?a=2&b=3")
    assert response.json() == {"result": 5}

def test_sum_negative():
    response = client.get("/sum?a=-1&b=-2")
    assert response.json() == {"result": -3}

def test_multiply():
    response = client.get("/multiply?a=2&b=3")
    assert response.json() == {"result": 6}

def test_multiply_zero():
    response = client.get("/multiply?a=5&b=0")
    assert response.json() == {"result": 0}