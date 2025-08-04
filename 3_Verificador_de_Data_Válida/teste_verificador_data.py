import unittest
from verificador_data import data_valida

class TestVerificadorData(unittest.TestCase):

    def test_data_valida(self):
        self.assertTrue(data_valida(29, 2, 2020))  # ano bissexto
        self.assertTrue(data_valida(31, 1, 2023))
        self.assertTrue(data_valida(30, 4, 2023))

    def test_data_invalida_dia(self):
        self.assertFalse(data_valida(31, 4, 2023))  # abril tem 30 dias
        self.assertFalse(data_valida(32, 1, 2023))
        self.assertFalse(data_valida(29, 2, 2019))  # não bissexto

    def test_data_invalida_mes(self):
        self.assertFalse(data_valida(15, 13, 2023))  # mês inválido
        self.assertFalse(data_valida(10, 0, 2023))

if __name__ == '__main__':
    unittest.main()