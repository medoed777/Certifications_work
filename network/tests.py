from rest_framework import status
from rest_framework.test import APITestCase

from .models import NetworkNode, Supplier


class SupplierViewSetTest(APITestCase):
    def setUp(self):
        self.supplier_data = {
            "name": "New Supplier",
            "email": "new_supplier@example.com",
            "country": "Country",
            "city": "City",
            "street": "Street",
            "house_number": "1",
        }

    def test_create_supplier(self):
        response = self.client.post("/api/suppliers/", self.supplier_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)


class NetworkNodeViewSetTest(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(
            name="Existing Supplier",
            email="existing_supplier@example.com",
            country="Country",
            city="City",
            street="Street",
            house_number="1",
        )
        self.network_node_data = {
            "name": "New Node",
            "email": "new_node@example.com",
            "country": "Country",
            "city": "City",
            "street": "Street",
            "house_number": "1",
            "product_name": "Product A",
            "product_model": "Model A",
            "product_release_date": "2023-01-01",
            "supplier": self.supplier.id,
            "debt_to_supplier": 50.00,
            "level": 1,
        }

    def test_create_network_node(self):
        response = self.client.post("/api/network-nodes/", self.network_node_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NetworkNode.objects.count(), 1)

    def test_create_network_node_with_invalid_level(self):
        invalid_data = self.network_node_data.copy()
        invalid_data["level"] = 0  # Уровень завода не может иметь поставщика
        response = self.client.post("/api/network-nodes/", invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
