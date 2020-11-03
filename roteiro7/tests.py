# Matheus Alves da Silva
# Hércules de Sousa Silva

import unittest

from grafo_adj_nao_dir import Grafo


class TesteGrafo(unittest.TestCase):
    def setUp(self):
        self.g1 = Grafo(list('ABCDE'))
        self.g1.adiciona_aresta_sem_separador('A B B C C D A E E D')

        self.g2 = Grafo(list('ABCDEFG'))
        self.g2.adiciona_aresta_sem_separador('A B B F F G B C C E C D D E E G')

        self.g3 = Grafo(list('ABCDEFG'))
        self.g3.adiciona_aresta_sem_separador('A B A D B D B C B E C E D E D F E F E G F G')

        self.g4 = Grafo(list('ABCDEFGHI'))
        self.g4.adiciona_aresta_sem_separador('A B A C A D B C B D B E C E C F D G E D F E F H F I G E H E H G H I')

        self.g5 = Grafo(list('ABCDEFGHI'))
        self.g5.adiciona_aresta_sem_separador('A B A D A H B F C D D E D G E A E C E I F G G A G C H B H I I B')

        self.g6 = Grafo(list('ABCDEFGHIJK'))
        self.g6.adiciona_aresta_sem_separador('A B A C A D B C B E C D C F C G D G E F E H F I G J H I H K I K I J J K')

        self.g7 = Grafo(list('ABCDEF'))
        self.g7.adiciona_aresta_sem_separador('A C A D B E C F D F')

    def test_menor_caminho_drone(self):
        # Grafo 1
        self.assertEqual(self.g1.menor_caminho_drone('A', 'D', 1, 2, ['B']), ['A', 'B', 'C', 'D'])
        self.assertEqual(self.g1.menor_caminho_drone('B', 'E', 1, 2, ['C']), ['B', 'C', 'D', 'E'])
        self.assertEqual(self.g1.menor_caminho_drone('A', 'D', 1, 1, ['E']), ['A', 'E', 'D'])

        # Grafo 2
        self.assertEqual(self.g2.menor_caminho_drone('A', 'G', 2, 2, ['C']), ['A', 'B', 'C', 'E', 'G'])
        self.assertEqual(self.g2.menor_caminho_drone('D', 'A', 1, 3, ['E', 'B']), ['D', 'E', 'G', 'F', 'B', 'A'])
        self.assertEqual(self.g2.menor_caminho_drone('D', 'A', 1, 2, ['E', 'B']), [])

        # Grafo 3
        self.assertEqual(self.g3.menor_caminho_drone('A', 'F', 1, 3, ['B', 'E']), ['A', 'B', 'E', 'F'])
        self.assertEqual(self.g3.menor_caminho_drone('A', 'G', 2, 2, ['F']), ['A', 'D', 'F', 'G'])
        self.assertEqual(self.g3.menor_caminho_drone('G', 'C', 2, 2, ['D']), ['G', 'E', 'C'])

        # Grafo 4
        self.assertEqual(self.g4.menor_caminho_drone('A', 'I', 1, 1, ['B', 'C', 'F']), ['A', 'C', 'F', 'I'])
        self.assertEqual(self.g4.menor_caminho_drone('A', 'H', 1, 1, ['E', 'F', 'G']), [])
        self.assertEqual(self.g4.menor_caminho_drone('A', 'F', 1, 2, ['D']), ['A', 'D', 'E', 'F'])

        # Grafo 5
        self.assertEqual(self.g5.menor_caminho_drone('G', 'I', 2, 2, ['E']), ['G', 'A', 'E', 'I'])
        self.assertEqual(self.g5.menor_caminho_drone('I', 'F', 1, 3, ['E', 'H']), ['I', 'E', 'A', 'G', 'F'])
        self.assertEqual(self.g5.menor_caminho_drone('C', 'B', 0, 5, ['D', 'E', 'G']), [])

        # Grafo 6
        self.assertEqual(self.g6.menor_caminho_drone('A', 'K', 2, 2, ['G']), ['A', 'C', 'G', 'J', 'K'])
        self.assertEqual(self.g6.menor_caminho_drone('A', 'F', 1, 1, ['B', 'E']), ['A', 'B', 'E', 'F'])
        self.assertEqual(self.g6.menor_caminho_drone('C', 'H', 2, 2, ['J']), ['C', 'G', 'J', 'K', 'H'])

        # Grafo 7
        self.assertEqual(self.g7.menor_caminho_drone('A', 'E', 2, 2, []), [])
        self.assertEqual(self.g7.menor_caminho_drone('B', 'E', 1, 1, []), ['B', 'E'])
        self.assertEqual(self.g7.menor_caminho_drone('C', 'D', 1, 1, ['F']), ['C', 'F', 'D'])
