# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "tomás CAETANO!"

# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name.split(' ')[0]
# listLenght = len(name.split(' '))
# last_name = name.split(' ')[listLenght-1]
# print(f'last_name: {last_name}')
# print(f'name: {name}')
first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]
# print(f'first name: {first_name}')
print(f'last name: {last_name}')
print(f'last character: {last_character}')
