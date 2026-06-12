
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name :{self.name} \nSalary :{self.salary}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Jack", 50000)
print(emp1)

print("-" * 60)
emp2 = Employee("Mike", 65000)
print(emp2)

print("-" * 60)
# compares the adresses of the objects by default
# after implementing the magic method we are comparing salaries
# print(emp1 == emp2)

if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
print("-" * 60)

# print(emp1 > emp2)

if emp1 < emp2:
    print("{}'s salary of {} is less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name,emp2.salary))
else:
    print("{}'s salary of {} is greater than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))