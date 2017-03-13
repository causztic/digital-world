import cmath
import copy


def norm(z1, z2, z3):
    s = z1 * z1.conjugate()
    s += z2 * z2.conjugate()
    s += z3 * z3.conjugate()
    return round(cmath.sqrt(s).real, 3)

# print norm(1+3j, -1+3j, -1-3j)
# print norm(1+2j, -1+2j, -1-2j)
# print norm(1+1j, -1+1j, -1-1j)


def factors(n):
    li = []
    for i in range(1, n + 1):
        if (n % i == 0):
            li.append(i)
    return li

# for test_num in [6,12,7,15,21,1,9]:
#     print factors(test_num)


def combinations(n1, n2):
    result = []
    for i in range(n1, n2 + 1):
        for j in range(i + 1, n2 + 1):
            result.append((i, j))
    return result, len(result)

# print combinations(1,7)
# print combinations(3,5)
# print combinations(-1,2)
# print combinations(0,0)

'''Part C'''


def readMatrix(f):
    d = {}
    arr = []
    current_key = ""
    lines = map(lambda line: line.strip(), f.readlines())
    for line in lines:
        if line == "DATA":
            current_key = "matrix"
        elif line == "OP":
            d[current_key] = arr
            arr = []
            current_key = "op"
        elif line == "END":
            d[current_key] = arr
            break
        elif current_key:
            arr += [line.split(" ")]
    return d


def mulRowByC(matOp, i, c):
    for idx, item in enumerate(matOp[i]):
        matOp[i][idx] = item * c
    return matOp


def addRowMulByC(matOp, i, c, j):
    values = []
    for item in matOp[i]:
        values.append(item * c)

    for idx in range(len(matOp[j])):
        matOp[j][idx] += values[idx]
    return matOp


def gaussElimination(data):
    data["matrix"] = [[float(item) for item in row] for row in data["matrix"]]
    matrix = copy.deepcopy(data["matrix"])
    for arr in data["op"]:
        if arr[0] == "1":
            matrix = mulRowByC(matrix, int(arr[1]), float(arr[2]))
        elif arr[0] == "2":
            matrix = addRowMulByC(matrix, int(
                arr[1]), float(arr[2]), int(arr[3]))

    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            matrix[i][j] = round(matrix[i][j], 2)
    return data["matrix"], matrix

# f = open('quizzes/gauss1.txt', 'r')
# data = {'matrix': [[2.0, -1.0, 0.0, 1.0, 0.0, 0.0], [-1.0, 2.0, -1.0, 0.0, 1.0, 0.0], [0.0, -1.0, 2.0, 0.0, 0.0, 1.0]], 'op': [['2', '0', '0.5', '1'], ['1', '1', '0.666666666667'], ['2', '1', '1', '2'], ['1', '2', '0.75'], ['2', '2', '0.666666666667', '1'], ['2', '1', '1', '0'], ['1', '0', '0.5']]}
# # data = readMatrix(f)
# matA, result = gaussElimination(data)
# print matA
# print result


def maxProductThree(num):
    s_n = sorted(num)
    s_n.remove(0)
    n_product = 0

    positive_count = 0
    for i in s_n:
        if i > 0:
            positive_count += 1
    if positive_count == 0:
        # all negative numbers, take smallest 3
        return s_n[-1] * s_n[-2] * s_n[-3]
    elif len(s_n) - positive_count >= 2:
        # if there are at least 2 negative numbers,
        # multiply two most negative numbers with
        # biggest positive number
        negative_product = s_n[0] * s_n[1] * s_n[-1]
        positive_product = s_n[-1] * s_n[-2] * s_n[-3]
        if negative_product > positive_product:
            return negative_product
        else:
            return positive_product

num = [6, -3, -10, 0, 2]
print maxProductThree(num)
