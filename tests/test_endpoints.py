import unittest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

class TestEndpoints(unittest.TestCase):
    def test_list_products(self):
        response = client.get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

def test_create_product():
    product_data = {
        "name": "New Product",
        "description": "New Product Description",
        "data_pub": "2023-08-12",
        "price_product": 200,
        "quantity": 20
    }
    response = client.post("/products", json=product_data)
    assert response.status_code == 201
    assert "name" in response.json()

def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_product_details():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_get_nonexistent_product():
    response = client.get("/products/999")
    assert response

if __name__ == "__main__":
    unittest.main()