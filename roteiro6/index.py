from grafo_adj_dir import Grafo

g = Grafo(list('ABCD'))
g.adicionar_arestas_sem_separador('A A A D B D C A D B')

print(g)
for linha in g.warshall():
    print(*linha)