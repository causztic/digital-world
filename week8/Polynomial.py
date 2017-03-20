class Polynomial(object):

    def __init__(self, coeff=[]):
        self.coeff = coeff

    def __add__(self, other):
        s = len(self.coeff)
        o = len(other.coeff)
        return Polynomial([(self.coeff[i] if i < s else 0) + (other.coeff[i] if i < o else 0) for i in range(max(s, o))])

    def __sub__(self, other):
        s = len(self.coeff)
        o = len(other.coeff)
        return Polynomial([(self.coeff[i] if i < s else 0) - (other.coeff[i] if i < o else 0) for i in range(max(s, o))])

    def __mul__(self, other):
        l = [0 for i in range(len(self.coeff) + len(other.coeff) - 1)]
        for i, c in enumerate(self.coeff):
            for j, d in enumerate(other.coeff):
                l[i+j] += c * d
        return Polynomial(l)

    def differentiate(self):
        for idx, item in enumerate(self.coeff):
            self.coeff[idx] = item * idx

        self.coeff = self.coeff[1:]

    def derivative(self):
        c = []
        for idx, item in enumerate(self.coeff):
            c.append(item * idx)

        return Polynomial(c[1:])

    def __call__(self, x):
        val = 0
        for idx, item in enumerate(self.coeff):
            val += item * x ** idx
        return val


p1 = Polynomial ([1 , -1])
p2 = Polynomial ([0 , 1 , 0 , 0 , -6 , -1])
p3 = p2 + p1
p4 = p1 * p2
p5 = p2.derivative()
print p5.coeff