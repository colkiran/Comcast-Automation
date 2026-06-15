
class Animal:
    def __init__(self, name):
        print("Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):
    def __init__(self, name, breed):     # overriding animal Ctor
        super().__init__(name)
        self.name = name
        self.breed = breed
        self.weight = '1 kg'
        print("Bird Ctor.....")

    def get_details(self):
        return f"Name :{self.name}\nBreed :{self.breed}"

    def fly(self):
        print("Birds fly.....")

brd = Bird("abc", "cuckoo")
print(brd.get_details())
brd.fly()
print(brd.__dict__)
