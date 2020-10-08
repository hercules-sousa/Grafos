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