from django.test import TestCase

# Create your tests here.

def add_num(num):
    return num + 1

class SimplesTestCase(TestCase):

    # Roda toda vez
    def setUp(self):
        print('Iniciando TestCase')
        self.numero = 41

    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 42)