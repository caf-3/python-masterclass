double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: f'{first_name} {last_name}'
age_check = lambda age: True if age >= 18 else False

print('Double: ', double(5))
print('Multiple: ', multiply(7, 8))
print('add: ', add(1, 2, 3))
print('full name: ', full_name('Julião', 'Estevão'))
print('age check: ', age_check(19))