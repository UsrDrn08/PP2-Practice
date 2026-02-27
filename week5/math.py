#built in functions 
print(min(5, 10, 2))  # 2
print(max(5, 10, 2))  # 10
print(abs(-7.25))     # 7.25
print(pow(4, 3))      # 64 

#import
import math
print(math.sqrt(64))  # 8.0
print(math.ceil(1.4)) # 2 (round up)
print(math.floor(1.8))# 1 (round down)
print(math.pi)        # 3.1415...

#random
import random

print(random.random())           # random number from 0 to 1
print(random.randint(1, 10))     # int from 1 to 10
items = ["A", "B", "C"]
print(random.choice(items))      # random element from items


