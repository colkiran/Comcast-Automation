
class Player:

    def __init__(self, name, runs):
        self.name = name
        self.runs = runs
        print("Player Initialized......")

    def get_details(self):
        print(f"Name :{self.name}\nRuns :{self.runs}")

ply1 = Player("Sachin", 98)
ply1.get_details()

print("-" * 60)

ply2 = Player("Rahul", 37)
ply2.get_details()
ply2.age = 32

print("-" * 60)
print(ply1.__dict__)

print("-" * 60)
print(ply2.__dict__)
