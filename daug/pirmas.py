from daug.antras import *
from daug.antras import kvadratu_suma as ks
from functions.functions import kvadratu_suma as kubu_suma

from math import factorial, ceil

faktorialas = factorial(5)

print(faktorialas)

print(kintamasis)

def kvadratu_suma(*args):
    return "suskaiciuota"

skaiciai = []

while True:
    ivesta = input("iveskite skaičių. Jei norite išeiti, spauskite q: ")
    if ivesta == "q":
        print("pabaiga")
        break

    try:
        skaicius = int(ivesta)
    except ValueError:
        print("įvedėte ne skaičių!")
        continue

    skaiciai.append(skaicius)

suma = ks(skaiciai)

suma_kubu = kubu_suma(skaiciai)

print("suma: ", suma, "kubu suma: ", suma_kubu)
