def bulles(table):
    comparaison = 0
    affectation = 0

    max = len(table) - 1
    isTableSorted = False
    while not isTableSorted:
        isTableSorted = True

        for i in range(max):
            if table[i] > table[i+1]:

                table[i], table[i+1] = table[i+1], table[i]
                affectation += 3
                isTableSorted = False

                max = i

            comparaison += 1

    operation = comparaison + affectation
    return operation
