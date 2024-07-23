class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def create_account(self, int_rate=0.02, balance=0):
        self.accounts.append(BankAccount(int_rate, balance))

    def make_deposit(self, amount, account_index=0):
        self.accounts[account_index].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_index=0):
        self.accounts[account_index].withdraw(amount)
        return self

    def display_user_balance(self, account_index=0):
        self.accounts[account_index].display_account_info()
        return self

    def transfer_money(self, amount, other_user, account_index=0, other_account_index=0):
        if self.accounts[account_index].balance >= amount:
            self.accounts[account_index].withdraw(amount)
            other_user.accounts[other_account_index].deposit(amount)
        else:
            print("Insufficient funds")
        return self

# Example usage:
user1 = User("John", "john@example.com")
user1.create_account()
user1.create_account(int_rate=0.03, balance=100)

user2 = User("Jane", "jane@example.com")
user2.create_account()

user1.make_deposit(100).make_withdrawal(50).display_user_balance()
user2.make_deposit(200).display_user_balance()

user1.transfer_money(50, user2).display_user_balance()
user2.display_user_balance()