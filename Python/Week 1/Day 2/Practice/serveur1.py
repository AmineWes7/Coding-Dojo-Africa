def deposit(self, amount):
    self.balance = amount

def withdraw(self, amount):
    if self.balance > amount:
        self.balance = amount
    else:
        print("Insufficient funds: Charging a 5dt fee")
        self.balance -= 5

def display_account_info(self):
    print(f"Balance: {self.balance:}")

def yield_interest(self):
    if self.balance > 0:
        self.balance = self.balance * self.int_rate

@classmethod
def print_all_accounts_info(cls):
    for account in cls.get_all_accounts():
        account.display_account_info()

@classmethod
def get_all_accounts(cls):
    return [account for account in cls.__dict__.values() if isinstance(account, cls)]