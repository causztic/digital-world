from libdw import sm


class CM(sm.SM):

    startState = 0

    def getNextValues(self, state, inp):
        is_state_one = self.state == 1
        is_state_zero = self.state == 0
        is_inp_100 = inp == 100
        is_inp_50 = inp == 50

        # return the input if not 50 cents or 1 dollar
        if is_state_zero and not is_inp_100 and not is_inp_50:
            nextState = 0
            output = (0, '--', inp)

        if is_state_zero and is_inp_50:
            nextState = 1
            output = (50, '--', 0)

        if is_state_zero and is_inp_100:
            nextState = 0
            output = (0, 'coke', 0)

        if is_state_one and is_inp_100:
            nextState = 0
            output = (0, "coke", 50)

        if is_state_one and is_inp_50:
            nextState = 0
            output = (0, 'coke', 0)

        return nextState, output

c = CM()
c.start()
print c.step(50)
print c.step(50)
