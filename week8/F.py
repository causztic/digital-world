import math

class F(object):
    def __init__(self, a=0, w=0):
        self.a = a
        self.w = w

    def __call__(self, x):
        return math.exp(-self.a * x) * math.sin(self.w * x)

f = F(a=1.0, w=0.1)
print f(x=math.pi)