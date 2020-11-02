from grafo_adj_nao_dir import Grafo

g = Grafo(list("ABCDE"))
g.adiciona_aresta_sem_separador("A B B C C D A E E D")
a = g.menor_caminho_drone("A", "D", 1, 2, ["B"])
print(a)

print()
g1 = Grafo(list('ABCDEFG'))
g1.adiciona_aresta_sem_separador('A B B F F G B C C E C D D E E G')
a = g1.menor_caminho_drone("A", "G", 10000, 50000, ["D", "E"])
print(a)

# g1.dijkstra(g1.M, g1.N.index('A'), g1.N)