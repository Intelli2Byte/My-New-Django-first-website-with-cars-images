import json

class Boss:
    def __init__(self,name, age):
        self.name = name 
        self.age = age 

Ryat = Boss("Ryat", 22)

def encode_ids_to_json__serializable(obj):
    if isinstance(obj, Boss):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: False}
    else:
        raise TypeError("Object not Serializable")
    
Ryat_json = json.dumps(Ryat, default=encode_ids_to_json__serializable)
print(Ryat_json)