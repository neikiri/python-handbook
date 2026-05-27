"""
Bank Account - A Practical Class Example

This example demonstrates:
- Real-world class design
- Encapsulation (private attributes with underscore)
- Methods for common operations
- Input validation
"""

from datetime import datetime


class BankAccount:
    """A simple bank account class."""
    
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        """Initialize the bank account."""
        self._account_number = account_number  # Private attribute
        self._owner = owner
        self._balance = float(initial_balance)
        self._transactions = []  # List of (amount, date, description)
    
    @property
    def account_number(self) -> str:
        """Get the account number (read-only)."""
        return self._account_number
    
    @property
    def owner(self) -> str:
        """Get the owner name (read-only)."""
        return self._owner
    
    @property
    def balance(self) -> float:
        """Get the current balance (read-only)."""
        return self._balance
    
    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        """Deposit money into the account."""
        if amount <= 0:
            print(f"Error: Deposit amount must be positive. Got: {amount}")
            return False
        
        self._balance += amount
        self._transactions.append((amount, datetime.now(), description))
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        """Withdraw money from the account."""
        if amount <= 0:
            print(f"Error: Withdrawal amount must be positive. Got: {amount}")
            return False
        
        if amount > self._balance:
            print(f"Error: Insufficient funds. Balance: ${self._balance:.2f}, Attempted: ${amount:.2f}")
            return False
        
        self._balance -= amount
        self._transactions.append((-amount, datetime.now(), description))
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True
    
    def get_statement(self) -> str:
        """Return a statement of the account."""
        lines = [
            f"Account Statement for {self._owner}",
            f"Account Number: {self._account_number}",
            f"Current Balance: ${self._balance:.2f}",
            "",
            "Transactions:",
        ]
        
        for amount, date, description in self._transactions:
            sign = "+" if amount > 0 else ""
            lines.append(f"  {date.strftime('%Y-%m-%d %H:%M')} | {sign}${amount:.2f} | {description}")
        
        return "\n".join(lines)
    
    def __str__(self) -> str:
        """Return a string representation of the account."""
        return f"BankAccount({self._account_number}, {self._owner}, balance=${self._balance:.2f})"
    
    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return f"BankAccount(account_number='{self._account_number}', owner='{self._owner}', initial_balance={self._balance})"


# Example usage
if __name__ == "__main__":
    print("=== Creating a Bank Account ===")
    account = BankAccount("123456789", "Alice", 1000.0)
    print(f"Created: {account}")
    print()
    
    print("=== Making Transactions ===")
    account.deposit(500.0, "Paycheck")
    account.withdraw(200.0, "Groceries")
    account.withdraw(1500.0, "Too much!")  # This will fail
    account.deposit(-100.0, "Negative deposit")  # This will also fail
    print()
    
    print("=== Account Statement ===")
    print(account.get_statement())
    print()
    
    print("=== Account Properties ===")
    print(f"Account number: {account.account_number}")
    print(f"Owner: {account.owner}")
    print(f"Balance: {account.balance}")
    
    # Try to modify balance directly (won't work)
    try:
        account.balance = 999999
    except AttributeError as e:
        print(f"\nCannot modify balance directly: {e}")
    print()
    
    print("=== Multiple Accounts ===")
    account1 = BankAccount("001", "Alice", 500)
    account2 = BankAccount("002", "Bob", 1000)
    
    print(f"Account 1: {account1}")
    print(f"Account 2: {account2}")
    
    account1.deposit(200)
    account2.withdraw(300)
    
    print(f"\nFinal balances:")
    print(f"  Alice: ${account1.balance:.2f}")
    print(f"  Bob: ${account2.balance:.2f}")
