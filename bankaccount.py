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
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=1.2, balance=500)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"${self.account.balance}")
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(f"${self.account.balance}")
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    
    def interest(self):
        self.account.yield_interest()
        return self

# adrien = BankAccount(1.2,500)
# sadie = BankAccount(1.5,600)

adrien= User("Adrien", "adrienf@gmail.com")
sadie= User("Sadie", "sadiem@gmail.com")

adrien.make_deposit(30).make_deposit(50).make_deposit(20).make_withdraw(15).interest().display_user_balance()
sadie.make_deposit(400).make_deposit(50).make_withdraw(30).make_withdraw(30).make_withdraw(60).make_withdraw(25).interest().display_user_balance()
