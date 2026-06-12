
class Product:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        print("getter called....")
        return self.__price

    def set_price(self, prc):
        print("setter called....")
        self.__price = prc

    def del_price(self):
        print("deleter called....")
        self.__price = 0

    price = property(get_price, set_price, del_price)

p1 = Product(250)

print("-" * 60)
print(p1.price)

print("-" * 60)
p1.price = 125

print("-" * 60)
print(p1.price)

print("-" * 60)
del p1.price

print("-" * 60)
print(p1.price)