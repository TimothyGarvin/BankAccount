class BankAccount:
    bank_name = "Garvin Credit Union"
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"${self.balance}")
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            print(f"${self.balance}")
        else:
            self.balance = self.balance-amount
        return self

    def display_account_info(self):
        print(f"Current Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.balance * self.int_rate
            print(f"${self.balance}")
        else:
            print("Error: Broke")
        return self

adriensAccount = BankAccount(1.2,500)
sadiesAccount = BankAccount(1.5,600)

adriensAccount.deposit(30).deposit(50).deposit(20).withdraw(15).yield_interest().display_account_info()
sadiesAccount.deposit(400).deposit(50).withdraw(30).withdraw(30).withdraw(60).withdraw(25).yield_interest().display_account_info()
