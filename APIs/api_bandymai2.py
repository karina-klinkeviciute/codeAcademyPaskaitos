import requests
import json

# paimam visų emoji sąrašą iš šios API
emoji_json = requests.get("https://emojihub.yurace.pro/api/all")

# gautus duomenis iš json string paverčiam į Python lists ir dictionaries
emoji_duomenys = json.loads(emoji_json.text)

# einam per visus emoji ir išrenkam iš jų visas galimas kategorijas (kad nesikartotų)
kategoriju_sarasas = []
for emoji in emoji_duomenys:
    if emoji["category"] not in kategoriju_sarasas:
        kategoriju_sarasas.append(emoji["category"])
print("Galimos kategorijos: ", kategoriju_sarasas)

# paprašom vartotojo pasirinkti kategoriją
pasirinkta_kategorija = input("iveskite kategorija: ")

# kadangi kategorija atspausdinama ir įvedama su tarpais, o mums nuorodoje reikia su brūkšneliais, pakeičiam juos
pasirinkta_kategorija = pasirinkta_kategorija.replace(' ', '-')

# siunčiam užklausą į API, kad gautume visus tos kategorijos emojius
emoji_json = requests.get("https://emojihub.yurace.pro/api/all/category/" + pasirinkta_kategorija)

# perkeliam iš eilutės į lists/dictionaries (iš json į python formatą)
emoji_duomenys = json.loads(emoji_json.text)

# einam per visus emoji ir išrenkam iš jų grupes (kad nesikartotų)
grupiu_sarasas = []
for emoji in emoji_duomenys:
    if emoji["group"] not in grupiu_sarasas:
        grupiu_sarasas.append(emoji["group"])
print(grupiu_sarasas)

