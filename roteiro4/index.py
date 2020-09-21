from grafo_adj_nao_dir import Grafo

g_l1 = Grafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('A-A')
g_l1.adicionaAresta('A-A')
g_l1.adicionaAresta('B-A')
print(g_l1)
print(g_l1.ha_paralelas())