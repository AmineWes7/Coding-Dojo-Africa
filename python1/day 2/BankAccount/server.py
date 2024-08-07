class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

# Create 2 accounts
account1 = BankAccount(0.02, 100)
account2 = BankAccount(0.03, 200)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code
account1.deposit(50).deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code
account2.deposit(100).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
all_accounts = [account1, account2]

class BankAccount:
    instances = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.instances.append(self)

    @classmethod
    def display_all_accounts_info(cls):
        for account in cls.instances:
            account.display_account_info()

BankAccount.display_all_accounts_info()