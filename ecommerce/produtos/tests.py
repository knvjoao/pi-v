from django.test import TestCase
from produtos.models import Produto
from produtos.models.categoria import Categoria
from decimal import Decimal


class ProdutoTestCase(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nome = 'Roupas')
        self.produto = Produto.objects.create(nome = 'Blusa', preco = Decimal('100.00'), categoria = categoria)

    def test_preco_maior_que_zero(self):
        self.assertGreater(self.produto.preco, 0, 'Preço deve ser positivo')

    def test_preco_com_desconto(self):
        self.produto.discount = 10 
        self.produto.save()
        preco_com_desconto = self.produto.discounted_price()
        self.assertEqual(preco_com_desconto, Decimal('90.00'), 'Erro no cálculo do preço com desconto')

    def test_preco_com_desconto_sem_desconto(self):
        self.produto.discount = 0 
        self.produto.save()
        preco_com_desconto = self.produto.discounted_price()
        self.assertEqual(preco_com_desconto, Decimal('100.00'), 'O preço com desconto deveria ser o preço original')