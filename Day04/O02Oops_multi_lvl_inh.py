
class Animal:
    def eat(self):
        print("Animals eat....")


class Bird(Animal):
    def fly(self):
        print("Birds fly....")

class Chicken(Bird):
    def message(self):
        print("Chickens are breeded for consumtion....")


    def fly(self):
        print("Chickens seldom fly......")
        # super().fly()

chick = Chicken()
chick.fly()
chick.eat()
Bird.fly(chick)