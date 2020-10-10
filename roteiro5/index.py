from grafo_adj_nao_dir import Grafo


g = Grafo(list('ABC'))
g.adiciona_aresta_sem_separador('A B A C B C')
print(g)


def caminho_euleriano_para_zero_impares(self):
    for i in range(len(self.N)):
        for j in range(i, len(self.N)):
            lista_de_vertices = [self.N[i], self.N[j]]
            caminho_para_zero_impares = self.caminho_euleriano_entre_dois_vertices(lista_de_vertices[0],
                                                                                   lista_de_vertices,
                                                                                   deepcopy(self.M))
            if caminho_para_zero_impares is None:
                caminho_para_zero_impares = self.caminho_euleriano_entre_dois_vertices(lista_de_vertices[-1],
                                                                                       lista_de_vertices,
                                                                                       deepcopy(self.M))
                if caminho_para_zero_impares is not None:
                    return caminho_para_zero_impares
            else:
                return caminho_para_zero_impares

    raise ErroNoRetornoDeCaminhoEulerianoException