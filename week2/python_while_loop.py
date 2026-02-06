# Простой while
i = 0
while i < 5:
    print(i)
    i += 1

# Сумма чисел
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total)

# break
i = 0
while True:
    if i == 3:
        break
    print(i)
    i += 1

# continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# while с флагом
running = True
count = 0
while running:
    count += 1
    if count == 3:
        running = False
