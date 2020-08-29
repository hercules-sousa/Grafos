# Alunos: Matheus Alves da Silva e Hércules de Sousa Silva


# from Roteiro3 import *
from grafo import Grafo


def remove_false_connections(graph, array):
    for position in range(len(array) - 2, 0, -2):
        edge = graph.A[array[position]].split('-')
        firstVertex = edge[0]
        secondVertex = edge[-1]
        if firstVertex != array[position - 1] and secondVertex != array[position - 1]:
            return [array[-1]] + array[position: len(array)]

    return array


def dunnoWhatCallIt(possibleCycleArray, position, possibleCycleArrayWithAllVertexesExceptFirstRoot):
    genericList = list()
    for element in possibleCycleArrayWithAllVertexesExceptFirstRoot:
        if element != possibleCycleArray[position]:
            genericList.append(element)
    return [possibleCycleArray[position]] + genericList + [possibleCycleArray[position]]


def get_cycle(graph, possibleCycleArray):
    for position in range(len(possibleCycleArray)):
        possibleCycleArrayWithAllVertexesExceptFirstRoot = possibleCycleArray[position + 1: len(possibleCycleArray)]

        if possibleCycleArray[position] in possibleCycleArrayWithAllVertexesExceptFirstRoot:
            return remove_false_connections(graph,
                                            dunnoWhatCallIt(
                                                possibleCycleArray,
                                                position,
                                                possibleCycleArrayWithAllVertexesExceptFirstRoot)
                                            )


def find_cycle(graph, root, visited=None, backtrack=None):
    if root not in graph.N:
        return False

    if visited is None:
        visited, backtrack = list(), list()

    if root not in visited:
        visited.append(root)

    for edgeId in graph.A.keys():
        if edgeId not in visited:
            firstVertex = graph.A[edgeId].split('-')[0]
            secondVertex = graph.A[edgeId].split('-')[-1]
            if firstVertex == root and secondVertex in visited:
                visited.append(edgeId), visited.append(secondVertex)
                return get_cycle(graph, visited)
            elif secondVertex == root and firstVertex in visited:
                visited.append(edgeId), visited.append(firstVertex)
                return get_cycle(graph, visited)

    for edgeId in graph.A.keys():
        if edgeId not in visited:
            firstVertex = graph.A[edgeId].split('-')[0]
            secondVertex = graph.A[edgeId].split('-')[-1]
            if firstVertex == root and secondVertex not in visited:
                visited.append(edgeId)
                backtrack.append(root)
                return find_cycle(graph, secondVertex, visited, backtrack)
            elif secondVertex == root and firstVertex not in visited:
                visited.append(edgeId)
                backtrack.append(root)
                return find_cycle(graph, firstVertex, visited, backtrack)

    if len(backtrack) > 0:
        return find_cycle(graph, backtrack.pop(), visited, backtrack)
    else:
        return False


def ha_ciclo(graph):
    if len(graph.N) == 0:
        return False

    cycle = None

    for vertex in graph.N:
        cycle = find_cycle(graph, vertex)

        if cycle:
            return cycle

    return False


def neighbors(graph, root):
    result = list()

    for i in graph.A.keys():
        value = graph.A[i].split('-')

        if value[0] == root:
            result.append(value[-1])
        elif value[-1] == root:
            result.append(value[0])

    return result


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
    if length >= len(graph.N):
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


