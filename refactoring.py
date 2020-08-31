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


grafo1 = Grafo(list("ABCDE"), {"1": "A-B", "2": "B-C", "3": "C-D", "4": "D-E", "5": "E-C"})


print(ha_ciclo(grafo1))