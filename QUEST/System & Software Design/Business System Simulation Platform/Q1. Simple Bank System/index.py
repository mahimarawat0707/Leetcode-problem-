from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            account1 > len(self.balance)
            or account2 > len(self.balance)
            or self.balance[account1 - 1] < money
        ):
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Example usage
if __name__ == "__main__":
    bank = Bank([100, 200, 300])
    
    print("Initial balances:", bank.balance)
    print("Transfer 50 from account 1 to 2:", bank.transfer(1, 2, 50))
    print("Balances after transfer:", bank.balance)
    print("Deposit 100 to account 3:", bank.deposit(3, 100))
    print("Balances after deposit:", bank.balance)
