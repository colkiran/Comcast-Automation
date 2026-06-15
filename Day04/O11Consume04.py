import sys
for pth in sys.path:
    print(pth)

print("-" * 60)

import gurgaon.mymodule as m

m.amount += 10000
print(m.amount)

m.get_balance()