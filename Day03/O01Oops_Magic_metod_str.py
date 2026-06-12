
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name :{self.name}\nAge :{self.age}"

ply1 = Player('Virat', 37)
print(ply1.__str__())

print("-" * 60)
print(str(ply1))

print("-" * 60)
# shows the formatted string instead of default memory address
print(ply1)
