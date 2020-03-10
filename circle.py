from math import pi


class Circle:

    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = 2 * radius

    def __repr__(self):
        return f"Circle({int(self.radius)})"

    @property
    def area(self):
        return pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
        self._diameter = diameter

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
        self._diameter = 2 * radius
