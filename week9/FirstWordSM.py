from libdw import sm


class FirstWordSM(sm.SM):
    startState = 'word'

    def getNextValues(self, state, inp):
        output = None

        if state == "word":
            if inp != " " and inp != "\n":
                nextState = "word"
                output = inp
            elif inp == " ":
                nextState = "ignore"
            else:
                nextState = "hard_find_word"

            if output == "#":
                nextState = "ignore"

        if state == "ignore":
            if inp == "\n":
                nextState = "hard_find_word"
            else:
                nextState = "ignore"

        if state == "hard_find_word":
            if inp != " " and inp != "\n":
                output = inp
                nextState = "word"
            else:
                nextState = "hard_find_word"

        return nextState, output

s = 'def\n f(x): # comment\n   return 1'
m = FirstWordSM()
print m.transduce(s)
