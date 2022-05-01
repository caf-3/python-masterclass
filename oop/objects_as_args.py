class Car:
    color = None

def change_color(car, color):
    car.color = color

car = Car()
change_color(car, 'purple')
print(car.color)