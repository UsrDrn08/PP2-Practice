from functools import reduce

nums = [1, 2, 3, 4, 5]

# 1. map() and filter()
squared = list(map(lambda x: x**2, nums))     # Square: [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, nums)) # Only even numbers: [2, 4]

# 2. reduce() — agregation (sum of all elements)
total = reduce(lambda x, y: x + y, nums) # 1+2+3+4+5 = 15

# 3. enumerate() and zip()
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}") # Output name and number

scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} набрал {score} баллов") # Join lists in pairs

# Check types and convertation 
val = "100"
if isinstance(val, str):
    num = int(val) # Convertation
    print(f"Тип изменен на {type(num)}")
