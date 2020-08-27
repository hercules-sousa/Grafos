def get_cycle(graph, array):
    for position in range(len(array)):
        arrayWithAllVertexesExceptFirstRoot = array[position + 1: len(array)]

        if array[position] in arrayWithAllVertexesExceptFirstRoot:
            return remove_false_connections(graph, [array[position]] + [j for j in arrayWithAllVertexesExceptFirstRoot if j != array[position]] + [array[position]])