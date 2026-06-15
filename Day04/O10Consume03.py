# c:\delhi\gurgaon\mymodule.py
import sys
# sys.path is a list
sys.path.append("c:/Delhi")
for path in sys.path:
    print(path)

print("-" * 60)
import gurgaon.mymodule as m

m.amount += 10000
print(m.amount)

m.get_balance()

print("-" * 60)
print(f"Banks :{m.banks}")



