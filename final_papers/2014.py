import math
from libdw import sm


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

# pline = Polyline2D(Point2D(1, 2), [Vector2D(3, 1)])
# pline.addSegment(Vector2D(1, 0))
# pline.addSegment(Vector2D(0, 2))
# print pline.length()
# for i in range(4):
#     print pline.vertex(i)


class CombLock(sm.SM):

    def __init__(self, combo):
        self.combo = combo
        self.startState = []

    def getNextValues(self, state, inp):
        nextState = state[:]
        output = "locked"
        if inp >= 1 and inp <= 9:
            nextState.append(inp)
        elif inp == -1:
            if nextState == self.combo:
                output = "unlocked"
            nextState = []

        return nextState, output


def mapT2P(x, y):
    if 0 <= x and x <= 3:
        if 0 <= y and y <= 3:
            return 1
        if 4 <= y and y <= 7:
            return 4
        if 8 <= y and y <= 11:
            return 7
    if 4 <= x and x <= 7:
        if 0 <= y and y <= 3:
            return 2
        if 4 <= y and y <= 7:
            return 5
        if 8 <= y and y <= 11:
            return 8
    if 8 <= x and x <= 11:
        if 0 <= y and y <= 3:
            return 3
        if 4 <= y and y <= 7:
            return 6
        if 8 <= y and y <= 11:
            return 9

class TouchMap(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        output = -1
        (e, x, y) = inp
        nextState = mapT2P(x, y)
        if e == "TouchDown" or e == "TouchUpdate":
            if state == nextState:
                output = 0
            else:
                output = nextState 
        #elif e == "TouchUp":
        return nextState, output

# lock = CombLock([1, 2, 5])
# print lock.transduce([1, 2, 5, -1])
# print lock.transduce([1, 0, 2, 5, -1])
# print lock.transduce([3, 2, 5, -1])
# print lock.transduce([1, 2, 5, -1, 1, 2, 5, -1])
# print lock.transduce([3, 2, 5, -1, 1, 2, 5, -1])

m = TouchMap()
print m.transduce([('TouchDown',2,2), ('TouchUpdate',3,3), ('TouchUp',4,4)])
print m.transduce([('TouchDown',3,3), ('TouchUpdate',4,3), ('TouchUp',4,4)])