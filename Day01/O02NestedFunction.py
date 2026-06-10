
def outerFun(info):     # HOF - Higher Order Function
    # outer func scope
    inf = "Mr." + info

    def innerFun():
        # inner func scope
        print(f"Welcome {inf}")

    innerFun()

outerFun("Mike")

"""
A closure in Python is a function object that remembers values from its enclosing lexical scope, even if that scope is no longer active. In simpler terms: if you define a function inside another function, and the inner function refers to variables from the outer function, Python keeps those variables alive through the closure.

"""