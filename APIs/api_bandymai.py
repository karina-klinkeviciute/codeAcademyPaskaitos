from pprint import pprint
import requests
import json

# duomenys = requests.get("https://cat-fact.herokuapp.com/facts")
#
# # print(duomenys.text)
#
# kaciu_faktai = json.loads(duomenys.text)
#
# # print(kaciu_faktai)
#
# for faktas in kaciu_faktai:
#     print(f"Vartotojas {faktas['user']} įkėlė faktą: {faktas['text']}")




emoji_json = requests.get("https://emojihub.yurace.pro/api/random")

print(emoji_json.text)

emoji_duomenys = json.loads(emoji_json.text)

pprint(emoji_duomenys)

print(f"pavadinimas: {emoji_duomenys['name']}")

print(f"\{emoji_duomenys['unicode'][0]}")

emoji_kodas = emoji_duomenys['unicode'][0][2:]

emoji_kodas = int(emoji_kodas, 16)

emoji = chr(emoji_kodas)
# emoji_kodas = "\\" + emoji_kodas.replace("+", "000")

print(emoji)

