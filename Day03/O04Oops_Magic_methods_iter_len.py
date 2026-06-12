
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'JSP', 'Spring', 'Hibernate', 'Angular', 'React']

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)    #self.tech.__iter__

emp1 = Employee("Moses", 75000)
print(emp1)

print("-" * 60)
print(len(emp1))

print("-" * 60)
print([t for t in emp1])        # list comprehension
