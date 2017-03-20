class Diff(object):
    def __init__(self, f, h=1E-4):
        self._f = f
        self._h = h

    def __call__(self, x):
        top = self._f(x + self._h) - self._f(x)
        return top / self._h

def f(x):
    return 0.25*x**4

df = Diff(f)
for x in (1,5,10):
    df_value = df(x)
    print df_value