"""
PART A
This question is related to GUI programming using Kivy.

a) Explain what App.build() method does and state what this method should return. [ 5 pts ]
App.build() instantiates the application with it's elements. It should return an instance of a Kivy object as a root widget.

b) Explain what widget.bind() method does and its argument. [ 5pts ]
widget.bind() binds an event to the relevant widget. The argument sets a function name to an event, which needs two arguments
for self and instance. Additional arguments can be added to it with partial or lambda functions.
When the event occurs on the widget, the widget will execute the relevant function specified.


c) What are the classes needed to create an application with several Screens? Show their
relationship with each other. [ 5 pts]
ScreenManager and Screen are required to create an application with several Screens.
A ScreenManager will be the root widget of the application, and it will have multiple Screens as children.
The screens are added to the ScreenManager instance with the add_widget function like any other widget.


4
Q.2 [10 points]In Week 9, you worked on a boundary follower problem in your 1D Mini Project.

a) State the minimum number of sonar sensors needed in this problem. Which are the minimum sonar sensors needed and explain why? [ 5 pts ]
We needed at least a minimum of 2 sonar sensors, the front[2] and the right sensor[4]. 
The front sensor is needed to detect if the robot is too close or too far away from the wall,
while the right sensor is needed to detect if the robot is beside a wall on the right.

b) The minimum number of states in this problem is two. State the two states and explain why at least two states are needed. [ 5 pts ]
"""

""" PART B """
from copy import deepcopy

def maxOccurrences(inp):
    """
        Takes in an non-empty string that contains numbers
        and returns a list of the numbers with the maximum
        occurrences and the maximum count of these numbers.
    """
    sorted_list = inp.split()
    max_count = 0
    arr = []

    # get max count
    for i in set(sorted_list):
        c = sorted_list.count(i)
        if max_count < c:
            max_count = c

    # loop again to get elements
    for i in set(sorted_list):
        if max_count == sorted_list.count(i):
            arr.append(i)

    return sorted(arr), max_count

# print maxOccurrences('2 3 40 3 5 4 -3 3 3 2 0')
# print maxOccurrences('9 30 3 9 3 2 4')

from libdw import sm


class RingCounter(sm.SM):

    def __init__(self):
        self.startState = 0

    def convert(self, state):
        if state == 1:
            return "001"
        elif state == 2:
            return "010"
        elif state == 3:
            return "011"
        elif state == 4:
            return "100"
        elif state == 5:
            return "101"
        elif state == 6:
            return "110"
        elif state == 7:
            return "111"
        else:
            return "000"

    def getNextValues(self, state, inp):
        if inp == 1 or (inp == 0 and state == 7):
            nextState = 0
        elif inp == 0:
            nextState = state + 1
        return nextState, self.convert(nextState)

# r = RingCounter()
# print r.transduce([0,0,0,0,0,0,0,0,0])
# print r.transduce([0,0,0,1,0,0,0,0,0])
# print r.transduce([0,0,0,1,0,0,1,0,0])

""" PART C """


class Avatar(object):

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getHP(self):
        return self._hp

    def setHP(self, hp):
        self._hp = hp

    def getPosition(self):
        return self._position

    def setPosition(self, position):
        self._position = position

    def heal(self, amount):
        if amount > 0:
            self.hp += amount

    def attacked(self, dmg=-1):
        if dmg < 0:
            self.hp += dmg

    def __init__(self, name, hp=100, position=(1, 1)):
        self.name = name
        self.hp = hp
        self.position = position

    # old style properties
    name = property(getName, setName)
    hp = property(getHP, setHP)
    position = property(getPosition, setPosition)


class Map(object):


    """ Part D """

    def generate_cost(self, pos, offset):
        if self.whatIsAt(pos) == "Wall":
            return 1000
        return offset + abs(self.getEnemyAttack(pos)) - (self.getFoodEnergy(pos) or 0)

    def getSearchMap(self):
        max_x = sorted([x[0] for x in self.world.keys()])[-1]
        max_y = sorted([x[1] for x in self.world.keys()])[-1]
        d = {}
        #offset is the maximum non-negative value in the map.
        offset = max([i for i in self.world.values() if type(i) == int])
        for i in range(max_x+1):
            for j in range(max_y+1):
                top = (i, j-1)    #0
                right = (i+1, j)  #1
                bottom = (i, j+1) #2
                left = (i-1, j)   #3

                inner_dict = {}
                if top[1] >= 0:
                    value = self.generate_cost(top, offset)
                    inner_dict[0] = (top, value)
                if right[0] <= max_x:
                    value = self.generate_cost(right, offset)
                    inner_dict[1] = (right, value)
                if bottom[1] <= max_y:
                    value = self.generate_cost(bottom, offset)
                    inner_dict[2] = (bottom, value)
                if left[0] >= 0:
                    value = self.generate_cost(left, offset)
                    inner_dict[3] = (left, value)

                d[(i, j)] = inner_dict

        return d


    def __init__(self, dictionary):
        self.world = dictionary

    def whatIsAt(self, position):
        if position not in self.world.keys():
            return "Empty"

        item = self.world[position]
        item_description = {"x": "Exit", 0: "Wall", "+": "Food", "-": "Enemy"}
        if type(item) == int:
            if int(item) > 0:
                return item_description["+"]
            elif int(item) < 0:
                return item_description["-"]
            else:
                return item_description[0]
        elif item == "x":
            return item_description["x"]
        else:
            return "Empty"

    def getEnemyAttack(self, position):
        if self.whatIsAt(position) == "Enemy":
            return self.world[position]
        else:
            return False

    def getFoodEnergy(self, position):
        if self.whatIsAt(position) == "Food":
            return self.world[position]
        else:
            return False

    def removeEnemy(self, position):
        if self.whatIsAt(position) == "Enemy":
            del self.world[position]
            return True
        else:
            return False

    def eatFood(self, position):
        if self.whatIsAt(position) == "Food":
            del self.world[position]
            return True
        else:
            return False

    def getExitPosition(self):
        if "x" in self.world.itervalues():
            for k, v in self.world.iteritems():
                if v == "x":
                    return k
        else:
            return None


