import json

# read the file

my_json_file = open("Project_Rogers\sample3.json", "r")
json_data = my_json_file.read()

# parse
obj = json.loads(json_data)

print(str(obj["color"]))
print(str(obj["value"]))
