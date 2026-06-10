from emojis import emojis
def outerFun(greet):

    def innerFun(Sep):

        def innerMostFun(name):

            emojized = emojis.encode(greet + " :" + Sep + ": " + name)
            print(emojized)

        return innerMostFun

    return innerFun

# engFun = outerFun("Welcome")
#
# sArwFun = engFun("----->")
# dArwFun = engFun("=====>>")
#
# sArwFun("Slater")
# dArwFun("Richard")

print("-" * 60)

engFun = outerFun("Welcome")

# sepFun = engFun("tiger")
# sepFun = engFun("lion")
sepFun = engFun("bear")

sepFun("Raju")
