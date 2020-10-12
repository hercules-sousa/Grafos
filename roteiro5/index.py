from grafo_adj_nao_dir import Grafo

g = Grafo(list('ABC'))
g.adiciona_aresta_sem_separador('A B B C C A')
g.ciclo_hamiltoniano()

g_c1 = Grafo(list('ABCDE'))
g_c1.adiciona_aresta_sem_separador('A B A C A E B C B D C D E D')
print(g_c1)
g_c1.ciclo_hamiltoniano()


