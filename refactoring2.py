def find_cycle(graph, root, visited=None, backtrack=None):
    if root not in graph.N:
        return False

    if visited is None:
        visited, backtrack = list(), list()

    if root not in visited:
        visited.append(root)

    for edgeId in graph.A.keys():
        if edgeId not in visited:
            value = graph.A[edgeId].split('-')
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
            value = graph.A[edgeId].split('-')
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