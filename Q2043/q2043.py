from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_in_range(account1-1): return False
        if not self.is_in_range(account2-1): return False
        if self.accounts[account1-1] < money:
            return False
        
        self.accounts[account1-1] -= money
        self.accounts[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_in_range(account-1): return False
        self.accounts[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_in_range(account-1): return False
        if self.accounts[account-1] < money:
            return False
        self.accounts[account-1] -= money
        return True

    def is_in_range(self, index):
        return index >= 0 and index < len(self.accounts)


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)