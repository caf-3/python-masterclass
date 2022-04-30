class Organism:
    is_alive = True

class Animal(Organism):
    def eat(self):
        print('This organism is eating')

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()

print(dog.is_alive)
dog.eat()
dog.bark()