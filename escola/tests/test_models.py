from django.test import TestCase
from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    #def teste_falha(self):
    #    self.fail('teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '87829234000',
            data_nascimento= '2023-02-02',
            celular = '55 99999-9999',
        )

    def test_verifica_atributos_de_estudante(self):
        '''teste que verifica os atributos do modelo de Estudante'''
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '87829234000')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.celular, '55 99999-9999')