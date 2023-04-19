
def raides(tekstas):
    """Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių."""
    zodziai = tekstas.split()
    zodziu_skaicius = len(zodziai)
    didziuju_kiekis = 0
    mazuju_kiekis = 0
    skaiciu_kiekis = 0
    for raide in tekstas:
        if raide.isupper():
            didziuju_kiekis = didziuju_kiekis + 1
        elif raide.islower():
            mazuju_kiekis += 1
        elif raide.isnumeric():
            skaiciu_kiekis += 1

    print(f"Zodziu kiekis: {zodziu_skaicius}, \n"
          f"didziuju raidziu kiekis: {didziuju_kiekis}, \n" 
          f"mazuju raidziu kiekis: {mazuju_kiekis}, \n"
          f"skaicius: {skaiciu_kiekis}"
          )


raides("Labas Vakaras, dabar yra 20 valandų ir 41 minutė")
raides("abcg123GFD")

