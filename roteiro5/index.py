from grafo_adj_nao_dir import Grafo

g = Grafo(list('ABC'))
g.adiciona_aresta_sem_separador('A B B C A C')
print(g.ciclo_hamiltoniano())

g_c1 = Grafo(list('BCADE'))
g_c1.adiciona_aresta_sem_separador('A B A C A E B C B D C D E D')
print(g_c1.ciclo_hamiltoniano())

g_p1 = Grafo(list('ABC'))
g_p1.adiciona_aresta_sem_separador('A B A B B C A C')
print(g_p1.ciclo_hamiltoniano())

g_l1 = Grafo(list('A'))
g_l1.adiciona_aresta_sem_separador('A A')
print(g_l1.ciclo_hamiltoniano())

g_sem1 = Grafo(list('ABCDE'))
g_sem1.adiciona_aresta_sem_separador('A B A D B C B D C D B E D E')
print(g_sem1.ciclo_hamiltoniano())