''' Part A'''


def stc(s1, s2):
    return abs(len(s1) - len(s2))


def sumVal(d):
    s = 0
    if d:
        for key, value in d.iteritems():
            if key < 3:
                s += value
        return s
    else:
        return None


def count(a, b, c):
    return len(range(a, b)) > len(range(b, c))

'''Part B'''


def getMRT(f):
    d = {}
    lines = map(lambda x: x.strip(), f.readlines())
    for line in lines:
        items = map(lambda x: x.strip(), line.split(","))
        d[items[0]] = items[1:]
    return d


def distance(d, s):
    if s:
        values = s.split(",")
        if len(values) == 1:
            return -1
        current_line = ""
        for key, value in d.iteritems():
            if values[0] in value and values[1] in value:
                current_line = key
                break
        if current_line:
            stations = set(values) & set(d[current_line])
            if len(stations) == 2:
                return abs(d[current_line].index(values[1]) - d[current_line].index(values[0]))
            else:
                return -1
        else:
            return -1
    else:
        return -2


class Matrix(object):

    def __init__(self, m, s="Matrix A", f="%6.2f"):
        self.m = m
        self.s = s
        self.f = f

    def __str__(self):
        s = "%s: Rows: %i Columns: %i\n" % (
            self.s, len(self.m), len(self.m[0]))
        for j in self.m:
            for i in j:
                s += self.f % i
            s += "\n"
        return s

    def all_other_zeroes(self, locs):
        pass

    def diag(self):
        for n in range(len(self.m)):
            if self.m[n][n] == 0:
                return False
        return True

    def upperDiag(self):
        row = 0
        while row < len(self.m) - 1:
            upper_triangle = [self.m[row][n]
                              for n in range(row + 1, len(self.m))]
            if upper_triangle[0] == 0:
                return False
            else:
                for item in upper_triangle[1:]:
                    if item != 0:
                        return False
            row += 1
        return True

    def lowerDiag(self):
        row = 1
        while row < len(self.m):
            lower_triangle = [self.m[row][n]
                              for n in range(0, row)]
            if lower_triangle[-1] == 0:
                return False
            else:
                for item in lower_triangle[:-1]:
                    if item != 0:
                        return False
            row += 1
        return True

    def triDiag(self):
        return self.lowerDiag() and self.upperDiag() and self.diag()
