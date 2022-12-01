from random import *
from selection import *
from insertion import *
from bulles import *
from bullesOpti import *


def generateTable(size, min, max):
    table = []
    for i in range(size):
        table.append(randint(min, max))
    return table


def generateBestTable(size, min, max):
    table = generateTable(size, min, max)
    table.sort()
    return table


def generateWorstTable(size, min, max):
    table = generateTable(size, min, max)
    table.sort(reverse=True)
    return table


def stats(min, max, step, nbr, sortingMethod):
    for i in range(min, max + step, step):

        mean = 0
        for j in range(nbr):
            randomTab = generateTable(i, 0, 100)
            mean += sortingMethod(randomTab)
        mean /= nbr

        print("Taille du tableau :", i, " Moyenne :", mean)
