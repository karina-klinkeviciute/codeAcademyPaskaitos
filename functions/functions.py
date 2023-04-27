# # def pasisveikinimas(vardas):
# #     print(f"Labas vakaras {vardas}!")
# #     print("Labas vakaras " + vardas + "!")
# #
# # pasisveikinimas("Lukai")
# #
# # pasisveikinimas("Agne")
# #
# # pasisveikinimas("Gžegož")
#
# def kvadratas(skaicius):
#     skaicius_kvadratu = skaicius**2
#     # print(skaicius_kvadratu)
#     return skaicius_kvadratu
#
# print(kvadratas(6))
#
# kvadratas5 = kvadratas(5)
# kvadratas9 = kvadratas(9)
# kvadratas15 = kvadratas(15)
#
# print(f"skaiciaus 5 kvadratas yra {kvadratas5}")
#
# kvadratu_suma = kvadratas5 + kvadratas9
#
# print(f"5 ir 9 kvadratu suma yra {kvadratu_suma}")
#
# skaicius = None
#
# if skaicius is None:
#     print("skaiciaus nera")
#
# # sudeti dvieju skaiciu kvadratus
#
def kvadratu_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius**3
    return suma

a = [1, 5, 9, 7, 2]
sarasas2 = [15, 0, 3, 8, 4, 6]
sarasas3 = [0.2, 1.5, 0.6, 1.7, 1.8, 2.1]

sumax = kvadratu_suma(a)

suma1 = kvadratu_suma([1, 2])

suma2 = kvadratu_suma(sarasas2)

suma3 = kvadratu_suma(sarasas3)

print(f"suma1: {suma1}, suma2: {suma2}, suma3: {suma3}")

def suma_sandauga(skaicius1, skaicius2, skaicius3):
    suma = skaicius1 + skaicius2
    sandauga = suma * skaicius3

    return sandauga

rezultatas = suma_sandauga(5, 14, 9)

print(rezultatas)
