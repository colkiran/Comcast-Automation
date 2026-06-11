

def outerfun():
    name = "Jack"
    def innerfun():
        nonlocal name       # only local variable can be converted to nonlocal
        name += " Slater"
        print(name)

    innerfun()

outerfun()
