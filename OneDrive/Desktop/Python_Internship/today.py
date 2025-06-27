import json
id = { "name":"Neha", "age": 25, "city": "New York" ,"spouse":"None","titles":["Bladeee"] }
id_json = json.dumps(id, indent=2, sort_keys=False)
print(type(id_json))

with open("id_data","w")as file:
    json.dump(id, file, indent=4)

id_py = json.loads(id_json)
print(id_py)

with open("id_data", "r") as file:
    id_pyf = json.load(file)
print(type(id_pyf))

