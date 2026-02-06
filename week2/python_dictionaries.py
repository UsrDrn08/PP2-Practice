# Создание словаря
student = {"name": "Ali", "age": 18}

# Доступ к значению
print(student["name"])

# Изменение значения
student["age"] = 19

# Добавление новой пары
student["grade"] = "A"

# Перебор словаря
for key, value in student.items():
    print(key, value)
