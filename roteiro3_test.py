import unittest
from roteiro3 import *
from grafo import Grafo


class Roteiro3(unittest.TestCase):

    def setUp(self):
        self.GP = Grafo(list('JCEPMTZ'), {'1': 'J-C', '2': 'C-E', '3': 'C-E', '4': 'C-P', '5': 'C-P', '6': 'C-M',
                                          '7': 'C-T', '8': 'M-T', '9': 'T-Z'})
        self.GE = Grafo(list('ABCDEFGHIJK'), {'1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'K-G', '5': 'K-J', '6': 'J-G',
                                              '7': 'J-I', '8': 'I-G', '9': 'G-H', '10': 'F-H', '11': 'B-F', '12': 'B-G',
                                              '13': 'B-C', '14': 'C-D', '15': 'D-E', '16': 'B-D', '17': 'B-E'})
        self.GVD = Grafo(list('ABC'), {'1': 'A-B', '2': 'B-A'})
        self.AB = Grafo(list('ABCDEFG'), {'1': 'A-B', '2': 'A-C', '3': 'C-E', '4': 'C-D', '5': 'B-F', '6': 'B-G'})
        self.BPC = Grafo(list('ABCDE'), {'1': 'A-B', '2': 'B-C', '3': 'A-D', '4': 'B-E', '5': 'C-D', '6': 'D-E'})
        self.GL = Grafo(list('ABC'), {'1': 'A-A', '2': 'B-A', '3': 'C-B', '4': 'C-C'})
        self.GH = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'],
                        {'A': '1-2', 'B': '1-2', 'C': '2-3', 'D': '3-3', 'E': '2-4', 'F': '4-5', 'G': '5-6', 'H': '5-7',
                         'I': '2-8', 'J': '4-8', 'K': '8-8', 'L': '9-8', 'M': '8-12', 'N': '9-10', 'O': '9-10',
                         'P': '10-11', 'Q': '11-12', 'R': '12-14', 'S': '14-13', 'T': '13-15'})
        self.DH = Grafo([str(x) for x in range(1, 5)], {'A': '1-1', 'B': '1-2', 'C': '1-3', 'D': '2-3', 'E': '2-3'})
        self.DH2 = Grafo([str(x) for x in range(1, 7)], {'A': '2-3', 'B': '3-4', 'C': '4-5'})
        self.GHT = Grafo([str(x) for x in range(1, 6)], {'A': '1-2', 'B': '2-3', 'C': '2-5', 'D': '2-4', 'E': '4-5'})
        self.G2D = Grafo(['1', '2'])
        self.GNC1 = Grafo([str(x) for x in range(1, 9)], {'A': '1-1', 'B': '1-2', 'C': '1-7', 'D': '1-3', 'E': '3-4',
                                                          'F': '3-4', 'G': '3-5', 'H': '5-6', 'I': '5-6', 'J': '6-7',
                                                          'K': '7-7'})
        self.GB = Grafo([str(x) for x in range(1, 21)], {'A': '1-10', 'B': '1-6', 'C': '1-11', 'D': '1-2', 'E': '2-3',
                                                         'F': '3-12', 'G': '3-4', 'H': '4-5', 'I': '4-16', 'J': '4-12',
                                                         'K': '12-15', 'L': '2-10', 'M': '7-11', 'N': '7-8', 'O': '8-10',
                                                         'P': '10-13', 'Q': '9-13', 'R': '14-15', 'S': '15-19',
                                                         'T': '15-17', 'U': '17-19', 'W': '19-18', 'X': '18-20',
                                                         'Y': '20-20'})

        self.GT1 = Grafo([str(x) for x in range(1, 11)],{'A': '1-2', 'B': '1-3', 'C': '3-7', 'D': '3-6', 'E': '4-7',
                                                         'F': '3-5', 'G': '5-6', 'H': '6-8', 'I': '8-9', 'J': '9-10'})

    def test_ha_ciclo(self):
        self.assertEqual(ha_ciclo(self.GVD), ['A', '1', 'B', '2', 'A'])
        self.assertFalse(ha_ciclo(self.AB))
        self.assertEqual(ha_ciclo(self.GP), ['C', '2', 'E', '3', 'C'])
        self.assertEqual(ha_ciclo(self.GE), ['A', '1', 'B', '11', 'F', '10', 'H', '9', 'G', '2', 'A'])
        self.assertEqual(ha_ciclo(self.BPC), ['A', '1', 'B', '2', 'C', '5', 'D', '3', 'A'])
        self.assertEqual(ha_ciclo(self.GL), ['A', '1', 'A'])
        self.assertEqual(ha_ciclo(self.GH), ['1', 'A', '2', 'B', '1'])  # Vértices são números e arestas letras
        self.assertEqual(ha_ciclo(self.GB), ['1', 'A', '10', 'L', '2', 'D', '1'])

    def test_caminho(self):
        self.assertEqual(caminho(self.GP, 3), ['J', '1', 'C', '6', 'M', '8', 'T'])
        self.assertEqual(caminho(self.GE, 5), ['A', '1', 'B', '11', 'F', '10', 'H', '9', 'G', '4', 'K'])
        self.assertEqual(caminho(self.GVD, 2), [])
        self.assertEqual(caminho(self.AB, 4), ['D', '4', 'C', '2', 'A', '1', 'B', '5', 'F'])
        self.assertEqual(caminho(self.BPC, 3), ['A', '1', 'B', '2', 'C', '5', 'D'])
        self.assertEqual(caminho(self.GL, 2), ['A', '2', 'B', '3', 'C'])
        self.assertEqual(caminho(self.GH, 7), ['1', 'A', '2', 'E', '4', 'J', '8', 'L', '9', 'N', '10', 'P', '11', 'Q',
                                               '12'])  # Vértices são números e arestas letras
        self.assertEqual(caminho(self.GT1, 6), ['1', 'B', '3', 'F', '5', 'G', '6', 'H', '8', 'I', '9', 'J', '10'])
        self.assertEqual(caminho(self.GT1, 9), [])

    def test_conexo(self):
        self.assertFalse(conexo(self.DH))
        self.assertFalse(conexo(self.DH2))
        self.assertTrue(conexo(self.GHT))
        self.assertFalse(conexo(self.G2D))
        self.assertFalse(conexo(Grafo()))
        self.assertFalse(conexo(self.GNC1))
        self.assertTrue((conexo(self.GB)))
