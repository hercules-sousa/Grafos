from grafo_adj_nao_dir import Grafo

g_p3 = Grafo(list('ABCD'))
g_p3.adiciona_aresta_sem_separador('A B A B A C A C B D B D D C D C')

print(g_p3)