import unittest
from grafo_adj_dir import*

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p.adiciona_aresta(i)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p_sem_paralelas.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p_sem_paralelas.adiciona_aresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
            self.g_c.adiciona_aresta(i)


        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in ['A-A', 'B-A', 'A-A']:
            self.g_l1.adiciona_aresta(i)

        self.g_l2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l2.adiciona_vertice(i)
        for i in ['A-B', 'B-B', 'B-A']:
            self.g_l2.adiciona_aresta(i)

        self.g_l3 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l3.adiciona_vertice(i)
        for i in ['C-A', 'C-C', 'D-D']:
            self.g_l3.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta('D-D')

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in ['D-C', 'C-C']:
            self.g_l5.adiciona_aresta(i)

        # Grafos do roteiro 6
        self.g1 = Grafo(list('ABC'))
        self.g1.adicionar_arestas_sem_separador('A B A C B C C B')

        self.g2 = Grafo(list('ABCD'))
        self.g2.adicionar_arestas_sem_separador('A B B C D A')

        self.g3 = Grafo(list('ABCD'))
        self.g3.adicionar_arestas_sem_separador('A A A B B C C B C C D C')

        self.g4 = Grafo(list('ABCD'))
        self.g4.adicionar_arestas_sem_separador('A A B B A C C D C D C B')

        self.g5 = Grafo(list('ABC'))

        self.g6 = Grafo(list('ABCD'))
        self.g6.adicionar_arestas_sem_separador('A B A B C A B C B C D B D C D C')

        self.g7 = Grafo(list('ABCDE'))
        self.g7.adicionar_arestas_sem_separador('A B B C C D D E E A')

        self.g8 = Grafo(list('ABCDE'))
        self.g8.adicionar_arestas_sem_separador('A B B C C D D B E B')

        self.g9 = Grafo(list('ABC'))
        self.g9.adicionar_arestas_sem_separador('A A A B A B A B A B B B B C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()), set(['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z',
                                                                      'C-J', 'C-C', 'C-Z',
                                                                      'E-J', 'E-C', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z',
                                                                      'P-J', 'P-C', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z',
                                                                      'M-J', 'M-C', 'M-E', 'M-P', 'M-M', 'M-Z',
                                                                      'T-J', 'T-C', 'T-E', 'T-P','T-M', 'T-T',
                                                                      'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T', 'Z-Z']))

        self.assertEqual(set(set(self.g_c.vertices_nao_adjacentes())), set(['J-J', 'C-C', 'E-E', 'P-P']))

        self.assertEqual(set(self.g_c3.vertices_nao_adjacentes()), set(['J-J']))

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 6)
        self.assertEqual(self.g_c.grau('C'), 6)
        self.assertEqual(self.g_c.grau('E'), 6)
        self.assertEqual(self.g_c.grau('P'), 6)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 3)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l4.grau('D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), ['J-C'])
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T'])
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), ['C-M', 'M-T'])

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse(self.g_p_sem_paralelas.eh_completo())
        self.assertTrue(self.g_c.eh_completo())
        self.assertTrue(self.g_c3.eh_completo())
        self.assertFalse(self.g_l1.eh_completo())
        self.assertFalse(self.g_l2.eh_completo())
        self.assertFalse(self.g_l3.eh_completo())
        self.assertTrue(self.g_l4.eh_completo())
        self.assertFalse(self.g_l5.eh_completo())

    def test_warshall(self):
        self.assertEqual(self.g1.warshall(), [[0, 1, 1], [0, 1, 1], [0, 1, 1]])
        self.assertEqual(self.g2.warshall(), [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0]])
        self.assertEqual(self.g3.warshall(), [[1, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]])
        self.assertEqual(self.g4.warshall(), [[1, 1, 1, 2], [0, 1, 0, 0], [0, 1, 0, 2], [0, 0, 0, 0]])
        self.assertEqual(self.g5.warshall(), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(self.g6.warshall(), [[1, 2, 2, 0], [1, 2, 2, 0], [1, 2, 2, 0], [1, 2, 2, 0]])
        self.assertEqual(self.g7.warshall(), [
            [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]
        ])
        self.assertEqual(self.g8.warshall(), [
            [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0]
        ])
        self.assertEqual(self.g9.warshall(), [[1, 4, 1], [0, 1, 1], [0, 0, 0]])
