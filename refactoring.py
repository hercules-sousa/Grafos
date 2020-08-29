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


def generate_cycle_array(root, possibleCycleArrayWithAllVertexesExceptFirstRoot):
    cycleArray = list()
    for element in possibleCycleArrayWithAllVertexesExceptFirstRoot:
        if element != root:
            cycleArray.append(element)
    return [root] + cycleArray + [root]



def check_whether_there_is_cycle(graph, possibleCycleArray):
    for position in range(len(possibleCycleArray)):
        possibleCycleArrayWithAllVertexesExceptFirstRoot = possibleCycleArray[position + 1: len(possibleCycleArray)]

        if possibleCycleArray[position] in possibleCycleArrayWithAllVertexesExceptFirstRoot:
            root = possibleCycleArray[position]
            return remove_false_connections(graph, generate_cycle_array(root, possibleCycleArrayWithAllVertexesExceptFirstRoot))


def get_array_of_walk(graph, root, visited=None, backtrack=None):
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
                return check_whether_there_is_cycle(graph, visited)
            elif secondVertex == root and firstVertex in visited:
                visited.append(edgeId), visited.append(firstVertex)
                return check_whether_there_is_cycle(graph, visited)

    for edgeId in graph.A.keys():
        if edgeId not in visited:
            firstVertex = graph.A[edgeId].split('-')[0]
            secondVertex = graph.A[edgeId].split('-')[-1]
            if firstVertex == root and secondVertex not in visited:
                visited.append(edgeId)
                backtrack.append(root)
                return get_array_of_walk(graph, secondVertex, visited, backtrack)
            elif secondVertex == root and firstVertex not in visited:
                visited.append(edgeId)
                backtrack.append(root)
                return get_array_of_walk(graph, firstVertex, visited, backtrack)

    if len(backtrack) > 0:
        return get_array_of_walk(graph, backtrack.pop(), visited, backtrack)
    else:
        return False


def ha_ciclo(graph):
    if len(graph.N) == 0:
        return False

    cycle = None

    for vertex in graph.N:
        cycle = get_array_of_walk(graph, vertex)

        if cycle:
            return cycle

    return False


grafo1 = Grafo(list("ABCDE"), {"1": "A-B", "2": "B-C", "3": "C-D", "4": "D-E", "5": "E-C"})


print(ha_ciclo(grafo1))