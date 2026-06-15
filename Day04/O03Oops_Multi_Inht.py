
class Animal:

    def __init__(self):
        self.a = 10
        print("Animal Ctor.....")

    def eat(self):
        print("Animals eat....")

    def disp(self):
        print("hello from Animal class...")

class Person:

    def __init__(self):
        self.p = 20
        print("Person Ctor.....")

    def Talk(self):
        print("Person Walks and runs.....")

    def disp(self):
        print("hello from Person class...")

class Girl(Person, Animal):

    def __init__(self):
        self.g = 30
        # super is the next class in the MRO (Method Resolution Order)
        # super already has access to the current class instance (self) through the method call
        super().__init__()
        # Person.__init__(self)
        Animal.__init__(self)
        print("Girl Ctor.....")

sofia = Girl()
sofia.disp()
print(sofia.__dict__)