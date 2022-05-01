from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You are driving the car")

    def stop(self):
        print("You stopped the card")

    def drift(self):
        print("This car is drifting")

car = Car()
car.go()
car.drift()
car.stop()