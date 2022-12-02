def insertion(table):
    comparaison = 0
    affectation = 0

    max = table[0]
    for i in range(1, len(table)):
        if table[i] > max:
            max = table[i]
        else:
            for j in range(i - 1, -1, -1):
                if table[j] < table[i]:
                    newPosition = j + 1
                    break
                comparaison += 1
                if j == 0:
                    newPosition = 0
            table.insert(newPosition, table.pop(i))
            affectation += 1
        comparaison += 1

    operation = comparaison + affectation
    return operation
