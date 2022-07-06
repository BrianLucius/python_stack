class BankAccount:
    all_accounts = []
    
    def __init__(self, interest_rate, balance = 0):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
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
    

user1 = BankAccount(balance=10000, interest_rate=.10)
user2 = BankAccount(interest_rate=.20)

user1.deposit(100).deposit(300).deposit(75).yield_interest().display_account_info()
user2.deposit(1245).deposit(412).withdraw(11124).withdraw(73).withdraw(154).withdraw(23).yield_interest().display_account_info()

BankAccount.print_bank_accounts()