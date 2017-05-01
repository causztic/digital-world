#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

class Parallelogram(object):

    def __init__(self, side1, side2, diagonal):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.set_diagonal(diagonal)

    def get_diagonal(self):
        return self._diagonal

    def set_diagonal(self, value):
        val = float(value)
        if val > 0:
            self._diagonal = val
        else:
            self._diagonal = 0

    def __str__(self):
        return "%.2f" % self.diagonal

    def __call__(self):
        return (self.side1 + self.side2) > self.diagonal and (self.side1 + self.diagonal) > self.side2 and (self.side2 + self.diagonal) > self.side1
    
    def calc_area(self):
        s = (self.side1 + self.side2 + self.diagonal) / 2
        return round(2 * (( s * ( s - self.side1 ) * (s - self.side2 ) * (s - self.diagonal)) ** 0.5), 2)

    diagonal = property(get_diagonal, set_diagonal)

class Rhombus(Parallelogram):
    def __call__(self):
        return self.side1 == self.side2

class Rectangle(Parallelogram):
    def __call__(self):
        return self.side1 == self.side2


class Square(Rectangle):
    def __call__(self):
        return self.side1 == self.side2 and (self.side1 ** 2 + self.side2 ** 2) ** 0.5 == self.diagonal
