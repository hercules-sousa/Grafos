# from Roteiro3 import *
from grafo import Grafo


from DFS import getConnectionsDict

def neighbors(graph, root):
    result = list()
    connectionsDict = getConnectionsDict(graph)
    rootNeighbors = getConnectionsDict(graph)[root]
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


grafo1 = Grafo(list("ABCDE"), {"1": "A-B", "2": "B-C", "3": "C-D", "4": "D-E", "5": "E-C"})


print(caminho(grafo1, 4))