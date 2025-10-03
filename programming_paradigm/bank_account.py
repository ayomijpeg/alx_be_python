# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add money to the account"""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are available"""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance formatted to 2 decimal places"""
        print(f"Current Balance: ${self.account_balance:.2f}")
