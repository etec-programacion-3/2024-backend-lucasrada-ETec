from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, User, OrderDetails, OrderItems  
# Asegúrate de que todos los modelos estén importados

class OrderIntegrationTest(APITestCase):
    def setUp(self):
        # Crear productos
        self.product1 = Product.objects.create(
            name="Test Product 1",
            descri="Product description 1",
            price=100,
            category=1
        )
        self.product2 = Product.objects.create(
            name="Test Product 2",
            descri="Product description 2",
            price=200,
            category=2
        )

