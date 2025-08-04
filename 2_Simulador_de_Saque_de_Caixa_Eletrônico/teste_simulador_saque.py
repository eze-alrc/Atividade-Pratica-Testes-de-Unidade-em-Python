import unittest
from simulador_saque import sacar

class TestSimuladorSaque(unittest.TestCase):

    def test_saque_valido(self):
        self.assertEqual(sacar(180), {100: 1, 50: 1, 20: 1, 10: 1})
        self.assertEqual(sacar(50), {50: 1})
    
    def test_saque_zero(self):
        with self.assertRaises(ValueError):
            sacar(0)
    
    def test_saque_nao_multiplo_de_10(self):
        with self.assertRaises(ValueError):
            sacar(25)
        with self.assertRaises(ValueError):
            sacar(7)
    
    def test_saque_valor_grande(self):
        self.assertEqual(sacar(380), {100: 3, 50: 1, 20: 1, 10: 1})

if __name__ == '__main__':
    unittest.main()