from pprint import pprint

amzius = {"Rokas": 25, "Andrius": 45, "Ieva": 22}

iteratorius = iter(amzius)

while True:
    try:
        print(next(iteratorius))
        print(next(iteratorius)[10])
    except StopIteration:
        break


# ivestas = input("iveskite")

# if ivestas.capitalize() in amzius:
#     print("yra")
# else:
#     print("nera")
#
# amzius1 = amzius["Rokas"]
#
# print(amzius1)
#
# amzius["Tomas"] = 19
#
# print(amzius["Tomas"])
#
# amzius["Rokas"] = 32
#
# print(amzius["Rokas"])
#
# print(amzius)
#
# del amzius["Rokas"]
#
# print(amzius)
#
# a = amzius.pop("Andrius")
#
# print(amzius)
#
# print(a)
#
# zmogus1 = {
#     "vardas": "Jonas",
#     "darbas": "programuotojas",
#     "miestas": "Šiauliu",
#     "telefonas": "+370 607 12345",
#     "amžius": 26
# }
#
# zmogus2 = {
#     "vardas": "Agnė",
#     "darbas": "autobuso vairuotoja",
#     "miestas": "Kaunas",
#     "telefonas": "123",
#     "amžius": 26
# }
#
# zmogus3 = {
#     "vardas": "Tomas",
#     "darbas": "pardavėjas",
#     "miestas": "Kaunas",
#     "telefonas": "55555",
#     "amžius": 35
# }
#
# zmones = [zmogus1, zmogus2, zmogus3]
#
# pprint(zmones)
#
# import datetime
#
# datetime.date()