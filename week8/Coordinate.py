class Coordinate(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
