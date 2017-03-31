from libdw import sm


class RunOfFive(sm.SM):

    startState = 0

    def getNextValues(self, state, inp):
        nextState = 0
        if (inp == 5):
            nextState = state + 1
        return nextState, nextState

m = RunOfFive()
print m.transduce([2,5,0,2,5,5,0,5,7,5,5,5,5])