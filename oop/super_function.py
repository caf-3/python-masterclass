class Rectange:

    def __init__(self, width, length):
        self.width = width
        self.length = length

class Square(Rectange):

    def __init__(self, width, length):
        super().__init__(width, length)
        
    def area(self):
        return self.length * self.width

class Cube(Rectange):

    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height

    def volume(self):
        return self.height * self.length * self.width

square = Square(10, 6)
cube = Cube(7, 8, 4)

print(square.area())
print(cube.volume())