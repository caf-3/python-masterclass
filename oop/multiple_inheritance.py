class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

