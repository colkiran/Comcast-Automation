
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Manager Job......")

class Developer(Employee):

    def doJob(self):
        print("Developer Job.....")


def BankFun(emp):
    print("Bank job strated".center(60, "-"))
    emp.doJob()
    print("Bank job completed".center(60, "-"))
    print("-" * 60)

Mike = Manager()
David = Developer()

BankFun(Mike)
BankFun(David)