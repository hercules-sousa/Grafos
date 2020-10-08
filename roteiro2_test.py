# Dupla: Matheus Alves da Silva; Hércules de Sousa Silva


import unittest
from grafo import Grafo
from roteiro2 import dfs


class TestDFS(unittest.TestCase):
    def setUp(self):
        # Grafo da Paraíba
        self.GP = Grafo(list('JCEPMTZ'), {'1': 'J-C', '2': 'C-E', '3': 'C-E', '4': 'C-P', '5': 'C-P', '6': 'C-M',
                                          '7': 'C-T', '8': 'M-T', '9': 'T-Z'})
        
        # Grafo do roteiro
        self.GE = Grafo(list('ABCDEFGHIJK'), {'1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'K-G', '5': 'K-J', '6': 'J-G',
                                              '7': 'J-I', '8': 'I-G', '9': 'G-H', '10': 'F-H', '11': 'B-F', '12': 'B-G',
                                              '13': 'B-C', '14': 'C-D', '15': 'D-E', '16': 'B-D', '17': 'B-E'})

        # Grafo com vértice desconexo
        self.GVD = Grafo(list('ABC'), {'1': 'A-B', '2': 'B-A'})

        # Árvore binária
        self.AB = Grafo(list('ABCDEFG'), {'1': 'A-B', '2': 'A-C', '3': 'C-E', '4': 'C-D', '5': 'B-F', '6': 'B-G'})

        # Grafo bipartido completo
        self.BPC = Grafo(list('ABCDE'), {'1': 'A-B', '2': 'B-C', '3': 'A-D', '4': 'B-E', '5': 'C-D', '6': 'D-E'})

        # Grafo com laços
        self.GL = Grafo(list('ABC'), {'1': 'A-A', '2': 'B-A', '3': 'C-B', '4': 'C-C'})
        self.GL2 = Grafo(list('ABCDEF'), {'1': 'A-D', '2': 'A-C', '3': 'A-B', '4': 'B-C', '5': 'A-A', '6': 'B-B',
                                          '7': 'D-D', '8': 'C-C', '9': 'C-E', '10': 'E-E', '11': 'E-F', '12': 'F-F'})

        # Grafo com paralelas
        self.GCP = Grafo(list('ABCDEFG'), {'1': 'A-B', '2': 'A-B', '3': 'B-C', '4': 'C-D', '5': 'D-E', '6': 'D-E',
                                           '7': 'E-F', '8': 'F-G', '9': 'D-G'})
        self.GHP = Grafo([str(x) for x in range(1, 7)], {'a1': '1-2', 'a2': '1-2', 'a3': '1-2', 'a4': '1-2',
                                                         'a5': '1-3', 'a6': '3-5', 'a7': '3-4', 'a8': '4-5',
                                                         'a9': '5-6'})

        # Grafo com laços e paralelas
        self.GCLP = Grafo(list('ABCD'), {'1': 'A-B', '2': 'A-B', '3': 'B-B', '4': 'B-C', '5': 'B-C', '6': 'C-D',
                                         '7': 'D-D'})
        self.GH = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'],
                        {'a1': '1-2', 'a2': '1-2', 'a3': '2-3', 'a4': '3-3', 'a5': '2-4', 'a6': '4-5', 'a7': '5-6',
                         'a8': '5-7', 'a9': '2-8', 'a10': '4-8', 'a11': '8-8', 'a12': '9-8', 'a13': '8-12',
                         'a14': '9-10', 'a15': '9-10', 'a16': '10-11', 'a17': '11-12', 'a18': '12-14', 'a19': '14-13',
                         'a20': '13-15'})

        # Grafo completo
        self.GC = Grafo(list('ABCD'), {'1': 'A-B', '2': 'A-C', '3': 'A-D', '4': 'B-C', '5': 'B-D', '6': 'C-D'})

        # Grafo vazio
        self.GV = Grafo()

        # Grafo bipartido incompleto
        self.BPIC = Grafo(list("123456"), {'a1': '1-2', 'a2': '2-3', 'a3': '6-4', 'a4': '3-4', 'a5': '4-5'})

    def test_DFS(self):
        self.assertEqual(dfs(self.GC, 'C'), ['C', '2', 'A', '1', 'B', '5', 'D'])
        self.assertEqual(dfs(self.GE, 'K'), ['K', '4', 'G', '2', 'A', '1', 'B', '11', 'F', '10', 'H', '13', 'C', '14',
                                             'D', '15', 'E', '3', 'J', '7', 'I'])
        self.assertEqual(dfs(self.GVD, 'C'), ['C'])
        self.assertEqual(dfs(self.AB, 'G'), ['G', '6', 'B', '1', 'A', '2', 'C', '3', 'E', '4', 'D', '5', 'F'])
        self.assertEqual(dfs(self.BPC, 'B'), ['B', '1', 'A', '3', 'D', '5', 'C', '6', 'E'])
        self.assertEqual(dfs(self.GL, 'A'), ['A', '2', 'B', '3', 'C'])
        self.assertEqual(dfs(self.GC, 'D'), ['D', '3', 'A', '1', 'B', '4', 'C'])
        self.assertEqual(dfs(self.GCP, 'D'), ['D', '4', 'C', '3', 'B', '1', 'A', '5', 'E', '7', 'F', '8', 'G'])
        self.assertEqual(dfs(self.GCLP, 'C'), ['C', '4', 'B', '1', 'A', '6', 'D'])
        self.assertEqual(dfs(self.GV, 'A'), [])
        self.assertEqual(dfs(self.GH, '8'), ['8', 'a9', '2', 'a1', '1', 'a3', '3', 'a5', '4', 'a6', '5', 'a7', '6',
                                             'a8', '7', 'a12', '9', 'a14', '10', 'a16', '11', 'a17', '12', 'a18', '14',
                                             'a19', '13', 'a20', '15'])
        self.assertEqual(dfs(self.GHP, '3'), ['3', 'a5', '1', 'a1', '2', 'a6', '5', 'a8', '4', 'a9', '6'])
        self.assertEqual(dfs(self.BPIC, '2'), ['2', 'a1', '1', 'a2', '3', 'a4', '4', 'a3', '6', 'a5', '5'])
        self.assertEqual(dfs(self.GL2, 'D'), ['D', '1', 'A', '2', 'C', '4', 'B', '9', 'E', '11', 'F']
)