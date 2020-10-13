from grafo_adj_dir import Grafo

g = Grafo(list('ABC'))
g.adicionar_arestas_sem_separador('A B A C B C C B')

print(g)
for linha in g.warshall():
    print(*linha)