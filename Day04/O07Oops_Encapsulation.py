"""
data hiding and controlled access
"""

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, new balance :{self.__balance}")
        else:
            print("Deposit amount must be positive...")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}, new balance :{self.__balance}")
        else:
            print("Invalid withdrawl amount....")

account = BankAccount("Mark", 5000)

print(account.get_balance())
account.deposit(2000)
account.withdraw(3500)
print(account.get_balance())