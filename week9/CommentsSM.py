from libdw import sm


class CommentsSM(sm.SM):
    startState = 'code'  # fix this

    def getNextValues(self, state, inp):
        output = None
        if state == "code" and inp == "#":
            output = "#"
            nextState = "comment"

        elif state == "comment" and inp == "\n":
            nextState = "code"
        else:
            nextState = state

        if state == "comment":
            output = inp

        if nextState == "code":
            output = None

        return nextState, output

s = 'def f(x): # comment\n   return 1'
m = CommentsSM()
print m.transduce(s)