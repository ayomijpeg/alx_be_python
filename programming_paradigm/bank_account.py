class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        """Initialize the bank account with an optional initial balance (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        self.account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw money if funds are sufficient. Return True if successful, False otherwise."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
def display_balance(self):
    """Display the current balance with 2 decimal places."""
    print(f"Current Balance: ${self.account_balance:.2f}")
