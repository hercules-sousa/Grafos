def get_cycle(graph, possibleCycleArray):
    for position in range(len(possibleCycleArray)):
        possibleCycleArrayWithAllVertexesExceptFirstRoot = possibleCycleArray[position + 1: len(possibleCycleArray)]

        if possibleCycleArray[position] in possibleCycleArrayWithAllVertexesExceptFirstRoot:
            return remove_false_connections(graph, [possibleCycleArray[position]] + [j for j in possibleCycleArrayWithAllVertexesExceptFirstRoot if j != possibleCycleArray[position]] + [possibleCycleArray[position]])
