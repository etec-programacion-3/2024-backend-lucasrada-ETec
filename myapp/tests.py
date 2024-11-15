from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, User, OrderDetails, OrderItems  
# Asegúrate de que todos los modelos estén importados

class OrderIntegrationTest(APITestCase):
    def setUp(self):
        # Crear productos
        self.product1 = Product.objects.create(
            name="Test Product 1",
            desc="Product description 1",
            price=100,
            category=1
        )
        self.product2 = Product.objects.create(
            name="Test Product 2",
            desc="Product description 2",
            price=200,
            category=2
        )

###ESTO ESTA MAL REVISAR#####
class OrderIntegrationTest(APITestCase):
    def setUp(self):
        # Crear usuario
        self.user = User.objects.create(
            username='testuser',
            password='password123',  # Utilizar create_user para encriptar la contraseña
            full_name='Test User',
            phone='123456789',
            full_address='123 Test Address'
        )
        # Crear productos
        self.product1 = Product.objects.create(
            name="Test Product 1",
            desc="Product description 1",
            price=100,
            category=1
        )
        self.product2 = Product.objects.create(
            name="Test Product 2",
            desc="Product description 2",
            price=200,
            category=2
        )

    def test_create_order_with_items(self):
        # Crear una orden
        order_data = {
            'total': 300,  # Total de la orden
            'user': self.user.id  # El ID del usuario que realiza la compra
        }
        response = self.client.post('/orders/', order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order_id = response.data['id']  # Obtener el ID de la orden creada
        