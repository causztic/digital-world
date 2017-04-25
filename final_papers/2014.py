import math


class Point2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point2D(' + str(self.x) + "," + str(self.y) + ')'

    def add(self, vector):
        return Point2D(self.x + vector.dx, self.y + vector.dy)


class Vector2D(object):

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def length(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)


class Polyline2D(object):

    def __init__(self, start, vectors):
        self.start = start
        self.vectors = vectors

    def addSegment(self, vector):
        self.vectors.append(vector)

    def length(self):
        return sum([vector.length() for vector in self.vectors])
        # return reduce(lambda x, y: x + y, [vector.length() for vector in
        # self.vectors])

    def vertex(self, idx):
        current = 0
        point = self.start
        while current != idx:
            point = point.add(self.vectors[current])
            current += 1
        return point

pline = Polyline2D(Point2D(1,2), [Vector2D(3,1)])
pline.addSegment(Vector2D(1, 0))
pline.addSegment(Vector2D(0, 2))
print pline.length()
for i in range(4):
  print pline.vertex(i)