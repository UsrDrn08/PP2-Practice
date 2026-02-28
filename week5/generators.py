"""n = int(input())
def squares(num):
    for i in range(n + 1):
        yield i * i

for i in squares(n):
    print(i)
    """
"""def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)
n = int(input())
print(", ".join(even_generator(n)))
"""
"""def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for i in divisible(n):
    print(i)
    """
"""def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a, b = list(map(int,input().split()))
fir, sec = a, b
for i in squares(fir,sec):
    print(i)
"""
"""def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for i in countdown(n):
    print(i)
"""