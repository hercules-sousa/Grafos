def getConnectionsDict(graph):
    conexionsDict = dict()

    for vertex in graph.N:
        connected = list()

        for edge in graph.A.values():
            firstVertexOfEdge = edge.split('-')[0]
            secondVertexOfEdge = edge.split('-')[-1]
            if vertex == firstVertexOfEdge:
                connected.append(secondVertexOfEdge)
            elif vertex == secondVertexOfEdge:
                connected.append(firstVertexOfEdge)

        conexionsDict[vertex] = connected[:]

    return conexionsDict


def dfs(graph, root):
    if root not in graph.N or len(graph.N) == 0:
        return list()

    conexionsDict = getConnectionsDict(graph)

    return dfs_search(conexionsDict, root, graph.A)


def generateListOfUnvisitedVetexes(visited, vertexesConnectedWithRoot):
    unvisitedVertexes = []
    for vertex in vertexesConnectedWithRoot:
        if vertex not in visited:
            unvisitedVertexes.append(vertex)
    return unvisitedVertexes


def isEdgeId(element, edges):
    if element in edges:
        return True
    return False


def dfs_search(conexionsDict, root, edges, visited=None):
    if visited is None:
        visited = list()

    if root not in visited:
        visited.append(root)

    unvisitedVertexes = generateListOfUnvisitedVetexes(visited, conexionsDict[root])

    for vertexStillToVisit in unvisitedVertexes:
        for edgeId, edge in edges.items():
            if edgeId not in visited and vertexStillToVisit not in visited:
                lastElementInVisited = visited[-1]
                edgesIdList = edges.keys()
                if not isEdgeId(lastElementInVisited, edgesIdList):
                    firstVertexOfEdge = edge.split('-')[0]
                    secondVertexOfEdge = edge.split('-')[-1]
                    if firstVertexOfEdge == root and secondVertexOfEdge == vertexStillToVisit:
                        visited.append(edgeId)
                    elif secondVertexOfEdge == root and firstVertexOfEdge == vertexStillToVisit:
                        visited.append(edgeId)

        dfs_search(conexionsDict, vertexStillToVisit, edges, visited)

    return visited