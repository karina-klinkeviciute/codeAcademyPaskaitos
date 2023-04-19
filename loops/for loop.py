from datetime import datetime

from objektinis.sukaktis import labas_vakaras
from objektinis.sukaktis import ar_keliamieji
from objektinis.sukaktis import Sukaktis


# import objektinis.sukaktis

# # sarasas = [45, 126, 7, "Labas", 45.45]
# #
# # for kintamasis in sarasas:
# #     print(kintamasis)
#
# sarasas = [2, 6, 7, 9, 41, 20, 46, 789]
#
# suma = 0
#
# # for skaicius in sarasas:
# #     suma = suma + skaicius
# #     print(skaicius)
# #     print(suma)
# #
# # print(suma)
#
# amzius = {"Rokas": 25, "Andrius": 45, "Ieva": 22}
#
#
# print(amzius.items())
#
# zmogus, amzius = list(amzius.items())[0]
# #
# print(zmogus)
# #
# print(amzius)
#
#
#
# # for zmogaus_amzius in amzius:
# #     print(zmogaus_amzius)
# #
# # for zmogaus_amzius in amzius.values():
# #     print(zmogaus_amzius)
# #
# for vardas, zmogaus_amzius in amzius.items():
#     # print(f"{vardas} amzius yra {zmogaus_amzius}")
#     print(vardas)
#     print(amzius)


# print("labas")
# print("rytas")

# for kazkas in range(1, 11):
#     for kazkas_kitas in range(kazkas):
#         # print(f"{kazkas} kart {kazkas_kitas} lygu {kazkas*kazkas_kitas}")
#         print("@", end="")
#     print("")

eilute = "kazkoks sakinys"

for index, raide in enumerate(eilute):
    # if
    print(index)
    print(raide)

labas_vakaras("Lina")

ar_kel = ar_keliamieji(datetime.now())

print(ar_kel)

siandien = Sukaktis("2023-04-14", "šiandien")

ar_kel = siandien.ar_keliamieji()

print(ar_kel)


