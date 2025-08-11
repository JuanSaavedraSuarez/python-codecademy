class Checking():
    def type(self):
        print('You have a checking account at bank')

    def balance(self):
        print('$20 left in checking')

class Savings():
    def type(self):
        print('You have a savings account at bank')

    def balance(self):
        print('$1000 left in savings')

account_a = Checking()
account_b = Savings()

for account in (account_a, account_b):
    account.type()
    account.balance()