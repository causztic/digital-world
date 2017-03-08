import cmath

def norm(z1, z2, z3):
    s = z1*z1.conjugate()
    s += z2*z2.conjugate()
    s += z3*z3.conjugate()
    return round(cmath.sqrt(s).real,3)

print norm(1+3j, -1+3j, -1-3j)
print norm(1+2j, -1+2j, -1-2j)
print norm(1+1j, -1+1j, -1-1j)

def factors(n):
    li = []
    for i in range(1,n+1):
        if (n % i == 0):
            li.append(i)
    return li

for test_num in [6,12,7,15,21,1,9]:
    print factors(test_num)

def combinations(n1, n2):
    result = []
    for i in range(n1, n2+1):
        for j in range(i+1, n2+1):
            result.append((i,j))
    return result, len(result)

print combinations(1,7)
print combinations(3,5)
print combinations(-1,2)
print combinations(0,0)

'''Part C'''
def readMatrix(f):
    pass

def mulRowByC(matOp, i, c):
    pass

def addRowMulBy(matOp, i, c, j):
    pass

def gaussElimination(data):
    pass