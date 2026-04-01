class BankAccount():
    def __init__(self,balance):
        self.balance = balance
        print(f"Account created with ${balance}" )
    
    def send_money(self,amount):
        self.balance -= amount
        print(f"After sending ${amount}, the balance is ${self.balance}")
        return self.balance

    def add_money(self,amount):
        self.balance += amount
        print(f"After receiving ${amount}, the balance is ${self.balance}")
        return self.balance


class SavingAccount(BankAccount):
    def __init__(self, balance,min_balance):
        super().__init__(balance) ##super() allows me to use the methods of the upper class
        self.min_balance = min_balance
    def send_money(self,amount):
        if amount < (self.balance - self.min_balance):
            self.balance -= amount
            print(f"After sending ${amount}, the balance is ${self.balance}")
            return self.balance
        else:
            raise ValueError (f"After sending ${amount}, the balance will be lower than the minimum allowed. The transaction cannot be executed.")

print("-"*50)
#Normal Account
Account_1 = BankAccount(100)
Account_1.send_money(110)
Account_1.add_money(200)

print("-"*50)
#Saving Account
Account_2 = SavingAccount(100,50)
Account_2.send_money(110)
Account_2.add_money(200)
