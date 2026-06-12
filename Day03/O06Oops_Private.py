
class Employee:

    def __init__(self, name):
        self.__name = name      # private variable
        self.tech = ['C++', 'Java', 'J2EE', 'JSP', 'Spring', 'Hibernate', 'Angular', 'React']

    def __str__(self):
        return self.__name + " " + ",".join([str(v) for v in self.tech])


emp1 = Employee("Peter")
print(emp1)

print("-" * 60)
# print(emp1.__name)
print(emp1.__dict__)
# access the private variable
emp1._Employee__name = "Ruben"
print("-" * 60)
print(emp1)
