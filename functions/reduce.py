import functools
from math import factorial

letters = ['T', 'O', 'M', 'A', 'S']

word = functools.reduce(lambda x, y: x+y, letters)
nums = [6, 5, 4, 3, 2, 1]
num_factorial = functools.reduce(lambda x, y: x * y, nums)

print(num_factorial)