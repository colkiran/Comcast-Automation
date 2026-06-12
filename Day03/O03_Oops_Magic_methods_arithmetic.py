
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return f"Name :{self.name}\nSalary :{self.salary}"

    def __add__(self, other):
        return Employee("", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("", self.salary / other.salary)



emp1 = Employee("John", 75000)
print(emp1)

print("-" * 60)
emp2 = Employee("Mary", 40000)
print(emp2)

print("-" * 60)
emp3 = Employee("Steve", 25000)
print(emp3)


print("add".center(60, "-"))
print(emp1 + emp2 + emp3)
"""
print(emp1 + emp2 + emp3)
print(temp_empObj + emp3)
"""

print("sub".center(60, "-"))
print(emp1 - emp2 - emp3)

print("mul".center(60, "-"))
print(emp1 * emp2 * emp3)

print("div".center(60, "-"))
print(emp1 / emp2 / emp3)

