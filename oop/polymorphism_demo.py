
import math
class Shape:
    """Base class for different shapes."""

    def area(self):
        """Method to compute the area of a shape."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle shape with length and width."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Circle shape with a radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)