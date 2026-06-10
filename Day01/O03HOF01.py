
def outerFun(info, choice):     # HOF - Higher Order Function
    # outer func scope
    inf = "Mr." + info

    def innerFun():
        # inner func scope
        print(f"Welcome {inf}")

    return innerFun

outerFun("Mike")

print("-" * 60)

print(outerFun.__name__)
print(outerFun("Mike").__name__)

print("-" * 60)

# calls the innerFun
outerFun("Mike")()

print("-" * 60)

inref = outerFun("Jack")
inref()


"""
HOF - Higher Order Fuction
1. it will take a function as an argument
2. it will return a function as a reference
"""