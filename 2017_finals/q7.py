#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

class MyTask(object):
    def __init__(self, deadline, duration):
        self.deadline = deadline
        self.duration = duration
        
    def __str__(self):
        return 'T(%d,%d)' %(self.deadline, self.duration)

    def __repr__(self):
        return self.repr((self.deadline, self.duration))

# this code is incorrect
def procrastination(assignments):
    # we create a guy to do the assignments.
    # first we find the closest time.
    sorted_assignments = sorted(assignments, key = lambda assignment: assignment.deadline)
    # after sorting, get the furthest deadline

    furthest_deadline = -1
    for assignment in assignments:
        if assignment.deadline > furthest_deadline:
            furthest_deadline = assignment.deadline

    # after getting assignment_deadline, work.
    # we start from time_index = 0 to work
    if furthest_deadline == -1:
        return -1 

    time_index = 0

    while time_index < furthest_deadline:
        t = 0 #this is the time for duration
        while t < furthest_deadline:
            # grab the sorted assignments by deadline and iterate through
            for assignment in sorted_assignments:
                t += assignment.duration
                # check if time has exceeded deadline
                if t > furthest_deadline:
                    if time_index == 0:
                        #not possible
                        return -1
                    else:
                        break
        time_index += 1 # try again with a better time

    return time_index



assignments = [ MyTask(9,1), MyTask(9,2), MyTask(7,1) ]
print procrastination(assignments)

# assignments1 = [ MyTask(3,2), MyTask(3,2) ]
# print procrastination(assignments1)

# assignments2 = [ MyTask(9,1), MyTask(9,2), MyTask(4,3) ]
# print procrastination(assignments2)

assignments3 = [MyTask(14,10), MyTask(33,2), MyTask(5,3), MyTask(14,1), MyTask(10,2)]
print procrastination(assignments3)


