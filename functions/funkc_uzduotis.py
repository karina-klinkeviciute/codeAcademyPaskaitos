# Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.

# 1. aprasyti funkcija
# 2. issiaiskinti, kas yra asmens kodas
# pirmas skaicius - nuo 1 iki 6
# antras ir trecias skaitmenys gali buti bet kokie
# ketvirtas ir penktas - bet kas nuo 01 iki 12
# sestas ir septintas - diena tam menesy, kur buvo pirma. jei mėnuo - vasaris ir diena 29 - ar metai keliamieji
# astuntas, devintas ir 10 - bet kokie skaitmenys
# 11 skaičiaus skaičiavimas:
# Jei asmens kodas užrašomas ABCDEFGHIJK, tai:
#
# S = A*1 + B*2 + C*3 + D*4 + E*5 + F*6 + G*7 + H*8 + I*9 + J*1
#
# Suma S dalinama iš 11, ir jei liekana nelygi 10, ji yra asmens kodo kontrolinis skaičius K. Jei liekana lygi 10, tuomet skaičiuojama nauja suma su tokiais svertiniais koeficientais:
#
# S = A*3 + B*4 + C*5 + D*6 + E*7 + F*8 + G*9 + H*1 + I*2 + J*3
#
# Ši suma S vėl dalinama iš 11, ir jei liekana nelygi 10, ji yra asmens kodo kontrolinis skaičius K. Jei vėl liekana yra 10, kontrolinis skaičius K yra 0.

# 3. Asmens kodo skaidymas:
# a) paimam pirmą skaičių
# b) paimam ketvirtą ir penktą kaip vieną divejų skaitmenų skaičių, pavadinam jį "mėnuo"
# c) paimam šeštą ir septintą kaip vieną skaičių, pavadinam jį "diena"
# d) paimam 11 skaitmenį

# 4. Amens kodo tikrinimas:
# a) pirmo skaičiaus tikrinimas - patikrinam, ar jis yra nuo 1 iki 6
#         jei nėra tarp 1 ir 6 - grąžinam, kad neteisingas (False)
# b) patikrinam, ar ketvritas ir penktas kartu ("mėnuo") yra tarp 01 ir 12
#         jei nėra tarp 01 ir 12 tai iš karto grąžinam, kad neteisingas (False)
# c) patikrinam, ar šeštas ir septintas kartu gali būti turimo mėnesio diena
#    c1 patikrinam, ar didesnis už 31
#        Jei didesnis, iš karto grąžinam, kad asmens kodas neteisingas (False)
#    c2 patikrinam, ar skaičius yra tarp 01 ir 28
#         jei yra - einam toliau
#           jei nėra - tikrinam ar jis gali būti to mėnesio diena.
#              jei "mėnuo" yra tarp 04, 06, 09, 11, tikrinam ar "diena" tarp 01 ir 30
#              jei "mėnuo" yra 02, tai priklausomai nuo metų, tikrinam ar yra tarp 28 ir 29
#                  tikrinam, ar metai dalijasi iš 4. Jei dalijasi, yra keliamieji, tada tikrinam
#                  ar diena tarp 01 ir 29, jei nesidalija, tikrinam ar diena tarp 01 ir 28
#                     jei nepatenka į reikiamus rėžius, grąžinam, kad False
# d) tikrinam, ar kontrolinis skaitmuo teisingas.
#   d1 išskaidom asmens kodą po skaitmenį
#   d2 suskaičiuojam sumą pagal duotą formulę
#   d3 paskaičiuojam liekaną padalinus iš 11, pavadinam ją "liekana"
#   jei liekana 10, skaičiuojam pagal antrą formulę, pavadinam "liekana"
#   jei liekana vis tiek 10, tada "liekana" priskiriam reikšmę 0
#   jei "liekana" lygi 11 skaitmeniui, tada asmens kodas teisingas, ir grąžinam "True"


# funkcija grąžins True arba False, priklausomai ar validus ar nevalidus kodas
def asmens_kodas_validus(kodas):
    # kodas - stringas
    # 50106121232
    lytis_simtmetis = int(kodas[0])
    print("LYTIS_SIMTMETIS: ", lytis_simtmetis)
    metai = int(kodas[1:3])
    print(metai)
    menuo = int(kodas[3:5])
    diena = int(kodas[5:7])
    kontrolinis = int(kodas[10])

    if not(lytis_simtmetis >= 1 and lytis_simtmetis <= 6):
        return False
    if not(menuo >= 1 and menuo < 12):
        return False

    # dienos tikrinimas
    if (diena > 31 or diena == 0):
        return False
    if diena > 28:
        if menuo in (4, 6, 9, 11):
            if diena == 31:
                return False
        if menuo == 2:
            if not(metai % 4 == 0):
                if diena == 29:
                    return False

    # todo patikrinti kontrolini skaiciu

    return True


ar_validus = asmens_kodas_validus("50106121233")

if ar_validus:
    print("kodas validus")
else:
    print("kodas nevalidus")

kodas2 = "58624963284"

ar_validus = asmens_kodas_validus(kodas2)

if ar_validus:
    print(f"kodas {kodas2} validus")
else:
    print(f"kodas {kodas2} nevalidus")

kodas3 = "48111154568"

ar_validus = asmens_kodas_validus(kodas3)

if ar_validus:
    print(f"kodas {kodas3} validus")
else:
    print(f"kodas {kodas3} nevalidus")
