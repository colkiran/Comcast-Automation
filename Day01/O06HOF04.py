
def fun1(*args):
    print(args)
    print(*args)        # unpack

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_details(fnc):
    logInfo = "Logging about done....."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

# inref = log_details(fun1)
# inref()
# inref(10)
# inref(10, 20)
# inref(10, 20, 30)

sumLogger = log_details(sum)
sumLogger(36, 85)

diffLogger = log_details(diff)
diffLogger(97, 53)
