cus1Balance = 0
cus2Balance = 0

cus1AccountNo = '4444444'
cus2AccountNo = '55555555'

def deposit(amount, account):
    global cus1Balance
    global cus2Balance

    if account == cus1AccountNo:
        cus1Balance = cus1Balance + amount
    elif account == cus2AccountNo:
        cus2Balance = cus2Balance + amount
    else:
        print('Invalid account no passed')

deposit(1000, cus1AccountNo)
print(cus1Balance)

deposit(5000, cus1AccountNo)
print(cus1Balance)


class BankAccount:

    def __init__(self, accountNo, amount=0):
        self.accountNo = accountNo
        self.balance = amount

    def deposit(self, amount):
        self.balance = self.balance + amount
        return

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return

    def showBalance(self):
        print(self.balance)
        return


cus1 = BankAccount('4444444', 5000)
cus1.showBalance()
cus1.deposit(5000)
cus1.showBalance()
cus1.withdraw(1000)
cus1.showBalance()

cus2 = BankAccount('55555555')
cus2.deposit(10000)
cus2.showBalance()
cus2.withdraw(3000)
cus2.showBalance()


class SavingsBankAccount(BankAccount):
    pass


class CurrentBankAccount(BankAccount):
    pass


savingsAccount = SavingsBankAccount('66666666', 20000)
savingsAccount.showBalance()
savingsAccount.deposit(5000)
savingsAccount.showBalance()

currentAccount = CurrentBankAccount('77777777', 30000)
currentAccount.showBalance()
currentAccount.withdraw(5000)
currentAccount.showBalance()