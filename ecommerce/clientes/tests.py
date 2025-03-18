from django.test import TestCase
from clientes.models.user import User, MyUserManager


class UserModelTestCase(TestCase):
    
    def test_usuario_sem_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email = '', password = 'password')

    def test_usuario_sem_senha(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email = 'usuario@teste.com', password = '')