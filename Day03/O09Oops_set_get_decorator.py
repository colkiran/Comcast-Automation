

class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter called....")
        return self.__price

    @price.setter
    def price(self, prc):
        print("setter called....")
        self.__price = prc

    @price.deleter
    def price(self):
        print("deleter called....")
        self.__price = 0


p1 = Product(250)

print("-" * 60)
print(p1.price)

print("-" * 60)
p1.price = 500

print("-" * 60)
print(p1.price)

print("-" * 60)
del p1.price
