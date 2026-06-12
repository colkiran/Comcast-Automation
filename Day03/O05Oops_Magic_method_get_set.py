
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

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value


emp1 = Employee("Steve", 70000)
print(emp1)

print("-" * 60)
print([t for t in emp1.tech])

print("-" * 60)
emp1.append('Python')

print("-" * 60)
print([t for t in emp1.tech])

print("-" * 60)
res = emp1[4]
print(res)

print("-" * 60)
# jsp => oracle
emp1[3] = 'Oracle'

print("-" * 60)
print([t for t in emp1.tech])
