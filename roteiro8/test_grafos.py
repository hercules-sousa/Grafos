import unittest

from grafo_adj_nao_dir import Grafo


class TesteFuncoes(unittest.TestCase):

    def setUp(self):
        self.g1 = Grafo(list("ABCDEFGH"))
        self.g1.adiciona_arestas_com_pesos("A-B 2 A-E 5 A-C 3 E-C 1 C-D 4 C-B 3 B-F 1 F-G 2 F-H 1 G-H 3 D-H 1")

        self.g2 = Grafo(list("ABCDEFGH"))
        self.g2.adiciona_arestas_com_pesos("A-D 1 A-B 2 C-B 3 C-D 1 E-D 4 E-C 1 F-E 4 F-B 5 F-G 1 G-H 1")

        self.g3 = Grafo(list("ABCDEFGHIJKLMNO"))
        self.g3.adiciona_arestas_com_pesos(
            "A-B 1 B-D 3 D-H 3 D-I 2 B-E 4 E-J 5 E-K 4 A-C 2 C-F 5 F-L 1 F-M 2 C-G 1 G-N 3 G-O 4")

        self.g4 = Grafo(list("ABCDEFGHI"))
        self.g4.adiciona_arestas_com_pesos("A-B 3 B-C 1 A-D 1 B-E 2 C-F 3 D-E 2 E-F 2 D-G 3 E-H 2 F-I 1 G-H 1 H-I 3")

        self.g5 = Grafo(list("ABCDEF"))
        self.g5.adiciona_arestas_com_pesos("A-B 2 A-C 2 B-C 2 B-D 3 D-E 1 D-F 2 E-F 1 F-A 1")

        self.g6 = Grafo(list("ABCDEFG"))
        self.g6.adiciona_arestas_com_pesos("A-B 1 B-C 1 A-D 2 D-C 3 D-E 4 E-F 7 F-G 12 E-G 11")

        self.g7 = Grafo(list("ABCDEFG"))
        self.g7.adiciona_arestas_com_pesos("A-G 1 G-B 11 G-C 72 G-D 2 D-E 1 D-F 80 E-F 95 F-C 2")

        self.g8 = Grafo(list("ABCD"))
        self.g8.adiciona_arestas_com_pesos("A-C 1 A-B 90 B-C 200 B-D 30 A-D 70")

    def test_prim_modificado(self):
        # Grafo1
        self.assertEqual(self.g1.prim_modificado("A"), ['A-B', 'B-F', 'F-H', 'H-D', 'F-G', 'A-C', 'C-E'])
        self.assertEqual(self.g1.prim_modificado("G"), ['G-F', 'F-B', 'B-A', 'B-C', 'C-E', 'F-H', 'H-D'])
        self.assertEqual(self.g1.prim_modificado("C"), ['C-E', 'C-A', 'A-B', 'B-F', 'F-H', 'H-D', 'F-G'])

        # Grafo 2
        self.assertEqual(self.g2.prim_modificado("B"), ['B-A', 'A-D', 'D-C', 'C-E', 'E-F', 'F-G', 'G-H'])
        self.assertEqual(self.g2.prim_modificado("F"), ['F-G', 'G-H', 'F-E', 'E-C', 'C-D', 'D-A', 'A-B'])
        self.assertEqual(self.g2.prim_modificado("D"), ['D-A', 'A-B', 'D-C', 'C-E', 'E-F', 'F-G', 'G-H'])

        # Grafo 3
        self.assertEqual(self.g3.prim_modificado("E"), ['E-B',
                                                        'B-A',
                                                        'A-C',
                                                        'C-G',
                                                        'G-N',
                                                        'G-O',
                                                        'C-F',
                                                        'F-L',
                                                        'F-M',
                                                        'B-D',
                                                        'D-I',
                                                        'D-H',
                                                        'E-K',
                                                        'E-J'])
        self.assertEqual(self.g3.prim_modificado("H"), ['H-D',
                                                        'D-I',
                                                        'D-B',
                                                        'B-A',
                                                        'A-C',
                                                        'C-G',
                                                        'G-N',
                                                        'G-O',
                                                        'C-F',
                                                        'F-L',
                                                        'F-M',
                                                        'B-E',
                                                        'E-K',
                                                        'E-J'])
        self.assertEqual(self.g3.prim_modificado("M"), ['M-F',
                                                        'F-L',
                                                        'F-C',
                                                        'C-G',
                                                        'G-N',
                                                        'G-O',
                                                        'C-A',
                                                        'A-B',
                                                        'B-D',
                                                        'D-I',
                                                        'D-H',
                                                        'B-E',
                                                        'E-K',
                                                        'E-J']
                         )

        # Grafo 4
        self.assertEqual(self.g4.prim_modificado("A"), ['A-D', 'D-E', 'E-B', 'B-C', 'E-F', 'F-I', 'E-H', 'H-G'])
        self.assertEqual(self.g4.prim_modificado("B"), ['B-C', 'B-E', 'E-D', 'D-A', 'E-F', 'F-I', 'E-H', 'H-G'])
        self.assertEqual(self.g4.prim_modificado("I"), ['I-F', 'F-E', 'E-B', 'B-C', 'E-D', 'D-A', 'E-H', 'H-G'])

        # Grafo 5
        self.assertEqual(self.g5.prim_modificado("C"), ['C-A', 'A-F', 'F-E', 'E-D', 'C-B'])
        self.assertEqual(self.g5.prim_modificado("E"), ['E-D', 'E-F', 'F-A', 'A-B', 'A-C'])
        self.assertEqual(self.g5.prim_modificado("F"), ['F-A', 'A-B', 'A-C', 'F-E', 'E-D'])

        # Grafo 6
        self.assertEqual(self.g6.prim_modificado("C"), ['C-B', 'B-A', 'A-D', 'D-E', 'E-F', 'E-G'])
        self.assertEqual(self.g6.prim_modificado("E"), ['E-D', 'D-A', 'A-B', 'B-C', 'E-F', 'E-G'])
        self.assertEqual(self.g6.prim_modificado("F"), ['F-E', 'E-D', 'D-A', 'A-B', 'B-C', 'E-G'])

        # Grafo 7
        self.assertEqual(self.g7.prim_modificado("E"), ['E-D', 'D-G', 'G-A', 'G-B', 'G-C', 'C-F'])
        self.assertEqual(self.g7.prim_modificado("A"), ['A-G', 'G-D', 'D-E', 'G-B', 'G-C', 'C-F'])
        self.assertEqual(self.g7.prim_modificado("F"), ['F-C', 'C-G', 'G-A', 'G-D', 'D-E', 'G-B'])

        # Grafo 8
        self.assertEqual(self.g8.prim_modificado("A"), ['A-C', 'A-D', 'D-B'])
        self.assertEqual(self.g8.prim_modificado("D"), ['D-B', 'D-A', 'A-C'])

