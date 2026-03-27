import os
import shutil
# Create and write
with open("example.txt", "w") as f:
    f.write("Привет! Это первая строка.\n")
    f.write("Это вторая строка.\n")

# Read
with open("example.txt", "r") as f:
    print("Содержимое файла:\n", f.read())

# Adding (mode 'a' - append)
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("Это добавленная строка.\n")

# Copy and backup
shutil.copy("example.txt", "example_backup.txt")
print("Файл скопирован успешно.")

# Safe remove
if os.path.exists("example_backup.txt"):
    os.remove("example_backup.txt")
    print("Бэкап удален.")
