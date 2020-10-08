from grafo_adj_nao_dir import Grafo

'''
g = Grafo(list('ABC'))
g.adiciona_aresta_sem_separador('A B A B A C B C B C')
print(g)
print(g.caminho_euleriano())

grafo_konisberg = Grafo(list("ABCD"))
grafo_konisberg.adiciona_aresta_sem_separador("A B A B B C B C A D B D C D")
print(grafo_konisberg.caminho_euleriano())

g1 = Grafo(list("ABCD"))
g1.adiciona_aresta_sem_separador("A B A B B D A D A C")
print(g1.caminho_euleriano())
'''

g2 = Grafo(list("ABCDE"))
g2.adiciona_aresta_sem_separador("A B A E A C C D C D C D D E")
print(g2.caminho_euleriano())