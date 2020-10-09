from grafo_adj_nao_dir import Grafo


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


g2 = Grafo(list("ABCDE"))
g2.adiciona_aresta_sem_separador("A B A E A C C D C D C D D E")
print(g2.caminho_euleriano())

g_par = Grafo(list('ABC'))
g_par.adiciona_aresta_sem_separador('A B A B A B A B A C A C')
print(g_par.caminho_euleriano())

g_par_invertido = Grafo(list('ABC'))
g_par_invertido.adiciona_aresta_sem_separador('A B A B A C A C A C A C')
print(g_par_invertido.caminho_euleriano())