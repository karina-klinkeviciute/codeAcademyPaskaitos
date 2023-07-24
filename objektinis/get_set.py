

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, atlyginimas):
        if atlyginimas < 0:
            # print("Atlyginimas negali buti neigiamas")
            raise ValueError("Atlyginimas negali buti neigiamas")
        else:
            self.__atlyginimas = atlyginimas


domas = Darbuotojas("Domas", "Rutkauskas", 1200)
domas.atlyginimas = 1500
# domas.set_atlyginimas(1500)
print(domas.atlyginimas)
# print(domas.get_atlyginimas())


domas = Darbuotojas("Domas", "Rutkauskas", 1200)
try:
    domas.atlyginimas = -150
except ValueError:
    print("per mazai moki")
# domas.set_atlyginimas(-150)
print(domas.atlyginimas)
# print(domas.get_atlyginimas())
