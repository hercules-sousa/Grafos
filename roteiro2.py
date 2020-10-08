# Dupla: Matheus Alves da Silva; Hércules de Sousa Silva


def dfs(graph, root):
    if root not in graph.N or len(graph.N) == 0:
        return list()

    new = dict()

    for i in graph.N:
        connected = list()

        for j in graph.A.values():
            if i == j.split('-')[0]:
                connected.append(j.split('-')[-1])
            elif i == j.split('-')[-1]:
                connected.append(j.split('-')[0])

        new[i] = connected[:]

    return dfs_search(new, root, graph.A)


def dfs_search(graph, root, edges, visited=None):
    if visited is None:
        visited = list()

    if root not in visited:
        visited.append(root)

    for vertex in [x for x in graph[root] if x not in visited]:
        for i, j in edges.items():
            if i not in visited and visited[-1] not in edges and vertex not in visited:
                if j.split('-')[0] == root and j.split('-')[-1] == vertex:
                    visited.append(i)
                elif j.split('-')[-1] == root and j.split('-')[0] == vertex:
                    visited.append(i)

        dfs_search(graph, vertex, edges, visited)

    return visited
