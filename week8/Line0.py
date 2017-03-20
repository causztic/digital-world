class Line0(object):

    def __init__(self, p1, p2):
        self.p1 = map(lambda x: float(x), p1)
        self.p2 = map(lambda x: float(x), p2)

    def __call__(self, x):
        m = (self.p1[1] - self.p2[1]) / (self.p1[0] - self.p2[0])
        c = self.p1[1] - m * self.p1[0]
        return m * x + c

line = Line0((0,-1), (2,4))
print line(0.5), line(0), line(1)