import unittest
from shapes import Rectangle, Triangle, Circle  

class TestShapes(unittest.TestCase):

    def test_calculate_rect_area(self):
        # Test case for the calculate_area method of the Rectangle class
        # Create Comment
        # Setup: Create an instance of Rectangle
        rect = Rectangle(10, 5)
        result = rect.calculate_area()
        self.assertEqual(result, 50, "The area of the rectangle should be 50")

    def test_calculate_triangle_area(self):

        tri = Triangle(10, 2)
        result = tri.calculate_area()
        self.assertEqual(result, 10, "The area of the triangle should be 10")

    def test_calculate_circle_area(self):

        cir = Circle(0, 0, 5)
        result = cir.calculate_area()
        self.assertEqual(result, 78.5, "The area of the circle should be 78.5")
        
if __name__ == '__main__':
    unittest.main()