import os 
import shutil
# Creating nested directories
os.makedirs("project/data/logs", exist_ok=True)

# List of files and folders on current directory 
print("Список объектов:", os.listdir("."))

# Search files by extension
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print("Текстовые файлы:", txt_files)

# File movement
# Create the file and move it to created file
with open("temp.log", "w") as f: f.write("log data")
shutil.move("temp.log", "project/data/logs/temp.log")
