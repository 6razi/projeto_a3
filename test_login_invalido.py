
import unittest
import sqlite3
from simulador_financeiro import init_db, create_user, authenticate_user

class TestLoginInvalido(unittest.TestCase):
    def setUp(self):
        # Cria um banco de dados em memória para testes
        self.conn = sqlite3.connect(':memory:')
        init_db(self.conn)  # Inicializa a estrutura do banco de dados
        create_user(self.conn, 'usuario_teste', 'senha123')

    def tearDown(self):
        self.conn.close()

    def test_login_incorreto(self):
        """Testa se o login falha com credenciais incorretas."""
        resultado = authenticate_user(self.conn, 'usuario_teste', 'senha_errada')
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
