class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Deduct the specified amount if sufficient funds exist."""
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
