from functions import *

# 3.b
print("Il faut ", selection(generateBestTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri par sélection dans le meilleur des cas.")
print("Il faut ", selection(generateWorstTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri par sélection dans le pire des cas.\n")

print("Il faut ", insertion(generateBestTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri par insertion dans le meilleur des cas.")
print("Il faut ", insertion(generateWorstTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri par insertion dans le pire des cas.\n")

print("Il faut ", bulles(generateBestTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri à bulles dans le meilleur des cas.")
print("Il faut ", bulles(generateWorstTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri à bulles dans le pire des cas.\n")

print("Il faut ", bullesOpti(generateBestTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri à bulles optimisé dans le meilleur des cas.")
print("Il faut ", bullesOpti(generateWorstTable(10, 0, 100)),
      " opérations pour trier un tableau de 10 éléments avec la méthode de tri à bulles optimisé dans le pire des cas.\n")


# 3.c
min = 10
max = 20
step = 5
nbr = 10

print("Selection")
stats(min, max, step, nbr, selection)

print("\nInsertion")
stats(min, max, step, nbr, insertion)

print("\nBulles")
stats(min, max, step, nbr, bulles)

print("\nBulles optimisé")
stats(min, max, step, nbr, bullesOpti)
