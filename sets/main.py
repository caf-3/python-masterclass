# set = A collection which is unordered, unindexed and with no duplated values

utensils = { "Garfo", "Faca", "Colher" }

pots = { "Copo", "Tigela", "Tirina", "Faca" }

utensils.add("Cortador de batatas")
utensils.remove("Faca")
utensils.clear()

pots.update(utensils)

new_set = pots.union(utensils)

print(f'New set {new_set}')

print(f'A diferença {pots.difference(utensils)}')
print(f'A intersessão {pots.intersection(utensils)}')

for x in pots:
    print(x, end=", ")