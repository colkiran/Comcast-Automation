
def funLogger(fnc):
    def helper(*args):
        print("My info logged into a service....")
        res = fnc(*args)            # callback
        print("My info logger channel closed.....")
        return res

    return helper

@funLogger
def add(x, y):
    return x + y


@funLogger
def sub(x, y):
    return x - y


print(add(38, 67))
print(sub(68, 44))

