class Duck:
    def talk(self):
        print("This duck is talking")

    def walk(self):
        print("This duck is talking")

class Chicken:
    def talk(self):
        print("This chicken is talking")

    def walk(self):
        print("This chicken is talking")

class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You got the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)