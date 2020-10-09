from grafo_adj_nao_dir import Grafo


g = Grafo(list('ABC'))
g.adiciona_aresta_sem_separador('A B A C B C')
print(g)
