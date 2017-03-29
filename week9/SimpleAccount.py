from libdw import sm


class SimpleAccount(sm.SM):

    def __init__(self, start_deposit):
        self.startState = start_deposit

    def getNextValues(self, state, inp):
        next_state = state + inp
        if inp < 0 and state < 100:
            next_state -= 5
        output = next_state
        return next_state, output

acct = SimpleAccount(110)
acct.start()
print acct.step(10)
print acct.step(-25)
print acct.step(-10)
print acct.step(-5)
print acct.step(20)
print acct.step(20)
