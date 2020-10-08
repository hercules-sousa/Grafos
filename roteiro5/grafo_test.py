
# Alunos: Hércules de Sousa Silva e Matheus Alves da Silva

import unittest
from grafo_adj_nao_dir import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        #{'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
        self.g_p.adicionaAresta('J-C')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-M')
        self.g_p.adicionaAresta('C-T')
        self.g_p.adicionaAresta('M-T')
        self.g_p.adicionaAresta('T-Z')


        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('J-C')
        self.g_p_sem_paralelas.adicionaAresta('C-E')
        self.g_p_sem_paralelas.adicionaAresta('C-P')
        self.g_p_sem_paralelas.adicionaAresta('C-M')
        self.g_p_sem_paralelas.adicionaAresta('C-T')
        self.g_p_sem_paralelas.adicionaAresta('M-T')
        self.g_p_sem_paralelas.adicionaAresta('T-Z')

        # Grafos completos
        #self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c = Grafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('J-C')
        self.g_c.adicionaAresta('J-E')
        self.g_c.adicionaAresta('J-P')
        self.g_c.adicionaAresta('C-E')
        self.g_c.adicionaAresta('C-P')
        self.g_c.adicionaAresta('E-P')

        self.g_c2 = Grafo(list('ABCDE'))
        self.g_c2.adiciona_aresta_sem_separador('A B A C A D A E')
        self.g_c2.adiciona_aresta_sem_separador('B C B D B E')
        self.g_c2.adiciona_aresta_sem_separador('C D C E')
        self.g_c2.adiciona_aresta_sem_separador('D E')

        self.g_c3 = Grafo(['J'])

        self.g_c4 = Grafo(list('ABCDEF'))
        self.g_c4.adiciona_aresta_sem_separador('A B A C A D A E A F')
        self.g_c4.adiciona_aresta_sem_separador('B C B D B E B F')
        self.g_c4.adiciona_aresta_sem_separador('C D C E C F')
        self.g_c4.adiciona_aresta_sem_separador('D E D F')
        self.g_c4.adiciona_aresta_sem_separador('E F')

        # Grafos com laco
        #self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('A-A')
        self.g_l1.adicionaAresta('A-A')
        self.g_l1.adicionaAresta('B-A')

        #self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('A-B')
        self.g_l2.adicionaAresta('B-B')
        self.g_l2.adicionaAresta('B-A')

        #self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('C-A')
        self.g_l3.adicionaAresta('C-C')
        self.g_l3.adicionaAresta('D-D')

        #self.g_l4 = Grafo(['D'], {'a2':'D-D'})
        self.g_l4 = Grafo(['D'])
        self.g_l4.adicionaAresta('D-D')

        #self.g_l5 = Grafo(['C', 'D'], {'a2':'D-C', 'a3':'C-C'})
        self.g_l5 = Grafo(['C', 'D'])
        self.g_l5.adicionaAresta('D-C')
        self.g_l5.adicionaAresta('C-C')

        # Grafos com paralelas
        self.g_p2 = Grafo(list('ABCD'))
        self.g_p2.adicionaAresta('A-B')
        self.g_p2.adicionaAresta('A-B')
        self.g_p2.adicionaAresta('B-C')
        self.g_p2.adicionaAresta('C-D')
        self.g_p2.adicionaAresta('D-B')
        self.g_p2.adicionaAresta('D-B')

        # Grafos com laços e paralelas
        self.g_lp = Grafo(list('ABCDE'))
        self.g_lp.adiciona_aresta_sem_separador('A A A C A E')
        self.g_lp.adiciona_aresta_sem_separador('B E B E')
        self.g_lp.adiciona_aresta_sem_separador('C C C D C D')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-P', 'P-M', 'P-T', 'P-Z', 'M-M', 'M-Z', 'T-T', 'Z-Z'])
        self.assertEqual(self.g_l1.vertices_nao_adjacentes(), ['A-C', 'A-D',
                                                               'B-B', 'B-C', 'B-D',
                                                               'C-C', 'C-D',
                                                               'D-D'])
        self.assertEqual(self.g_l2.vertices_nao_adjacentes(), ['A-A', 'A-C', 'A-D',
                                                               'B-C', 'B-D',
                                                               'C-C', 'C-D',
                                                               'D-D'])
        self.assertEqual(self.g_l4.vertices_nao_adjacentes(), [])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])
        self.assertEqual(self.g_c2.vertices_nao_adjacentes(), ['A-A', 'B-B', 'C-C', 'D-D', 'E-E'])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])
        self.assertEqual(self.g_c4.vertices_nao_adjacentes(), ['A-A', 'B-B', 'C-C', 'D-D', 'E-E', 'F-F'])

        self.assertEqual(self.g_lp.vertices_nao_adjacentes(), ['A-B', 'A-D', 'B-B', 'B-C', 'B-D', 'C-E', 'D-D', 'D-E', 'E-E'])

    def test_ha_laco(self):
        # Sem laço
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertFalse(self.g_c4.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())

        # Com laço
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_lp.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)

        # g_c
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # g_l1
        self.assertEqual(self.g_l1.grau('A'), 3)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l2.grau('C'), 0)
        self.assertEqual(self.g_l2.grau('D'), 0)

        # g_l2
        self.assertEqual(self.g_l2.grau('A'), 2)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l2.grau('C'), 0)
        self.assertEqual(self.g_l2.grau('D'), 0)

        # g_lp
        self.assertEqual(self.g_lp.grau('A'), 3)
        self.assertEqual(self.g_lp.grau('B'), 2)
        self.assertEqual(self.g_lp.grau('C'), 4)
        self.assertEqual(self.g_lp.grau('D'), 2)
        self.assertEqual(self.g_lp.grau('E'), 3)

        # g_p2
        self.assertEqual(self.g_p2.grau('A'), 2)
        self.assertEqual(self.g_p2.grau('B'), 5)
        self.assertEqual(self.g_p2.grau('C'), 2)
        self.assertEqual(self.g_p2.grau('D'), 3)

        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l4.grau('D'), 1)

    def test_arestas_ha_paralelas(self):
        # Tem arestas paralelas
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertTrue(self.g_lp)
        self.assertTrue(self.g_p2)

        # Não tem arestas paralelas
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertFalse(self.g_c4.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        # g_p
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'J-C'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'C-M', 'M-T'})

        # g_c4
        self.assertEqual(self.g_c4.arestas_sobre_vertice('A'), {'A-B', 'A-E', 'A-F', 'A-D', 'A-C'})
        self.assertEqual(self.g_c4.arestas_sobre_vertice('B'), {'B-D', 'A-B', 'B-E', 'B-C', 'B-F'})
        self.assertEqual(self.g_c4.arestas_sobre_vertice('C'), {'A-C', 'B-C', 'C-F', 'C-E', 'C-D'})
        self.assertEqual(self.g_c4.arestas_sobre_vertice('D'), {'B-D', 'D-F', 'C-D', 'A-D', 'D-E'})
        self.assertEqual(self.g_c4.arestas_sobre_vertice('F'), {'B-F', 'E-F', 'C-F', 'A-F', 'D-F'})

        # g_lp
        self.assertEqual(self.g_lp.arestas_sobre_vertice('A'), {'A-E', 'A-C', 'A-A'})
        self.assertEqual(self.g_lp.arestas_sobre_vertice('B'), {'B-E'})
        self.assertEqual(self.g_lp.arestas_sobre_vertice('C'), {'C-C', 'C-D', 'A-C'})
        self.assertEqual(self.g_lp.arestas_sobre_vertice('D'), {'C-D'})

        # g_l1
        self.assertEqual(self.g_l1.arestas_sobre_vertice('A'), {'A-A', 'A-B'})
        self.assertEqual(self.g_l1.arestas_sobre_vertice('B'), {'A-B'})
        self.assertEqual(self.g_l1.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_l1.arestas_sobre_vertice('D'), set())

        # g_p2
        self.assertEqual(self.g_p2.arestas_sobre_vertice('A'), {'A-B'})
        self.assertEqual(self.g_p2.arestas_sobre_vertice('B'), {'B-C', 'B-D', 'A-B'})
        self.assertEqual(self.g_p2.arestas_sobre_vertice('C'), {'B-C', 'C-D'})
        self.assertEqual(self.g_p2.arestas_sobre_vertice('D'), {'B-D', 'C-D'})

    def test_eh_completo(self):
        # É completo
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue(self.g_c2.eh_completo())
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertTrue((self.g_c4.eh_completo()))
        self.assertTrue((self.g_l4.eh_completo()))
        self.assertTrue((self.g_l5.eh_completo()))

        # Não é completo
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
