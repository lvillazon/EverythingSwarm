import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        m = self.magnitude()
        self.x /= m
        self.y /= m
