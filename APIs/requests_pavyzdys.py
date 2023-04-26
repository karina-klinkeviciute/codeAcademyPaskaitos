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

# payload = {'q': 'pep', 'page': '2'}
# r = requests.get('https://www.python.org/search/', params=payload)
# print(r.url)

data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)


