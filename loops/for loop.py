from datetime import datetime
# importavimo iš vietinių failų pavyzdžiai
from objektinis.sukaktis import labas_vakaras
from objektinis.sukaktis import ar_keliamieji
from objektinis.sukaktis import Sukaktis
import objektinis.sukaktis


# sąrašo elementų spausdinimas po vieną
sarasas = [45, 126, 7, "Labas", 45.45]

for kintamasis in sarasas:
    print(kintamasis)


# sąrašo elementų sumavimas ciklų pagalba
sarasas = [2, 6, 7, 9, 41, 20, 46, 789]

suma = 0

for skaicius in sarasas:
    suma = suma + skaicius
    print(skaicius)
    print(suma)

print(suma)


# pavyzdžiai su žodynais
amzius = {"Rokas": 25, "Andrius": 45, "Ieva": 22}


print(amzius.items())

zmogus, amzius = list(amzius.items())[0]
#
print(zmogus)
#
print(amzius)


# paimam tik raktus
for zmogaus_amzius in amzius:
    print(zmogaus_amzius)

# paimam tik reikšmes
for zmogaus_amzius in amzius.values():
    print(zmogaus_amzius)

# paimam ir rakšut ir reikšmes
for vardas, zmogaus_amzius in amzius.items():
    # print(f"{vardas} amzius yra {zmogaus_amzius}")
    print(vardas)
    print(amzius)

# kaip paimti iš sąrašo indeksą ir elementą

eilute = "kazkoks sakinys"

for index, raide in enumerate(eilute):
    # if
    print(index)
    print(raide)


# kviečiam funkcijas, importuotas iš kito failo
labas_vakaras("Lina")

ar_kel = ar_keliamieji(datetime.now())

print(ar_kel)

siandien = Sukaktis("2023-04-14", "šiandien")

ar_kel = siandien.ar_keliamieji()

print(ar_kel)


