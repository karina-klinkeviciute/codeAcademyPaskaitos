
def skaiciu_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma

skaiciu_sarasas = (1, 5, 6)

suskaiciuota = skaiciu_suma(skaiciu_sarasas)

print(suskaiciuota)
