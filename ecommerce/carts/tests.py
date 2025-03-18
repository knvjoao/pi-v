from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Cart, Order
from produtos.models import Produto, Categoria
from clientes.models import User
from decimal import Decimal


class CartTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('usuario@teste.com', 'senhateste')

    def test_criar_carrinho(self):
        cart = Cart.objects.create(user = self.user)
        self.assertEqual(cart.user, self.user)

    def test_relacao_carrinho_usuario(self):
        cart = Cart.objects.create(user = self.user)
        self.assertEqual(cart.user.email, 'usuario@teste.com')

    def test_carrinho_sem_usuario(self):
        with self.assertRaises(IntegrityError):
            Cart.objects.create(user = None)

class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('usuario@teste.com', 'senhateste')
        self.categoria = Categoria.objects.create(nome = 'Categoria X')
        self.produto = Produto.objects.create(nome = 'Produto Y', preco = Decimal('100.00'), categoria = self.categoria)
        self.cart = Cart.objects.create(user = self.user)

    def test_ordem_sem_carrinho(self):
        with self.assertRaises(IntegrityError):
            Order.objects.create(cart = None, product = self.produto, quantity = 2)
    
    def test_ordem_sem_produto(self):
        with self.assertRaises(IntegrityError):
            Order.objects.create(cart = self.cart, product = None, quantity = 2)

    def test_ordem_quantidade_negativa(self):
        order = Order.objects.create(cart = self.cart, product = self.produto, quantity = -1)
        self.assertEqual(order.quantity, -1)