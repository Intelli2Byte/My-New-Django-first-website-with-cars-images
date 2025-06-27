import json
from json import JSONEncoder

class Boss:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
Neha = Boss("Neha", 20)

class BossEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Boss):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)
    
Neha_json = json.dumps(Neha, cls=BossEncoder)
print(Neha_json)

Neha_json = BossEncoder().encode(Neha)
print(Neha_json)

def BossDecoder(dct):
    if Boss.__name__ in dct:
        return Boss(name=dct['name'], age=dct['age'])
    return dct

Neha_py = json.loads(Neha_json, object_hook=BossDecoder)
print(Neha.name)