
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, prc):
        if (prc < 0):
            raise ValueError("Price cannot be less than zero")
        else:
            self.__price = prc

    def del_price(self):
        self.__price = 0


import sys
try:
    p1 = Product(25)
    print(p1.get_price())
    p1.set_price(30)
    print(p1.get_price())
    p1.del_price()
    print(p1.get_price())

except:
    print("Exception happened....")
    print(sys.exc_info()[0], "Occured")
    print(sys.exc_info()[1])
