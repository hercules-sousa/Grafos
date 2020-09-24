from grafo_adj_nao_dir import Grafo

g = Grafo(list('ABC'))
g.adicionaAresta('A-B')
g.adicionaAresta('B-C')
g.adicionaAresta('A-C')

print(g.grau('B'))