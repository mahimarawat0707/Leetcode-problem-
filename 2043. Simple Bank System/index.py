from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        # Store balances for all accounts
        self.balance = balance
        # Total number of accounts
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Transfer 'money' from account1 to account2.
        Returns True if successful, False otherwise.
        """
        # Check if both accounts exist
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False

        # Check if account1 has enough balance
        if self.balance[account1 - 1] < money:
            return False

        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        """
        Deposit 'money' into the given account.
        Returns True if successful, False otherwise.
        """
        # Check if account exists
        if not (1 <= account <= self.n):
            return False

        # Perform deposit
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        """
        Withdraw 'money' from the given account.
        Returns True if successful, False otherwise.
        """
        # Check if account exists
        if not (1 <= account <= self.n):
            return False

        # Check if account has enough balance
        if self.balance[account - 1] < money:
            return False

        # Perform withdrawal
        self.balance[account - 1] -= money
        return True

if __name__ == "__main__":
    bank = Bank([10, 100, 20, 50, 30])

    print(bank.withdraw(3, 10))   # True
    print(bank.transfer(5, 1, 20)) # True
    print(bank.deposit(5, 20))    # True
    print(bank.transfer(3, 4, 15)) # False
