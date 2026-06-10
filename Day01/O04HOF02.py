
def outerFun(greet):

    def innerFun(name):

        print(greet, name)

    return innerFun

outerFun("Welcome")("James")

print("_" * 60)

engFun = outerFun("Welcome")
tmlFun = outerFun("Vanakam")

engFun("James")
tmlFun("Ramu")
