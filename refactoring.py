# from Roteiro3 import *
from grafo import Grafo


def remove_false_connections(graph, array):
    for x in range(len(array) - 2, 0, -2):
        edge = graph.A[array[x]].split('-')

        if edge[0] != array[x - 1] and edge[-1] != array[x - 1]:
            return [array[-1]] + array[x: len(array)]

    return array


def get_cycle(graph, array):
    for position in range(len(array)):
        arrayWithAllVertexesExceptFirstRoot = array[position + 1: len(array)]

        if array[position] in arrayWithAllVertexesExceptFirstRoot:
            return remove_false_connections(graph, [array[position]] + [j for j in arrayWithAllVertexesExceptFirstRoot if j != array[position]] + [array[position]])

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


grafo1 = Grafo(list("ABCD"), {"1": "A-B", "2": "B-C", "3": "A-C", "4": "A-D"})


print(ha_ciclo(grafo1))