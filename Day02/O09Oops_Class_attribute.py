
class Player:
    team = "India"  # class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name: {self.name}\nAge: {self.age}")

ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 30)
ply2.get_details()

print("-" * 60)
print(f"Ply1 :{ply1.team}")
print(f"Ply2 :{ply2.team}")
print(f"Player :{Player.team}")

print("-" * 60)
ply1.team = ("MI")
print(f"Ply1 :{ply1.team}")

print(f"Ply2 :{ply2.team}")
print(f"Player :{Player.team}")

print("-" * 60)
Player.team = "RCB"
print(Player.team)
print(ply2.team)
print(ply1.team)

print("-" * 60)
# ply1.team = ("MI")    # new instance variable team: 'MI'
print(ply1.__dict__)

print("-" * 60)
print(Player.__dict__)
