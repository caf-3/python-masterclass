# Dictionary = A changeable, unordered collection of unique key:value pairs
#              They are fast because thei use hashing, allowing us to access a value kickly

capitals = { 'Portugal': 'Lisbon', 'Spain': 'Madrid', 'Mozambique': 'Maputo', 'Brazil': 'Brasilia'}

capitals.update({'Germany': 'Berlin'})
capitals.update({ 'Mozambique': 'Maputo Provincia'})

# print(capitals.items())
# print(capitals['Portugal'])
# print(capitals['Angola'])
# print(capitals.get('Angola'))
# print(capitals.keys())
# print(capitals.values())

for key, value in capitals.items():
    print(f'{key} -> {value}')