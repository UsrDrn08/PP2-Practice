import json

# JSON -> Python (dict)
json_data = '{"name": "Daryn", "age": 18}'
user = json.loads(json_data)

# Python -> JSON (str)
python_dict = {"brand": "Tesla", "model": "S"}
json_string = json.dumps(python_dict, indent=4)

# record in file
data = {"project": "Alpha", "status": "Active"}
with open("data.json", "w") as f:
    json.dump(data, f)

# reading from file
with open("data.json", "r") as f:
    loaded_data = json.load(f)