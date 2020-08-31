# Alunos: Matheus Alves da Silva e Hércules de Sousa Silva

# from Roteiro3 import *
from grafo import Grafo

from roteiro2 import getConnectionsDict


def remove_false_connections(graph, array):
    for position in range(len(array) - 2, 0, -2):
        edge = graph.A[array[position]].split('-')
        firstVertex = edge[0]
        secondVertex = edge[-1]
        if firstVertex != array[position - 1] and secondVertex != array[position - 1]:
            return [array[-1]] + array[position: len(array)]

    return array


def generate_cycle_array(root, possibleCycleArrayWithAllVertexesExceptFirstRoot):
    cycleArray = list()
    for element in possibleCycleArrayWithAllVertexesExceptFirstRoot:
        if element != root:
            cycleArray.append(element)
    return [root] + cycleArray + [root]


def check_whether_there_is_cycle_in_possible_cycle_array(graph, possibleCycleArray):
    for position in range(len(possibleCycleArray)):
        possibleCycleArrayWithAllVertexesExceptFirstRoot = possibleCycleArray[position + 1: len(possibleCycleArray)]

        if possibleCycleArray[position] in possibleCycleArrayWithAllVertexesExceptFirstRoot:
            root = possibleCycleArray[position]
            cycle = generate_cycle_array(root, possibleCycleArrayWithAllVertexesExceptFirstRoot)
            return remove_false_connections(graph, cycle)


def get_array_of_possible_cycle(graph, root, possibleCycleArray=None, backtrack=None):
    if root not in graph.N:
        return False

    if possibleCycleArray is None:
        possibleCycleArray, backtrack = list(), list()

    if root not in possibleCycleArray:
        possibleCycleArray.append(root)

    for edgeId in graph.A.keys():
        if edgeId not in possibleCycleArray:
            firstVertex = graph.A[edgeId].split('-')[0]
            secondVertex = graph.A[edgeId].split('-')[-1]
            if firstVertex == root and secondVertex in possibleCycleArray:
                possibleCycleArray.append(edgeId)
                possibleCycleArray.append(secondVertex)
                return check_whether_there_is_cycle_in_possible_cycle_array(graph, possibleCycleArray)
            elif secondVertex == root and firstVertex in possibleCycleArray:
                possibleCycleArray.append(edgeId)
                possibleCycleArray.append(firstVertex)
                return check_whether_there_is_cycle_in_possible_cycle_array(graph, possibleCycleArray)

    for edgeId in graph.A.keys():
        if edgeId not in possibleCycleArray:
            firstVertex = graph.A[edgeId].split('-')[0]
            secondVertex = graph.A[edgeId].split('-')[-1]
            if firstVertex == root and secondVertex not in possibleCycleArray:
                possibleCycleArray.append(edgeId)
                backtrack.append(root)
                return get_array_of_possible_cycle(graph, secondVertex, possibleCycleArray, backtrack)
            elif secondVertex == root and firstVertex not in possibleCycleArray:
                possibleCycleArray.append(edgeId)
                backtrack.append(root)
                return get_array_of_possible_cycle(graph, firstVertex, possibleCycleArray, backtrack)

    if len(backtrack) > 0:
        return get_array_of_possible_cycle(graph, backtrack.pop(), possibleCycleArray, backtrack)
    else:
        return False


def ha_ciclo(graph):
    if len(graph.N) == 0:
        return False

    for vertex in graph.N:
        cycle = get_array_of_possible_cycle(graph, vertex)

        if cycle:
            return cycle

    return False


def neighbors(graph, root):
    connectionsDict = getConnectionsDict(graph)
    rootNeighbors = connectionsDict[root]
    return rootNeighbors


def get_edges(graph, array):
    result = list()

    for x in range(len(array)):
        current = list()

        for i in range(len(array[x])):
            current.append(array[x][i])

            if i < len(array[x]) - 1:
                for j in graph.A.keys():
                    value = graph.A[j].split('-')

                    if value[0] == array[x][i] and value[-1] == array[x][i + 1]:
                        current.append(j)
                        break
                    if value[0] == array[x][i + 1] and value[-1] == array[x][i]:
                        current.append(j)
                        break

        result.append(current)

    return result


def root_paths(graph, root, size, ex=None):
    if ex is None:
        ex = {root}
    else:
        ex.add(root)

    if size == 0:
        return [[root]]

    paths = [[root] + way for x in neighbors(graph, root) if x not in ex for way in root_paths(graph, x, size - 1, ex)]

    ex.remove(root)

    return paths


def caminho(graph, length):
    if length > len(graph.A):
        return list()

    result = list()

    for root in graph.N:
        try:
            result = get_edges(graph, root_paths(graph, root, length))[0]

            if len(result) == length * 2 + 1:
                return result
        except IndexError:
            pass

    return result


def caminho_dois_vertices(graph, x, y, visited=None):
    if visited is None:
        visited = list()

    combinations = list()
    visited.append(x)

    for i in graph.A.values():
        value = i.split('-')

        if value[0] == x:
            if value[-1] == y:
                return True
        elif value[-1] == x:
            if value[0] == y:
                return True

    for i in graph.A.values():
        value = i.split('-')

        if value[0] == x:
            if value[-1] not in visited:
                combinations += [caminho_dois_vertices(graph, value[-1], y, visited)]
        elif value[-1] == x:
            if value[0] not in visited:
                combinations += [caminho_dois_vertices(graph, value[0], y, visited)]

    return any(combinations)


def conexo(graph):
    if len(graph.N) == 0:
        return False

    for i in range(len(graph.N)):
        for j in range(i + 1, len(graph.N)):
            if not caminho_dois_vertices(graph, graph.N[i], graph.N[j]):
                return False

    return True


