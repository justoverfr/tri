def bullesOpti(table):
    comparaison = 0
    affectation = 0

    indexMin = 0
    indexMax = len(table) - 1
    isTableSorted = False
    while not isTableSorted:
        isTableSorted = True

        for i in range(indexMin, indexMax):
            if table[i] > table[i+1]:

                table[i], table[i+1] = table[i+1], table[i]
                affectation += 3

                if (isTableSorted):
                    indexMin = max(i - 1, 0)
                    isTableSorted = False
                indexMax = i

            comparaison += 1

    operation = comparaison + affectation
    return operation
