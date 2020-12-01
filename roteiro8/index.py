from grafo_adj_nao_dir import Grafo

g = Grafo(list("ABCDEF"))

arestas = 'A-B A-C C-D C-E D-E E-F'.split()
pesos = [2, 3, 5, 1, 2, 2]

for a, p in zip(arestas, pesos):
    g.adicionaArestaComPeso(a, p)

print(g)
print(g.prim_modificado('C'))
