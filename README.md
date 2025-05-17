import unittest
import sqlite3

def create_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (username, password) VALUES (?, ?)",
        (username, password)
    )
    conn.commit()

def authenticate_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM usuarios WHERE username = ? AND password = ?",
        (username, password)
    )
    return cursor.fetchone() is not None

class TestUsuarioIntegracao(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.init_db_with_connection(self.conn)

    def tearDown(self):
        self.conn.close()

    def init_db_with_connection(self, conn):
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )''')
        conn.commit()

    def test_criar_e_autenticar_usuario(self):
        username = "usuario_teste"
        password = "senha_segura"

        create_user(self.conn, username, password)

        self.assertTrue(authenticate_user(self.conn, username, password))
        self.assertFalse(authenticate_user(self.conn, username, "senha_errada"))

unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestUsuarioIntegracao))





