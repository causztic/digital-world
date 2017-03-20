import numpy


class Line(object):

    def __init__(self, c0=0, c1=0):
        self.set_c0(c0)
        self.set_c1(c1)

    def __call__(self, x):
        return float(self._c0) + float(self._c1) * x

    def get_c0(self):
        return self._c0

    def set_c0(self, c0):
        self._c0 = c0

    def get_c1(self):
        return self._c1

    def set_c1(self, c1):
        self._c1 = c1

    def table(self, L, R, n):
        if n > 0:
            t = ""
            if L == R:
                n = 1
            for x in numpy.linspace(L, R, n):
                t += "%10.2f%10.2f\n" % (x, self(x))
            return t
        else:
            return "Error in printing table"

line = Line(1,2)
print line(2)
print line.table(1,5,4)