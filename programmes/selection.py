def selection(table):
    comparaison = 0
    affectation = 0

    for i in range(len(table) - 1):
        swap = False
        min = table[i]

        for j in range(i + 1, len(table)):
            if (table[j] < min):
                min = table[j]
                indexMin = j
                swap = True
            comparaison += 1

        if swap:
            table[i], table[indexMin] = table[indexMin], table[i]
            affectation += 3

    operation = comparaison + affectation
    return operation
