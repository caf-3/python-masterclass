import random

random_int = random.randint(5, 22)

random_num = random.random()

myList = ['Rock', 'Papper', 'Scissors']

myChoice = random.choice(myList)

cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)