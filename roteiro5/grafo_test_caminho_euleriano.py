
import unittest
from grafo_adj_nao_dir import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafos sem caminho euleriano:
        self.grafo_konisberg = Grafo(list("ABCD"))
        self.grafo_konisberg.adiciona_aresta_sem_separador("A B A B B C B C A D B D C D")
        self.g_vazio = Grafo()

        # Grafos com dois vértices ímpares:
        self.g_i1 = Grafo(list('ABC'))
        self.g_i1.adiciona_aresta_sem_separador('A B A B A C B C B C')

        self.g_i2 = Grafo(list("ABCD"))
        self.g_i2.adiciona_aresta_sem_separador("A B A B B D A D A C")

        self.g_i3 = Grafo(list("ABCDE"))
        self.g_i3.adiciona_aresta_sem_separador("A B A E A C C D C D C D D E")

        self.g_i4 = Grafo(list('AB'))
        self.g_i4.adiciona_aresta_sem_separador('A A A B B B')

        # Grafos com zero ímpares:

        self.g_p1 = Grafo(list('ABC'))
        self.g_p1.adiciona_aresta_sem_separador('A B A B A B A B A C A C')

        self.g_p2 = Grafo(list('ABC'))
        self.g_p2.adiciona_aresta_sem_separador('A B A B A C A C A C A C')

        self.g_laco = Grafo(list('A'))
        self.g_laco.adiciona_aresta_sem_separador('A A')



        self.g_laco2 = Grafo (list('B'))
        self.g_laco2.adiciona_aresta_sem_separador('B B B B B B')

    def test_caminho_euleriano(self):
        self.assertEqual(self.grafo_konisberg.caminho_euleriano(), [])
        self.assertEqual(self.g_vazio.caminho_euleriano(), [])

        self.assertEqual(self.g_i1.caminho_euleriano(), ['A', 'a1', 'B', 'a2', 'A', 'a3', 'C', 'a4', 'B', 'a5', 'C'])
        self.assertEqual(self.g_i2.caminho_euleriano(), ['B', 'a1', 'A', 'a2', 'B', 'a3', 'D', 'a4', 'A', 'a5', 'C'])
        self.assertEqual(self.g_i3.caminho_euleriano(), ['B', 'a1', 'A', 'a2', 'C', 'a3', 'D', 'a4', 'C', 'a5', 'D', 'a6', 'E', 'a7', 'A'])
        self.assertEqual(self.g_i4.caminho_euleriano(), ['A', 'a1', 'A', 'a2', 'B', 'a3', 'B'])

        self.assertEqual(self.g_p1.caminho_euleriano(), ['A', 'a1', 'B', 'a2', 'A', 'a3', 'B', 'a4', 'A', 'a5', 'C', 'a6', 'A'])
        self.assertEqual(self.g_p2.caminho_euleriano(), ['A', 'a1', 'B', 'a2', 'A', 'a3', 'C', 'a4', 'A', 'a5', 'C', 'a6', 'A'])

        self.assertEqual(self.g_laco.caminho_euleriano(), ['A', 'a1', 'A'])
        self.assertEqual(self.g_laco2.caminho_euleriano(), ['B', 'a1', 'B', 'a2', 'B', 'a3', 'B'])
