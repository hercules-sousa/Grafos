from grafo_adj_nao_dir import Grafo

g1 = Grafo(list('ABCDEF'))
g1.adiciona_aresta_sem_separador('A B B C A D D E E F F C')

# g1.dijkstra(g1.M, g1.N.index('A'), g1.N)

g1.menor_caminho_drone("A", "F", 10000, 50000, ["D", "E"])