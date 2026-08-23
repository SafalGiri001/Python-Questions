class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def david(self,amount):
        self.balance -= amount
        print("Rs.",  amount ,"was devited")
        print("Total balance = ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance = ", self.balance)


    def balance(self):
        return self.balance







account1 = Account(10000, 1235)
print(account1.balance)
print(account1.account)
account1.david(1000)
account1.credit(1500)
