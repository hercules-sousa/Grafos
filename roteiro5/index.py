from grafo_adj_nao_dir import Grafo

'''
g = Grafo(list('ABCD'))
g.adiciona_aresta_sem_separador('A B A B B C B C A D B D C D')
print(g.há_caminho_euleriano())
'''

g = Grafo(list('ABC'))
g.adiciona_aresta_sem_separador('A B A B A C B C B C')
print(g)
print(g.caminho_euleriano())
