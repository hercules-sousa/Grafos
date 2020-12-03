from grafo_adj_nao_dir import Grafo

g = Grafo(list("ABCDE"))

arestas = 'A-C A-B B-E A-D B-D D-E'.split()
pesos = [5, 3, 3, 2, 3, 5]

for a, p in zip(arestas, pesos):
    g.adicionaArestaComPeso(a, p)

print(g)
print(g.kruskal_modificado())
