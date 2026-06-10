
def funLogger(fnc):
    def helper():
        print("My info logged into the service.....")
        fnc()
        print("My info logged out of the service......")
    return helper


def normalFun():
    print(f"Execute the equation :{10 + 30}")

print("-" * 60)
funLogger(normalFun)()

print("-" * 60)
resFun = funLogger(normalFun)
resFun()

print("-" * 60)
normalFun = funLogger(normalFun)
normalFun()

print("-" * 60)
@funLogger
def basicFun():
    print(f"basic equation :{800 - 342}")

basicFun()      # helperFun()
