
class Shapes:

    def __init__(self, base, height, radius):
        self.base = base
        self.height = height
        self.radius = radius


    def calculate_area(self):
        print("hello")
        pass

class Triangle(Shapes):
    pass

#First method tested
class Rectangle(Shapes):
    
    def __init__(self, base, height):
        super().__init__(base, height, 0.0)

    def calculate_area(self):
        return self.base * self.height

class Circle(Shapes):
    pass
