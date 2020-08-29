def generate_cycle_array(root, possibleCycleArrayWithAllVertexesExceptFirstRoot):
    cycleArray = list()
    for element in possibleCycleArrayWithAllVertexesExceptFirstRoot:
        if element != root:
            cycleArray.append(element)
    return [root] + cycleArray + [root]
