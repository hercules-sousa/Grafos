from grafo_adj_nao_dir import Grafo

arestas1 = "A-B A-E A-C E-C C-D C-B B-F F-G F-H G-H D-H".split()
pesos1 = [2, 5, 3, 1, 4, 3, 4, 1, 2, 1, 3, 1]
g1 = Grafo(list("ABCDEFGH"))


g2 = Grafo(list("ABCDEFGH"))
g2.adiciona_arestas_com_pesos("A-B 2 A-E 5 A-C 3 E-C 1 C-D 4 C-B 3 B-F 1 F-G 2 F-H 1 G-H 3 D-H 1")

for aresta, peso in zip(arestas1, pesos1):
    g1.adicionaArestaComPeso(aresta, peso)

print(g1)
print(g2)
# print(g1.prim_modificado("A"))
