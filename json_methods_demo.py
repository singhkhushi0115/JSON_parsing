import json

print("===== json.load() Demo =====")
with open("data_dump.json", "r") as file:
    data = json.load(file)
print("Type of data:", type(data))
print("Company Short Name:", data["company"]["short_name"])
print("\n")

print("===== json.loads() Demo =====")
with open("data_dump.json", "r") as file:
    json_string = file.read()
print("Type of json_string:", type(json_string))
data = json.loads(json_string)
print("Type of data:", type(data))
print("Company Short Name:", data["company"]["short_name"])
print("\n")