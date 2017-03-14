''' Part A 
Q1

b = a copies the list's memory address
c = a[:] creates a new list but for [3,4] it copies the memory address
d = copy.deepcopy(a) copies the list into a new memory address
 
Q2
 The while condition is only checked once.
 This is because the leftObstacle and rightObstacle is set before the while loop
 and does not obtain any new values with the obstacle() method of Finch.
 If the initial conditions of the while loop is met, the robot would
 move indefinitely and will not stop.

 Instead, the code should look like this:

 while not leftObstacle and not rightObstacle:
   finch.wheels(0.2, 0.2)
   leftObstacle, rightObstacle = finch.obstacle()

'''


def comp(x):
    return x ** 3 + 4 * x ** 2 + 6 * x + 1


def genList(n1, n2):
    while n1 % 3 != 0:
        n1 += 1
    return range(n1, n2 + 1, 3)


def matAdd(A, B):
    return [[i[idx] + j[idx] for idx in range(len(i))] for i in A for j in B]


def getSchedule(f):
    lines = f.readlines()
    schedule = {}
    li = []
    current_day = ""
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    for line in lines:
        line = line.strip()
        if line in days:
            if li:
                schedule[current_day] = li
                li = []
            current_day = line

        elif current_day:
            li.append(tuple(map(lambda x: int(x), line.split(" "))))
    return schedule

schedule = getSchedule(open("quizzes/data1.txt", 'r'))


def findLength(dictSchedule):
    d = {}
    for key, value in dictSchedule.iteritems():
        hours = 0
        for t in value:
            hours += abs(t[0] - t[1])
        d[key] = hours
    return d


def findConflict(dictSchedule):
    d = {}
    for key, value in dictSchedule.iteritems():
        count = 0
        times = []
        for t in value:
            for i in range(t[0], t[1] + 1):
                count += 1
                times.append(i)
        # if unique hours are the same as count,
        # this means that there is no overlap.
        d[key] = (len(set(times)) == count)
    return d


def countLitPixel(cx, cy, r):
    x = range(cx - r, cx + r + 1)
    y = range(cy - r, cy + r + 1)
    count = 0
    x.remove(cx)
    y.remove(cy)

    for i in x:
        for j in y:
            if (abs(i-cx)-1) ** 2 + (abs(j-cy)-1) ** 2 < r ** 2:
                count += 1
    return count