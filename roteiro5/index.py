from grafo_adj_nao_dir import Grafo

'''
g = Grafo(list('ABCD'))
g.adiciona_aresta_sem_separador('A B A B B C B C A D B D C D')
print(g.há_caminho_euleriano())
'''

g_sem_caminho_euleriano = Grafo(list('ABC'))
g_sem_caminho_euleriano.adiciona_aresta_sem_separador('A B A B A C B C B C')
print(g_sem_caminho_euleriano.caminho_euleriano())
