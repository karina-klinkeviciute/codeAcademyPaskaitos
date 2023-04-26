import json

import requests

# puslapis = "https://lrv.lt/"
#
# puslapio_duomenys = requests.get(puslapis)
#
# print(puslapio_duomenys.text)
#
# print(puslapio_duomenys.status_code)
#
# if puslapio_duomenys.ok:
#     print("viskas gerai, puslapis užsikrovė")
# else:
#     print("kažkas ne taip")
#
# print(puslapio_duomenys.headers)

payload = {'number': 5}
r = requests.get('https://dog-api.kinduff.com/api/facts', params=payload)
print(r.text)

faktai = json.loads(r.text)

for faktas in faktai["facts"]:
    print(f"you probably didn't know this about dogs: {faktas}")

# data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)


