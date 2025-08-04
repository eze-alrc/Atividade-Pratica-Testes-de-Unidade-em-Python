import unittest
from validador_cpf import validar_cpf

class TestValidadorCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("52998224725"))
    
    def test_cpf_invalido_tamanho(self):
        self.assertFalse(validar_cpf("123"))
        self.assertFalse(validar_cpf("5299822472"))  # 10 dígitos
    
    def test_cpf_invalido_digitos_repetidos(self):
        self.assertFalse(validar_cpf("111.111.111-11"))
        self.assertFalse(validar_cpf("00000000000"))
    
    def test_cpf_invalido_digito_verificador(self):
        self.assertFalse(validar_cpf("529.982.247-26"))  # último dígito errado

if __name__ == '__main__':
    unittest.main()
