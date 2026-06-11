
glb_var = 50        # global variable

def fun(x):             # local variable
    global glb_var      # do not assign any value in this line
    print(f"Global :{glb_var}")
    print(x)
    # glb_var = 250     # local variable with the same name as global
    glb_var += 100
    print(f"Global :{glb_var}")

fun(10)
