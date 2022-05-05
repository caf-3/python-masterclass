class Car:
    
    def turn_on(self):
        print("You turn on the engine")
        return self

    def drive(self):
        print("You are driving the car")
        return self
    
    def brake(self):
        print("You tstep on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()