class Account(object):

    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._amount = amount

    def deposit(self, amount):
        self._amount += amount

    def withdraw(self, amount):
        self._amount -= amount

    def __str__(self):
        return "%s, %s, balance: %d" % (self._owner, self._account_number, self._amount)
