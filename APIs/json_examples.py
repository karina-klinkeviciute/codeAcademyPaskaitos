import json
import random
from pprint import pprint

data = '''{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price" 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson" 
     } 
  ]   
}'''

duomenys = json.loads(data)

pprint(duomenys)

for studentas in duomenys["student"]:
    print(studentas["name"])
    studentas["year"] = random.randint(1, 4)

pprint(duomenys)

json_duomenys = json.dumps(duomenys)

print(type(json_duomenys))

print(json_duomenys)

