import math


def area_r_polygon(n, s):
    return round((n * s ** 2) / (4 * math.tan(math.pi / n)), 3)

# print area_r_polygon(5, 6.5)
# print area_r_polygon(7, 3.25)
# print area_r_polygon(2, 12.5)


def mysum(a, b, limit):
    if type(a) != int or type(b) != int or a < 1 or b < 1:
        return "Wrong input"

    a_l = range(a, limit, a)
    b_l = range(b, limit, b)
    return sum(set(a_l) | set(b_l))

print mysum(3, 5, 10)
print mysum(2, 4, 12)
print mysum(3, 3, 15)
print mysum(7, 9, 100)
print mysum(21, 34, 10000)
print mysum(0, 5, 10)
print mysum(0.5, 5, 10)
print mysum(3, 'x', 10)
print mysum(2, 3, 0)

students = [("Alan", ["CompSci", "Physics", "Math"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Edward", ["CompSci", "Philosophy", "Economics"]),
            ("Margaret", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Philip", ["Sociology", "Economics", "Law", "Stats", "Music"]),
            ("Mary", ["Math", "CompSci", "Stats"]),
            ("Vera", ["CompSci", "Philosophy", "Economics"]),
            ("Mike", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Donna", ["Sociology", "Economics", "Law", "Stats"])]


def get_students(students, course):
    results = []
    for student in students:
        if course in student[1]:
            results.append(student[0])
    return results

# print get_students(students, 'Philosophy')
# print get_students(students, 'History')
# print get_students(students, 'Math')
# print get_students(students, 'CompSci')


def get_nodes(fid):
    result = []
    lines = map(lambda x: x.strip(), fid.readlines())
    for line in lines:
        s = map(lambda x: int(x), line.split())
        result.append((s[0], s[1]))
    return result

import itertools


def create_graph(nodes):
    d = {}
    for item in set(itertools.chain(*nodes)):
        d[item] = {}
    for t in nodes:
        d[t[0]][t[1]] = 1
        d[t[1]][t[0]] = 1
    return d


def get_friends(G, index):
    return G[index].keys()


def suggested_new_friends(G, index):
    friends = get_friends(G, index)
    suggested = []
    for friend in friends:
        suggested.append(get_friends(G, friend))
    suggested = set(itertools.chain(*suggested))
    suggested.remove(index)

    candidate_counts = [len(get_friends(G, candidate))
                        for candidate in suggested]
    max_count = max(candidate_counts)
    return [candidate for candidate in suggested if len(get_friends(G, candidate)) == max_count], max_count

fk = open("quizzes/facebook_less.txt", "r")
s1 = open("quizzes/sutdbook1.txt", "r")
s2 = open("quizzes/sutdbook2.txt", "r")

nodes = get_nodes(s1)
g = create_graph(nodes)
G = {0: {1: 1, 2: 1, 3: 1}, 1: {0: 1, 5: 1, 6: 1, 7: 1}, 2: {0: 1, 5: 1, 7: 1}, 3: {
    0: 1, 4: 1, 5: 1}, 4: {3: 1}, 5: {1: 1, 2: 1, 3: 1}, 6: {1: 1}, 7: {1: 1, 2: 1}}
print suggested_new_friends(G, 0)
fk.close()
s1.close()
s2.close()


def num_of_sol(n):
    count =0
    for x1 in range(0, n + 1):
        for x2 in range(0, n - x1 + 1):
            for x3 in range(0, n - x2 + 1):
                for x4 in range(0, n - x3 + 1):
                    for x5 in range(0, n - x4 + 1):
                        if x1 + x2 + x3 + x4 + x5 == n:
                            count += 1
    return count

def cheat(n):
    return math.factorial(n+4) / (math.factorial(4) * math.factorial(n))

print cheat(150)
