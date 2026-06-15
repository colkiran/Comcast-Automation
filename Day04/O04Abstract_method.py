
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account Ctor....")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def getBalance(self):
        print(f"Balace in the account is {self.amt}")
    def deposit(self, amt):
        self.amt = amt
        print(f"{self.amt} successfully credited into the account")


sav = Savings()
sav.deposit(50000)
sav.getBalance()
