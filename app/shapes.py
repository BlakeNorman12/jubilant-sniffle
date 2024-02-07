
class Shapes:

    def __init__(self, base, height, radius):
        self.base = base
        self.height = height
        self.radius = radius


    def calculate_area(self):
        print("hello")
        pass

class Triangle(Shapes):
    
    def __init__(self, base, height):
        super().__init__(base, height, 0.0)

    def calculate_area(self):
        return ((self.base * self.height) / 2)

#First method tested
class Rectangle(Shapes):
    
    def __init__(self, base, height):
        super().__init__(base, height, 0.0)

    def calculate_area(self):
        return self.base * self.height

class Circle(Shapes):
    
    def __init__(self, base, height, radius):
        super().__init__(base, height, radius)

    def calculate_area(self):
        return (self.radius * self.radius * 3.14)