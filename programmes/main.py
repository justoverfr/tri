from functions import *

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
