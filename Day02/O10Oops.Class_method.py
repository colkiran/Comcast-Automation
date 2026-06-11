
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

    @classmethod
    def createPlayer(cls, fname, lname, age):
        print("Factory.....")               # factory
        return cls(f"Mr.{fname} {lname}", age)   # calls the cons

ply1 = Player("Virat", 37)
ply1.get_details()

print("-" * 60)
# ply2 = Player.createPlayer("Dhoni", 42)
ply2 = Player.createPlayer("Dhoni", "Mahendar", 42)
ply2.get_details()

