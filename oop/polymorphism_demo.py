# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method to be overridden in subclasses"""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate area of rectangle: length × width"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Calculate area of circle: π × r²"""
        return math.pi * (self.radius ** 2)
