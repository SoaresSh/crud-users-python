import unittest
import os
import usuarios 

class TestUsuarios(unittest.TestCase):

    def setUp(self):
        usuarios.usuarios.clear()
        if os.path.exists('usuarios.json'):
            os.remove('usuarios.json')

    def tearDown(self):
        if os.path.exists('usuarios.json'):
            os.remove('usuarios.json')

    def test_criar_usuario_com_dados_validos(self):
        user = usuarios.criar_usuario("Guilherme", "gui@email.com", "senha", "11122233344")
        self.assertEqual(user['nome'], "Guilherme")
        self.assertEqual(len(usuarios.usuarios), 1)

    def test_listar_usuarios(self):
        usuarios.criar_usuario("Pedro", "pedro@email.com", "123", "22233344455")
        usuarios.criar_usuario("Vinicius", "vinicius@email.com", "456", "33344455566")
        lista = usuarios.listar_usuarios()
        self.assertEqual(len(lista), 2)

    def test_buscar_usuario_por_cpf(self):
        usuarios.criar_usuario("Daniel", "daniel@email.com", "senha", "44455566677")
        usuario = usuarios.buscar_usuario("44455566677")
        self.assertEqual(usuario['nome'], "Daniel")

    def test_deletar_usuario_existente(self):
        usuarios.criar_usuario("Bada", "bada@email.com", "senha", "55566677788")
        resultado = usuarios.deletar_usuario("55566677788")
        self.assertTrue(resultado)
        self.assertEqual(len(usuarios.usuarios), 0)

    def test_buscar_usuario_cpf_nao_encontrado(self):
        with self.assertRaises(ValueError) as e:
            usuarios.buscar_usuario("00000000000")
        self.assertEqual(str(e.exception), "Usuário não encontrado.")

    def test_deletar_usuario_cpf_nao_encontrado(self):
        with self.assertRaises(ValueError) as e:
            usuarios.deletar_usuario("00000000000")
        self.assertEqual(str(e.exception), "Usuário não encontrado.")

if __name__ == '__main__':
    unittest.main()
