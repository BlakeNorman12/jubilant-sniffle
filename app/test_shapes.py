import unittest
from shapes import Rectangle  

class TestShapes(unittest.TestCase):

    def test_calculate_area(self):
        # Test case for the calculate_area method of the Rectangle class

        # Setup: Create an instance of Rectangle
        rect = Rectangle(10, 5)
        result = rect.calculate_area()
        self.assertEqual(result, 50, "The area of the rectangle should be 50")

if __name__ == '__main__':
    unittest.main()