import requests
import json

emoji_json = requests.get("https://emojihub.yurace.pro/api/all")

# print(emoji_json.text) #  json eilute
emoji_duomenys = json.loads(emoji_json.text)
kategoriju_sarasas = []
for emoji in emoji_duomenys:
    if emoji["category"] not in kategoriju_sarasas:
        kategoriju_sarasas.append(emoji["category"])
print("Galimos kategorijos: ", kategoriju_sarasas)

pasirinkta_kategorija = input("iveskite kategorija: ")

pasirinkta_kategorija = pasirinkta_kategorija.replace(' ', '-')

emoji_json = requests.get("https://emojihub.yurace.pro/api/all/category/" + pasirinkta_kategorija)

emoji_duomenys = json.loads(emoji_json.text)
grupiu_sarasas = []
for emoji in emoji_duomenys:
    if emoji["group"] not in grupiu_sarasas:
        grupiu_sarasas.append(emoji["group"])
print(grupiu_sarasas)

