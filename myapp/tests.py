from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import MiModelo

class MiModeloTests(TestCase):

    def setUp(self):
        # Este método se ejecuta antes de cada prueba
        MiModelo.objects.create(nombre='Prueba', valor=10)

    def test_mi_modelo_creado_correctamente(self):
        # Verifica que el objeto se haya creado correctamente
        objeto = MiModelo.objects.get(nombre='Prueba')
        self.assertEqual(objeto.valor, 10)

    def test_mi_modelo_string(self):
        objeto = MiModelo.objects.get(nombre='Prueba')
        self.assertEqual(str(objeto), 'Prueba')
