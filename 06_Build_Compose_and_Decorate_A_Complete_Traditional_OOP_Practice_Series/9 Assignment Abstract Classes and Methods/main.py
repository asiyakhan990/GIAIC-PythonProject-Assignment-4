from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


try:
    shape = Shape()  
except TypeError as e:
    print(f"Error: {e}")

rect = Rectangle(10, 5)
print("\nRectangle Area Calculation:")
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")
print(f"Area: {rect.area()}")
