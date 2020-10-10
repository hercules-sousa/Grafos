from grafo_adj_nao_dir import Grafo


g = Grafo(list('ABC'))
g.adiciona_aresta_sem_separador('A B B C')
print(g)
g.ciclo_hamiltoniano()