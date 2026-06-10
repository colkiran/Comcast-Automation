
# numbers can accept more than one value and store it in a list
def fun(*numbers):
    print(numbers)
    res = 0
    for num in numbers:
        res = res + num
    return res

print(fun(10, 20, 30, 40, 50))

print("-" * 60)

# accepts more than one value in form of named arguments and stores it in a dictionary
def extract_details(**details):
    print(details)
    print(details['age'])
    print(details['name'])
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)


# function args - name, age, gender
extract_details(name="Jack", age=34, gender="M")

