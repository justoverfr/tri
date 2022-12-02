from functions import *

# 3.b
print("EXERCICE 3.b\n")

size = 10

print("Il faut ", selection(generateBestTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri par sélection dans le meilleur des cas.")
print("Il faut ", selection(generateWorstTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri par sélection dans le pire des cas.\n")

print("Il faut ", insertion(generateBestTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri par insertion dans le meilleur des cas.")
print("Il faut ", insertion(generateWorstTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri par insertion dans le pire des cas.\n")

print("Il faut ", bulles(generateBestTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri à bulles dans le meilleur des cas.")
print("Il faut ", bulles(generateWorstTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri à bulles dans le pire des cas.\n")

print("Il faut ", bullesOpti(generateBestTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri à bulles optimisé dans le meilleur des cas.")
print("Il faut ", bullesOpti(generateWorstTable(size, 0, 100)),
      " opérations pour trier un tableau de", size, "éléments avec la méthode de tri à bulles optimisé dans le pire des cas.\n")


# 3.c
print("EXERCICE 3.c\n")

min = 10
max = 20
step = 5
nbr = 10

print("Sélection\n")
stats(min, max, step, nbr, selection)

print("Insertion\n")
stats(min, max, step, nbr, insertion)

print("Bulles\n")
stats(min, max, step, nbr, bulles)

print("Bulles optimisé\n")
stats(min, max, step, nbr, bullesOpti)
