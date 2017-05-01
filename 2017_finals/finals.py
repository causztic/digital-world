# This problem will be graded manually.
# Please ignore the points given out by Tutor.


def complete_ISBN(ins):
    d10 = 0
    for index, i in enumerate(ins):
        d10 += int(i) * (index + 1)
    checksum = d10 % 11
    if checksum == 10:
        checksum = "X"
    return str(ins) + str(checksum)

# print 'Test case 1: ins=013601267'
# print complete_ISBN('013601267')

# print 'Test case 2: ins=013031997'
# print complete_ISBN('013031997')

# print 'Test case 3: ins=020139829'
# print complete_ISBN('020139829')


def get_products(inlist, test):
    d = {}
    for item in inlist:
        multiplied = reduce(lambda x, y: x * y, item)
        if d.has_key(multiplied):
            d[multiplied].append(item)
        else:
            d[multiplied] = [item]
    # bad naming!
    o = None
    if test in d.keys():
        o = d[test]
    return d, o

# inlist = [(3,5), (2,2), (2,2,3), (12,2), (7,3), (3,7,1)]
# get_products(inlist, 15)
# d,o = get_products(inlist, 15)
# print sorted(d.keys())
# print sorted(d.values())
# print o
# d,o = get_products(inlist, 21)
# print o
# d,o = get_products(inlist, 11)
# print o

# This problem will be graded manually.
# Please ignore the points given out by Tutor.

from libdw import sm


class SpellCheckSM(sm.SM):

    """
        Each word must have only two letters.
        The first letter must be one of the following lower-case consonant letters
        The second must be one of the following lower-case vowel letters
        There must be at least one space afer the end of each word
    """

    def is_valid_consonant(self, inp):
        return inp in ['k', 'g', 's', 't', 'd', 'n', 'h', 'b', 'm', 'r']
    
    def is_valid_vowel(self, inp):
        return inp in ['a', 'e', 'i', 'o', 'u']

    def is_blank_space(self, inp):
        return inp == " "

    def __init__(self):
        self.startState = "new word"

    def getNextValues(self, state, inp):
        nextState = state
        out = ""

        if state == "new word": #A1 E8 and E10
            if self.is_valid_consonant(inp):
                nextState = "consonant"
            elif self.is_blank_space(inp):
                nextState = "new word"
            else:
                # not a consonant and not a blank space
                nextState = "error"

        elif state == "consonant": # A2, E4 and E5
            if self.is_valid_vowel(inp):
                nextState = "vowel"
            elif self.is_blank_space(inp):
                out = "error"
                nextState = "new word"
            else: #not a vowel nor blank space
                nextState = "error"

        elif state == "vowel": # A3 and E6
            if self.is_blank_space(inp):
                out = "ok"
                nextState = "new word"
            else: # not a blank space
                nextState = "error"

        elif state == "error": #E7 and E9
            if self.is_blank_space(inp):
                out = "error"
                nextState = "new word"
            else:
                nextState = "error"
        
        return nextState, out

# print 'Test case A'
# a = SpellCheckSM()
# line = 'a si tu ne mai me pas je '
# print a.transduce(line)

# print 'Test case B'
# a = SpellCheckSM()
# line = 'hi ka ru no de '
# print a.transduce(line)
        
# print 'Test case C'
# a = SpellCheckSM()
# line = 'mu '
# a.transduce(line,verbose=True)

