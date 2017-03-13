import math


class Circle(object):

    def __init__(self, radius = 1):
        self.radius = radius

    def __eq__(self, other):
      return self.radius == other.radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return math.pi * self.radius * 2