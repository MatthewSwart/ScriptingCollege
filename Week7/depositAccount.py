#Deposit section for week 7 exercise 2

from bankAcc import Bank_account

class Deposit_Account(Bank_account):
    '''
    Name and balance are inherited from the Bank_Account
    in bankAcc.py file.

    __init__ takes the name and balance, then it
    passes the information through to the Bank_Account
    class in bankAcc.py
    '''

    def __init__(self, name, balance, deposit_rate):


        Bank_account.__init__(self, name, balance)

        self.deposit_rate = deposit_rate

    def __str__(self):
        return Bank_account.__str__(self) + "\nDeposit Rate: " + str(self.deposit_rate)

    def add_interest(self):

        interest = self.balance * self.deposit_rate/100
        self.balance = self.balance + interest
        return "Interest earned: \xe2\x82\xac" + str(interest) + "\nNew balance: \xe2\x82\xac" + \
               str(self.balance)


if __name__ == "__main__":

    client = Deposit_Account("Matthew Swart", 1234.54, 5)
    print client
    client.lodgement()
    client.withdrawal()
    print client.add_interest()
    balance = client.balance()
    print str(balance)
