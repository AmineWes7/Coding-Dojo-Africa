class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def create_account(self, int_rate=0.02, balance=0):
        new_account = (int_rate, balance)
        self.accounts.append(new_account)

    def make_deposit(self, amount, account_index=0):
        self.accounts[account_index].deposit(amount)

    def make_withdrawal(self, amount, account_index=0):
        self.accounts[account_index].withdraw(amount)

    def display_user_balance(self, account_index=0):
        print(f"User: {self.name}, Account Balance: {self.accounts[account_index].balance}")

    def transfer_money(self, amount, other_user, account_index=0, other_account_index=0):
        self.make_withdrawal(amount, account_index)
        other_user.make_deposit(amount, other_account_index)