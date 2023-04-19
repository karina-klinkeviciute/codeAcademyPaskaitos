class Automobilis:

    def __init__(self, maks_greitis=200):
        self.greitis = 0
        self.maksimalus_greitis = maks_greitis

    def greiteti(self):
        self.greitis = self.greitis + 1

    def vaziuoti(self):
        self.greitis = 20

    def ilgai_pypseti(self):
        for i in range(5):
            self.pypseti()

    def pypseti(self):
        print("Pyyyp")

mano_masina = Automobilis()

# mano_masina.pypseti()
# mano_masina.pypseti()


auto = Automobilis()

auto1 = Automobilis()

auto1.ilgai_pypseti()

# mano_masina.greiteti()


print(mano_masina.greitis)

for i in range(30):
    mano_masina.greiteti()

print(mano_masina.greitis)

print(mano_masina.maksimalus_greitis)

porshe = Automobilis(400)

