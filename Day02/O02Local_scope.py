
def fun(x):     # x is a local variable
    print(x)
    st = "hello world"      # local variable
    print(st)
    x += 100
    print(x)
    print(y)

y = "python"            # global variable by default
fun(50)
# print(x)
# print(st)
