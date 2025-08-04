import unittest
from classificador import classificar_aluno

class TestClassificarAluno(unittest.TestCase):

    def test_aprovado(self):
        self.assertEqual(classificar_aluno([7, 8, 9]), "Aprovado")
    
    def test_recuperacao(self):
        self.assertEqual(classificar_aluno([4, 4, 5]), "Recuperacao")
    
    def test_reprovado(self):
        self.assertEqual(classificar_aluno([0, 2, 3]), "Reprovado")
    
    def test_borda_aprovado(self):
        self.assertEqual(classificar_aluno([7, 7, 7]), "Aprovado")
    
    def test_borda_recuperacao(self):
        self.assertEqual(classificar_aluno([4, 4, 4]), "Recuperacao")
    
    def test_borda_reprovado(self):
        self.assertEqual(classificar_aluno([3.9, 3.9, 3.9]), "Reprovado")

    def test_lista_vazia(self):
        with self.assertRaises(ValueError):
            classificar_aluno([])
    
    def test_nota_negativa(self):
        with self.assertRaises(ValueError):
            classificar_aluno([5, -1, 7])
    
    def test_nota_maior_que_10(self):
        with self.assertRaises(ValueError):
            classificar_aluno([5, 11, 7])

if __name__ == "__main__":
    unittest.main()