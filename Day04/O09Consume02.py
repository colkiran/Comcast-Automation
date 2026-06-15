
# import mypackage.mymodule as m
from mypackage.mymodule import amount, get_balance, banks
# amount and get_Balance will become local to the code (no need of prefixing the module name)


amount += 10000
print(amount)

get_balance()

print("-" * 60)
print(f"Banks :{banks}")

print("-" * 60)
import sys
for path in sys.path:
    print(path)
