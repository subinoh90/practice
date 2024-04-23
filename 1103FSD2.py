# import math as m
# n = int(input("n = "))

# for e in range(1, n+1):
#     f = 1
#     for i in range(1,e+1):
#         f = i
#     print(f'factorial({e}) = {f}')
    
# print()

# for e in range(1, n+1):
#     print(f'factorial({e}) = {m.factorial(e)}')
import sys

rain = int(input("Rain: "))
count = 0
maximum = -sys.maxsize

while rain != -1:
    if rain == 0:
        count += 1
    else: 
        maximum = max(count, maximum)
    