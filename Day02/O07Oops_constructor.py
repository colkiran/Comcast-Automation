
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.runs = 120
        print("Player Initialized.....")


    def get_details(self):
        print(f"name = {self.name}\nRuns = {self.runs}")

ply1 = Player()
ply1.get_details()

print("-" * 60)
ply2 = Player()
ply2.name = "Rahul"
ply2.runs = 85
ply2.get_details()

