# -*- coding: utf-8 -*-

from copy import deepcopy


class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class ErroNoRetornoDeCaminhoEulerianoException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append(self.SEPARADOR_ARESTA)
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == self.SEPARADOR_ARESTA):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append(self.SEPARADOR_ARESTA)  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def adiciona_aresta_sem_separador(self, arestas_sem_separador):
        arestas_sem_separador = arestas_sem_separador.split()
        for vertex_counter in range(len(arestas_sem_separador)):
            if vertex_counter % 2 == 1:
                new_edge = arestas_sem_separador[vertex_counter - 1] + self.SEPARADOR_ARESTA + arestas_sem_separador[
                    vertex_counter]
                self.adicionaAresta(new_edge)

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str

    def vertices_nao_adjacentes(self):
        list_of_edges_not_adjacent = list()

        for line_counter in range(len(self.M)):
            for column_counter in range(line_counter, len(self.M)):
                connection = self.M[line_counter][column_counter]
                if connection == 0:
                    edge_not_adjacent = str()
                    edge_not_adjacent += (self.N[line_counter] + self.SEPARADOR_ARESTA + self.N[column_counter])
                    list_of_edges_not_adjacent.append(edge_not_adjacent)

        return list_of_edges_not_adjacent

    def ha_laco(self):
        for position in range(len(self.N)):
            vertex = self.M[position][position]
            if vertex > 0:
                return True
        return False

    def ha_paralelas(self):
        for line_counter in range(len(self.M)):
            for column_counter in range(line_counter, len(self.M)):
                vertex = self.M[line_counter][column_counter]
                if vertex > 1:
                    return True

        return False

    def grau(self, vertex):
        if vertex not in self.N:
            raise VerticeInvalidoException('O vértice ' + vertex + ' é inválido')

        position = self.N.index(vertex)

        grau = 0

        for line_counter in range(len(self.M)):
            if line_counter != position:
                element = self.M[line_counter][position]
                if element != self.SEPARADOR_ARESTA:
                    grau += int(element)
                else:
                    break
            else:
                grau += sum(self.M[line_counter][line_counter:])

        return grau

    def arestas_sobre_vertice(self, vertex):
        position_of_vertex_in_array = self.N.index(vertex)

        list_of_edges = set()

        for element_counter in range(len(self.M[position_of_vertex_in_array])):
            if self.M[position_of_vertex_in_array][element_counter] != self.SEPARADOR_ARESTA:
                if self.M[position_of_vertex_in_array][element_counter] > 0:
                    other_vertex = self.N[element_counter]
                    list_of_edges.add(f'{vertex}{self.SEPARADOR_ARESTA}{other_vertex}')

        for line_counter in range(len(self.M)):
            if self.M[line_counter][position_of_vertex_in_array] != self.SEPARADOR_ARESTA:
                if self.M[line_counter][position_of_vertex_in_array] > 0:
                    first_vertex = self.N[line_counter]
                    list_of_edges.add(f'{first_vertex}{self.SEPARADOR_ARESTA}{vertex}')
            else:
                break

        return list_of_edges

    def eh_completo(self):
        for line_counter in range(len(self.M)):
            for column_counter in range(line_counter + 1, len(self.M)):
                vertex = self.M[line_counter][column_counter]
                if vertex == 0:
                    return False

        return True

    def há_caminho_euleriano(self):
        if self.esta_vazia_matriz_de_adjacencia(self.M):
            return -1
        qtd_impares = 0
        for vertice in self.N:
            grau_do_vertice = self.grau(vertice)
            if grau_do_vertice % 2 == 1:
                qtd_impares += 1
            if qtd_impares > 2:
                return -1

        if qtd_impares == 1 and len(self.N) == 1:
            return 0

        if qtd_impares == 1:
            return -1

        return qtd_impares

    def encontrar_dupla_de_vertices_impares(self):
        vertices_impares = list()
        for vertice in self.N:
            if self.grau(vertice) % 2 == 1:
                vertices_impares.append(vertice)
            if len(vertices_impares) == 2:
                return vertices_impares

    def checar_se_linha_possui_conexoes(self, linha):
        for elemento in linha:
            if elemento > 0:
                return True
        return False

    def esta_vazia_matriz_de_adjacencia(self, matriz_adjacencia):
        for line_counter in range(len(matriz_adjacencia)):
            linha_de_conexoes = matriz_adjacencia[line_counter][line_counter:]
            if self.checar_se_linha_possui_conexoes(linha_de_conexoes):
                return False
        return True

    def caminho_euleriano_entre_dois_vertices(self,
                                            vertice,
                                            vertices_impares,
                                            copia_matriz_adjacencia,
                                            numero_da_aresta=2,
                                            caminho_euleriano=None):
        if caminho_euleriano is None:
            caminho_euleriano = list()
            caminho_euleriano.append(vertice)
            caminho_euleriano.append("a1")
        if self.esta_vazia_matriz_de_adjacencia(copia_matriz_adjacencia):
            caminho_euleriano = caminho_euleriano[:-1]
            if caminho_euleriano[0] == vertices_impares[0] and caminho_euleriano[-1] == vertices_impares[-1]:
                return caminho_euleriano
            elif caminho_euleriano[0] == vertices_impares[-1] and caminho_euleriano[-1] == vertices_impares[0]:
                return caminho_euleriano
            else:
                return None
        else:
            posicao_vertice_na_lista = self.N.index(vertice)
            for line_counter in range(len(copia_matriz_adjacencia)):
                if line_counter == posicao_vertice_na_lista:
                    for column_counter in range(line_counter, len(copia_matriz_adjacencia)):
                        if copia_matriz_adjacencia[line_counter][column_counter] > 0:
                            copia_matriz_adjacencia[line_counter][column_counter] -= 1
                            novo_vertice = self.N[column_counter]
                            caminho_euleriano += [novo_vertice, f'a{numero_da_aresta}']
                            numero_da_aresta += 1
                            return self.caminho_euleriano_entre_dois_vertices(
                                novo_vertice,
                                vertices_impares,
                                copia_matriz_adjacencia,
                                numero_da_aresta,
                                caminho_euleriano)
                else:
                    if copia_matriz_adjacencia[line_counter][posicao_vertice_na_lista] != self.SEPARADOR_ARESTA:
                        if copia_matriz_adjacencia[line_counter][posicao_vertice_na_lista] > 0:
                            copia_matriz_adjacencia[line_counter][posicao_vertice_na_lista] -= 1
                            novo_vertice = self.N[line_counter]
                            caminho_euleriano += [novo_vertice, f'a{numero_da_aresta}']
                            numero_da_aresta += 1
                            return self.caminho_euleriano_entre_dois_vertices(
                                novo_vertice,
                                vertices_impares,
                                copia_matriz_adjacencia,
                                numero_da_aresta,
                                caminho_euleriano)
            return None

    def caminho_euleriano_para_zero_impares(self):
        for i in range(len(self.N)):
            for j in range(i, len(self.N)):
                lista_vertices_impares = [self.N[i], self.N[j]]
                caminho_para_zero_impares = self.caminho_euleriano_entre_dois_vertices(lista_vertices_impares[0],
                                                                                     lista_vertices_impares,
                                                                                     deepcopy(self.M))
                if caminho_para_zero_impares is None:
                    caminho_para_zero_impares = self.caminho_euleriano_entre_dois_vertices(lista_vertices_impares[-1],
                                                                                         lista_vertices_impares,
                                                                                         deepcopy(self.M))
                    if caminho_para_zero_impares is not None:
                        return caminho_para_zero_impares
                else:
                    return caminho_para_zero_impares

        raise ErroNoRetornoDeCaminhoEulerianoException

    def caminho_euleriano(self):
        qtd_impares = self.há_caminho_euleriano()
        if qtd_impares < 0:
            return []

        if qtd_impares == 2:
            vertices_impares = self.encontrar_dupla_de_vertices_impares()
            primeiro_vertices_impar = vertices_impares[0]
            caminho_euleriano_para_primeiro_impar = self.caminho_euleriano_entre_dois_vertices(primeiro_vertices_impar,
                                                                                             vertices_impares,
                                                                                             deepcopy(self.M))
            if caminho_euleriano_para_primeiro_impar is None:
                segundo_vertice_impar = vertices_impares[-1]
                caminho_euleriano_para_segundo_impar = self.caminho_euleriano_entre_dois_vertices(segundo_vertice_impar,
                                                                                                vertices_impares,
                                                                                                deepcopy(self.M))
                return caminho_euleriano_para_segundo_impar
            else:
                return caminho_euleriano_para_primeiro_impar
        else:
            return self.caminho_euleriano_para_zero_impares()
