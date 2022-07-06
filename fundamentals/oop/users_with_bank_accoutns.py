class BankAccount:
    all_accounts = []

    def __init__(self, interest_rate, balance = 0, account_type = "checking"):
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_type = account_type
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"The current balance is: ${self.balance}.")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

    @classmethod
    def print_bank_accounts(cls):
        print("\nListing all accounts:")
        for account in (cls.all_accounts):
            print(f"The current balance is: ${account.balance} with an interest rate of: {account.interest_rate}%")
        return

class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)

    def display_user_balance(self):
        self.account.display_account_info()

user_john = User("John Swift","swiftly@explorer.net")
print(f"\nName: {user_john.name} \nEmail: {user_john.email} \nBalance: {user_john.account.balance} \nInterest Rate: {user_john.account.interest_rate}")

user_alice = User("Alice Chan","achan@email.net")
print(f"\nName: {user_alice.name} \nEmail: {user_alice.email} \nBalance: {user_alice.account.balance} \nInterest Rate: {user_alice.account.interest_rate}")


user_john.make_deposit(100)
print(f"\nName: {user_john.name} \nEmail: {user_john.email} \nBalance: {user_john.account.balance} \nInterest Rate: {user_john.account.interest_rate}")

user_john.make_withdrawl(50)
print(f"\nName: {user_john.name} \nEmail: {user_john.email} \nBalance: {user_john.account.balance} \nInterest Rate: {user_john.account.interest_rate}")

user_john.display_user_balance()

BankAccount.print_bank_accounts()