class DW2Game(sm.SM):

    def __init__(self, avatar, m):
        self.startState = (avatar, m)

    def checkMove(self, avatar, m, pos):
        item = m.whatIsAt(pos)
        if item == "Wall":
            return avatar, False
        if item == "Empty" or item == "Exit":
            # move to pos
            return avatar, True
        if item == "Food":
            # heal avatar by the food
            avatar.heal(m.getFoodEnergy(pos))
            # remove the food
            m.eatFood(pos)
            return avatar, True
        if item == "Enemy":
            avatar.attacked(m.getEnemyAttack(pos))
            return avatar, False
        return avatar, False

    def getNextValues(self, state, inp):
        nextState = deepcopy(state)
        avatar = nextState[0]
        m = nextState[1]

        if inp[1].strip() in ["up", "right", "down", "left"]:
            # if it's a valid move
            # check if it's neither a wall nor enemy
            pos = list(avatar.position[:])
            # update position
            if inp[1] == "up":
                pos[1] -= 1
            elif inp[1] == "right":
                pos[0] += 1
            elif inp[1] == "down":
                pos[1] += 1
            elif inp[1] == "left":
                pos[0] -= 1
            if inp[0] == "move":
                # valid move, check if movable
                a, move = self.checkMove(avatar, m, tuple(pos))
                if move:
                    avatar = a
                    avatar.position = tuple(pos)
            elif inp[0] == "attack":
                # valid attack, check if attackable
                if m.whatIsAt(tuple(pos)) == "Enemy":
                    m.removeEnemy(tuple(pos))

        return nextState, (avatar.name, avatar.position, avatar.hp)

    def done(self, state):
        return state[1].getExitPosition() == state[0].position
    
# print 'Question 7 Test Cases \n'

# world={(0,0):0, (1,0):0 , (2,0):0, (0,1):0, (1,1):-2, (2,1): 0, (0,2):0, (1,2): 'x', (2,2): 0}
# #world2={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (5,1): 0, (0,2):0, (1,2): -2, (5,2): 0, (0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0, (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}
# m = Map(world)
# print m.getSearchMap()
# print 'test 1'
# inp=[('move','down'),('attack','down'),('move','down'),( 'move','down'),('move','down'),('move','right'),('move','right'),('move','right'),('move','down'),('move','down')]
# av = Avatar('John')
# m = Map(world2)
# g = DW2Game(av,m)
# print g.transduce(inp)

# print 'test 2'
# inp=[('move','left'),('move','right'),('move','right'),('move','right'),('move','right'),('move','down'),('move','down'),('move','down'),('move','up')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp)

# print 'test 3'
# inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp)

# print 'test 4'
# inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left'),('move','left'),('move','down'),('move','right')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp)

# print 'test 5'
# inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left'),('move','left'),('move','down'),('move','right'),('move','right'),('move','right'),('move','down'),('move','down'),('move','down')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp)

# print 'test 6'
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# g.start()
# n,o=g.getNextValues(g.startState,('move','right'))
# ans = g.state[0].getPosition() == n[0].getPosition()
# print ans, g.state[0].getPosition(), n[0].getPosition()

# print '\n'
from libdw import ucSearch

def findPath(avatar, m):
    x = m.getExitPosition()
    search = m.getSearchMap()
    optimized = ucSearch.search(avatar.position, lambda pos: x == pos, [0,1,2,3], lambda state, action: (search[state][action][0], search[state][action][1]))
    # for this question I didn't get the cost because it's too troublesome.
    return optimized

world={(0,0):0, (1,0):0, (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (5,1): 0,(0,2):0, (1,2): -2, (5,2): 0, (0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0, (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}
print('test 1')
av=Avatar('John',position=(1,3))
m=Map(world)
print(findPath(av,m))